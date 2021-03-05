def main():
    longest_cycle = 0
    number = 0
    for d in range(2, 1000):
        if d%2==0 or d%5==0:
            continue
        else:
            cycle = check_by_Euler(d)
            if cycle > longest_cycle:
                longest_cycle = cycle
                number = d
    print(number)

def check_by_Euler(num):
    n = 1
    while((10**n)%num!=1):
        n += 1
    return n

if __name__ == "__main__":
    main()

#出力結果: 983
#実行時間: 0.173s
