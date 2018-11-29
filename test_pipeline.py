from spikelib import mean_rate, read_data, save_data
from mock import patch
from os.path import isfile
from os import remove

@patch('spikelib.create_testfile')
@patch('spikelib.read_data', return_value = ([1,0,1,1,1,0], 40))
def test_mean_rate_pipeline_end_to_end(read_data, create_testfile):
    testfilename = 'testfile'
    with open(testfilename, 'w'):
        pass
    spikes, samplingrate = read_data(testfilename)
    remove(testfilename)
    assert not isfile(testfilename)
    assert spikes == [1,0,1,1,1,0]
    assert samplingrate == 40
    mrate = mean_rate(spikes, samplingrate)
    assert mrate == 4 / 6 * 40
    testfilename_analyzed = 'testfile_ana'
    save_data(testfilename_analyzed)
    with open(testfilename_analyzed, 'r') as file:
        read_mrate = file.read()
    assert read_mrate == str(mrate)
    remove(testfilename_analyzed)
    assert exists(testfilename_analyzed)