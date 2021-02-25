def main():
    num_str = str(2**1000)
    sum = 0
    for i in num_str:
        sum += int(i)
    print(sum)

if __name__ == "__main__":
    main()

#出力結果: 1366
#実行時間: 0.103s
