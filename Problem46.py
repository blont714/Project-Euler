import math

def main():
    number = 3
    prime_numbers = []
    answer = 0
    while(answer==0): #合成数numberが条件を満たすまで走査
        if is_prime(number):
            number += 2
            continue
        prime_numbers = get_sieve_of_eratosthenes(number)
        for i in prime_numbers: #number
            if check_square((number-i)/2):
                break
            if i == prime_numbers[-1]:
                answer = number
                break
        number += 2
    print(answer)

def check_square(num): #numが平方数か調べる
    tmp = num**0.5
    if tmp.is_integer():
        return True
    else:
        return False

def get_sieve_of_eratosthenes(n): #エラトステネスの篩
    prime = []
    limit = math.sqrt(n)
    data = [i+1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [i for i in data if i % p != 0]

def is_prime(q): #素数判定
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

if __name__ == "__main__":
    main()

#出力結果:5777
#実行時間:2.108s

'''
<思考方法>
合成数を走査し、条件を満たすか調べた。
毎回エラトステネスの篩を行うのは効率が悪いので、要改善。

素数判定を拝借した。
https://pashango-p.hatenadiary.org/entry/20090704/1246692091
'''
