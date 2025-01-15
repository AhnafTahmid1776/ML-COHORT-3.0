x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

if x > y and x > z:  # Logical AND ensures both conditions are true.
    print("x is the largest")
elif y > x and y > z:
    print("y is the largest")
else:
    print("z is the largest")