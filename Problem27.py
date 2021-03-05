import math

def main():
    prime_numbers = get_sieve_of_eratosthenes(1000)
    answer, n, max_count = 0, 0, 0
    for b in prime_numbers:
        for a in range(-b, 1001):
            n = 0
            while(n**2+a*n+b in prime_numbers and n < b):
                n += 1
            if n > max_count:
                max_count = n
                answer = a*b
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

#出力結果: -59231
#実行時間: 0.959s
