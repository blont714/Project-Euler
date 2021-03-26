def main():
    with open("words.txt", 'r') as f:
        words = f.read().strip().replace('"', '').split(',')
    answer = 0
    for word in words:
        total = 0
        for char in word:
            total += ord(char)-64
        if check_triangle(total):
            answer += 1
    print(answer)

def check_triangle(num):
    if ((num*8+1) ** 0.5).is_integer():
        return True
    else:
        return False

if __name__ == "__main__":
    main()

#出力結果:162
#実行時間:0.098s

'''
<思考方法>
自然数Nが三角数であるには、√(8N+1)が整数であることが必要十分である。
(wikipedia参照)

したがって各単語の単語値が三角数になるか調べ上げれば良い。
'''
