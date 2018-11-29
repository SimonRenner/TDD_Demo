def mean_rate(spikes, samplingrate):
    spikecount = sum(spikes)
    bincount = len(spikes)
    return spikecount / bincount * samplingrate

def read_data(filename):
    return spikes, samplingrate

def save_data(filename, mrate):
    with open(filename, 'w') as f:
        f.write(str(mrate))