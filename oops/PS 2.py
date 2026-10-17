# n = 9
# while n <= 0:
#     print('positive')
#     break
# else:
#     print('negative')


# # count number of digits
# n = (int(input ("enter a number")))
# count = 0
# while n > 0:
#     ld = n%10
#     count+=1
#     n = n//10
# print(count)


# # sum of digits
# n = (int(input ("enter a number")))
# sum = 0
# while n > 0:
#     ld = n%10
#     sum+=ld
#     n = n // 10
# print(sum)



#automorfic number 
n = (int(input ("enter a number")))
sq = n*n
while n > 0:
    ld=n%10
    ld2=sq%10
    if ld!=ld2:
        print('not a automorfic number')
        break
    n = n//10
    sq=sq//10
else:
    print('automorfic number')

