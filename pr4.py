# 6a + 9b + 20c =n
from math import *
n=0
count=0
storen=0
print("Finding The highest value of n for which This equation is not true")
while True:
    counter=0
    sa = 0
    sb = 0
    sc = 0
    a = 0
    def swap1():
        global p1
        global p2
        temp = p1
        p1 = p2
        p2 = temp


    def swap2():
        global p2
        global p3
        temp = p2
        p2 = p3
        p3 = temp


    while ((6 * a) <= n):
        p1 = 0
        p2 = 0
        p3 = 0
        count1 = 0
        mid = 0
        if a != 0:
            mid = int(floor(a / 2)) + 1
        else:
            mid = 0
        for i1 in range(mid):
            p1 = int(a) - count1
            count2 = 0
            a2 = int(a) - p1
            mid2 = 0
            if a2 != 0:
                mid2 = int(floor(float(a2) / 2)) + 1
            else:
                mid2 = 0
            for i2 in range(mid2):
                p2 = a2 - count2
                count3 = 0
                a3 = a2 - p2
                p3 = 0
                mid3 = 0
                if a3 != 0:
                    mid3 = int(floor(float(a3) / 2)) + 1
                else:
                    mid3 = 0
                for i3 in range(mid3):
                    p3 = a3 - count3
                    for loop1 in range(3):
                        if ((6 * p1 + 9 * p2 + 20 * p3) == n):
                            if(counter==0):
                                count+=1
                            counter+=1
                            sa = p1
                            sb = p2
                            sc = p3
                        swap2()
                        if ((6 * p1 + 9 * p2 + 20 * p3) == n):
                            if (counter == 0):
                                count += 1
                            counter += 1
                            sa = p1
                            sb = p2
                            sc = p3
                        swap1()

                    count3 += 1
                if (a3 == 0):
                    for loop1 in range(3):
                        if ((6 * p1 + 9 * p2 + 20 * p3) == n):
                            if (counter == 0):
                                count += 1
                            counter += 1
                            sa = p1
                            sb = p2
                            sc = p3
                        swap2()
                        if ((6 * p1 + 9 * p2 + 20 * p3) == n):
                            if (counter == 0):
                                count += 1
                            counter += 1
                            sa = p1
                            sb = p2
                            sc = p3
                        swap1()
                count2 += 1
            if (a2 == 0):
                for loop1 in range(3):
                    if ((6 * p1 + 9 * p2 + 20 * p3) == n):
                        if (counter == 0):
                            count += 1
                        counter += 1
                        sa = p1
                        sb = p2
                        sc = p3
                    swap2()
                    if ((6 * p1 + 9 * p2 + 20 * p3) == n):
                        if (counter == 0):
                            count += 1
                        counter += 1
                        sa = p1
                        sb = p2
                        sc = p3
                    swap1()
            count1 += 1
        a += 1
    n+=1
    if count==6:
        storen=n
        break
    if sa == 0 and sb == 0 and sc == 0 and n!=0 :
        count=0
print( " And That is : ", (storen-7))