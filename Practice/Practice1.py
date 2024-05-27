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
"""4.题目：输入某年某月某日，判断这一天是这一年的第几天？"""

year= int(input("Year:\n"))
month= int(input("Month:\n"))
day= int(input("Day:\n"))
sum=0
list_day=[0,31,59,90,120,151,181,212,243,273,304,334,]

if 0< month <=12:
    sum= list_day[month-1]
else:
    print(f"wrong month")

if year%4==0 or year%400 == 0 and year%100!=0:
    leap=1
else:
    leap=0
if month>2:
    sum+=leap
sum+=day
print(f"The day is {sum}")
