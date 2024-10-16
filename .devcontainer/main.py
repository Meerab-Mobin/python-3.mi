# class no 1


#methods of assigning name to a variable :


userName:int=10 #camel case : first letter is small and first letter of second name is capital
user_name:int=10 #snake case: all letter are small with underscore
UserName:int=10 #pascalcode: first letters of all words is capital
username:int=10 #smallcase : all letters are small
USERNAME:int=10 #upper case: all letters are capital


#Data types : 
 #1) Integer : int ; 1,2 
 #2) float : float; 1.1 , 2.9
 #3) Boolean : bool ; true or false
 #4) string : str ; "My name is Meerab"
 #5) complex : complex ; pie , sigma , iota (i)


#OPERATORS: 
    #1) arithematic operators + ,- ,* /
    #2) assignment operator =
    #3) arithematic assignment operator += ,-= , /= , */ 
    #4) comparison operator <, > , == ,!=    
    # comparison operators: 
        # greater > ,
        # smaller < ,
        # equals to == 
        # not equals to !=
        # these operators present answer in boolean( True or False)
    #5) logical operators  AND ,NOT , OR
    #6) unordinary operators :  
        # Floor(//) : it will present the answer of division(quotient) in whole  numbers 
        # Exponent(**): it will raise the power of number to given number e:g 2**3 = 8
#7 int(input("enter a number":))
#8   
#practice:  
#userName:str="nouraiz
# num1:int=10
#not:float=10.5
#active:bool=truepython  

#pactice of int
num1:int=10
num2:int=20
print(10+20) 
 
 #practice of str
firstName:str="meerab"
lastName:str="mobin"
print(firstName+lastName)

#pactice of arthematic operations

num3=num1-num2*6
print(num3)

print(id(num1))

print(type(num3))

a:int=55
b:int=60
c:int=60%55
print(c)

a=2
b=5
c=2**5
print(c)

c = 2//5
print(c)

#arthematic asignment operators
a+=5
a-=5
a*=5
a/=5
a%=5 


#clas no 2

#practice of str 
userName1:str= "meerab"#you can only write string in one line
userName2:str= 'mobin'# same as above 
username3: str =""" meerab mobin""" # you can create paragrafhs
#ex to know how to ad statements
userNAm:str =userName1 + "is a good student "
print (userNAm)


#method 1 
usernama :str = userName2 +"isa good student "
print(usernama)


#method 2
username: str ="{} is a {}  good student" . format(username3  , userName2)
print(username)


#method 3 
userHat :str = f" {userName1 } is a { userName2} daughter"
print(userHat)


# making blocks 
def ADDTWONUM (): 
    num1 = 10
    num2 = 20 
    result = num1 + num2
    print (result)


# METHOD 2
def addthreenum (num1:int,num2:int) : # nm in ( )caled apra metiers
    result:int  =( num1+num2 )
    return( result)
 
 # runing blocks
addthreenum(10,20) # built_in function # nm in () called argumaenT

#for out put 
finalOUTPUT:int = addthreenum(50,40)

print(finalOUTPUT)


#what is calling functions 
print()
int()
str()
float() 
input() #etc. 
#id() # gives address

# classs 4444444444444
# to call code many times #we will run about it #called loop 
 
# range 
#loop 
# #braek
#  #continue 
# #for
#  #while 
#i for index 
# first make list and name then then we take take "i" ,then we make statement that
while i < len(nums): # len means lenght of number 













#classs4 


#loop will not stop until value is false 
 count :int = 1
while count < 10 :
    print("hello world ", count )
    count = count +1
    

print("total ", count )

#list function
 
studentnames:list [str] = ["ali ","umer ", "meeran"]#list functoin will always be in[]

for username in studentnames:
    print(username )

print( "all is" ,username)

#different functions is list 

studentnames.append("tariq ")#to add something
studentnames.insert(2 ,"abc")# to add abc into no 2
studentnames.remove("ali")# to remove ali 
studentnames.pop(3) #we provide this no to remove 
studentnames.reverse()# to reverse student names 

# makiing of table of two 


#classs 7-8




try:
    result = 10/0 
except zerodivisionerror: 
    print("error ")

value error # for int 
exception as e # for unknown error 
zero division error # for zero 
# practice 


try: 
    result = 10/2  # always run 

except eexception as e :
    print ("an error occured: e ") # in case of error 

else :
    print ("suceess the result is :", result )   # it wil run 

finally : 
    print ( "close the file ")    # always run 

def division(a/b ):
    raise value error ("this is due to coustom error ")

# to run one file into other 
import # file name 
# now to call fuc from other file 
#file name . block  name 
                        # it willl take you to other file 
import helper.utilis as utillis                         
from data import printstudent 

#built in module 
# math ,random ,time                        
# random int  
# start time 
#sum
# end time  
#time.sleep()#ibrac()line no 

# file handling 
file = open ('example . txt ', 'r')# to open file in read mode 
content = file. read ()
print (content )
file . close 

#mehod 2 
with open('example.txt','r')as file  :
    content = file . read 
    print (content )

# same as    write w 
# same as append to combine both a ("/n then line ")

import os  
if os.path.exist ('example . txt ', ''):


os .mkdir('newfolder')
os.rename(newfolder, no folder )
os.rmdir ('renamed folder ')
os.listdir()
os.rm('')# to remove 

errors 
synthex error == system tell us about it 
logical error == system cnnot detect  only programmer can 
runtime error == program crash kar jata ha or iss kay liye try or except use kartay hai 
try ,except #like if and else 
except # ZerodivisionError:                       

class #parent 
supar 
constructre 
object 


