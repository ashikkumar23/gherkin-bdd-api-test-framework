class GeneralException(Exception):
    """Base class for other exceptions"""

    message = "[EXCEPTION: GENERAL_EXCEPTION] General exception"

    def __init__(self, msg=None):
        super().__init__(f"{self.message} - {msg}" if msg else self.message)


class FileNotFoundException(GeneralException):
    """Raised when the file is missing"""

    message = "[EXCEPTION: FILE_NOT_FOUND] File Not Found"


class InvalidFileFormatException(GeneralException):
    """Raised when the file format is invalid"""

    message = "[EXCEPTION: INVALID_FILE_FORMAT] Invalid File Format"
