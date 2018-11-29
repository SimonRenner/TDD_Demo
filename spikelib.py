def mean_rate(spikes, samplingrate):
    spikecount = sum(spikes)
    bincount = len(spikes)
    return spikecount / bincount * samplingrate

def create_testfile():
    pass

def read_data(filename):
    return spikes, samplingrate

def save_data(filename):
    pass