from spikelib import save_data

def test_save_data():
    mrate = 25
    filename = 'testfile'
    save_data(filename, mrate)
    with open(filename, 'r') as f:
        read_mrate = int(f.read())
    assert read_mrate == mrate
        