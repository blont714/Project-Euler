def main():
    for i in range(1000, 8000): #最小の数値の取りうる範囲で走査
        for j in range(1000, (9999-i)//2): #最大の数値が4桁になる範囲で走査
            a, b, c = i, i+j, i+j+j
            if is_prime(a) and is_prime(b) and is_prime(c) and check(a, b, c):
                if a == 1487:
                    continue
                else:
                    print(str(a)+str(b)+str(c))

def is_prime(n): #素数判定
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return all(n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2))

def check(a, b, c): #同じ数字を使っているか調べる
    new1 = sorted(str(a))
    new2 = sorted(str(b))
    new3 = sorted(str(c))
    if sorted(new1)==sorted(new2)==sorted(new3):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

#出力結果:296962999629
#実行時間:15.200s

'''
<思考方法>
素数判定と、4桁を越えないような加算を行って条件を満たす値を見つけた。
これもいまひとつ高速化の方法が思いつかなかったので愚直に解いた。

'''
