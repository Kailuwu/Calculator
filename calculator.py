def add(a, b):
    return a + b;

def subtract(a, b):
    pass

def multiply(a, b):
    return a * b

def divide(a, b):
    pass

def main():
    print("Simple CLI Calculator")
    print("1. Add  2. Subtract  3. Multiply  4. Divide")
    choice = input("Select operation (1-4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
>>>>>>> 731e946231627d72d0d46e3245629e1d1f15963f
