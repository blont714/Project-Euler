def main():
    terms = []
    for a in range(2, 101):
        for b in range(2, 101):
            terms.append(a**b)
    print(len(list(set(terms))))

if __name__ == "__main__":
    main()

#出力結果: 9183
#実行時間: 0.106s
