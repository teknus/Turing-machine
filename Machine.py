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
        self.__listOfStates = listOfStates
        self.__commands = commands
        self.__tape = tape

    def run(self):
        state = (self.__listOfStates[0],self.__tape.blank)
        symbol = self.__tape.ReadFromTape()
        while True:
            command = self.__commands[state]
            if command != None:
                return self.__tape
        pass