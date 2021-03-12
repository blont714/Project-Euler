from fractions import Fraction

def main():
    answer = 1
    for den in range(11, 100):
        for mol in range(11, den):
            if mol%10==0 or den%10==0:
                continue
            if check(mol, den):
                answer = answer*Fraction(mol, den)
    print(answer)

def check(mol, den): #分子と分母を引数とし、条件を満たすかチェック
    if mol//10==den//10: #分子の十の位と分母の十の位が一致
        if Fraction(mol, den)==Fraction((mol%10), (den%10)):
            return True
    elif mol%10==den//10: #分子の一の位と分母の十の位が一致
        if Fraction(mol, den)==Fraction((mol//10), (den%10)):
            return True
    elif mol//10==den%10: #分子の十の位と分母の一の位が一致
        if Fraction(mol, den)==Fraction((mol%10), (den//10)):
            return True
    elif mol%10==den%10: #分子の一の位と分母の一の位が一致
        if Fraction(mol, den)==Fraction((mol//10), (den//10)):
            return True
    return False

if __name__ == "__main__":
    main()

#出力結果: 1/100
#実行時間: 0.108s

'''
<思考方法>
調査範囲が狭くかつ二桁同士なので、チェックは条件分岐で行った。
'''
