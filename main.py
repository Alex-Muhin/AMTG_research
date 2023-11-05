# This is a sample Python script.
import configparser
from Lessons import L001_PrimeNumbers

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ != '__main__':
    exit(0)

config = configparser.ConfigParser()
config.read("AMTA.cfg")

if "Default" in config.sections():
    taskToRun = config['Default']['taskToRun']
else:
    taskToRun=0

taskInput = input("Task no (press enter for {}): ".format(taskToRun))

if taskInput.isnumeric():
    taskToRun = int(taskInput)

if taskToRun <= 0:
    exit(0)

if taskToRun==1:
    L001_PrimeNumbers.lesson001_PrimeNumber()   # Lesson 001: find prime numbers


config['Default'] = {'taskToRun': taskToRun}
with open('AMTA.cfg', 'w') as configfile:
  config.write(configfile)







