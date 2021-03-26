def main():
    check_number1 = [i for i in range(5, 10)]
    check_number2 = [i for i in range(25, 34)]
    check_number3 = [i for i in range(100, 333)]
    check_number4 = [i for i in range(5000, 9999)]
    check_numbers = check_number1+check_number2+check_number3+check_number4

    max_pandigital = 0
    nine_numbers_set = set("123456789")
    for num in check_numbers: #乗算したものを文字列としてリストに加え、1から9までの数字から構成されるか調べる
        numbers = [str(num*i) for i in range(1, 7-len(str(num)))]
        number_str = ''.join(numbers)
        if set(number_str)==nine_numbers_set:
            pandigital = int(number_str)
            if max_pandigital < pandigital:
                max_pandigital = pandigital
    print(max_pandigital)

if __name__ == "__main__":
    main()

#出力結果:932718654
#実行時間:0.10s

'''
<思考方法>
操作後は9桁の整数になることから、走査範囲は以下の通り。
1桁の場合n=5 (1,2,2,2,2) 5≦n≦9 ※1を掛けたら1桁、2を掛けたら2桁の範囲
2桁の場合n=4 (2,2,2,3) 25≦n≦33 ※3を掛けたら2桁、4を掛けたら3桁の範囲
3桁の場合n=3 (3,3,3) 100≦n≦333 ※何を掛けても3桁の範囲
4桁の場合n=2 (4,5) 5000≦n≦9999 ※1を掛けたら4桁、2を掛けたら5桁の範囲
'''
