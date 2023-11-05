# TA&AM mutual learning project

Here we are going to do excercises for Python online courses and keep the results. Also we will train our Git skills.

## Development
Notice 1: commits of new lessons must be prefixed with __[FTC]__  
Notice 2: Main entry of the lesson called __lesson00#_<file_name>__ . Each file begins 
from the __ name __ variable check. e.g.:  
```code
if __name__ == '__main__':
    exit(0)
    
#========================================== module start =============================================
def Lesson003_NumberQuizz():
```

## App structure

The main app is just a dispatcher running one of the training task.
The task you are working on (default task) is definded in __AMTA.cfg__ 
file in the "__tasktorun__" variable. 
Each task is a function defined in a separate file situated in the
__./Lessons__ directory. If the task assumed to have more then one
file we put it into the dedicated subdirectory.

## Lessons list
* Ex001: Output prime numbers laying in the range entered by user  
        (L001_PrimeNumbers.py)
* Ex002: MagicBall game  
        (L002_MagicBall.py)
* Ex003: User need to find out the random number  
        (L003_NumberQuizz.py)
* Ex004: ...  
        (L004_....py)




