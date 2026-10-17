# # Print spy number

# n = 123
# sum = 0
# prod = 1
# while n>0:
#     d = n%10
#     sum+=d
#     prod*=d
#     n=n//10
# if sum == prod:
#     print("spy number")
# else:
#     print("not spy")


# #pritn a fibonacci number

# a = 0
# b = 1
# for i in range (1,6):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c



# #print 1 to 1000 armostrong numbers

for num in range(1,1001):
    st=str(num)
    l = len(st)
    arm = 0  
    for a in st:
        arm+=int(a)**l
    if arm==0:
        print("num")




##print 1 to 100 primre numbers

# for num in range(1,101):
#     count = 0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print(num)





