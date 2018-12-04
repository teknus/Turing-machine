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

    def runCommand(self, command, symbol):
        if command[0] == "R":
#            print("Right")
            self.__tape.moveHeadToRight()
            symbol = self.__tape.readFromTape()
        elif command[0] == "L":
#            print("Left")
            self.__tape.moveHeadToLeft()
            symbol = self.__tape.readFromTape()
        else:
 #           print("Write")
            self.__tape.writeOnTape(command[0])
            symbol = command[0]
        return symbol
    
    def verifyState(self,state):
        ret = False
        for key,value in self.__commands:
            if (key,value) == state:
                ret = True
        return ret

    def run(self):
        interations = 0
        state = (self.__listOfStates[0],self.__tape.blank)
        symbol = self.__tape.readFromTape()
        while interations < 1000:
            interations += 1
            command, symbol = self.__commands[state]
            symbol = self.runCommand(command,symbol)
            state = (command[1], symbol)
            if not self.verifyState(state):
                return self.__tape