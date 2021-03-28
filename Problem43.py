import itertools

def main():
    pandigital_list = make_pandigital_list()
    answer = []
    for num in pandigital_list:
        if check(num):
            answer.append(int(num))
    print(sum(answer))

def make_pandigital_list(): #パンデジタル数のリスト作成
    number = ['0','1','2','3','4','5','6','7','8','9']
    tmp = list(itertools.permutations(number))
    pandigital_list = []
    for i in tmp:
        pandigital_list.append(''.join(i))
    print(pandigital_list)
    return pandigital_list

def check(num): #題意を満たすかチェック
    if int(num[7:])%17!=0:
        return False
    if int(num[6:9])%13!=0:
        return False
    if int(num[5:8])%11!=0:
        return False
    if int(num[4:7])%7!=0:
        return False
    if int(num[5])%5!=0:
        return False
    if (int(num[2])+int(num[3])+int(num[4]))%3!=0:
        return False
    if int(num[3])%2!=0:
        return False
    return True

if __name__ == "__main__":
    main()

#出力結果:16695334890
#実行時間:119.6s

'''
<思考方法>
効率的な方法が全く思いつかず、愚直にパンデジタル数をリストアップした後走査するしかなかった。

'''
