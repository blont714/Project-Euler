import math

def main():
    n = 1
    triangle = culc_triangle(n)
    while(count_divisor(triangle)<=500):
        n += 1
        triangle = culc_triangle(n)

    print(triangle)

def culc_triangle(n):
    return n*(n+1)//2

def count_divisor(n):
    count = 0
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n%i==0:
            count += 2
    if math.floor(math.sqrt(n))**2 == n:
        count -= 1
    return count

if __name__ == "__main__":
    main()
