def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    total = 200
    count = check(coins, total)
    print(count)

def check(coins, total):
    count = 1
    for c in coins[:-1]: #硬貨について繰り返し
        for n in range((total//c)): #totalを超えない枚数の範囲で繰り返し
            tmp = c*(n+1)
            if tmp == total: #合計200ペンスになった場合、カウントアップ
                count += 1
            else: #硬貨の種類とtotalを減算し、再帰
                count += check(coins[coins.index(c)+1:], total-tmp)
    return count

if __name__ == "__main__":
    main()

#出力結果: 73682
#実行時間: 0.142

'''
<思考方法>
動的計画法と再帰を用いて考えた。
合計が200ペンスを越えない範囲で、硬貨とその枚数を繰り返した。

再帰は変数の扱いが難しいですね。
TypeError:'int' object is not subscriptableでハマったので、15行目の書き方は以下のサイトを参考にした。
https://qiita.com/yopya/items/b5cd0a16b8f03bf2f33b
https://qiita.com/makostagram/items/209174a40e73f0b094ad

余談だが、1ペンス硬貨があるので、動的計画法よりも条件を狭めて考えられそうな気がした。
'''
