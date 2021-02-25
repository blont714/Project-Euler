def main():
    list = []
    for i in range(1, 1000):
        if i%3==0 or i%5==0:
            list.append(i)
    print(sum(list))

if __name__ == "__main__":
    main()

#出力結果: 233168
#実行時間: 0.104s
