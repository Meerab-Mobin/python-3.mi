# problem no 1:your age 
def age (current_year:int, ) :
    current_year = 2024
    birth_year = int(input("your birth year: "))
    your_age = current_year - birth_year
    print(your_age )



#area of rectangle
def area ():
    lenght=int(input("enter the lenght of rectangle"))
    width=int(input("enter width of ractangle "))
    area= lenght*width
    print(area)

#area of circle 
def area2 ():
    r = float(input("radius of the circle: "))
    pie_of_circle = float(input("pie:   "))
    area = (r**2)*pie_of_circle
    print(area)

#area of cube
#area=6a**2
def area_of_cube ():
    a =float(input("a is equal to: "))
    v=int(6)
    area_of_cube =(a**2)*v
    print(area_of_cube)

#temp from F to C
def celsius():
    FRY=float(input("temp in F:  "))
    Celsius =(5) /(9)*(FRY)-(32)
    print(Celsius)

#calculate a percentage
def percentage():
    obtain_number =float(input("obtain number:  "))
    total_number = float(input("total number:  "))
    percentage = (obtain_number)/(total_number)*(100)
    print(percentage)

#seconds into minutes
def sacond():
    variable=int(input("variables:  "))
    seconds=(variable)/(60)
    print(seconds)
 
#minutes into seconds
def minutes():
    variable=int(input("variable:  "))
    minutes= (variable)*(60)
    print(minutes)

#volume of a cylinder
#formula :pie r saqure h
def volume():
    height = float(input("heightof a cylinder: "))
    r = float(input("r :  "))
    pie =float(input("pie:  ")) 
    volume =(pie)*(r)**2 *(height)
    print (volume)

#calculate the BMI
def BMI ():
    height =float(input("height: "))
    weight =float(input("weight: "))
    BMI =(weight)/(height)**2
    print(BMI)       

