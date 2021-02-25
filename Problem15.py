from scipy.special import comb

def main():
    print(comb(40, 20, exact=True))

if __name__ == "__main__":
    main()

#出力結果: 137846528820
#実行時間: 0.435s
