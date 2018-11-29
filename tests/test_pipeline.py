from spike_analysis.spikelib import mean_rate, read_data, save_data
from mock import patch
from os.path import isfile
from os import remove
from pytest import fixture

@fixture
def create_testfile():
    def _create_testfile(filename, line1, line2):
        with open(filename, 'w') as f:
            f.write(line1)
            f.write(line2)
    return _create_testfile

@fixture
def read_testfile():
    def _read_testfile(filename):
        with open(filename, 'r') as f:
            content = f.read()
        return float(content)
    return _read_testfile

def test_mean_rate_pipeline_end_to_end(create_testfile, read_testfile):
    testfilename = 'testfile'
    line1 = '40\n'
    line2 = '101110'
    create_testfile(testfilename, line1, line2)
    spikes, samplingrate = read_data(testfilename)
    remove(testfilename)
    assert not isfile(testfilename)
    assert samplingrate == 40
    assert spikes == [1,0,1,1,1,0]
    mrate = mean_rate(spikes, samplingrate)
    assert mrate == 4 / 6 * 40
    testfilename_analyzed = 'testfile_ana'
    save_data(testfilename_analyzed, mrate)
    read_mrate = read_testfile(testfilename_analyzed)
    assert mrate == read_mrate
    remove(testfilename_analyzed)
    assert not isfile(testfilename_analyzed)