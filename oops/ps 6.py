# #patterns


# #square pattern
# n = int(input("enter a number"))
# for i in range(n):
#     print("*  "*n)
         #OR
# n  = int(input ("enter a number"))
# for i in range(n):
#     for j in range(n):
#         print("*" ,ends=' ')



# #rectangle pattern
# n = int(input("enter a number"))
# for i in range(5):
#     print("* "*n)


#triangles
# n = 5
# for i in range(n):
#     print(" ")
# for j in range(n):
#     print("*"*j)


# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i)


# n = 4
# for i in range(n , 0 , -1):
#     print(' '*(n-i)+'*'*i)


#perimid
# for i in range(1,6):
#     print(" " *(5-i)+"*" *(2*i-1))


# #hallow square
# n = 4
# for i in range(n):
#     for j in range(n):
#         if i ==0 or j ==0 or i ==n-1 or j ==n-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()




# #hellow triangle
# n = 7
# for i in range(n):
#     for j in range(n):
#         if  i ==n-1 or j==0 or i==j:
#              print("*", end=' ')
#         else:
#             print(' ',end=' ')
#     print()
   


# #+ pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if   j==2 or i==2:
#              print("*", end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# #dimond
# n = 3
# for i in range(1,n+1):
#     print(" " *(n-i)+"*" *(2*i-1))
# for j in range(n-1,0,-1):
#     print(" "*(n-j)+"*" * (2*j-1))



#number pattern
for i in range (1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()