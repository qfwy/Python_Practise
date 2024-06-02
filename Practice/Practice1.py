# """https://www.runoob.com/python/python-100-examples.html"""
# """1.题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？"""
# for i in range (1,5):
#     for j in range (1,5):
#         for k in range (1,5):
#             if i !=j and i !=k and j!=k:
#                 print(i,j,k)
#
# """2.题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？"""
#
# profit= int(input("profit"))
# list=[1000000,600000,400000,200000,100000,0]
# percentage=[0.01,0.015,0.03,0.05,0.075,0.1]
# r=0
#
# for j in range (0,6):
#     if profit > list[j]:
#         r+=(profit-list[j])*percentage[j]
#         profit=list[j]
# print(r)
#
# """3.题目一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？"""
# """
# x+100=n^2
# x+100+168=m^2
# (m+n)(m-n)=168
# m+n=i  m-n=j均为偶数，所以1<i<168/2+1=85
# m = (i + j) / 2， n = (i - j) / 2
# """
# for i in range(1,85):
#     if 168%i ==0:
#         j = 168/i;
#         if i>j and (i+j) % 2 ==0 and (i-j) % 2 ==0:
#             n = (i - j) / 2
#             x=n*n-100
#             print (x)
# """4.题目：输入某年某月某日，判断这一天是这一年的第几天？"""
#
# year= int(input("Year:\n"))
# month= int(input("Month:\n"))
# day= int(input("Day:\n"))
# sum=0
# list_day=[0,31,59,90,120,151,181,212,243,273,304,334,]
#
# if 0< month <=12:
#     sum= list_day[month-1]
# else:
#     print(f"wrong month")
#
# if year%4==0 or year%400 == 0 and year%100!=0:
#     leap=1
# else:
#     leap=0
# if month>2:
#     sum+=leap
# sum+=day
# print(f"The day is {sum}")
#
# """5.题目：输入三个整数x,y,z，请把这三个数由小到大输出。"""
# list=[]
# for i in range(0,3):
#     num=int(input("Num:"))
#     list.append(num)
# list.sort()
# print(list)
#
# """题目：斐波那契数列
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# """
#5
# a=1
# b=1
# list=[]
# no=int(input("No."))
# for i in range(no-1):
#     a, b = b, a + b
#     list.append(a)
# print(list)
# """题目：输出 9*9 乘法口诀表"""
#
# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         print('%d×%d=%d'%(i,j,i*j),end=' ')
#
# """题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# 1,1,2,3,5,6,11
# """
#
# month=int(input("Month:"))
# list=[1,1,2]
#
# if month <4:
#     for i in range(1, month + 1):
#         total=list[i-1]
# else:
#     a, b, c = 1, 1, 2
#     for i in range(4,month+1):
#         total=b+c
#         a,b,c=b,c,total
# print(total)
#
# """题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　　　
# 程序源代码："""
#
# from math import sqrt
# leap=0
# total=0
# for i in range(101,201):
#     k= int(sqrt(i))
#     leap = 0
#     for m in range(2,k+1):
#         if i%m==0:
#             leap=1
#             break
#     if leap==0:
#         total+=1
#         print(i)
# print(total)
#
# """题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。"""
#
# for i in range(100,1000):
#     hun=int(i/100)
#     ten=int((i-hun*100)/10)
#     one=int(i-hun*100-ten*10)
#     if i == hun ** 3 + ten ** 3 + one ** 3:
#         print(i)
#
# """题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。"""
# from math import sqrt
# num=int(input("Enter a number:"))
# num_orign=num
# list=[]
# while num<=0:
#     print("wrong num,plz enter again")
#     num=int(input("Enter a number:"))
# for i in range(2,num+1):
#     while num%i==0:
#         num=num//i
#         list.append(i)
# if len(list)==1:
#     print("It is a prime num.")
# else:
#     output= '*'.join(map(str,list))
#     print(num_orign,"=",output)
# """题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。"""
# name_score={}
# while True:
#     name=input("Enter your name(type exit to stop): ")
#     if name.lower() =="exit":
#         break
#     score=int(input("Input score for {}:".format(name)))
#     name_score[name]=score
# for name,score in name_score.items():
#     if score>=90:
#         grade = "A"
#     elif score >=60:
#         grade = "B"
#     else:
#         grade = "C"
#     print(f"{name} scored {score},belongs to {grade}")
# """求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。"""
# a=int(input("Give a number:"))
# n=int(input("How many times:"))
# sum=0
# Tn=0
# for i in range(1,n+1):
#     Tn+=a
#     a*=10
#     sum+=Tn
#     print (sum)
# """题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。"""
# perfect_numbers = []
# for i in range(2,1001):
#     factors=[k for k in range(1,i) if i%k==0]
#     if sum(factors)==i:
#         perfect_numbers.append((i, factors))
# for num, factors in perfect_numbers:
#     print(f"{num} is a perfect number with{"," .join(map(str,factors))}")
# """题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"""
# total=0
# height_now=100
# times=int(input("Which time:"))
# for i in range(1,times+1):
#     if i==1:
#         total=height_now
#     else:
#         total+=height_now*2
#     height_now/=2
# print(height_now,total)
# """猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，
# 又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。"""
# now=1
# for i in range(9):
#     yesterday=(now+1)*2
#     now=yesterday
# print(yesterday)
# """两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。"""
# for i in range(ord('x'),ord('z') + 1):
#     for j in range(ord('x'),ord('z') + 1):
#         if i != j:
#             for k in range(ord('x'),ord('z') + 1):
#                 if (i != k) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))
#
# """
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *"""
# for i in range(1,5):
#     print(" "*(4-i),"*"*(2*i-1))
# for i in range(3,0,-1):
#     print(" "*(4-i),"*"*(2*i-1))

# """有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。"""
# result=0
# total=int(input("Total:"))
# def num_up(total):
#     a, b = 1, 2
#     for i in range(1,total+1):
#         a,b=b,a+b
#     return a
#
# def num_down(total):
#     a, b = 1, 2
#     for i in range(1,total):
#         a,b=b,a+b
#     return a
#
# for i in range(1,total+1):
#     numerator=num_up(i)
#     denominator=num_down(i)
#     result+=numerator/denominator
# print(result)
# """题目：求1+2!+3!+...+20!的和。"""
# new_now=1
# result=0
# for i in range(1,21):
#     now=i
#     new_now *= now
#     result += new_now
# print(result)