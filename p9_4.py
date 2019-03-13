try:
    f = open("dfsdsgs.txt")
    print(f.read())
    f.close()
    sum = 1 + '1'
except OSError as reason:
    print("文件出错啦，错误原因是:" + str(reason))
except TypeError as reason:
    print("类型出错啦，错误原因是:" + str(reason))
    
