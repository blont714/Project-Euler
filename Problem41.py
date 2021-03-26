import math

def main():
    prime_list = get_sieve_of_eratosthenes(10000000)
    prime_list.reverse()
    for num in prime_list:
        pand = [str(i) for i in range(1, len(str(num))+1)]
        pand_set = set(''.join(pand))
        if pand_set == set(str(num)):
            print(num)
            break
def get_sieve_of_eratosthenes(n):
    prime = []
    limit = math.sqrt(n)
    data = [i+1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [i for i in data if i % p != 0]
if __name__ == "__main__":
    main()

#出力結果:7652413
#実行時間:60.99s

'''
<思考方法>
9桁、8桁の場合は3の倍数なので素数になり得ない。したがって7桁以下の素数について調べれば良い。
エラストテネスの篩で少し時間が掛かるが、7桁の素数から順に調べていけば早そうと考えた。先に素数判定を済ませてしまえばパンデジタルかどうかの判定だけで済む。

'''
