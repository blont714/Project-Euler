def main():
    answer = []
    for i in range(1000, 10000):
        if check_pandigital(i):
            answer.append(i)
    print(sum(answer))

def check_pandigital(num): #パンデジタルか否かチェック
    for i in range(1, int(num**0.5)+1): # 約数を調べて掛ける数、掛けられる数を算出
        if num%i==0 and check(num, i, num//i):
            return True
    return False

def check(num, multi1, multi2):
    pandigital = [i for i in range(1, 10)]
    check_list = make_lst(num) + make_lst(multi1) + make_lst(multi2)
    check_list.sort()
    if pandigital == check_list:
        return True
    else:
        return False

def make_lst(num): #数値をリストに変換
    return [int(i) for i in str(num)]

if __name__ == "__main__":
    main()

#出力結果: 45228
#実行時間: 0.290s

'''
<思考方法>
99×99<10000より(二桁×二桁の最大値)<(五桁の最小値)
10000×1>999より(五桁×一桁の最小値)>(三桁の最大値)

以上より、積が四桁の範囲を調査すれば良い。
'''
