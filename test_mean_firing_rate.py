from spikelib import mean_rate

def test_mean_rate():
    spikes = [1,0,0,1,0,1]
    samplingrate = 50
    mrate = mean_rate(spikes, samplingrate)
    assert mrate == 3 / 6 * 50