def main():
    number_str = [str(i) for i in range(200000)]
    numbers = ''.join(number_str)
    answer = int(numbers[1])*int(numbers[10])*int(numbers[100])*int(numbers[1000])*int(numbers[10000])*int(numbers[100000])*int(numbers[1000000])
    print(answer)
if __name__ == "__main__":
    main()

#出力結果:210
#実行時間:0.137s

'''
<思考方法>
100万桁まで得るには、20万ほどの数字を連結させる必要がある。
(連結する数字は5桁と6桁が大半を占めており、100万/5=20万)
'''
