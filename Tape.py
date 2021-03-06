from typing import List

class Tape(object):
    def __init__(self, payload: str, alphabetSymbols: List[str],blank :str = "_"):
        self.__payload = payload.split()
        self.__blank = blank
        self.__alphabetSymbols = alphabetSymbols
        self.__lowestIndex = 0
        self.__highestIndex = len(payload) - 2
        self.__head = 0

    def moveHeadToRight(self):
        self.__head += 1
        print(self.__head,self.__highestIndex)
        if self.__head >= self.__highestIndex:
            self.__payload = self.__payload + [self.__blank]
            self.__highestIndex = len(self.__payload)
    
    def moveHeadToLeft(self):
        self.__head -= 1
        if self.__head < self.__lowestIndex:
            self.__payload = [self.__blank] + self.__payload
            self.__highestIndex = len(self.__payload)
            self.__head = 0

    def writeOnTape(self, symbol: str):
        (self.__head,self.__payload)

    def ReadFromTape(self):
        return self.__payload[self.__head]

#Attributes access
    @property
    def blank(self):
        return self.__blank

    @blank.setter
    def blank(self, symbol):
        self.__blank = symbol
        
    @property
    def payload(self):
        return self.__payload
    @property
    def head(self):
        return self.__head
#Magic
    def __str__(self):
        return str(self.__payload)

    def __eq__(self,other):
        for i in range(0,len(self.payload)-1):
            if self.__payload[i] != other.payload[i]:
                False
        return True