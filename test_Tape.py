from Tape import Tape
payload = "_ 1 _"
def create():
    return Tape(payload,['0','1'])
payloadLen = payload.split()

def test_leftCreation():
    tape = create()
    tape.left()
    assert tape.getHead() == "_"
    assert len(tape) == (len(payloadLen) + 1)

def test_rightMove():
    tape = create()
    tape.right()
    assert tape.getHead() == "1"
    assert len(tape) == len(payloadLen)

def test_MoveInfinityLeft():
    tape = create()
    i = 2
    for j in range(i):
        tape.left()
    assert len(tape) == len(payloadLen) + i
    assert tape.getHead() == "_"

def test_MoveInfinityRigth():
    tape = create()
    i = 5
    for j in range(i):
        tape.right()
    assert tape.getHead() == "_"

def test_MoveRightAndLeft():
    tape = create()
    tape.right()
    tape.right()
    tape.right()
    tape.left()
    tape.left()
    assert tape.getHead() == "1"
    assert len(tape) == len(payloadLen) + 1

