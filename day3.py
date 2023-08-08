# LCM and HCF of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf= lambda a, b:a if b == 0 else hcf(b, a % b)
lcm = lambda a, b: (a * b) // hcf(a, b)
print(f"The lcm is {lcm(a,b)}.")
print(f"The hcf is {hcf(a,b)}.")
