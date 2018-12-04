from Machine import Machine
from Tape import Tape

i = None
states = None
alphabet = None
input_data = None
commands = None
with open("instance.tm") as file:
    i = int(file.readline())
    states = file.readline().split()
    alphabet = file.readline()
    input_data = file.readline()
    commands = dict()
    while i > 0:
        line = file.readline()
        slpited_line = line.strip().split(" ")
        commands[(slpited_line[0],slpited_line[1].rstrip())] = (slpited_line[2],slpited_line[3])
        i -= 1

payload = input_data

def createTape():
    return Tape(payload,alphabet,blank="_")
payloadLen = payload.split()
machine = Machine(states,commands,createTape())
machine.run()