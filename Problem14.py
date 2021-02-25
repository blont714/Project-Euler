
def main():
    max_chain = 0
    number = 0
    for i in range(1, 1000001):
        chain = count_chain(i)
        if max_chain < chain:
            max_chain = chain
            number = i
    print(number, max_chain)


def count_chain(n):
    chain = 1
    while(n!=1):
        if n%2==0:
            n = n//2
        else:
            n = 3*n+1
        chain += 1
    return chain

if __name__ == "__main__":
    main()
