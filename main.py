# This is a sample Python script.
import configparser
from Lessons import L001_PrimeNumbers
from Lessons import L002_MagicBall
from Lessons import L003_NumberQuizz

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ != '__main__':
    exit(0)

config = configparser.ConfigParser()
config.read("AMTA.cfg")

# load last executed lesson
taskToRun = 0
if "Default" in config.sections():
    taskToRun = int(config['Default']['taskToRun'])

# asc for new lesson to proceed
taskInput = input("Task no (press enter for {}): ".format(taskToRun))

# if number is correct
if taskInput.isnumeric():
    taskToRun = int(taskInput)      # get it

# if nothing entered (just Enter) then exit
if taskToRun <= 0:
    exit(0)

# saving last lesson choise
config['Default'] = {'taskToRun': taskToRun}
with open('AMTA.cfg', 'w') as configfile:
    config.write(configfile)


# run lesson proc
if taskToRun==1:
    L001_PrimeNumbers.lesson001_PrimeNumber()   # Lesson 001: find prime numbers
elif taskToRun == 2:
    L002_MagicBall.lesson002_MagicBall()        # Lesson 002: Magic ball
elif taskToRun == 3:
    L003_NumberQuizz.Lesson003_NumberQuizz()    # Lesson 003: Number quizz








