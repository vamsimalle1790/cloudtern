# from pprint import pprint

# data = {
#     "name": "Vamsi",
#     "age": 25,
#     "skills": ["Python", "FastAPI", "Kubernetes", "Azure"],
#     "projects": [
#         {"name": "Blog Platform", "status": "In Progress"},
#         {"name": "Task Management System", "status": "Planned"}
#     ]
# }
# pprint(data)

# pprint(data, width=40, indent=4)



###PYTHON DEBUGGER#####

#functions

# def calculate_sum(n):
#     total = 0
#     for i in range(n + 1):
#         total += i                    #break points to reviwe our code 
#     return total

# number = int(input("Enter a number: "))
# result = calculate_sum(number)
# print(f"Sum of numbers from 0 to {number} is: {result}")

# def factorial(n):
#     fact=1
#     print('factorial of n is ',1) if n in (0,1) else None
#     while n>0:
#         fact*=n
#         n-=1
# n=int(input("enter nuber:"))
# factorial(n)

# def fab(n,a,b):
#     for i in range(n):     ##we can also add conditinal break points
#         print(a)
#         a,b=b,a+b
# fab(6,0,1)

# def prime(n):
#         l=[]
#         for i in range(1,n):
#             if i>1:
#                 for j  in range(2,i//2+1):  ###wtches and call stack
#                      if i%j==0:
#                           break
#                 else:
#                      l.append(i)
#         print(l)
# prime(10)


# a=10
# globals()['a']=20
# print(a)
# x=20
# def vamsi():
#     globals()['x']=30
#     x=40
#     print(x)
# vamsi()
# print(x)


####RECURSION


#Fibonacci Series: Write a recursive function to calculate the nth Fibonacci number.

# def feb(n,a,b):
#     if n==0:
#         return None
#     print(a)
#     feb(n-1,b,a+b)
# feb(6,0,1)
    
# def sum(n):
#     if n==0:
#         return 0
#     return n%10+sum(n//10)
# print(sum(123))


# def revese(k):
#     if len(k)==1:
#         return k[0]
#     return k[-1]+revese(k[:-1])
# k='vamsi'
# print(revese(k))
##lambda
# y=2
# x=lambda x:x*x
# print(x(y))

# x=lambda x:'odd' if x%2!=0 else 'even'
# print(x(2))

# k=[(2, 3), (1, 2), (4, 1)]
# m=sorted(k,key=lambda x:x[0],reverse=True)
# print(m)

# l=[-1, 2, -3, 4, -5]
# h=filter(lambda x:x>0,l)
# print(list(h))

# from functools import reduce
# k=123
# h=reduce(lambda x,y:int(x)+int(y),''.join(str(k)))
# print((h))

# k = ["apple", "banana", "cherry", "date"]
# h = sum(k,key=lambda x: len(x))
# print(h)
# m=filter(lambda x: x[0] in 'aeiou',k)
# print(list(m))

# k='racecar'
# h=lambda x: ''.join(reversed(k))==k 
# print(h(k))

# l1=[1,2,3]
# l2=[1,2,3]
# k=map(lambda x,y:x*y,l1,l2)
# print(*k)



# def sub(l):
#     target=3
#     k=set()
#     for i in l:
#         s=target-i
#         if s in k:
#             return s,i
#         else:
#             k.add(i)
#     return None
# l1=[1,2,3,4,5,6,7]
# print(sub(l1))



def flatlist(l1):
    k=[]
    for i in l1:
         if isinstance(i,list):
            k.extend(flatlist(i))
         else:
            k.append(i)

    return k
l1 = [1, [2, [3, 4], 5], 6]

print(flatlist(l1))
