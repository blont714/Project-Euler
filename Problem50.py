import math

def main():
    answer = 0
    prime_numbers = get_sieve_of_eratosthenes(5000)
    for i in reversed(range(len(prime_numbers))): #条件を満たす数列が長くなる方からループ
        for j in reversed(range(len(prime_numbers)-i)): #開始位置に関するループ
            total = sum(prime_numbers[j:j+i])
            if total < 1000000 and is_prime(total): #和が100万を越えておらず、かつ素数か調べる
                answer = sum(prime_numbers[j:j+i])
                break
        if answer!=0:
            break
    print(answer)

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

def is_prime(n): #素数判定
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return all(n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2))

if __name__ == "__main__":
    main()

#出力結果:997651
#実行時間:0.143s

'''
<思考方法>
条件を満たす数列が長い方から走査を開始した。問題文に21の長さが示されているので、エラトステネスの篩の範囲を狭く設定した。何度か実行してみて、合計値が100万を越えないくらいの範囲に設定したが、一般性に欠ける。
開始位置に関して走査し、条件を満たす数列が見つかったら、和を出力して走査を終了した。

'''
