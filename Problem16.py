def main():
    num_str = str(2**1000)
    sum = 0
    for i in num_str:
        sum += int(i)
    print(sum)

if __name__ == "__main__":
    main()
