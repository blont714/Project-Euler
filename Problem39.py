def main():
    max_solution = 0
    answer = 0
    for p in range(3, 1001):
        solution = find_number_of_solutions(p)
        if max_solution < solution:
            answer = p
            max_solution = solution
    print(answer)

def find_number_of_solutions(num):
    solutions = 0
    for a in range(1, num//3+1):
        for b in range(a, (num-a)//2+1):
            c = num-a-b
            if a**2+b**2==c**2:
                solutions += 1
    return solutions

if __name__ == "__main__":
    main()


#出力結果:840
#実行時間:29.167s

'''
<思考方法>
三角形を構成する辺をa,b,c(a<b<c)としても一般性を損なわない。
したがって上記の条件下でp≦1000の範囲で走査した。

'''
