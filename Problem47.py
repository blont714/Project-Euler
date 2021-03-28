def main():
    N = 4 #いくつの素因数を持つか
    count = 0
    num = 1
    while(count!=N):
        tmp = prime_factorize(num)
        if len(tmp)!=N: #素因数の種類数が指定数でなければ調べ直し
            count = 0
            num += 1
            continue
        num += 1
        if prime_factorize(num).isdisjoint(tmp): #前の数字の素因数と重複していない場合
            count += 1
        else: #重複したら調べ直し
            count = 0

    print(num-N)

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return set(a)

if __name__ == "__main__":
    main()

#出力結果:134043
#実行時間:1.043s

'''
<思考方法>
連続する数字の素因数を求めて、setで比較することを考えた。
素因数分解を行い、setで重複を許さないようにした。

素因数分解を行うコードを拝借した。
https://note.nkmk.me/python-prime-factorization/
'''
