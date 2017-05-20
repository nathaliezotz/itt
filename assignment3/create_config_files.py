import sys
import random


def createConfigFiles(num_files):
    stimuli = []

    for x in range(5):
        stimuli.append('ADB')
        stimuli.append('ADR')
        stimuli.append('ANB')
        stimuli.append('ANR')
        stimuli.append('PDE')
        stimuli.append('PDO')
        stimuli.append('PNE')
        stimuli.append('PNO')

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
