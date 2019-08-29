def mtest1():
    print("module test:")
    if __name__ =='__main__':  #查看maintest这个模块的__name__属性
        print("this's main module")
    else:
        print("not main module")
