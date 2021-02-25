import math

def main():
    prime_number_list = []
    number = 2
    while(len(prime_number_list)<10001):
        if judge_prime(number):
            prime_number_list.append(number)
        number += 1
    print(prime_number_list[-1])

def judge_prime(number):
    if number%2==0 and number!=2:
        return False
    for i in range(2, math.floor(math.sqrt(number))+1):
        if number%i==0:
            return False
    return True

if __name__ == "__main__":
    main()
