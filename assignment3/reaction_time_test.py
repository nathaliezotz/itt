# participant ID
# shown stimulus (concrete word/color/number/etc.),
# mental complexity (pre-attentive vs. attentive) of stimulus
# distraction (yes/no)
# pressed key
# whether the correct key was pressed
# reaction time
# timestamp
# all other information you deem important


"""
A = Attentive (Even/Odd)
P = Pre-Attentive (Red/Blue)

D = Distraction
N = No Distraction

B = Blau
R = Rot

E = Even
O = Odd

5xADB f
5xADR j

5xANB f
5xANR j

5xPDE f
5xPDO j

5xPNE f
5xPNO j
"""

# ADB ANB PDE PNE


'''
TODO:
nicht das ganze fenster mit blinkenden quadraten vollmachen sondenr in der mitte etwas platz lassen?

start taskXXX x 8

pause screen (drawPause)
Handle Input
Logging (writeLogToFile)


'''

import csv
import os
import random
import sys
import datetime
from PyQt5 import QtGui, QtWidgets, QtCore


class ReactionTimeExperiment(QtWidgets.QWidget):

    WIDTH = 960
    HEIGHT = 960
    NUM_SQUARES = 10
    SQUARE_WIDTH = WIDTH / NUM_SQUARES
    SQUARE_HEIGHT = HEIGHT / NUM_SQUARES
    BLINK_SPEED = 1000

    def __init__(self):
        super().__init__()
        self.initUI()
        self.initConfig()

        self.current_task = -1
        self.current_state = 'Pause'

        self.tasks = {'ADB': self.taskADB(),
                      'ADR': self.taskADR(),
                      'ANB': self.taskANB(),
                      'ANR': self.taskANR(),
                      'PDE': self.taskPDE(),
                      'PDO': self.taskPDO(),
                      'PNE': self.taskPNE(),
                      'PNO': self.taskPNO()}

        self.counter = 0
        self.current_trial = None
        self.timer_draw = QtCore.QTimer(self)
        self.timer_draw.timeout.connect(self.drawDistraction)
        self.timer_draw.start(self.BLINK_SPEED)

# participant ID
# shown stimulus (concrete word/color/number/etc.),
# mental complexity (pre-attentive vs. attentive) of stimulus
# distraction (yes/no)
# pressed key
# whether the correct key was pressed
# reaction time
# timestamp
# all other information you deem important
        self.logging_dict = {'id': [],
                             'shown_stimulus': [],
                             'mental_complexity': [],
                             'distraction': [],
                             'pressed_key': [],
                             'correct_key_pressed': [],
                             'reaction_time_in_microseconds': [],
                             'timestamp': [],
                             }


    def initUI(self):
        # setGeometry(int posx, int posy, int w, int h)
        self.setGeometry(480, 480, self.WIDTH, self.HEIGHT)
        self.setWindowTitle('Reaction Time Experiment')
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.show()

    def initConfig(self):
        with open(sys.argv[1]) as config_file:
            for line in config_file:
                if line.startswith('PARTICIPANT'):
                    print(line)
                    self.participant_id = line.split(" ")[1].rstrip()
                elif line.startswith('TRIALS'):
                    print(line)
                    self.trials = line.split('[')[1][:-2].replace(" ", "").replace("'", "").split(",")


    def drawDistraction(self):
        # print("DISTRACTION")
        self.update()

    def drawPauseScreen(self, event, qp):
        print("draw pause")
        self.current_state = 'Pause'

        qp.setFont(QtGui.QFont('Helvetica', 32))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, "PAUSE\n\nPRESS 'SPACE' TO CONTINUE!")
        self.update()

    def startNextTask(self):
        print("start next task")
        self.current_task += 1
        self.current_state = 'Trial'

        self.current_trial = self.trials[self.current_task]
        self.task_start_time = datetime.datetime.now()


    def taskADB(self):
        self.update()

    def taskADR(self):
        self.update()

    def taskANB(self):
        self.update()

    def taskANR(self):
        self.update()

    def taskPDE(self):
        self.update()

    def taskPDO(self):
        self.update()

    def taskPNE(self):
        self.update()

    def taskPNO(self):
        self.update()

    def handleInput(self, key):
        self.task_end_time = datetime.datetime.now()
        self.current_state = 'Pause'
        self.update()

        self.logging_dict['id'].append(self.participant_id)
        self.logging_dict['shown_stimulus'].append(self.current_trial[2])
        self.logging_dict['mental_complexity'].append(self.current_trial[0])
        self.logging_dict['distraction'].append('yes' if self.current_trial[1] == 'D' else 'no')
        self.timedelta = self.task_end_time - self.task_start_time
        self.logging_dict['reaction_time_in_microseconds'].append((self.timedelta.seconds * 1000000 + self.timedelta.microseconds))
        self.logging_dict['timestamp'].append(int(self.task_end_time.timestamp()))
        self.logging_dict['pressed_key'].append(key.text())
        # self.current_trial = self.trials[self.current_task]
        if self.current_trial in ['ADB', 'ANB', 'PDE', 'PNE'] and key == QtCore.Qt.Key_F:
            self.logging_dict['correct_key_pressed'].append('true')
        elif self.current_trial in ['ADR', 'ANR', 'PDO', 'PNO'] and key == QtCore.Qt.Key_J:
            self.logging_dict['correct_key_pressed'].append('true')
        else:
            self.logging_dict['correct_key_pressed'].append('false')

    def writeLogToFile(self):
        """

        check logging indexing and maybe different method!!!


        """


        filepath = 'reaction_time_test_log.csv'
        log_file_exists = os.path.isfile(filepath)
        print(log_file_exists)
        with open(filepath, 'a') as log_file:
            w = csv.DictWriter(log_file, self.logging_dict.keys())
            if not log_file_exists:
                w.writeheader()


            for x in range(0, len(self.logging_dict['timestamp'])):
                current_row = ''
                for key in self.logging_dict.keys():
                    if x == 0:
                        current_row += self.logging_dict[key][x]
                    else:
                        current_row += ',{}'.format(str(self.logging_dict[key][x]))


            # w.writerows(self.logging_dict)

    def keyPressEvent(self, event):
        print(event.key())

        if event.key() == QtCore.Qt.Key_S:
            print(self.logging_dict)
            self.writeLogToFile()
        if self.current_state == "Pause":
            if event.key() == QtCore.Qt.Key_Space:
                self.startNextTask()

        elif self.current_state == "Trial":
            if event.key() == QtCore.Qt.Key_F:
                self.handleInput(QtCore.Qt.Key_F)
            elif event.key() == QtCore.Qt.Key_J:
                self.handleInput(QtCore.Qt.Key_J)


    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)

        print(event)
        print(self.current_state)
        print(self.trials[self.current_task])

        if self.current_state == 'Pause':
            self.drawPauseScreen(event, qp)

        elif self.current_state == 'Trial':
            print(self.current_trial)
            if 'D' in self.current_trial:
                for x in range(self.NUM_SQUARES):
                    for y in range(self.NUM_SQUARES):
                        qp.setBrush(QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                        self.rect = QtCore.QRect(x*self.SQUARE_WIDTH, y*self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT)
                        qp.drawRect(self.rect)

        qp.end()


def main():
    app = QtWidgets.QApplication(sys.argv)
    experiment = ReactionTimeExperiment()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
