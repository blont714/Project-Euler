import math

def main():
    n = 1000000
    global prime_list
    prime_list = get_sieve_of_eratosthenes(n)
    answer_list = []
    for num in prime_list:
        if l_cut(num) and r_cut(num):
            answer_list.append(num)
            if len(answer_list)==15:
                break
    print(sum(answer_list)-17)

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

def l_cut(num): #左から連続的に削除した場合、題意を満たすか調べる関数
    num_str = str(num)
    for i in range(len(num_str)-1):
        num_str = num_str[:-1]
        if int(num_str) not in prime_list:
            return False
    return True

def r_cut(num): #右から連続的に削除した場合、題意を満たすか調べる関数
    num_str = str(num)
    for i in range(len(num_str)-1):
        num_str = num_str[1:]
        if int(num_str) not in prime_list:
            return False
    return True

if __name__ == "__main__":
    main()

#出力結果:748317
#実行時間:121.1s

'''
<思考方法>
問35の反省を活かし、偶数か5が含まれた場合題意を満たさないという条件を入れようとしたが、2,3,5,7が素数なので上手く組み込むことが出来なかった。

汎用性を考えるのであればwhile文で回すべきだが、題意を満たす素数が11個であることが示されており、かつ桁数が増えるほど題意を満たすことは難しくなる。
したがって定数nまでエラストテネスの篩で素数リストを作成し、素数判定を行った。answer_listが11個になるまで定数nを増加した。
'''
