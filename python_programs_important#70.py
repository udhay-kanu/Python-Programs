#!/usr/bin/env python
# coding: utf-8

# #basic syntax andi/o
# #1.print hello world
# 

# In[1]:


print('hello world')


# #2.take the user input and print it
# 

# In[2]:


abc=input('enter the input:')
print(abc)


# #.3.swap two variables
# 

# In[8]:


a=5
b=2
temp=a
a=b
b=temp
print(a,b)


# #4.check if a number is an even or odd

# In[11]:


def even_or_odd(num):
    if num%2==0:
        print('even')
    else:
        print('odd') 


# In[12]:


even_or_odd(3)


# #5.find the largest of two number.

# In[13]:


lst=[1,2,34,5,6,89]
maximum=lst[0]
for i in lst:
    if maximum>0:
        maximum=i
print('the highest number is:',maximum)


# In[14]:


def lowest(lst):
    minimum=lst[0]
    for i in lst:
        if i<minimum:
            minimum=i
    return minimum


# In[16]:


lowest([2,3,-44,5,6])


# #.find the lowest and the highest

# In[18]:


def lowest_highest(lst):
    maximum=lst[0]
    minimum=lst[0]
    for i in lst:
        if i>maximum:
            maximum=i
        else:
            for i in lst:
                if i<minimum:
                    minimum=i
    print('the highest number in the list:',maximum)
    print('the lowest number in the list:',minimum)


# In[20]:


lowest_highest([1,2,3,4,5,6,7])


# ##operators
# #6.perform arithmetic operations(+,-,*,/,%,**)take any values as "a" and "b"

# In[21]:


def add_sub_mul_div(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    sqrt=a**b
    print('the sum of two numbers:',add)
    print('the subtraction of two numbers:',sub)
    print('the multiplication of two numbers:',mul)
    print('the division of two numbers:',div)
    print('the square of the numbers is:',sqrt)


# In[24]:


add_sub_mul_div(7,2)


# #7.calculate the square and cube of a number|

# In[25]:


def square_cube(num):
    sqrt=num*num
    cube=num**num
    print('the square of number :',sqrt)
    print('the cube of number:',cube)


# In[27]:


square_cube(4)


# #8.convert celcius to fahrenheit

# In[28]:


def celsius_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
    


# In[30]:


celsius_fahrenheit(37)


# #9.convert kilometres to miles

# In[31]:


def kilo_miles(kilo):
    miles=kilo*0.621371
    return miles


# In[33]:


kilo_miles(100)


# #10.check if a number is positive ,negative,zero

# In[34]:


def pos_zer_neg(num):
    if num>0:
        return 'postive'
    elif num==0:
        return 'zero'
    else:
        return 'negative'


# In[36]:


pos_zer_neg(0)


# #conditional statements
# #11.find the largest of the three numbers

# In[37]:


def largest(lst):
    maximum=lst[0]
    for i in lst:
        if i>maximum:
            maximum=i
    return maximum


# In[38]:


largest([1,92,390,78,0,89])


# In[39]:


#using loops
list1=[2,3,4,65,0,4,90]
maximum=list1[0]
for i in list1:
    if i>maximum:
        maximum=i
print('the highest of the list', maximum)
    


# #12.check if a year is a leap year ,a leap year that is divisible by 4,but if it is century year(divisible by 100),it must be divided by 400
# 

# In[41]:


year=int(input('enter the year'))
if year%4==0:
    print('leap_year')
elif year%100==0:
    print('leap_year')
elif year%400==0:
    print('leap_year')
else:
    print('non_leap_year')


# #13.check if a character is a vowel or consonent

# In[42]:


cha=str(input('enter the character:'))
#for i in cha:
if cha.isalpha():
    if cha.lower() in 'aeiou':
        print('vowels')
    else:
        print('consonents')
else:
    print('not a valid character')
    


# In[43]:


def check_char(char):
    if char.isalpha():
        if char.lower() in "aeiou":
            return 'vowel'
        else:
            return 'consonent'
    else:
        return 'nota valid character'


# In[45]:


check_char('u')


# #14.code to assign grades for the subjects based on grade

# In[47]:


marks=int(input('enter the marks'))
if marks>=90:
    print('A grade')
elif marks>=80:
    print('B grade')
elif marks>=70:
    print('C grade')
elif marks>=60:
    print('D grade')
elif marks>=50:
    print('E grade')
else:
    print('fail')


# #15.prgm to check if a number is divisible by both 5 and 11

# In[48]:


def divi_5_11(num):
    if num%5==0:
        if num%11==0:
            print('number is divisible:')
        else:
            print('number is not divisible:')
    else:
         print(' number is not divisible by :')
            


# In[50]:


divi_5_11(55)


# #16.print the numbers from 1 to the given number N

# In[52]:


for i in range(1,8):
    print(i)


# #17.print the even numbers up to the given number

# In[53]:


def even_num(n):
    for i in range(2,n+1,2):
        print(i)


# In[56]:


even_num(20)


# #18.sum of first n natural numbers

# In[57]:


def sum_numbers(n):
    return n*((n+1)/2)
     


# In[59]:


sum_numbers(5)


# #.calculate the factorial of numbers

# In[61]:


def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)


# In[62]:


factorial(2)


# #20.print mutiplication of a number

# In[63]:


def multiply(n):
    for i in range(1,11):
        print(4*i)


# In[65]:


multiply(4)


# #21.strings
# #write the prgm to reverse a given string

# In[66]:


def reverse_string(input_str):
    return ','.join(input_str)[::-1]


# In[68]:


reverse_string('uday')


# #22.check wheather the string is a palindrome or not

# In[70]:


def palindrome(input_str):
    input_str=input_str.replace('','').lower()
    return input_str==input_str[::-1]


# In[72]:


palindrome('110011')


# #23.count the niumber of vowels in the string

# In[73]:


def count_str(input_str):
    vowels='aeiouAEIOU'
    count=0
    for vowel in input_str:
        if vowel in vowels:
            count+=i
    return count


# In[75]:


count_str('a')


# #24.convert the uppercase() to lower case and vice versa

# In[76]:


def upper_lower_case(input_str):
    upper=input_str.upper()
    lower=input_str.lower()
    return lower,upper
    


# In[77]:


upper_lower_case('Uday')


# #25.find the length of the string without using len()

# In[78]:


def string_length(input_str):
    count=0
    for char in input_str:
        count+=1
    return count


# In[80]:


string_length('uday')


# #26.find the largest element in the  list

# In[81]:


def upper(lst):
    maximum=0
    for i in lst:
        if i>maximum:
            maximum=i
    return maximum


# In[83]:


upper([3,4,5,6])


# #27.find the smallest in the list

# In[84]:


def lower(lst):
    minimum=0
    for i in lst:
        if i<minimum:
            minimum=i
    return minimum


# In[86]:


lower([1,2,3,4,5,6])


# #28.find the sum of elements in alist

# In[87]:


def sum_elements(lst):
    total=sum(lst)
    return total


# In[89]:


sum_elements([1,2,3,4,5])


# #29.sort the list in ascending order

# In[1]:


def ascending(lst):
    sorted_lst=sorted(lst)
    return sorted_lst


# In[2]:


ascending([4,3,2,9,5,1])


# #30.remove duplicates fromthe list

# In[3]:


def duplicates(lst):
    return list(set(lst))


# In[5]:


duplicates([1,2,3,2,3,4,5])


# #31.tuples:find the maximum AND MINIMUM NUMBER IN A TUPLE

# In[6]:


def max_min(my_tuple):
    mini=min(my_tuple)
    maxi=max(my_tuple)
    return mini,maxi


# In[8]:


max_min((9,2,3,84,-2,5,))


# #32.convert a tuple into a list

# In[9]:


def con_lst_tple(my_tuple):
    new_list=list(my_tuple)
    return new_list


# In[11]:


con_lst_tple((1,2,3,4,5))


# #33.convert occurences of an element ina tuple

# In[12]:


def count_1(my_tple):
    count=my_tple.count(2)
    return count


# In[15]:


count_1((2,3,4,5,6,7,7,3))


# #34.find the index of an elements in a tuple

# In[16]:


def index(my_tuple):
    inde=my_tuple.index(4)
    return inde


# In[18]:


index((1,2,3,4,2,3,4))


# #35.reverse a tuple

# In[19]:


def reverse(my_tuple):
    rev=my_tuple[::-1]
    return rev


# In[21]:


reverse(('kanugonda','uday','kumar'))


# #36.create an empty set

# In[23]:


empty_set=set()
print(empty_set)


# #37.perform union of two sets

# In[24]:


def union_set(set1,set2):
    union=set1.union(set2)
    return union


# In[27]:


union_set({2,3,4,5},{2,7,6,4})


# #38.perform instructions of two sets

# In[28]:


def ins_set(set1,set2):
    union_set=set1 | set2##union-set1.union(set2)
    return union_set
def inter(set1,set2):
    intersect=set1&set2##intersection_set-set1.intersection(set2)
    return intersect
def difference(set1,set2):
    diff=set1-set2##difference-set1.difference(set2)
    return difference
def symmetric_difference(set1,set2):
    symm=set1^set2#symmetric_difference=set1.symmetric_difference(set2)
    return symm


# In[30]:


ins_set({2,3,4,5},{4,5,6,7})


# #39.perform the difference of two sets

# In[31]:


def diff(set1,set2):
    differ=set1-set2
    return differ


# In[32]:


diff({9,8,6,7,2},{5,6,4,3,2})


# #40.check if a set is subset of another

# In[35]:


def subset(set1,set2):
    res=set1.issubset(set2)
    if res==True:
        print('subset')
    else:
        print('not a subset')


# In[37]:


subset({2,3,4,5,6},{3,4,5})


# #41.remove an element from a set

# In[39]:


def discard(set1):
    res=set1.discard(4)
    return set1


# In[40]:


discard({2,3,4,5,6})


# In[42]:


my_set={2,3,4,5,6}
result=my_set.remove(4)
print(my_set)


# #35.reverse a tuple
# 

# In[49]:


def reverse(my_tuple):
    rev=my_tuple[::-1]
    return rev


# In[44]:


reverse('uday')


# #42.dictionaries
# #.create a dictionary and print the keys and values

# In[45]:


my_dict={'name':'Uday Kumar','education':'B.tech','age':23}


# In[46]:


print(my_dict)


# In[47]:


print(my_dict.keys())


# In[49]:


print(my_dict.values())


# #43.find the sum of dictionaries values

# In[53]:


my_val={'banana':23,'apple':22,'papaya':2}


# In[54]:


total=sum(my_val.values())


# In[55]:


print(total)


# #44.merge of two dictionaries

# In[56]:


def merge(dict1,dict2):
    dict1.update(dict2)
    return dict1


# In[57]:


merge({'a':2,'b':4},{'b':4,'c':6})


# #45.sort the dictionary by its values

# In[58]:


def sorting(my_dict):
    sort=dict(sorted(my_dict.items(),key=lambda item:item[0]))
    return my_dict


# In[60]:


sorting({'a':24,'b':21,'c':25})


# #46.count the occurences of elements in a dictionary

# In[65]:


from collections import Counter
my_dict={'a':2,'b':4,'c':6,'d':6}
count_dict=Counter(my_dict.values())
print(count_dict)


# #47.mathematical programs
# #check if a number is prime or not

# In[66]:


def prime_number(num):
    if num<=1:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
    return True


# In[68]:


prime_number(43)


# #48.find the sum of digits of a number

# In[69]:


def sum_digits(num):
    total=0
    for i in str(num):
        total+=int(i)
    return total


# In[71]:


sum_digits(678)


# #49.lcm of two numbers

# In[72]:


def lcm(a,b):
    larger=max(a,b)
    while True:
        if larger%a==0 and larger%b==0:
            return larger
        larger+=1


# In[73]:


lcm(12,18)


# #50.find the GCD of two numbers

# In[74]:


def gcf(a,b):
    while b:
        a,b=b,a%b
    return a


# In[76]:


gcf(48,180)


# #51.define a function to find the sum of two numbers

# In[77]:


def total(num1,num2):
    total=num1+num2
    return total
    


# In[78]:


total(3,4)


# #52.define a function to return the square of the number

# In[79]:


def square(num):
    numb=num*num
    return numb


# In[81]:


square(3)


# #53.define a function with default arguments

# In[82]:


def greet(name='guest',message='hello'):
    return name,message


# In[84]:


greet('ramu','kumar')


# #54.define a function  with varaible length arguments

# In[85]:


def display(*args,**kwargs):
    return args,kwargs


# In[87]:


display(1,2,3, name='uday',age=30)


# #55.define a function that returns multiple values
# 

# In[88]:


def add_sub_mul_div(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return add,sub,mul,div


# In[90]:


add_sub_mul_div(4,6)


# #56.use a lambda function to add two numbers

# In[91]:


add=lambda x,y:x+y
result=add(5,4)
print(result)


# #57.use a lambda function to find the maximum of two numbers

# In[92]:


maxi=lambda x,y:x if x>y else y
result=maxi(4,5)
print(result)


# #58.use a lambda function to square a number

# In[93]:


square=lambda x:x*x
result=square(5)
print(result)


# #59.use a lambda function inside map()

# In[94]:


numbers=[1,2,3,4,5]
number=map(lambda x:x*2,numbers)

print(list(number))


# #60.use a lambda function inside filter()

# In[96]:


numbers=[1,2,3,4,5,6]
even_numbers=filter(lambda x:x%2==0,numbers)
print(list(even_numbers))


# #list comprehension
# #61.generate a list of squares using list comprehension

# In[98]:


squares=[x**2 for x in range(10)]
print(squares)


# #62.generate the list of even_numbers using the list comprehension

# In[100]:


even_numbers=[x for x in range(20) if x%2==0]
print(even_numbers)


# #63.reverse the list using list comprehension

# In[102]:


lis1=[2,3,4,5,6,7,9]
reverse=[lis1[i] for i in range(len(lis1)-1,-1,-1)]
print(reverse)


# #64.flattern the nested list using list comprehension

# In[104]:


nested_list=[[1,2,3,4],[5,6],[9,8,7,7]]
flattened_list=[item for sublist in nested_list for item in sublist]
print(flattened_list)


# #65.find the common elements in two lists using list comprehension

# In[105]:


list1=[1,2,3,4,5]
list2=[2,3,5,6,7]
common_elements=[x for x in list1 if x in list2]
print(common_elements)


# #66.miscellanious
# #.swap two numbers without using a third variable

# In[107]:


a=5
b=10
a,b=b,a
print('a',a)
print('b',b)


# #67.count occurences of each word in a sentence

# In[108]:


sentence='My name is kanugonda uday kumar and my father name is Sivanna'
words=sentence.split()
word_cnt={words:words.count(words) for words in set(words)}
print(word_cnt)


# In[109]:


from collections import Counter
sentence='this is my name my name is uday'
words=sentence.split()
word_cnt=Counter(words)
print(word_cnt)


# #68.find the second largest number in a list

# In[111]:


numbers=[10,70,20,30,40,90]
numbers.sort()
second_largest=numbers[-2]
print(second_largest)


# #69.check if  two strings are anagrams

# In[112]:


def are_anagrams(str1,str2):
    return sorted(str1)==sorted(str2)


# In[114]:


are_anagrams('listen','silent')


# #70.print pascals triangle

# In[116]:


def pascals_triangle(n):
    triangle=[]
    for i in range(n):
        row =[1]*(i+1)
        for j in range(1,i):
            row[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
    for row in triangle :
        print(''.join(map(str,row)))


# In[117]:


pascals_triangle(5)

