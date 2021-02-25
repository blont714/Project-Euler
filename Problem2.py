def main():
    list = []
    a, b = 1, 2
    max = 4000000
    fib_list = make_fib_list(list, a, b, max)
    print(sum([i for i in fib_list if i%2==0]))

def make_fib_list(list, a, b, max):
    list.append(a)
    list.append(b)
    n = 0
    while(list[-1] <= max):
        list.append(list[n] + list[n+1])
        n += 1
    del list[-1]
    return list

if __name__ == "__main__":
    main()
