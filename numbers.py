if __name__ == "__main__":
    first_number = input('Enter first number: ')
    second_number = input('Enter second number: ')
    third_number = input('Enter third number: ')
    fourth_number = input('Enter fourth number: ')
    
    first_sum = int(first_number) + int(second_number)
    second_sum = int(third_number) + int(fourth_number)

    print("\nResult of division: %.2f" % (first_sum / second_sum))