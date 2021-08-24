from pair import Pair


def main():
    p1 = Pair(1, 2)
    p2 = Pair(3, 4)
    p3 = Pair(1, 2)

    print(p1 == p2)
    print(p1 == p3)

    print(p1)

    print(p1[0])

    p1[0] = 14
    

if __name__ == '__main__':
    main()
