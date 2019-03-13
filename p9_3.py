try:
    f = open("dfsfsd.txt")
    print(f.read())
    f.close()
except OSError as reason:
    print("文件打开的过程出错啦~！" + str(reason))
