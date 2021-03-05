import math

def main():
    answer_index = 1000000
    num = 10
    num_list = [i for i in range(num)]
    answer = []
    for i in range(num):
        div = (answer_index-1)//math.factorial((num-1)-i)
        answer.append(num_list[div])
        num_list.pop(div)
        answer_index = answer_index%math.factorial((num-1)-i)
    print(answer)

if __name__ == "__main__":
    main()

#出力結果: [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
#実行時間: 0.089s
