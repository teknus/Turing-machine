from Tape import Tape
payload = "_ 1 _"

def create():
    return Tape(payload,['0','1'],blank="_")
payloadLen = payload.split()

def test_leftCreation():
    tape = create()
    tape.moveHeadToLeft()
    assert tape.readFromTape() == "_"

def test_rightMove():
    tape = create()
    tape.moveHeadToRight()
    assert tape.readFromTape() == "1"

def test_MoveInfinityLeft():
    tape = create()
    i = 2
    for j in range(i):
        tape.moveHeadToLeft()
    assert tape.readFromTape() == "_"

def test_MoveInfinityRigth():
    tape = create()
    i = 5
    for j in range(i):
        tape.moveHeadToRight()
    assert tape.readFromTape() == "_"

def test_MoveRightAndLeft():
    tape = create()
    tape.moveHeadToRight()
    tape.moveHeadToRight()
    tape.moveHeadToRight()
    tape.moveHeadToLeft()
    tape.moveHeadToLeft()
    assert tape.readFromTape() == "1"
