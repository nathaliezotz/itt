import sys
import random


def createConfigFiles(num_files):
    stimuli = []

    for x in range(5):
        stimuli.append('ADE')
        stimuli.append('ADO')
        stimuli.append('ANE')
        stimuli.append('ANO')
        stimuli.append('PDB')
        stimuli.append('PDR')
        stimuli.append('PNB')
        stimuli.append('PNR')


    for x in range(1, int(num_files)+1):
        print(x)
        random.shuffle(stimuli)

        with open('config_' + str(x), 'w') as config_file:
            config_file.write('PARTICIPANT: ' + str(x) + '\n')
            config_file.write('TRIALS: ' + str(stimuli))


def main():
    createConfigFiles(sys.argv[1])


if __name__ == '__main__':
    main()
