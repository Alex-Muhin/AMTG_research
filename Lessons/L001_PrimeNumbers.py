if __name__ == '__main__':
    exit(0)

def is_prime(num):
    if num == 1:
        return False

    if num%2 == 0:
        return False

    for i in range(3, int(num**0.5+1), 2):
        if num % i == 0:
            return False
    return True

#========================================== module start =============================================
def lesson001_PrimeNumber():

    searchStart = int(input("Ищем простые числа от: "))
    searchEnd   = int(input("                   до: "))

    for i in range(searchStart,searchEnd):
        if is_prime(i):
            print(i)



