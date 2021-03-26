import math

def main():
    answer = 0
    prime_list = get_sieve_of_eratosthenes(1000000)
    for num in prime_list:
        num_str = str(num)
        if len(num_str)==1: #一桁なら巡回素数
            answer += 1
        for i in range(len(num_str)-1): #二桁以上なら(桁数-1)回ループ
            num_str = num_str[-1] + num_str
            num_str = num_str[:-1]
            if int(num_str) in prime_list:
                if i==len(num_str)-2:
                    answer += 1
                continue
            else:
                break
    print(answer)

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

#出力結果:55
#実行時間:219.3s

'''
<思考方法>
以前使用したエラストテネスの篩による素数リスト作成関数を流用した。
100万までの素数を列挙し、リスト内の要素に対してforループを行った。

今回素数を回転させて逐一素数判定を行った。途中で文字列の中に1文字でも偶数や5が含まれていればその素数は調べる必要がないことに気づいてしまったが、予定通り組んだ場合どの程度実行時間が掛かるか興味があったのでそのまま組んだ。

問題では100万までの数字について調べることになっているが、まず100まで算出できるようにコーディングし、後に100万に増やせば良いと考えていた。そのため、桁数が増えるごとに回転回数が増え、後に行くほど実行時間が掛かることを失念した。

'''
