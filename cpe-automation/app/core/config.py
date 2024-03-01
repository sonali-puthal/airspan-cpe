import logging
import pathlib
import sys


def initialize_logging(
    filename: str = "logs/icnt_runtime.log",
    log_level_file: int = logging.DEBUG,
    log_level_console: int = logging.INFO,
    disable_logging: bool = False,
) -> None:
    """
    Initialize logging for the icnt application project.
    Creates a file handler and a console handler for the root logger and sets the log levels for each handler.
    Call this once at the start of the application to initialize the root logger

    :param filename: name(+path) of the log file to write to.
    :param log_level_file: log level for the file handler
    :param log_level_console: log level for the console handler
    :param disable_logging:  if True, disable all logging
    """
    DATEFORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%S"

    # respecting the log disable option in the global config file
    if disable_logging:
        logging.disable(logging.CRITICAL + 1)  # block everything including CRITICAL

    root_logger = logging.getLogger()
    # 'root' logger's log level is by default WARNING.
    # This cause effective log level to be WARNING even when other child loggers have lower log levels
    root_logger.setLevel(logging.DEBUG)

    if not pathlib.Path(filename).exists():
        pathlib.Path(filename).parent.mkdir(mode=0o777, parents=True, exist_ok=True)

    # create handler for logging to file
    file_log_handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
    file_log_handler.setLevel(log_level_file)
    file_log_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s.%(msecs)03d] [%(levelname)-8s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s",
            datefmt=DATEFORMAT_ISO_8601,
        )
    )
    root_logger.addHandler(file_log_handler)

    # create handler for logging to stdout
    console_log_handler = logging.StreamHandler(sys.stdout)
    console_log_handler.setLevel(log_level_console)
    console_log_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s",
            datefmt=DATEFORMAT_ISO_8601,
        )
    )
    root_logger.addHandler(console_log_handler)

