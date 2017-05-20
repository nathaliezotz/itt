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




'''
TODO:
nicht das ganze fenster mit blinkenden quadraten vollmachen sondenr in der mitte etwas platz lassen?

start taskXXX x 8

pause screen (drawPause)
Handle Input
Logging (writeLogToFile)


'''

import random
import sys

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
        self.current_state = "Pause"

        self.tasks = {'ADB': self.taskADB(),
                      'ADR': self.taskADR(),
                      'ANB': self.taskANB(),
                      'ANR': self.taskANR(),
                      'PDE': self.taskPDE(),
                      'PDO': self.taskPDO(),
                      'PNE': self.taskPNE(),
                      'PNO': self.taskPNO()}

        self.counter = 0

        self.timer_draw = QtCore.QTimer(self)
        self.timer_draw.timeout.connect(self.drawDistraction)
        self.timer_draw.start(self.BLINK_SPEED)



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
                    self.participant_id = line.split(" ")[1]
                elif line.startswith('TRIALS'):
                    print(line)
                    self.trials = line.split('[')[1][:-2].replace(" ", "").replace("'", "").split(",")


    def drawDistraction(self):
        # print("DISTRACTION")
        self.update()

    def drawPauseScreen(self, event, qp):
        print("draw pause")
        self.current_state = "Pause"

        qp.drawText(self.WIDTH/2, self.HEIGHT/2, "PAUSE \n PRESS 'SPACE' TO CONTINUE!")


    def startNextTask(self):
        print("start necxt task")
        self.current_task += 1
        self.current_state = "Trial"

        self.trials[self.current_task]


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


    def writeLogToFile(self):
        pass

    def keyPressEvent(self, event):
        print(event.key())
        if self.current_state == "Pause":
            if event.key() == QtCore.Qt.Key_Space:
                self.startNextTask()

        elif self.current_state == "Trial":
            if event.key() == QtCore.Qt.Key_F:
                """

                handleInput


                """
                self.current_state = 'Pause'
                self.update()
            elif event.key() == QtCore.Qt.Key_J:
                """

                handleInput


                """
                self.current_state = 'Pause'
                self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)

        print(event)
        print(self.current_state)
        print(self.trials[self.current_task])


        if self.current_state == 'Pause':
            self.drawPauseScreen(event, qp)

        elif self.current_state == 'Trial':
            if 'D' in self.trials[self.current_task]:
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
