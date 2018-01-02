# https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/shubham-and-xor-8526868e/


def read_input():
    n = int(input())
    line = input()
    a = line.rstrip('\n').split(' ')
    a = list(map(int , a))
    process(n,a)


def process(n, a):
    count = 0
    for x in range(0, n):
        for y in range(x+1 , n):
            if (a[x] ^ a[y]) == 0:
                count = count + 1

    result(count)


def result(count):
    print(count , end='')


def init():
    read_input()


if __name__ == '__main__':
    init()

