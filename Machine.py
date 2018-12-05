from typing import List, Dict, Tuple
from Tape import Tape

from time import sleep
sleepTime = 1.5
timeOnPrint = 1

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
        print("\nExecutando ↪ Ação | Próximo Estado: ", command[0],command[1])
        sleep(sleepTime)
        if command[0] == "R":
            self.__tape.moveHeadToRight()
            symbol = self.__tape.readFromTape()
            print("Posição cabeçote:  ", self.__tape.head)
            sleep(timeOnPrint)
        elif command[0] == "L":
            self.__tape.moveHeadToLeft()
            symbol = self.__tape.readFromTape()
            print("Posição cabeçote:  ", self.__tape.head)
            sleep(timeOnPrint)
        else:
            self.__tape.writeOnTape(command[0])
            symbol = command[0]
            print("Posição cabeçote:  ", self.__tape.head)
            sleep(timeOnPrint)
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
        while interations < 10:
            sleep(sleepTime)
            interations += 1
            command = self.__commands[state]
            print("Estado | leitura atual: ", state[0]," ",state[1])
            sleep(timeOnPrint)
            print("Fita: ", self.__tape.payload)
            sleep(timeOnPrint)
            print("Posição do cabeçote: ",self.__tape.head)
            sleep(timeOnPrint)
            symbol = self.runCommand(state,command,symbol)
            state = (command[1], symbol)
            sleep(sleepTime)
            if not self.verifyState(state):
                sleep(sleepTime)
                print("Final Tape", self.__tape, "\nCabeçote: ",self.__tape.head,"\nEstado Atual: ", state[0]," ",state[1])
                return
        print("Final Tape", self.__tape, "\nCabeçote: ",self.__tape.head,"Estado Atual: ", state[0]," ",state[1])
