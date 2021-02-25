
def main():
    num = 1000
    a, b, c = culc_Pythagorean(num)
    print(a, b, c)
    print(a*b*c)
def culc_Pythagorean(num):
    for a in range(1, num//3):
        for b in range(a, (num-a)//2):
            c = num - a - b
            if a**2+b**2==c**2:
                return a, b, c
    print(None)

if __name__ == "__main__":
    main()
