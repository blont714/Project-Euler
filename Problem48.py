def main():
    total = 0
    for i in range(1, 1001):
        total += i**i
    print(str(total)[-10:])

if __name__ == "__main__":
    main()

#出力結果:9110846700
#実行時間:0.462s

'''
<思考方法>
0の0乗は1(自戒)

'''
