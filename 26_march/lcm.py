# You are given two numbers find their lcm  using formula

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return (a * b) // gcd

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = find_lcm(num1, num2)
print(f"LCM of {num1} and {num2} is: {lcm}")
