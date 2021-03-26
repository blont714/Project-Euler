import math

def main():
    answer = 0
    for i in range(3, 2000000):
        total = sum_fact(i)
        if total == i:
            answer += i
    print(answer)

def sum_fact(num):
    sum = 0
    for i in str(num):
        sum += math.factorial(int(i))
    return sum

if __name__ == "__main__":
    main()

#出力結果:40730
#実行時間:4.165s

'''
<思考方法>
(9!=362880)
2!+9!+9!+9!+9!+9!+9! = 2177278 < 2999999
2!+0!+9!+9!+9!+9!+9! = 1814398 < 2099999
1!+9!+9!+9!+9!+9!+9! = 2177277 > 1999999

以上より、200万以上に該当する数は存在しないので、走査範囲は3~200万。
'''
