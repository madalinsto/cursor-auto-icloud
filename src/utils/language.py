import os
from enum import Enum
from typing import Dict

class Language(Enum):
    """Language enum for supported languages"""
    ENGLISH = "en"
    CHINESE = "zh"

class LanguageManager:
    """Manages language translations and settings for the application"""
    
    _instance = None
    
    def __new__(cls):
        """Singleton pattern to ensure only one instance of LanguageManager exists"""
        if cls._instance is None:
            cls._instance = super(LanguageManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize the language manager with translations"""
        if self._initialized:
            return
            
        # Set default language (can be overridden by env var or user selection)
        env_lang = os.environ.get("LANGUAGE", "").lower()
        if env_lang == "en" or env_lang == "english":
            self.current_language = Language.ENGLISH
        elif env_lang == "zh" or env_lang == "chinese":
            self.current_language = Language.CHINESE
        else:
            self.current_language = Language.CHINESE  # Default to Chinese for backward compatibility
        
        self._translations = self._load_translations()
        self._initialized = True
    
    def _load_translations(self) -> Dict[str, Dict[str, str]]:
        """Load all translations for the application"""
        return {
            # Main UI messages
            "program_init": {
                Language.ENGLISH: "\n=== Initializing Program ===",
                Language.CHINESE: "\n=== 初始化程序 ==="
            },
            "select_operation_mode": {
                Language.ENGLISH: "\nPlease select operation mode:",
                Language.CHINESE: "\n请选择操作模式:"
            },
            "reset_machine_code_only": {
                Language.ENGLISH: "1. Reset machine code only",
                Language.CHINESE: "1. 仅重置机器码"
            },
            "complete_registration": {
                Language.ENGLISH: "2. Complete registration process",
                Language.CHINESE: "2. 完整注册流程"
            },
            "generate_icloud_email": {
                Language.ENGLISH: "3. Generate iCloud hidden email",
                Language.CHINESE: "3. 生成 iCloud 隐藏邮箱"
            },
            "complete_registration_icloud": {
                Language.ENGLISH: "4. Complete registration process (using iCloud hidden email)",
                Language.CHINESE: "4. 完整注册流程（使用 iCloud 隐藏邮箱）"
            },
            "select_language": {
                Language.ENGLISH: "5. Switch language (当前语言: English)",
                Language.CHINESE: "5. 切换语言 (Current language: 中文)"
            },
            "enter_option": {
                Language.ENGLISH: "Please enter option (1-5): ",
                Language.CHINESE: "请输入选项 (1-5): "
            },
            "invalid_option": {
                Language.ENGLISH: "Invalid option, please try again",
                Language.CHINESE: "无效的选项,请重新输入"
            },
            "enter_valid_number": {
                Language.ENGLISH: "Please enter a valid number",
                Language.CHINESE: "请输入有效的数字"
            },
            
            # Machine code reset
            "reset_complete": {
                Language.ENGLISH: "Machine code reset complete",
                Language.CHINESE: "机器码重置完成"
            },
            
            # iCloud email generation
            "enter_email_count": {
                Language.ENGLISH: "Please enter the number of emails to generate: ",
                Language.CHINESE: "请输入要生成的邮箱数量: "
            },
            "email_count_gt_zero": {
                Language.ENGLISH: "Email count must be greater than 0",
                Language.CHINESE: "邮箱数量必须大于0"
            },
            "icloud_module_import_failed": {
                Language.ENGLISH: "Failed to import iCloud email generation module",
                Language.CHINESE: "导入 iCloud 邮箱生成模块失败"
            },
            "install_dependencies": {
                Language.ENGLISH: "Cannot import iCloud email generation module, please make sure all dependencies are installed",
                Language.CHINESE: "无法导入 iCloud 邮箱生成模块，请确保安装了所有依赖"
            },
            "generated_emails": {
                Language.ENGLISH: "Successfully generated {0} email addresses:",
                Language.CHINESE: "成功生成 {0} 个邮箱地址:"
            },
            "no_emails_generated": {
                Language.ENGLISH: "No email addresses were generated",
                Language.CHINESE: "未生成任何邮箱地址"
            },
            "invalid_count": {
                Language.ENGLISH: "Invalid count",
                Language.CHINESE: "无效的数量"
            },

            # Browser initialization
            "initializing_browser": {
                Language.ENGLISH: "Initializing browser...",
                Language.CHINESE: "正在初始化浏览器..."
            },
            "getting_user_agent_failed": {
                Language.ENGLISH: "Failed to get user agent, using default",
                Language.CHINESE: "获取user agent失败，使用默认值"
            },
            
            # Configuration info
            "config_info": {
                Language.ENGLISH: "\n=== Configuration Info ===",
                Language.CHINESE: "\n=== 配置信息 ==="
            },
            "generating_random_account": {
                Language.ENGLISH: "Generating random account information...",
                Language.CHINESE: "正在生成随机账号信息..."
            },
            "generated_email_account": {
                Language.ENGLISH: "Generated email account: {0}",
                Language.CHINESE: "生成的邮箱账号: {0}"
            },
            "initializing_email_verification": {
                Language.ENGLISH: "Initializing email verification module...",
                Language.CHINESE: "正在初始化邮箱验证模块..."
            },
            
            # Registration process
            "start_registration": {
                Language.ENGLISH: "\n=== Starting Registration Process ===",
                Language.CHINESE: "\n=== 开始注册流程 ==="
            },
            "visiting_login_page": {
                Language.ENGLISH: "Visiting login page: {0}",
                Language.CHINESE: "正在访问登录页面: {0}"
            },
            "getting_session_token": {
                Language.ENGLISH: "Getting session token...",
                Language.CHINESE: "正在获取会话令牌..."
            },
            "updating_auth_info": {
                Language.ENGLISH: "Updating authentication information...",
                Language.CHINESE: "更新认证信息..."
            },
            "resetting_machine_code": {
                Language.ENGLISH: "Resetting machine code...",
                Language.CHINESE: "重置机器码..."
            },
            "all_operations_complete": {
                Language.ENGLISH: "All operations complete",
                Language.CHINESE: "所有操作已完成"
            },
            "session_token_failed": {
                Language.ENGLISH: "Failed to get session token, registration process incomplete",
                Language.CHINESE: "获取会话令牌失败，注册流程未完成"
            },
            
            # Sign-up process specific
            "filling_personal_info": {
                Language.ENGLISH: "Filling personal information...",
                Language.CHINESE: "正在填写个人信息..."
            },
            "input_first_name": {
                Language.ENGLISH: "Entered first name: {0}",
                Language.CHINESE: "已输入名字: {0}"
            },
            "input_last_name": {
                Language.ENGLISH: "Entered last name: {0}",
                Language.CHINESE: "已输入姓氏: {0}"
            },
            "input_email": {
                Language.ENGLISH: "Entered email: {0}",
                Language.CHINESE: "已输入邮箱: {0}"
            },
            "submit_personal_info": {
                Language.ENGLISH: "Submitting personal information...",
                Language.CHINESE: "提交个人信息..."
            },
            "signup_page_access_failed": {
                Language.ENGLISH: "Failed to access signup page: {0}",
                Language.CHINESE: "注册页面访问失败: {0}"
            },
            "setting_password": {
                Language.ENGLISH: "Setting password...",
                Language.CHINESE: "正在设置密码..."
            },
            "submit_password": {
                Language.ENGLISH: "Submitting password...",
                Language.CHINESE: "提交密码..."
            },
            "password_setup_complete": {
                Language.ENGLISH: "Password setup complete, waiting for system response...",
                Language.CHINESE: "密码设置完成，等待系统响应..."
            },
            "password_setup_failed": {
                Language.ENGLISH: "Password setup failed: {0}",
                Language.CHINESE: "密码设置失败: {0}"
            },
            "email_already_used": {
                Language.ENGLISH: "Registration failed: Email already in use",
                Language.CHINESE: "注册失败：邮箱已被使用"
            },
            "registration_successful": {
                Language.ENGLISH: "Registration successful - entered account settings page",
                Language.CHINESE: "注册成功 - 已进入账户设置页面"
            },
            "getting_verification_code": {
                Language.ENGLISH: "Getting email verification code...",
                Language.CHINESE: "正在获取邮箱验证码..."
            },
            "verification_code_failed": {
                Language.ENGLISH: "Failed to get verification code",
                Language.CHINESE: "获取验证码失败"
            },
            "verification_code_success": {
                Language.ENGLISH: "Successfully got verification code: {0}",
                Language.CHINESE: "成功获取验证码: {0}"
            },
            "entering_verification_code": {
                Language.ENGLISH: "Entering verification code...",
                Language.CHINESE: "正在输入验证码..."
            },
            "verification_code_complete": {
                Language.ENGLISH: "Verification code input complete",
                Language.CHINESE: "验证码输入完成"
            },
            "verification_process_error": {
                Language.ENGLISH: "Verification process error: {0}",
                Language.CHINESE: "验证码处理过程出错: {0}"
            },
            "waiting_for_processing": {
                Language.ENGLISH: "Waiting for system processing... {0} seconds remaining",
                Language.CHINESE: "等待系统处理中... 剩余 {0} 秒"
            },
            "getting_account_info": {
                Language.ENGLISH: "Getting account information...",
                Language.CHINESE: "正在获取账户信息..."
            },
            "account_usage_limit": {
                Language.ENGLISH: "Account usage limit: {0}",
                Language.CHINESE: "账户可用额度上限: {0}"
            },
            "get_account_limit_failed": {
                Language.ENGLISH: "Failed to get account limit information: {0}",
                Language.CHINESE: "获取账户额度信息失败: {0}"
            },
            "registration_complete": {
                Language.ENGLISH: "\n=== Registration Complete ===",
                Language.CHINESE: "\n=== 注册完成 ==="
            },
            "cursor_account_info": {
                Language.ENGLISH: "Cursor Account Information:\nEmail: {0}\nPassword: {1}",
                Language.CHINESE: "Cursor 账号信息:\n邮箱: {0}\n密码: {1}"
            },
            
            # End messages
            "program_execution_error": {
                Language.ENGLISH: "Error during program execution: {0}",
                Language.CHINESE: "程序执行过程中出错: {0}"
            },
            "program_complete": {
                Language.ENGLISH: "Press Enter to exit...",
                Language.CHINESE: "按回车键退出..."
            },
            "operation_complete": {
                Language.ENGLISH: "\n\n\n\n\n\n============================\nAll operations complete\n\n=== Get More Information ===\nPlease visit the open source project for more information: https://github.com/Ryan0204/cursor-auto-icloud",
                Language.CHINESE: "\n\n\n\n\n\n============================\n所有操作已完成\n\n=== 获取更多信息 ===\n请前往开源项目查看更多信息：https://github.com/Ryan0204/cursor-auto-icloud"
            },
            
            # Language selection
            "select_new_language": {
                Language.ENGLISH: "\nSelect language / 选择语言:\n1. English\n2. 中文\nPlease enter option (1-2): ",
                Language.CHINESE: "\nSelect language / 选择语言:\n1. English\n2. 中文\n请输入选项 (1-2): "
            },
            "language_switched": {
                Language.ENGLISH: "Language switched to English",
                Language.CHINESE: "语言已切换为中文"
            },
            
            # Application main
            "application_starting": {
                Language.ENGLISH: "Starting Cursor Pro Keep Alive application...",
                Language.CHINESE: "正在启动 Cursor Pro Keep Alive 应用程序..."
            },
            "application_error": {
                Language.ENGLISH: "An error occurred: {0}",
                Language.CHINESE: "发生错误: {0}"
            },
            
            # Reset Machine
            "appdata_not_set": {
                Language.ENGLISH: "APPDATA environment variable is not set",
                Language.CHINESE: "APPDATA 环境变量未设置"
            },
            "unsupported_os": {
                Language.ENGLISH: "Unsupported operating system: {0}",
                Language.CHINESE: "不支持的操作系统: {0}"
            },
            "checking_config_file": {
                Language.ENGLISH: "Checking configuration file",
                Language.CHINESE: "正在检查配置文件"
            },
            "config_file_not_exist": {
                Language.ENGLISH: "Configuration file does not exist",
                Language.CHINESE: "配置文件不存在"
            },
            "config_file_no_permission": {
                Language.ENGLISH: "Cannot read/write configuration file, please check file permissions!",
                Language.CHINESE: "无法读写配置文件，请检查文件权限！"
            },
            "go_cursor_help_warning": {
                Language.ENGLISH: "If you have used go-cursor-help to modify the ID; please modify the read-only permission of the file",
                Language.CHINESE: "如果你使用过 go-cursor-help 来修改 ID; 请修改文件只读权限"
            },
            "reading_current_config": {
                Language.ENGLISH: "Reading current configuration",
                Language.CHINESE: "读取当前配置"
            },
            "generating_new_machine_ids": {
                Language.ENGLISH: "Generating new machine identifiers",
                Language.CHINESE: "生成新的机器标识"
            },
            "saving_new_config": {
                Language.ENGLISH: "Saving new configuration",
                Language.CHINESE: "保存新配置"
            },
            "machine_id_reset_success": {
                Language.ENGLISH: "Machine identifier reset successful!",
                Language.CHINESE: "机器标识重置成功！"
            },
            "new_machine_ids": {
                Language.ENGLISH: "New machine identifiers",
                Language.CHINESE: "新的机器标识"
            },
            "permission_error": {
                Language.ENGLISH: "Permission error",
                Language.CHINESE: "权限错误"
            },
            "run_as_admin_suggestion": {
                Language.ENGLISH: "Please try running this program as administrator",
                Language.CHINESE: "请尝试以管理员身份运行此程序"
            },
            "reset_process_error": {
                Language.ENGLISH: "Reset process error",
                Language.CHINESE: "重置过程出错"
            },
            "cursor_machine_id_reset_tool": {
                Language.ENGLISH: "Cursor Machine ID Reset Tool",
                Language.CHINESE: "Cursor 机器标识重置工具"
            },
            "press_enter_exit": {
                Language.ENGLISH: "Press Enter to exit",
                Language.CHINESE: "按回车键退出"
            },
            
            # Auth Manager
            "no_values_to_update": {
                Language.ENGLISH: "No values provided for update",
                Language.CHINESE: "没有提供任何要更新的值"
            },
            "value_updated_success": {
                Language.ENGLISH: "Successfully updated {0}",
                Language.CHINESE: "成功更新 {0}"
            },
            "value_not_found_or_unchanged": {
                Language.ENGLISH: "{0} not found or value unchanged",
                Language.CHINESE: "未找到 {0} 或值未变化"
            },
            "database_error": {
                Language.ENGLISH: "Database error: {0}",
                Language.CHINESE: "数据库错误: {0}"
            },
            "general_error": {
                Language.ENGLISH: "An error occurred: {0}",
                Language.CHINESE: "发生错误: {0}"
            },
            
            # iCloud Email Generator
            "generate_email_failed": {
                Language.ENGLISH: "Failed to generate email: {0}",
                Language.CHINESE: "生成邮箱失败: {0}"
            },
            "unknown_error": {
                Language.ENGLISH: "Unknown error",
                Language.CHINESE: "未知错误"
            },
            "generate_email_failed_no_address": {
                Language.ENGLISH: "Failed to generate email: Unable to get email address",
                Language.CHINESE: "生成邮箱失败: 无法获取邮箱地址"
            },
            "reserve_email_failed": {
                Language.ENGLISH: "Failed to reserve email: {0}",
                Language.CHINESE: "保留邮箱失败: {0}"
            },
            "email_generated_success": {
                Language.ENGLISH: "Email {0} generated successfully",
                Language.CHINESE: "邮箱 {0} 生成成功"
            },
            "generate_email_error": {
                Language.ENGLISH: "Error occurred during email generation: {0}",
                Language.CHINESE: "生成邮箱过程中发生错误: {0}"
            },
            "icloud_cookies_not_configured": {
                Language.ENGLISH: "iCloud Cookies not configured, please set ICLOUD_COOKIES in the .env file",
                Language.CHINESE: "iCloud Cookies 未配置，请在 .env 文件中设置 ICLOUD_COOKIES"
            },
            "start_generating_emails": {
                Language.ENGLISH: "Starting to generate {0} iCloud hidden emails...",
                Language.CHINESE: "开始生成 {0} 个 iCloud 隐藏邮箱..."
            },
            "emails_generated_success": {
                Language.ENGLISH: "Successfully generated {0} email addresses",
                Language.CHINESE: "成功生成 {0} 个邮箱地址"
            },
            "emails_saved_to_file": {
                Language.ENGLISH: "Email addresses have been saved to {0}",
                Language.CHINESE: "邮箱地址已保存到 {0}"
            },
            "invalid_count_parameter": {
                Language.ENGLISH: "Invalid count parameter: {0}",
                Language.CHINESE: "无效的数量参数: {0}"
            },
            
            # iCloud Hide My Email
            "generating_icloud_hidden_email": {
                Language.ENGLISH: "Generating iCloud hidden email...",
                Language.CHINESE: "正在生成 iCloud 隐藏邮箱..."
            },
            "generate_email_timeout": {
                Language.ENGLISH: "Email generation timed out",
                Language.CHINESE: "生成邮箱超时"
            },
            "request_timeout": {
                Language.ENGLISH: "Request timed out",
                Language.CHINESE: "请求超时"
            },
            "reserving_email": {
                Language.ENGLISH: "Reserving email {0}...",
                Language.CHINESE: "正在保留邮箱 {0}..."
            },
            "reserve_email_timeout": {
                Language.ENGLISH: "Email reservation timed out",
                Language.CHINESE: "保留邮箱超时"
            },
            "getting_email_list": {
                Language.ENGLISH: "Getting email list...",
                Language.CHINESE: "正在获取邮箱列表..."
            },
            "list_email_timeout": {
                Language.ENGLISH: "Getting email list timed out",
                Language.CHINESE: "获取邮箱列表超时"
            },
            "list_email_failed": {
                Language.ENGLISH: "Failed to get email list: {0}",
                Language.CHINESE: "获取邮箱列表失败: {0}"
            },
            "deleting_email": {
                Language.ENGLISH: "Deleting email {0}...",
                Language.CHINESE: "正在删除邮箱 {0}..."
            },
            "delete_email_timeout": {
                Language.ENGLISH: "Deleting email timed out",
                Language.CHINESE: "删除邮箱超时"
            },
            "delete_email_failed": {
                Language.ENGLISH: "Failed to delete email: {0}",
                Language.CHINESE: "删除邮箱失败: {0}"
            },
            
            # go_cursor_help.py
            "current_operating_system": {
                Language.ENGLISH: "Current operating system: {0}",
                Language.CHINESE: "当前操作系统: {0}"
            },
            "executing_macos_command": {
                Language.ENGLISH: "Executing macOS command",
                Language.CHINESE: "执行macOS命令"
            },
            "executing_linux_command": {
                Language.ENGLISH: "Executing Linux command",
                Language.CHINESE: "执行Linux命令"
            },
            "executing_windows_command": {
                Language.ENGLISH: "Executing Windows command",
                Language.CHINESE: "执行Windows命令"
            },
            
            # exit_cursor.py
            "starting_cursor_exit": {
                Language.ENGLISH: "Starting to exit Cursor...",
                Language.CHINESE: "开始退出Cursor..."
            },
            "no_cursor_processes_found": {
                Language.ENGLISH: "No running Cursor processes found",
                Language.CHINESE: "未发现运行中的 Cursor 进程"
            },
            "all_cursor_processes_closed": {
                Language.ENGLISH: "All Cursor processes have been closed normally",
                Language.CHINESE: "所有 Cursor 进程已正常关闭"
            },
            "processes_not_closed_in_time": {
                Language.ENGLISH: "The following processes did not close within the time limit: {0}",
                Language.CHINESE: "以下进程未能在规定时间内关闭: {0}"
            },
            "error_closing_cursor": {
                Language.ENGLISH: "Error occurred while closing Cursor processes: {0}",
                Language.CHINESE: "关闭 Cursor 进程时发生错误: {0}"
            },
            
            # patch_cursor_get_machine_id.py
            "cursor_path_not_found_linux": {
                Language.ENGLISH: "Cursor installation path not found on Linux system",
                Language.CHINESE: "在 Linux 系统上未找到 Cursor 安装路径"
            },
            "cursor_path_not_default": {
                Language.ENGLISH: "Your Cursor installation is not in the default path, please create a symbolic link with the following command:",
                Language.CHINESE: "可能您的Cursor不是默认安装路径,请创建软连接,命令如下:"
            },
            "create_symlink_command": {
                Language.ENGLISH: 'cmd /c mklink /d "C:\\Users\\<username>\\AppData\\Local\\Programs\\Cursor" "default installation path"',
                Language.CHINESE: 'cmd /c mklink /d "C:\\Users\\<username>\\AppData\\Local\\Programs\\Cursor" "默认安装路径"'
            },
            "example_command": {
                Language.ENGLISH: "For example:",
                Language.CHINESE: "例如:"
            },
            "example_command_path": {
                Language.ENGLISH: 'cmd /c mklink /d "C:\\Users\\<username>\\AppData\\Local\\Programs\\Cursor" "D:\\SoftWare\\cursor"',
                Language.CHINESE: 'cmd /c mklink /d "C:\\Users\\<username>\\AppData\\Local\\Programs\\Cursor" "D:\\SoftWare\\cursor"'
            },
            "file_not_exist": {
                Language.ENGLISH: "File does not exist: {0}",
                Language.CHINESE: "文件不存在: {0}"
            },
            "file_no_write_permission": {
                Language.ENGLISH: "No write permission for file: {0}",
                Language.CHINESE: "没有文件写入权限: {0}"
            },
            "invalid_version_format": {
                Language.ENGLISH: "Invalid version format: {0}",
                Language.CHINESE: "无效的版本号格式: {0}"
            },
            "version_below_minimum": {
                Language.ENGLISH: "Version {0} is below the minimum requirement {1}",
                Language.CHINESE: "版本号 {0} 小于最小要求 {1}"
            },
            "version_above_maximum": {
                Language.ENGLISH: "Version {0} is above the maximum requirement {1}",
                Language.CHINESE: "版本号 {0} 大于最大要求 {1}"
            },
            "version_check_failed": {
                Language.ENGLISH: "Version check failed: {0}",
                Language.CHINESE: "版本检查失败: {0}"
            },
            "file_modified_success": {
                Language.ENGLISH: "File modified successfully",
                Language.CHINESE: "文件修改成功"
            },
            "file_modification_error": {
                Language.ENGLISH: "Error while modifying file: {0}",
                Language.CHINESE: "修改文件时发生错误: {0}"
            },
            "mainjs_backup_created": {
                Language.ENGLISH: "main.js backed up: {0}",
                Language.CHINESE: "已备份 main.js: {0}"
            },
            "backup_failed": {
                Language.ENGLISH: "File backup failed: {0}",
                Language.CHINESE: "备份文件失败: {0}"
            },
            "mainjs_restored": {
                Language.ENGLISH: "main.js has been restored",
                Language.CHINESE: "已恢复 main.js"
            },
            "backup_not_found": {
                Language.ENGLISH: "Backup file not found",
                Language.CHINESE: "未找到备份文件"
            },
            "restore_backup_failed": {
                Language.ENGLISH: "Failed to restore backup: {0}",
                Language.CHINESE: "恢复备份失败: {0}"
            },
            "script_execution_started": {
                Language.ENGLISH: "Script execution started...",
                Language.CHINESE: "开始执行脚本..."
            },
            "backup_restore_complete": {
                Language.ENGLISH: "Backup restoration complete",
                Language.CHINESE: "备份恢复完成"
            },
            "backup_restore_failed": {
                Language.ENGLISH: "Backup restoration failed",
                Language.CHINESE: "备份恢复失败"
            },
            "current_cursor_version": {
                Language.ENGLISH: "Current Cursor version: {0}",
                Language.CHINESE: "当前 Cursor 版本: {0}"
            },
            "reading_version_failed": {
                Language.ENGLISH: "Failed to read version: {0}",
                Language.CHINESE: "无法读取版本号: {0}"
            },
            "version_not_supported": {
                Language.ENGLISH: "Version not supported (requires >= 0.45.x)",
                Language.CHINESE: "版本不符合要求（需 >= 0.45.x）"
            },
            "version_check_passed": {
                Language.ENGLISH: "Version check passed, preparing to modify files",
                Language.CHINESE: "版本检查通过，准备修改文件"
            },
            "backup_failed_abort": {
                Language.ENGLISH: "File backup failed, aborting operation",
                Language.CHINESE: "文件备份失败，终止操作"
            },
            "script_execution_complete": {
                Language.ENGLISH: "Script execution complete",
                Language.CHINESE: "脚本执行完成"
            },
            "execution_error": {
                Language.ENGLISH: "Error during execution: {0}",
                Language.CHINESE: "执行过程中发生错误: {0}"
            },
            "press_enter_exit": {
                Language.ENGLISH: "\nExecution complete, press Enter to exit...",
                Language.CHINESE: "\n程序执行完毕，按回车键退出..."
            },
            
            # New translation keys for config.py
            "env_file_not_exist": {
                Language.ENGLISH: "File {0} does not exist",
                Language.CHINESE: "文件 {0} 不存在"
            },
            "icloud_email": {
                Language.ENGLISH: "iCloud Email",
                Language.CHINESE: "iCloud 邮箱"
            },
            "icloud_app_password": {
                Language.ENGLISH: "iCloud App Password",
                Language.CHINESE: "iCloud 应用专用密码"
            },
            "config_not_set": {
                Language.ENGLISH: "{name} not configured, please set {key} in the .env file",
                Language.CHINESE: "{name}未配置，请在 .env 文件中设置 {key}"
            },
            "icloud_email_info": {
                Language.ENGLISH: "iCloud Email: {0}@icloud.com",
                Language.CHINESE: "iCloud 邮箱: {0}@icloud.com"
            },
            "icloud_password_info": {
                Language.ENGLISH: "iCloud App Password: {0}",
                Language.CHINESE: "iCloud 应用专用密码: {0}"
            },
            "env_loaded_success": {
                Language.ENGLISH: "Environment variables loaded successfully!",
                Language.CHINESE: "环境变量加载成功！"
            },
            "error_message": {
                Language.ENGLISH: "Error: {0}",
                Language.CHINESE: "错误: {0}"
            },
            "reading_version_failed": {
                Language.ENGLISH: "Failed to read version: {0}",
                Language.CHINESE: "无法读取版本号: {0}"
            },
            # New translation keys for cursor_pro_keep_alive.py
            "screenshot_saved": {
                Language.ENGLISH: "Screenshot saved: {0}",
                Language.CHINESE: "截图已保存: {0}"
            },
            "screenshot_save_failed": {
                Language.ENGLISH: "Failed to save screenshot: {0}",
                Language.CHINESE: "截图保存失败: {0}"
            },
            "verification_success_page": {
                Language.ENGLISH: "Verification success - Reached {0} page",
                Language.CHINESE: "验证成功 - 已到达{0}页面"
            },
            "detecting_turnstile": {
                Language.ENGLISH: "Detecting Turnstile verification...",
                Language.CHINESE: "正在检测 Turnstile 验证..."
            },
            "verification_attempt": {
                Language.ENGLISH: "Verification attempt {0}",
                Language.CHINESE: "第 {0} 次尝试验证"
            },
            "turnstile_detected": {
                Language.ENGLISH: "Turnstile verification detected, processing...",
                Language.CHINESE: "检测到 Turnstile 验证框，开始处理..."
            },
            "turnstile_passed": {
                Language.ENGLISH: "Turnstile verification passed",
                Language.CHINESE: "Turnstile 验证通过"
            },
            "attempt_failed": {
                Language.ENGLISH: "Current attempt failed: {0}",
                Language.CHINESE: "当前尝试未成功: {0}"
            },
            "verification_max_retries_reached": {
                Language.ENGLISH: "Verification failed - Maximum retries reached: {0}",
                Language.CHINESE: "验证失败 - 已达到最大重试次数 {0}"
            },
            "visit_project_for_info": {
                Language.ENGLISH: "Please visit the open source project for more information: https://github.com/Ryan0204/cursor-auto-icloud",
                Language.CHINESE: "请前往开源项目查看更多信息：https://github.com/Ryan0204/cursor-auto-icloud"
            },
            "turnstile_exception": {
                Language.ENGLISH: "Turnstile verification process exception: {0}",
                Language.CHINESE: "Turnstile 验证过程发生异常: {0}"
            },
            "getting_cookies": {
                Language.ENGLISH: "Getting cookies",
                Language.CHINESE: "开始获取cookie"
            },
            "token_attempt_failed": {
                Language.ENGLISH: "Attempt {0} failed to get CursorSessionToken, retrying in {1} seconds...",
                Language.CHINESE: "第 {0} 次尝试未获取到CursorSessionToken，{1}秒后重试..."
            },
            "token_max_attempts": {
                Language.ENGLISH: "Maximum attempts reached ({0}), failed to get CursorSessionToken",
                Language.CHINESE: "已达到最大尝试次数({0})，获取CursorSessionToken失败"
            },
            "get_cookie_failed": {
                Language.ENGLISH: "Failed to get cookie: {0}",
                Language.CHINESE: "获取cookie失败: {0}"
            },
            "retry_in_seconds": {
                Language.ENGLISH: "Will retry in {0} seconds...",
                Language.CHINESE: "将在 {0} 秒后重试..."
            },
            "env_file_load_failed": {
                Language.ENGLISH: "Failed to load .env file: {0}",
                Language.CHINESE: "加载 .env 文件失败: {0}"
            },
            "icloud_feature_enabled": {
                Language.ENGLISH: "iCloud hidden email feature enabled",
                Language.CHINESE: "已启用 iCloud 隐藏邮箱功能"
            },
            "icloud_module_import_failed_local": {
                Language.ENGLISH: "Failed to import iCloud email module, will use local email list",
                Language.CHINESE: "导入 iCloud 邮箱生成模块失败，将使用本地邮箱列表"
            },
            "names_dataset_loaded": {
                Language.ENGLISH: "Names dataset loaded from {0}",
                Language.CHINESE: "名称数据集已从 {0} 加载"
            },
            "names_dataset_not_found": {
                Language.ENGLISH: "Names dataset file not found in any known location",
                Language.CHINESE: "未在任何已知位置找到名称数据集文件"
            },
            "icloud_email_gen_failed": {
                Language.ENGLISH: "iCloud email generation failed, will use local email list",
                Language.CHINESE: "iCloud 邮箱生成失败，将使用本地邮箱列表"
            },
            "icloud_email_gen_error": {
                Language.ENGLISH: "iCloud email generation error: {0}",
                Language.CHINESE: "iCloud 邮箱生成失败: {0}"
            },
            "using_local_email_list": {
                Language.ENGLISH: "Using local email list",
                Language.CHINESE: "将使用本地邮箱列表"
            },
            "empty_email_file_created": {
                Language.ENGLISH: "Created empty email list file at {0}",
                Language.CHINESE: "已在 {0} 创建空的邮箱列表文件"
            },
            "email_list_empty": {
                Language.ENGLISH: "Email list is empty, program execution completed",
                Language.CHINESE: "邮箱列表为空，程序执行完毕"
            },
            "email_file_read_error": {
                Language.ENGLISH: "Error reading email file: {0}",
                Language.CHINESE: "读取邮箱文件时出错: {0}"
            },
            "get_user_agent_failed": {
                Language.ENGLISH: "Failed to get user agent: {0}",
                Language.CHINESE: "获取user agent失败: {0}"
            },
            "saving_account_to_csv": {
                Language.ENGLISH: "Saving account information to CSV file: {0}",
                Language.CHINESE: "正在保存账号信息到CSV文件: {0}"
            },
            "account_saved_to_csv": {
                Language.ENGLISH: "Account information saved to {0}",
                Language.CHINESE: "账号信息已保存至 {0}"
            },
            "save_account_failed": {
                Language.ENGLISH: "Failed to save account information: {0}",
                Language.CHINESE: "保存账号信息失败: {0}"
            },
            # New translation keys for get_email_code.py
            "verification_code_attempt": {
                Language.ENGLISH: "Attempting to get verification code (attempt {0}/{1})...",
                Language.CHINESE: "尝试获取验证码 (第 {0}/{1} 次)..."
            },
            "verification_code_not_found_retry": {
                Language.ENGLISH: "Verification code not found, retrying in {0} seconds...",
                Language.CHINESE: "未获取到验证码，{0} 秒后重试..."
            },
            "verification_code_fetch_failed": {
                Language.ENGLISH: "Failed to get verification code: {0}",
                Language.CHINESE: "获取验证码失败: {0}"
            },
            "error_will_retry": {
                Language.ENGLISH: "An error occurred, will retry in {0} seconds...",
                Language.CHINESE: "发生错误，{0} 秒后重试..."
            },
            "max_retries_reached_with_error": {
                Language.ENGLISH: "Failed to get verification code and reached maximum retries: {0}",
                Language.CHINESE: "获取验证码失败且已达最大重试次数: {0}"
            },
            "verification_code_not_found_after_attempts": {
                Language.ENGLISH: "Verification code not found after {0} attempts.",
                Language.CHINESE: "经过 {0} 次尝试后仍未获取到验证码。"
            },
            "using_icloud_imap": {
                Language.ENGLISH: "Using iCloud IMAP to get email...",
                Language.CHINESE: "使用 iCloud IMAP 获取邮件..."
            },
            "verification_code_timeout": {
                Language.ENGLISH: "Verification code retrieval timed out",
                Language.CHINESE: "获取验证码超时"
            },
            "icloud_email_list_failed": {
                Language.ENGLISH: "Failed to get iCloud email list: {0}",
                Language.CHINESE: "获取 iCloud 邮件列表失败: {0}"
            },
            "no_emails_in_icloud": {
                Language.ENGLISH: "No emails found in iCloud mailbox",
                Language.CHINESE: "iCloud 邮箱中没有找到邮件"
            },
            "icloud_imap_fetch_failed": {
                Language.ENGLISH: "iCloud IMAP fetch failed: {0}",
                Language.CHINESE: "iCloud IMAP fetch failed: {0}"
            },
            "icloud_imap_fetch_status_failed": {
                Language.ENGLISH: "iCloud IMAP fetch failed with status: {0}",
                Language.CHINESE: "iCloud IMAP fetch failed with status: {0}"
            },
            "verification_code_found_in_email": {
                Language.ENGLISH: "Verification code found in iCloud email: {0}",
                Language.CHINESE: "从 iCloud 邮件中找到验证码: {0}"
            },
            "no_verification_code_in_email": {
                Language.ENGLISH: "No verification code found in iCloud emails",
                Language.CHINESE: "在 iCloud 邮件中未找到验证码"
            },
            "icloud_imap_operation_failed": {
                Language.ENGLISH: "iCloud IMAP operation failed: {0}",
                Language.CHINESE: "iCloud IMAP 操作失败: {0}"
            },
            "email_body_decode_failed": {
                Language.ENGLISH: "Failed to decode email body: {0}",
                Language.CHINESE: "解码邮件正文失败: {0}"
            },
            # Token refresh translations
            "token_refresh_success": {
                Language.ENGLISH: "Successfully refreshed token",
                Language.CHINESE: "成功刷新令牌"
            },
            "token_refresh_failed": {
                Language.ENGLISH: "Failed to refresh token: {0}",
                Language.CHINESE: "刷新令牌失败: {0}"
            },
            "token_refresh_exception": {
                Language.ENGLISH: "Exception during token refresh: {0}",
                Language.CHINESE: "刷新令牌过程中发生异常: {0}"
            },
            # New translations for get_cursor_session_token function
            "start_getting_session_token": {
                Language.ENGLISH: "Starting to get session token",
                Language.CHINESE: "开始获取会话令牌"
            },
            "try_deep_login": {
                Language.ENGLISH: "Trying to get token using deep login method",
                Language.CHINESE: "尝试使用深度登录方式获取token"
            },
            "visiting_deep_login_url": {
                Language.ENGLISH: "Visiting deep login URL: {0}",
                Language.CHINESE: "访问深度登录URL: {0}"
            },
            "clicking_confirm_login": {
                Language.ENGLISH: "Clicking login confirmation button",
                Language.CHINESE: "点击确认登录按钮"
            },
            "polling_auth_status": {
                Language.ENGLISH: "Polling authentication status: {0}",
                Language.CHINESE: "轮询认证状态: {0}"
            },
            "token_userid_success": {
                Language.ENGLISH: "Successfully obtained account token and userId",
                Language.CHINESE: "成功获取账号token和userId"
            },
            "api_request_failed": {
                Language.ENGLISH: "API request failed with status code: {0}",
                Language.CHINESE: "API请求失败，状态码: {0}"
            },
            "login_confirm_button_not_found": {
                Language.ENGLISH: "Login confirmation button not found",
                Language.CHINESE: "未找到登录确认按钮"
            },
            "deep_login_token_failed": {
                Language.ENGLISH: "Deep login token acquisition failed: {0}",
                Language.CHINESE: "深度登录获取token失败: {0}"
            },
            "max_attempts_reached": {
                Language.ENGLISH: "Maximum attempts reached ({0}), failed to get session token",
                Language.CHINESE: "已达到最大尝试次数({0})，获取会话令牌失败"
            },
        }
    
    def get_text(self, key: str, *args) -> str:
        """
        Get translated text for the current language
        
        Args:
            key: The translation key
            *args: Optional format arguments
            
        Returns:
            str: The translated text
        """
        if key not in self._translations:
            # Fallback to key if translation not found
            return key
            
        translation = self._translations[key].get(self.current_language, key)
        
        # Apply formatting if args are provided
        if args:
            try:
                return translation.format(*args)
            except:
                return translation
                
        return translation
    
    def switch_language(self, language: Language) -> None:
        """
        Switch the current language
        
        Args:
            language: The language to switch to
        """
        self.current_language = language
        
    def toggle_language(self) -> Language:
        """
        Toggle between available languages
        
        Returns:
            Language: The new language
        """
        if self.current_language == Language.ENGLISH:
            self.current_language = Language.CHINESE
        else:
            self.current_language = Language.ENGLISH
            
        return self.current_language
        
    def select_language(self) -> Language:
        """
        Prompt user to select a language
        
        Returns:
            Language: The selected language
        """
        while True:
            try:
                choice = input(self.get_text("select_new_language")).strip()
                if choice == "1":
                    self.current_language = Language.ENGLISH
                    print(self.get_text("language_switched"))
                    break
                elif choice == "2":
                    self.current_language = Language.CHINESE
                    print(self.get_text("language_switched"))
                    break
                else:
                    print(self.get_text("invalid_option"))
            except ValueError:
                print(self.get_text("enter_valid_number"))
                
        return self.current_language


# Helper function for easier access to translations
def _(key: str, *args) -> str:
    """
    Shorthand function to get translated text
    
    Args:
        key: The translation key
        *args: Optional format arguments
        
    Returns:
        str: The translated text
    """
    return LanguageManager().get_text(key, *args)

# More descriptive alternative to _()
def getTranslation(key: str, *args) -> str:
    """
    Get translated text for the current language setting
    
    This is a more descriptive alternative to the shorthand _() function
    
    Args:
        key: The translation key
        *args: Optional format arguments
        
    Returns:
        str: The translated text
    """
    return LanguageManager().get_text(key, *args) 