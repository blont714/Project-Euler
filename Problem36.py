def main():
    answer = 0
    for num in range(1000000):
        if check(num):
            answer += num
    print(answer)

def check(num): #題意を満たすか調べる関数
    bin_num = format(num, 'b')
    num_str = str(num)
    if palind(bin_num) and palind(num_str):
        return True
    else:
        return False

def palind(str): #文字列が回文か調べる関数
    if str==str[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    main()

#出力結果:872187
#実行時間:0.891s


'''
<思考方法>
与えられた数字とその2進数が回文(?)になっていれば良いので、比較的シンプルに考えられた。
'''
