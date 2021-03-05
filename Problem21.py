def main():
    amicable = []
    for i in range(1, 10000):
        if check_amicable_number(i):
            amicable.append(i)

    print(sum(amicable))

def check_amicable_number(num):
    sum_divisors1 = sum(make_divisors(num)) - num
    sum_divisors2 = sum(make_divisors(sum_divisors1)) - sum_divisors1
    if num == sum_divisors2 and num != sum_divisors1:
        return True
    else:
        return False

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

if __name__ == "__main__":
    main()

#出力結果:31626
#実行時間:0.229s
