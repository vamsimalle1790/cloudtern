# n=6
# while n>1:
#     if n%2==0:
#         n=n//2
#     else:
#         n=n*3+1
# print(n)
# n=1235
# x=''
# while n!=0:
#     y=n%10
#     x+=str(y)
#     n=n//10k=4387
# def hii():
#     nonlocal k
#     k=3738
#     print(k)

# hii()

# print(x)

# n=91
# x=2
# s=[]

# while x<(n//2)+1:
#     if n%x==0:
#         s.append(x)     
#     x+=1

# print(min(s))

# n=int(input("entre:"))
# k="yes" if (n%4==0 or n%100!=0) and n%400==0 else "not"
# print(k)
k=4387
# def hii():
#     nonlocal k
#     k=3738
#     print(k)

# hii()

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # Expected Output: [2, 4, 6, 8]
# x=[]
# k=[x.append(j) for i in matrix for j in i if j%2==0]
# print(x)

# s = "123"
# k = 3
# # Expected Output: ['abc', 'bcd', 'cde', 'def']
# x=[s[i:k+i]for i in range(len(s)) if len(s[i:k+i])==k]
# print(x)

# k=[1,2,3]
# h=[]
# result=[[]]
# for i in k:
    
#     result+=[num+[i]for num in result]
# print(result)

# x,*y=1,[1,2,34]
# print(*y[0])

# h=[[]]
# k=[1,2,3]
# y=[h.extend([i+[j] for i in h])for j in k]
# print(h)

# print("chat with chatbpt(say to bye to exist)")

# while True:
#     k=input("enter")
#     if k.lower()=="bye":
#         print("my time is comoplted bye man")
#         break
    
#     else:
#         print(f"u said {k} intresting !")
    

# loan=5000
# emi=1000
# month =0
# while True:
#     k=int(input("enter emi amount:"))
#     if k!=emi:
#         print("enter corect emi amount")
#     else:
#         loan-=k
#         month+=1
#     if loan==0:
#         print(f"your baclanceamount is {loan} is fully paid for months {month}")
#         break

# from time import sleep
# l=[]
# hour=0
# while len(l)<=24:
#     temp=int(input("eter weather reading:"))
#     hour+=1
#     l.append(temp)
#     sleep(2)
# print(f"avaerage of tempature {sum(l)/len(l)}")

# l1=["vmai",'krishna','ajau']
# borow=[]
# view=[]
# while True:
#     print("these are the books available",l1)
#     k=input('enter book name:')
#     if len(l1)>0:
#         if k in l1:
#             borow.append(k)
#             l1.remove(k)
#         else:
#             print("plases enter valid book name")
#     else:
#         print("no books aailable now")
#         break
#     if k.lower()=='no':
#         print("iam exit")
#         break    
# quiz = {
#     "What is the capital of France?": "Paris",
#     "Which planet is known as the Red Planet?": "Mars",
#     "Who wrote the play 'Romeo and Juliet'?": "Shakespeare",
#     "What is the largest mammal in the world?": "Blue Whale",
#     "Which element has the chemical symbol 'O'?": "Oxygen"
# }
# sum=0
# for i,j in quiz.items():
#     print("each question have 100 marks",i)
#     k=input("enter ans for this::::")
#     if quiz[i].lower()==k:
#         sum+=100
# print("your final score is",sum)

    
# def vamsi():
#     return 'vamsi'
# # print(vamsi())
# result=vamsi()
# print(result)
# n=1
# while n<=5:
#     [print(" ",end="") for j in range(5,n,-1)]k=4387
# def hii():
#     nonlocal k
#     k=3738
#     print(k)

# hii()

#     [print('*',end='')for i in range(n)]
        
#     print()
#     n+=1

######FUCTIONS
# def vamsi(a,b):
#     print(a)
# vamsi(b=20,a=10)

# def sub(nums):
#     result=[[]]
#     [result.extend([j+[num]for j in result])for num in nums]
#     return result

# nums=[1,2,3]
# print(sub(nums))

#####ASSIGNMENT

# num=int(input("enter a number:"))
# assert num<0, 'number always greterthan zero'
# x="given number is even" if num%2==0 else "given number is odd"
#print(x)



# #Create a function that takes two numbers as input and returns their sum.
# def sum(a,b):

#     return a+b
# result=sum(10,20)
# print(result)

#Write a loop to print all prime numbers between 1 and 100.
#l=[]
# for i in range(1,100):
#     if i >1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             l.append(i)
# print(l)

#Create a dictionary with 5 key-value pairs and iterate through it to print the keys and values.
# d1={1:'vamsi',2:'krishna',3:'cloud',4:'ai',5:'future'}
# [print((i,j)) for i,j in d1.items()]

#Write a program to find the factorial of a number using a while loop.

# n=int(input("enter a number:"))
# fact=1
# while n>=1:
#    print("factorial of n is", 1) if n in (0, 1) else None
#    fact*=n
#    n-=1
# print("factorial of a given numberis",fact)

#Use a list comprehension to create a list of squares for numbers between 1 and 10 that are divisible by 2.
#[print(i**2)for i in  range(1,10) if i%2==0]

#Implement a function that accepts a string and returns the count of vowels in the string.
# def strg(s1):
#     # print(type(s1))
#     if type(s1)!=str:
#         raise TypeError("input must be the string")
    
#     return sum(1 for i in s1.lower() if i in 'aeiou')
# # k=input('enter:')
# print(strg('gtssh'))


    
######functions again ########
x=10
def hello():
    y=30
    #print(m)
    print(y)
    def hi():
        m=10
        # nonlocal y
        # y=45
        # print(45)
        print(x)
        def mmm():
            nonlocal y
            y=10
            print(y)
        mmm()
    def hmm():
        global z
        z=1111
        print(y)
    
    hi()
    hmm()
    print(y)
hello()
print(z)

# k=4387
# def hii():
#     nonlocal k  ##shows error because we have to define
#     k=3738
#     print(k)

# hii()

k="1(*) 9(*) 3(*) 5(*)"
print(k)

m=k.split()
print(m)
h=[]
for i in m:
    # print(len(i))\
    # for j in i:
        # if 
    
    k=i.split('(*)')[0]
    #print(k)
    h.append(k)
#print(h)
for i in h:
    print('*'*int(i))
    
   
           











