def main():
    N, a, b, tmp = 1, 1, 1, 0
    while(len(str(a))<1000):
        N += 1
        tmp = a
        a = a + b
        b = tmp
    print(N+1)
if __name__ == "__main__":
    main()

#出力結果: 4782
#実行時間: 0.124s
