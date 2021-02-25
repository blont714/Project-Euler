def main():
    list = [i for i in range(1, 101)]
    print(culc_square_of_sum(list)-culc_sum_of_squares(list))

def culc_sum_of_squares(list):
    result = sum([i**2 for i in list])
    return result

def culc_square_of_sum(list):
    result = sum(list)**2
    return result

if __name__ == "__main__":
    main()

#出力結果: 25164150
#実行時間: 0.103s
