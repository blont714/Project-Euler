from functools import reduce
import math

def main():
    list = [i for i in range(1, 21)]
    print(lcm(*list))

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

if __name__ == "__main__":
    main()
