# def greet():
#     print('Hello World')
# greet()
# def greet(name='User',time='day'):
#     print(f'Good{time} {name} , hope you are well')
# name=input('Enter your name: ')
# time=input('Enter the time of day: ')
#
# greet(name='Akash')
def area(radius):
    return 3.142*radius*radius
def vol(area,length):
    print(area*length)

radius = int(input('enter the radius: '))
length = int(input('enter a length: '))

area_calc = area(radius)
#vol(area_calc,length) #or
vol(area(radius),length)
