def main():
    penta = [culc_penta(1)]
    p = 1
    answer = 0
    while(answer==0):
        p += 1
        penta.append(culc_penta(p))
        for i in penta[:-1]: #新たな五角数と、既存の五角数が条件を満たすか調べる
            if check_penta(penta[-1]-i) and check_penta(penta[-1]+i):
                answer = penta[-1]-i
                break
    print(answer)

def culc_penta(num): #num番目の五角数を計算
    return num*(3*num-1)/2

def check_penta(num): #numが五角数か調べる
    tmp = ((24*num+1)**0.5+1)/6
    if tmp.is_integer():
        return True
    else:
        return False

if __name__ == "__main__":
    main()

#出力結果:5482660
#実行時間:1.251s

'''
<思考方法>
五角数の一般項は an = n(3n-1)/2
五角数の判定は (√(24n+1)+1)/6 が整数であること

したがって、条件を満たす五画数が現れるまでwhile文で走査した。
'''
