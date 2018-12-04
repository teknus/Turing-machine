from Machine import Machine
from Tape import Tape

payload = "_ 1 _"

def createTape():
    return Tape(payload,['0','1'],blank="_")
payloadLen = payload.split()
states = ["q1","q2"]
commands = {
    ("q1","_"):("R","q1"),
    ("q1","1"):("_","q2")
}
machine = Machine(states,commands,createTape())
print(machine.run())