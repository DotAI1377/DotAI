import logging

def setup_logger(name, log_file, level=logging.INFO):
    """
    Sets up a logger with the specified name, log file, and logging level.

    Args:
        name (str): The name of the logger.
        log_file (str): The file to which logs will be written.
        level (int): The logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        logging.Logger: Configured logger instance.
    """
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger("example_logger", "example.log")
    logger.info("This is an info message")
    logger.error("This is an error message")
