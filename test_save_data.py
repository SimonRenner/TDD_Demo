from spikelib import save_data
from os import remove
from os.path import isfile

def test_save_data():
    mrate = 25
    filename = 'testfile'
    save_data(filename, mrate)
    with open(filename, 'r') as f:
        read_mrate = int(f.read())
    remove(filename)
    assert not isfile(filename)
    assert read_mrate == mrate
    
        