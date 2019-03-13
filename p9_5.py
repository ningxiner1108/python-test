try:
    int('abc')
    sum = 1 + '1'
    f = open("dsfsdfsf.txt")
    print(f.read())
    f.close()
except (ValueError, OSError, TypeError) as reason:
    print("出错啦，出错原因是:" + str(reason))
