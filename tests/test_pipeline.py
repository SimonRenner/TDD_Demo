from spike_analysis.spikelib import mean_rate, read_data, save_data
from mock import patch
from os.path import isfile
from os import remove

def test_mean_rate_pipeline_end_to_end():
    testfilename = 'testfile'
    with open(testfilename, 'w') as file:
        file.write('40\n')
        file.write('101110')
    spikes, samplingrate = read_data(testfilename)
    remove(testfilename)
    assert not isfile(testfilename)
    assert samplingrate == 40
    assert spikes == [1,0,1,1,1,0]
    mrate = mean_rate(spikes, samplingrate)
    assert mrate == 4 / 6 * 40
    testfilename_analyzed = 'testfile_ana'
    save_data(testfilename_analyzed, mrate)
    with open(testfilename_analyzed, 'r') as file:
        read_mrate = file.read()
    assert str(mrate) == read_mrate
    remove(testfilename_analyzed)
    assert not isfile(testfilename_analyzed)