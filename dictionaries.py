def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f'This is {key} and this is {val} belt')


ninja_belts = {}

while True:
    ninja_name = input("Enter a ninja name: ")
    ninja_belt = input("Enter a ninja belt: ")
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another(y/n)')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)
