import logging
import os
import sys
from datetime import datetime

# Import translation utilities
try:
    from src.utils.language import getTranslation, _
except ImportError:
    try:
        from utils.language import getTranslation, _
    except ImportError:
        # Fallback if language module is not available
        def getTranslation(key, *args):
            if args:
                return key.format(*args)
            return key

# Global variable to track if logger has been initialized
_logger_initialized = False

def initialize_logger():
    """Initialize logger if not already initialized"""
    global _logger_initialized
    
    if _logger_initialized:
        return
    
    # Configure logging - determine the log directory based on whether we're in a frozen executable
    if getattr(sys, 'frozen', False):
        # If we're running in a PyInstaller bundle, use the directory of the executable
        application_path = os.path.dirname(sys.executable)
        log_dir = os.path.join(application_path, "logs")
    else:
        # If we're in development environment, use the existing path
        log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "logs")
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    class PrefixFormatter(logging.Formatter):
        """自定义格式化器，为 DEBUG 级别日志添加开源项目前缀"""

        def format(self, record):
            if record.levelno == logging.DEBUG:  # 只给 DEBUG 级别添加前缀
                record.msg = getTranslation("debug_prefix_format").format(record.msg)
            return super().format(record)

    # Clear any existing handlers
    root_logger = logging.getLogger()
    if root_logger.handlers:
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)

    # Configure basic logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(
                os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log"),
                encoding="utf-8",
            ),
        ],
    )

    # 为文件处理器设置自定义格式化器
    for handler in logging.getLogger().handlers:
        if isinstance(handler, logging.FileHandler):
            handler.setFormatter(
                PrefixFormatter("%(asctime)s - %(levelname)s - %(message)s")
            )

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(PrefixFormatter("%(message)s"))

    # 将控制台处理器添加到日志记录器
    logging.getLogger().addHandler(console_handler)

    # 打印日志目录所在路径
    logging.info(getTranslation("logger_initialized").format(os.path.abspath(log_dir)))
    
    _logger_initialized = True

# Initialize logger when module is imported
initialize_logger()

# Rest of the original code
def main_task():
    """
    Main task execution function. Simulates a workflow and handles errors.
    """
    try:
        logging.info(getTranslation("main_task_starting"))

        # Simulated task and error condition
        if some_condition():
            raise ValueError(getTranslation("simulated_error"))

        logging.info(getTranslation("main_task_completed"))

    except ValueError as ve:
        logging.error(getTranslation("value_error_occurred").format(ve), exc_info=True)
    except Exception as e:
        logging.error(getTranslation("unexpected_error_occurred").format(e), exc_info=True)
    finally:
        logging.info(getTranslation("task_execution_finished"))


def some_condition():
    """
    Simulates an error condition. Returns True to trigger an error.
    Replace this logic with actual task conditions.
    """
    return True


if __name__ == "__main__":
    # Application workflow
    logging.info(getTranslation("application_started"))
    main_task()
    logging.info(getTranslation("application_exited"))
