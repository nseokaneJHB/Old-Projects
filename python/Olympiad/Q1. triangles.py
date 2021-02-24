side_one = int(input("First side: "))
side_two = int(input("Second side: "))
side_three = int(input("Third side: "))

all_sides = side_one + side_two + side_three
triangle = 180

if all_sides != triangle:
    print('Not equal to 180')
else:
    if side_one == side_two and side_two == side_three:
        print('Equilateral')
    elif side_one == side_two or side_one == side_three or side_two == side_three:
        print('Isosceles')
    else:
        print('Scalene')
