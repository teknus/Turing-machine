from typing import List, Dict, Tuple
from Tape import Tape
from copy import copy

from time import sleep
sleepTime = 1

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
        self.__return = list()

    def runCommand(self, state, command, symbol):
        sleep(sleepTime)
        if command[0] == "R":
            self.__tape.moveHeadToRight()
            symbol = self.__tape.readFromTape()
        elif command[0] == "L":
            self.__tape.moveHeadToLeft()
            symbol = self.__tape.readFromTape()
        else:
            self.__tape.writeOnTape(command[0])
            symbol = command[0]
        return symbol, {"instruction":command,"headPosition":copy(self.__tape.head)}
    
    def verifyState(self,state):
        ret = False
        for key,value in self.__commands:
            if (key,value) == state:
                ret = True
        return ret

    def show(self, arg):
        #print(*arg)
        self.__return.append(arg)

    def run(self):
        interations = 0
        state = (self.__listOfStates[0],self.__tape.blank)
        symbol = self.__tape.readFromTape()
        while interations < 10:
            sleep(sleepTime)
            interations += 1
            command = self.__commands[state]
            instruction = {"instruction":command,"headPosition":self.__tape.head}
            yield {"state":state,"tape":self.__tape.payload,"headPosition":self.__tape.head,"exec":instruction}
            symbol, instruction = self.runCommand(state,command,symbol)
            state = (command[1], symbol)
            sleep(sleepTime)
            if not self.verifyState(state):
                yield {"state":state,"tape":self.__tape.payload,"headPosition":self.__tape.head,"exec":{"instruction":("Exit",command[1]),"headPosition":self.__tape.head}}
                return 
