from typing import List

class Tape(object):
    def __init__(self, payload: str, alphabetSymbols: List[str]):
        self.__payload = payload.split()
        self.__blank = "_"
        self.__alphabetSymbols = alphabetSymbols
        self.__lowestIndex = 0
        self.__highestIndex = len(payload) - 2
        self.__head = 0

    def right(self):
        self.__head += 1
        print(self.__head,self.__highestIndex)
        if self.__head >= self.__highestIndex:
            self.__payload = self.__payload + [self.__blank]
            self.__highestIndex = len(self.__payload)
        print(self.__head,self.__payload)
    
    def left(self):
        self.__head -= 1
        if self.__head < self.__lowestIndex:
            self.__payload = [self.__blank] + self.__payload
            self.__highestIndex = len(self.__payload)
            self.__head = 0
        print(self.__head,self.__payload)

            
    
    def write(self, symbol: str):
        (self.__head,self.__payload)

    def getHead(self):
        return self.__payload[self.__head]

    def __getitem__(self,index):
        if index in range(self.__lowestIndex, self.__highestIndex):
            return self.__payload[index]
        else:
            return self.__blank
    
    def __len__(self):
        return len(self.__payload)
    
    def __str__(self):
        return str(self.__payload)