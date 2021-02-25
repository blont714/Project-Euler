def main():
    num = 600851475143
    prime = max_prime_number(num)
    print(prime)

def max_prime_number(num):
    i = 2
    while(i < num):
        if num%i==0:
            num = num//i
        else:
            i += 1
    return num

if __name__ == '__main__':
    main()
