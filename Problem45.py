def main():
    hex, p = 0, 1
    while True:
        p += 1
        hex = culc_hex(p)
        if check_tri(hex) and check_penta(hex) and hex!=40755:
            print(hex)
            break

def culc_hex(num): #num番目の六角数を計算
    return num*(2*num-1)

def check_tri(num): #numが三角数か調べる(なお要らない模様)
    tmp = ((8*num+1)**0.5-1)/2
    if tmp.is_integer():
        return True
    else:
        return False

def check_penta(num): #numが五角数か調べる
    tmp = ((24*num+1)**0.5+1)/6
    if tmp.is_integer():
        return True
    else:
        return False


if __name__ == "__main__":
    main()

#出力結果:1533776805
#実行時間:0.127s

'''
<思考方法>
六角数を、三角数と五角数の判定関数(前問の流用)で調べた。
(六角数が一番数が大きくなるペースが早いので)

シンプルに書けたと思ったのだが、六角数は常に三角数であるという書き込みを見て、それはそう、となった。
'''
