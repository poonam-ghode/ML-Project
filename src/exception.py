import sys
from logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()#talks about execution info
    '''
        tells about three important thing
    
    '''
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occurred in python script name [{0}] error message [{1}]".format(
    file_name , exc_tb.tb_lineno, str(error)
    )
    return error_msg
    
    
class CustomException(Exception):
    def __init__(self, error_msg, error_detail:sys):
        super.__init__(error_msg)
        self.error_msg = error_message_detail(error_msg, error_detail = error_detail)
    
    def __str__(self):
        return self.error_msg
    
# if __name__=="__main__":
#     try:
#          a = 1/10
         
#     except Exception as e:
#         logging.info("Divided by zero")
#         raise CustomException(e, sys)
        