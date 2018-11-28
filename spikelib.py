def mean_rate(spikes, samplingrate):
    spikecount = sum(spikes)
    bincount = len(spikes)
    return spikecount / bincount / samplingrate