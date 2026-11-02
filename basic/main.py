from operations import add, divide, multiply, subtract

number_1 = 10
number_2 = 5

def main():
    print(f"{number_1} + {number_2} = {add(number_1, number_2)}")
    print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")
    print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")
    print(f"{number_1} / {number_2} = {divide(number_1, number_2)}")

if __name__ == "__main__":
    main()