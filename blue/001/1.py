def func1():
    str1 = input("请输入一个人的名字：")
    str2 = input("请输入一个国家名字：")
    print("世界这么大，{}想去{}看看。".format(str1, str2))
    pass


def func2():
    n = input("请输入整数N：")
    num = 0
    for i in range(int(n)):
        num += i + 1
    print("1到N求和结果是：", num)
    pass


def func3():
    for i in range(1, 10):
        for j in range(1,i+1):
            print("{} × {} = {:2}".format(j, i, j*i), end=' ')
        print('')
    pass


def func4():
    sum, tmp = 0, 1
    for i in range(1, 11):
        tmp *= i
        sum += tmp
    print("the result is: {}".format(sum))
    pass


def func5():
    n = 1
    for i in range(5, 0, -1):
        n = (n+1) << 1
    print(n)
    pass


def func6():
    diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
    for x in range(0, 5):
        for y in range(0, 5):
            if not (x == y):
                print("{}{}".format(diet[x], diet[y]))
    pass


def func7():
    import turtle
    turtle.fillcolor("red")
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.right(144)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    pass


def func8():
    import turtle
    turtle.color("red", "yellow")
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.right(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()
    pass


if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    # func4()
    # func5()
    # func6()
    # func7()
    func8()
    pass
