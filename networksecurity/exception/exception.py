import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_details: Exception):
        self.error_message = error_message
        _, _, exc_tb = sys.exc_info()  # Get the traceback

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )

if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block")
        a = 1 / 0  # This will raise a ZeroDivisionError
        print('This will not be printed', a)
    except Exception as e:
        raise NetworkSecurityException("An error occurred during execution", e)