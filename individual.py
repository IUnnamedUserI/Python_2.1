if __name__ == "__main__":
    age_x = input("Enter Tanya's age: ")
    age_y = input("Enter Mitya's age: ")
    average_age = (int(age_x) + int(age_y)) / 2
    difference_age_x = int(age_x) - average_age
    difference_age_y = int(age_y) - average_age
    
    print("\nAverage age: {0}".format(average_age))
    print("Difference with average age and:")
    print("Tanya's age: {0}".format(difference_age_x))
    print("Mitya's age: {0}".format(difference_age_y))