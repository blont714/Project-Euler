def main():
    answer = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if check_palindromic(i*j):
                if i*j > answer:
                    answer = i*j
    print(answer)

def check_palindromic(num):
    for i in range(len(str(num))//2):
        if str(num)[i]!=str(num)[-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    main()

#出力結果: 906609
#実行時間: 0.928s
