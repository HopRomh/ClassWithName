
import random
from File_libra_base import pri_log, suh_stv 

class FunRandomName():  
    def __init__(self): 
        self.__adjective = pri_log
        self.__essential = suh_stv

    def __get_random_adjective(self):
        return random.choice(self.__adjective)

    def __get_random__essential(self): 
        return random.choice(self.__essential)

    def get_name(self):
        adjective = self.__get_random_adjective()
        ssential = self.__get_random__essential()
        return f"{adjective} {ssential}"
    

fun_name_generator = FunRandomName()
print(fun_name_generator.get_name())