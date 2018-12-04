from typing import List, Dict, Tuple
from Tape import Tape

class Machine:
    def __init__(self,listOfStates :List[str] ,
        commands:Dict[Tuple[str,str],Tuple[str,str]],
        tape: Tape,
        leftSymbol:str="L", 
        rightSymbol:str="R"
        ):
        self.__leftSymbol = leftSymbol
        self.__rightSymbol = rightSymbol
        self.__actualState = listOfStates
        self.__listOfStates = listOfStates
        self.__commands = commands
        self.__tape = 
    def run():
        pass