def main():
    f_digit = finish_digit()
    answer = []
    max = int('9'*f_digit)
    for num in range(2, max+1):
        if num == cul_fifth_power(num):
            answer.append(num)
    print(sum(answer))

def finish_digit():
    digit = 1
    left = 9
    while(left<9**5*digit):
        digit += 1
        left = int('9'*digit)
    return digit

def cul_fifth_power(num):
    fifth_power = sum([int(i)**5 for i in str(num)])
    return fifth_power

if __name__ == "__main__":
    main()

#出力結果: 443839
#実行時間: 3.806s
