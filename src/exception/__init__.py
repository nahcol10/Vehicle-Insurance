import sys
import logging
from typing import Any

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    Parameters:
        error: The exception that occurred
        error_detail: The sys module to access traceback details

    Returns:
        A formatted error message string with file location and error details
    """
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    # Log the error with appropriate severity
    logging.error(error_message)

    return error_message


class CustomException(Exception):
    """
    Custom exception class for handling application-specific errors with detailed tracking.
    Provides enhanced error reporting with file and line information.
    """

    def __init__(self, error_message: Any, error_detail: sys = sys) -> None:
        """
        Initializes the CustomException with a detailed error message.

        Parameters:
            error_message: Description of the error that occurred
            error_detail: The sys module to access traceback details (default: sys)
        """
        # Convert error_message to string if it's not already
        error_message = str(error_message)

        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.

        Returns:
            Formatted error message string
        """
        return self.error_message