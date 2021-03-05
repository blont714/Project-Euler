import datetime

def main():
    count = count_sundays()
    print(count)

def count_sundays():
    count = 0
    dt = datetime.datetime(year=1900, month=1, day=1)
    for i in range(100):
        for j in range(12):
            dt1 = datetime.datetime(year=1901+i, month=1+j, day=1)
            print(dt1)
            print (dt1-dt)
            if (dt1-dt).days%7==6:
                count += 1
    return count

if __name__ == "__main__":
    main()

#出力結果:171
#実行時間:0.104s
