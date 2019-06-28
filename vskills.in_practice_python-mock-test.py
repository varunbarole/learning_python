#list1 = [1,2,3,4,5]
#new_list = list1.insert(2,5)
#print (list1)

########################
#def func(a,b=4,c=12):
#    print(a,b,c)
#func(2,7)
#func(20,c = 13)
#func(c = 50,a = 10)
########################
#range11= range(2)
#print (range11)
########################
#def power(x, y=2):
#    r = 1
#    for i in range(y):
##        print(i)
#        r = r * x
#    return r
#print(power(2))
#print(power(2,3))
########################
#def maximum(x,y):
#    if x > y:
#        return x
#    elif x == y:
#        return 'the numbers are equal'
#    else:
#        return y
#print(maximum(2,3))
########################
#def foo():
#    return total + 1
#total = 0
#print(foo())
########################
#print("hello\example\test.txt")
########################
#def f1(x = 1, y = 2):
#    x = x + y
#    y += 1
#    print(x,y)
#f1(y = 2,x = 1)
########################
#x = ['ab','cd']
#for i in x:
#    x.append(i.upper())
#print(x)
########################
#print(0xA)
#print(0xB)
#print(0xC)
#print(0xA + 0xB + 0xC)
########################
#print('abcdedcdghcd'.split('cd',2))
########################
#count={}
#count[(1,2,4)] = 5
#print(count)
#count[(4,2,1)] = 7
#print(count)
#count[(1,2)] = 6
#print(count)
#count[(4,2,1)] = 2
#print(count)
#tot = 0
#print('initial value of tot is',tot)
#for i in count:
#    tot=tot+count[i]
#    print('Value of tot in loop is',tot)
#print('=======')
#print('Value in count is',count)
#print('=======')
#print('tot is', tot)
#print('=======')
#print('length of count + tot is',len(count)+tot)
########################
#[x*5 for x in range(2,10,2)]
#str = input("Enter you input: "); print("Received input is : ", str)
########################
#from unittest.mock import Mock
#mock = Mock()
#mock
#print (mock)
########################
#def test_args_kwargs(arg1, arg2, arg3):
#    print("arg1:", arg1)
#    print("arg2:", arg2)
#    print("arg3:", arg3)
#args = ("two", 3, 5)
##args = ["two", 3, 5]
#test_args_kwargs(*args)
#kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
#test_args_kwargs(**kwargs)
########################
#a = [0,1,2,3]
#i = -2
#for i not in a:
#    print(i)
#    i += 1
########################
#list1 = [3,4,5,20,5,25,1,3]
#list1.extend([34,5])
#print(list1)
########################
''' Infinite loop '''
#n=9
#while n!=0:
#    print(n)
#    n=n-2
########################
#def foo(x):
#    x[0]=['def']
#    x[1]=['abc']
#    return id(x)
#q = ['abc','def']
#print(id(q) == foo(q))
########################
#list1 = [1,3]
#list2 = list1
#list1[0] = 4
#print(list2)
########################
#a = [0,1,2,3]
#i = -2
#for i not in a:
#    print(i)
#    i += 1
########################
#def a(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return a(n-1)+a(n-2)
#for i in range(0,4):
#    print(a(i),end=" ")
########################
#x = 10
#def func(x):
#    x = 5
#    print(x)
#    x = 15
##    print(x)
#func(x)
#print(x)
########################
#class demo():
#    def __repr__(self):
#        return '__repr__ built-in function called'
#    def __str__(self):
#        return '__str__ built-in fucntion called'
#s = demo()
#print (s)
########################
#str = "Hello Python"
#str[3] = 'o'
#str[7] = 'i'
#print(str)
########################
#i = 0
#while i < 5:
#    print(i)
#    i += 1
#    if i == 3:
#        break
#else:
#    print(0)
########################
#class demo(dict):
#    def __test__(self,key):
#        return []
#a = demo()
#a['test'] = 7
#print(a)
########################
#print("abcdef".center(7,'1'))
########################
#a = [0,1,2,3]
#for a[-1] in a:
#    print(a)
#    print(a[-1])
########################
#str = "Vshills"
#print str.find("s")
##print (str.find("s"))
########################
#x = 'abcd'
#for i in range(len(x)):
#    x = 'a'
#    print(x)
########################
#def  foo(k):
#    k = [1]
#    q = [0]
#foo(q)
#print(q)
########################
#print type (type(int))
########################
#A = [[1,2,3],[4,5,6],[7,8,9]]
#B = [[3,3,3,],[4,4,4],[5,5,5]]
#col1 = A[0]
#col2 = A[1]
#print(col1)
#print(col2)
#[[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(A,B)]
########################
