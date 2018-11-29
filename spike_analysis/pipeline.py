from os.path import dirname, abspath
from spike_analysis.spikelib import read_data, mean_rate, save_data
from sys import argv

filepath = dirname(abspath(__file__))[:-14] + 'data/'

def main(filename):
    if filename == []:
        raise NameError('no filename to analyze specified')
    else:
        filename = filename[0]
        spikes, samplingrate = read_data(filepath + filename)
        mrate = mean_rate(spikes, samplingrate)
        filename_analyzed = filename[:-4] + '_rate.txt'
        save_data(filepath + filename_analyzed, mrate)
    
if __name__ == '__main__':
    main(argv[1:])