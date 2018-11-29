from spike_analysis.spikelib import mean_rate, read_data, save_data
from spike_analysis import pipeline
from mock import patch
from os.path import isfile, dirname, abspath
from os import remove
from pytest import fixture, raises

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
    
def test_importable_pipeline(create_testfile, read_testfile):
    testfilename = 'testfile.txt'
    testfilepath = dirname(abspath(__file__))[:-5] + 'data/'
    line1 = '50\n'
    line2 = '100011010'
    mrate = 4 / 9 * 50
    create_testfile(testfilepath + testfilename, line1, line2)
    pipeline.main(testfilename)
    testfilename_analyzed = 'testfile_rate.txt'
    read_mrate = read_testfile(testfilepath + testfilename_analyzed)
    assert read_mrate == mrate
    remove(testfilepath + testfilename)
    remove(testfilepath + testfilename_analyzed)
    assert not isfile(testfilepath + testfilename)
    assert not isfile(testfilepath + testfilename_analyzed)
    
def test_importable_pipeline_raises_error_if_no_commandline_argument_is_supplied(create_testfile, read_testfile):
    testfilename = 'testfile.txt'
    testfilepath = dirname(abspath(__file__))[:-5] + 'data/'
    line1 = '50\n'
    line2 = '100011010'
    mrate = 4 / 9 * 50
    empty_argument = []
    create_testfile(testfilepath + testfilename, line1, line2)
    with raises(Exception):
        pipeline.main(empty_argument)
    remove(testfilepath + testfilename)
    assert not isfile(testfilepath + testfilename)