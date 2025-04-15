import psutil
import time
import os
import sys

# Add parent directory to path to import language module
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

try:
    from src.utils.logger import logging
    from src.utils.language import getTranslation, _
except ImportError:
    from logger import logging
    try:
        from utils.language import getTranslation, _
    except ImportError:
        # Fallback if language module is not available
        def getTranslation(key, *args):
            if args:
                return key.format(*args)
            return key

def ExitCursor(timeout=5):
    """
    温和地关闭 Cursor 进程
    
    Args:
        timeout (int): 等待进程自然终止的超时时间（秒）
    Returns:
        bool: 是否成功关闭所有进程
    """
    try:
        logging.info(getTranslation("starting_cursor_exit"))
        cursor_processes = []
        # 收集所有 Cursor 进程
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'].lower() in ['cursor.exe', 'cursor']:
                    cursor_processes.append(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        if not cursor_processes:
            logging.info(getTranslation("no_cursor_processes_found"))
            return True

        # 温和地请求进程终止
        for proc in cursor_processes:
            try:
                if proc.is_running():
                    proc.terminate()  # 发送终止信号
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        # 等待进程自然终止
        start_time = time.time()
        while time.time() - start_time < timeout:
            still_running = []
            for proc in cursor_processes:
                try:
                    if proc.is_running():
                        still_running.append(proc)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            if not still_running:
                logging.info(getTranslation("all_cursor_processes_closed"))
                return True
                
            # 等待一小段时间再检查
            time.sleep(0.5)
            
        # 如果超时后仍有进程在运行
        if still_running:
            process_list = ", ".join([str(p.pid) for p in still_running])
            logging.warning(getTranslation("processes_not_closed_in_time").format(process_list))
            return False
            
        return True

    except Exception as e:
        logging.error(getTranslation("error_closing_cursor").format(str(e)))
        return False

if __name__ == "__main__":
    ExitCursor()
