from os.path import dirname, abspath
from spikelib import read_data, mean_rate, save_data
from sys import argv

filepath = dirname(abspath(__file__))[:-14] + 'data/'
print(filepath)

def main():
    filename = 'exp1.txt'
    spikes, samplingrate = read_data(filepath + filename)
    mrate = mean_rate(spikes, samplingrate)
    filename_analyzed = filename[:-4] + '_rate.txt'
    save_data(filepath + filename_analyzed, mrate)
    
if __name__ == '__main__':
    main()