import os
import sys

def error_massage_details(error,error_details:sys):
        _,_,exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_massage = " error occur in python script name  [{0}] line number [{1} error massage [{2}]]".format(
        file_name,exc_tb.tb_lineno, str(error))

        return error_massage


class USvisaException(Exception):
        def __init__(self,error_massege, error_detail):
                """
                :param error_massage: error message in string 
                """
                super().__init__(error_massege)
                self.error_massage = error_massage_details(
                        error_massege, error_details=error_detail
                )

        def __str__(self):
                return self.error_massage