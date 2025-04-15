from datetime import datetime
import logging
import time
import re
from config import Config
import requests
import email
import imaplib
import poplib
from email.parser import Parser
import json
import socket

# Import translation functions
from src.utils.language import getTranslation, _


class EmailVerificationHandler:
    def __init__(self,account):
        self.session = requests.Session()
        self.account = account

    def get_verification_code(self, max_retries=5, retry_interval=60):
        """
        获取验证码，带有重试机制。

        Args:
            max_retries: 最大重试次数。
            retry_interval: 重试间隔时间（秒）。

        Returns:
            验证码 (字符串或 None)。
        """

        for attempt in range(max_retries):
            try:
                logging.info(getTranslation("verification_code_attempt").format(attempt + 1, max_retries))

                verify_code = self._get_latest_mail_code()
                if attempt < max_retries - 1 and not verify_code:  # 除了最后一次尝试，都等待
                    logging.warning(getTranslation("verification_code_not_found_retry").format(retry_interval))
                    time.sleep(retry_interval)
                else: 
                    return verify_code

            except Exception as e:
                logging.error(getTranslation("verification_code_fetch_failed").format(e))  # 记录更一般的异常
                if attempt < max_retries - 1:
                    logging.error(getTranslation("error_will_retry").format(retry_interval))
                    time.sleep(retry_interval)
                else:
                    raise Exception(getTranslation("max_retries_reached_with_error").format(e)) from e

        raise Exception(getTranslation("verification_code_not_found_after_attempts").format(max_retries))

    # 手动输入验证码
    def _get_latest_mail_code(self):
        """
        获取最新邮件中的验证码:
        1. iCloud IMAP
        
        Returns:
            str or tuple: 验证码或 (验证码, 邮件ID) 元组
        """
        # 首先尝试 iCloud IMAP
        icloud_imap = Config().get_icloud_imap()
        if icloud_imap:
            logging.info(getTranslation("using_icloud_imap"))
            verify_code = self._get_mail_code_by_icloud_imap(icloud_imap)
            if verify_code:
                return verify_code
        
        return None
    

    def _get_mail_code_by_icloud_imap(self, icloud_config, retry=0):
        """使用 iCloud IMAP 获取邮件验证码
        
        Args:
            icloud_config: iCloud IMAP 配置信息
            retry: 重试次数
            
        Returns:
            str or None: 验证码
        """
        if retry > 0:
            time.sleep(3)
        if retry >= 20:
            raise Exception(getTranslation("verification_code_timeout"))
        
        try:
            # 连接到 iCloud IMAP 服务器
            mail = imaplib.IMAP4_SSL(icloud_config['imap_server'], icloud_config['imap_port'])
            
            mail.login(icloud_config['imap_user'], icloud_config['imap_pass'])
            mail.select(icloud_config['imap_dir'] or 'INBOX')
            
            # 获取最近的邮件
            status, messages = mail.search(None, 'ALL')
            if status != 'OK':
                logging.error(getTranslation("icloud_email_list_failed").format(status))
                return None
            
            mail_ids = messages[0].split()
            print(mail_ids)
            if not mail_ids:
                # 没有获取到邮件
                logging.info(getTranslation("no_emails_in_icloud"))
                return self._get_mail_code_by_icloud_imap(icloud_config, retry=retry + 1)
            
            # 检查最新的10封邮件
            for i in range(min(10, len(mail_ids))):
                mail_id = mail_ids[len(mail_ids) - 1 - i]  
                try:
                    status, msg_data = mail.fetch(mail_id, '(BODY[])')
                except (EOFError, ConnectionError, socket.error) as e:
                    logging.error(getTranslation("icloud_imap_fetch_failed").format(e))
                    mail.logout()
                    return None
                if status != 'OK':
                    logging.error(getTranslation("icloud_imap_fetch_status_failed").format(status))
                    continue
                raw_email = msg_data[0][1]

                email_message = email.message_from_bytes(raw_email)
                sender = email_message.get('from', '')
                recipient = email_message.get('to', '')

                if self.account not in recipient:
                    continue
                if 'no-reply_at_cursor_sh' not in sender:
                    continue
                

                body = self._extract_imap_body(email_message)
                if body:
                    # 查找 6 位数验证码
                    code_match = re.search(r"(?<![a-zA-Z@.])\b\d{6}\b", body)
                    if code_match:
                        code = code_match.group()
                        logging.info(getTranslation("verification_code_found_in_email").format(code))
                        
                        mail.store(mail_id, '+FLAGS', '\\Deleted')
                        mail.expunge()
                        
                        mail.logout()
                        return code
            
            logging.info(getTranslation("no_verification_code_in_email"))
            mail.logout()
            return None
            
        except Exception as e:
            logging.error(getTranslation("icloud_imap_operation_failed").format(e))
            return None

    def _extract_imap_body(self, email_message):
        # 提取邮件正文
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    charset = part.get_content_charset() or 'utf-8'
                    try:
                        body = part.get_payload(decode=True).decode(charset, errors='ignore')
                        return body
                    except Exception as e:
                        logging.error(getTranslation("email_body_decode_failed").format(e))
        else:
            content_type = email_message.get_content_type()
            if content_type == "text/plain":
                charset = email_message.get_content_charset() or 'utf-8'
                try:
                    body = email_message.get_payload(decode=True).decode(charset, errors='ignore')
                    return body
                except Exception as e:
                    logging.error(getTranslation("email_body_decode_failed").format(e))
        return ""

if __name__ == "__main__":
    email_handler = EmailVerificationHandler()
    code = email_handler.get_verification_code()
    print(code)
