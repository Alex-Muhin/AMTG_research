import random

if __name__ == '__main__':
    exit(0)


#========================================== module start =============================================

def lesson002_MagicBall():

    searchStart = int(input("Magic Ball: "))
    searchEnd   = searchStart+10

    for i in range(searchStart,searchEnd):
     #   if is_prime(i):
            print(i)
