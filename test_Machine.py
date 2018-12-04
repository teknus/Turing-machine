from Machine import Machine
from Tape import Tape

payload = "_ 1 _"

def createTape():
    return Tape(payload,['0','1'],blank="_")
payloadLen = payload.split()

def createMachine():
    states = ["q1","q2"]
    commands = {
        ("q1","1"):("q2","R"),
        ("q1","_"):("q1","R")
    }
    return Machine(states,commands,createTape())

def test_Run():
    assert createMachine().run() == createTape() 