def main():
    #過剰数を列挙
    abundant_number = make_abundant_number()
    sum_abundant_number = make_sum_abundant_number(abundant_number)
    number = [i for i in range(1, 28123)]
    print(sum(list(set(number)-set(sum_abundant_number))))

def make_abundant_number():
    abundant_number = []
    for i in range(1, 28123):
        if is_excess_number(i):
            abundant_number.append(i)
    return abundant_number

def make_sum_abundant_number(abundant_number):
    sum_abundant_number = []
    for i in range(len(abundant_number)-1):
        for j in range(0, len(abundant_number)-i):
            sum_abundant_number.append(abundant_number[i]+abundant_number[i+j])
    sum_abundant_number_list = list(set(sum_abundant_number))
    return sum_abundant_number_list


def is_excess_number(n):
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i ** 2 != n:
                sum_divisors += n // i
        if sum_divisors > n:
            return True
    return False


if __name__ == "__main__":
    main()

#出力結果: 4179871
#実行時間: 4.973s
