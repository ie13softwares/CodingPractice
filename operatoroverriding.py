class New:
    def __init__(self, r):
        self.__r = r

    def __str__(self):
        return str(self.__r)


def main():
    global obj
    obj = New(5)
    print(obj)


def oldmain():
    print(obj)


obj = New(7)


def newmain():
    print(obj)


if __name__ == '__main__':
    newmain()
    main()
    oldmain()
