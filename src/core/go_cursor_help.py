import platform
import os
import subprocess
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
            return key

def go_cursor_help():
    system = platform.system()
    logging.info(getTranslation("current_operating_system").format(system))
    
    base_url = "https://aizaozao.com/accelerate.php/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run"
    
    if system == "Darwin":  # macOS
        cmd = f'curl -fsSL {base_url}/cursor_mac_id_modifier.sh | sudo bash'
        logging.info(getTranslation("executing_macos_command"))
        os.system(cmd)
    elif system == "Linux":
        cmd = f'curl -fsSL {base_url}/cursor_linux_id_modifier.sh | sudo bash'
        logging.info(getTranslation("executing_linux_command"))
        os.system(cmd)
    elif system == "Windows":
        cmd = f'irm {base_url}/cursor_win_id_modifier.ps1 | iex'
        logging.info(getTranslation("executing_windows_command"))
        # 在Windows上使用PowerShell执行命令
        subprocess.run(["powershell", "-Command", cmd], shell=True)
    else:
        logging.error(getTranslation("unsupported_os").format(system))
        return False
    
    return True
