#coding=utf-8
#Version:python3.5.2
#Tools:pyCharm2017.2
"""
- 题 1:
编程实现功能:
功能是求出字符串s 与字符串t的第二公共单词(这里，假设两个
字符串均由英字母和空格字符组成);若找到这样的公共单词，
函数返回该单词，否则，函数返回NULL，如果有多个满足要
求，则返回第一个单词。
例如:若 s=“This is C programming text”，t=“This is a text for C
programming”，则函数返回“this”。
"""
#疑问是是否单词位置必须一样还是不一样
#获取相同的单词,位置不管,重复不管
#将两个字符串按空格切割，将text1每个子串在text2中遍历是否存在
def getCompareString(Ctext1,Ctext2,textSum = 0):
    text1,text2= Ctext1.split(" "),Ctext2.split(" ")
    for  i in text1:
        if i in text2:
            textSum+=1
    if textSum ==0:
        return  "NULL"
    elif textSum==len(text2) if len(text2)>len(text1) else len(text1) :
        return Ctext1
    else:
        return text1[0]
    pass

if __name__ == '__main__':
    s ="This is C programming text"
    t = "This is a text for C programming"
    print(getCompareString(s,t))