import math

def main():
    num = 100
    fact = math.factorial(num)
    result = sum(list(map(int, str(fact))))
    print(result)

if __name__ == "__main__":
    main()

#出力結果:648
#実行時間:0.098s
