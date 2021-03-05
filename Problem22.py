import string

def main():
    score = 0
    with open("names.txt") as f:
        s = f.read()
    name_list = s.split(',')
    name_list.sort()
    for name in name_list:
        name = name[1:-1]
        score += name_value(name)*(name_list.index("\""+name+"\"")+1)
    print(score)

def name_value(name):
    value = 0
    alphabets = string.ascii_uppercase
    for char in name:
        value += alphabets.index(char) + 1
    return value

if __name__ == "__main__":
    main()

#出力結果: 871198282
#実行時間: 0.321s
