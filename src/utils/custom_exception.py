import sys

class CustomException(Exception):
    def __init__(self, message : str , error_details : Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_details)
        super().__init__(self.error_message)
    
    @staticmethod
    def get_detailed_error_message(message : str, error_details : Exception = None):
        _,_,exc_tb = sys.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown file"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown line"
        return f"Error occurred in file: {filename} at line number: {line_number} with message: {message} and error details: {str(error_details)}"
    
    def __str__(self):
        return self.error_message
    