#coding=utf-8
#Version:python3.5.2
#Tools:pyCharm2017.2
"""
- 题 2:
某些整数能分解成若干个连续整数的和的形式，例如
15 = 1 + 2+3+4+5
15 = 4 + 5 + 6
15 = 7 + 8
某些整数不能分解为连续整数的和，例如:16
输入: 一个整数N(N <= 10000)
输出:整数N对应的所有分解组合，按照每个分解中的最小整数
从小到大输出，每个分解占一行 ，每个数字之间有一个空格(每
行最后保留一个空格);如果没有任何分解组合，则输出NONE。
"""
#对于任意连续数字都有m到m+k-1,N = (m+m+k-1）*k/2，需要考虑是否为负数
def numberRecount(number):
    if number > 10000:
        raise SyntaxError("数字过大")
    recount = []
    if number>=0:
        for i in range(1,number//2+1):
            for j in range(0,number):
                if 2*number == (2*i+j-1)*j:
                    recount.append("{}=".format(number)+"+".join(map(str, [x for x in range(i, i+j)])))
    else:
        for i in range(number,-1):
            for j in range(2,abs(number)):
                if 2*number == (2*i+j-1)*j:
                    t = ""
                    for x in range(i, i+j):
                        if x<0:
                            t+="{}".format(x)
                        else:
                            t += "+{}".format(x)
                    recount.append("{}=".format(number)+t)
                    #recount.append("{}=".format(number)+"+".join(map(str, [x for x in range(i, i+j)])))
    return recount
if __name__ == '__main__':
    number = numberRecount(-15)
    for i in number:
        print(i)