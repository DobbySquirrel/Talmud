# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 12:31:53 2021

@author: dobby

"""
# MY分部
#以题目为例，可修改 per 和 total

"""输入各个人需要的价钱"""
per=[98,102,200,300,400]
"""输入总价钱"""
total=[100,300,350,400,600,700,900,1000,1100]
half=[i/2 for i in per]
per.sort()
lenPer=len(per)
solve=[0]*lenPer
value=list(range(lenPer))
#第二轮,计算差值
err=[0]*(lenPer-1)
for i in range(lenPer-1):
    err[i]=(per[i+1]-per[i])/2* (lenPer-1-i)

for i in total:
    remain=i
    for j in range(lenPer):
        if(remain/(lenPer-j)<half[j]):
            solve[j:]=[remain/(lenPer-j)]*(lenPer-j)
            break
        else:
            solve[j]=half[j]
            remain=remain-solve[j]
            if(j==lenPer-1):
            #还有剩余，开始第二轮
                for e in range(j):
                    if(remain<err[j-1-e]): 
                        solve[j-e:]=[s+remain/(e+1) for s in solve[j-e:]]
                        break
                    else:
                        remain=remain-err[j-1-e]
                        solve[j-e:]=[s+err[j-1-e]/((e+1)) for s in solve[j-e:]]
   #第三轮，平均给                    
    if(remain!=0):
        solve=[s+remain/lenPer for s in solve]
    dictout=dict(zip(per,solve))
    print("总金额为%d的分配金额{希望获得：实际获得}"%(i))
    print(dictout)
            