if __name__ == "__main__":
    hours = input("Enter hour: ")
    minutes = input("Enter minutes: ")
    seconds = input("Enter seconds: ")

    hours = int(hours) * 30
    minutes = int(minutes) / 2
    seconds = int(seconds) / 120

    degrees = hours + minutes + seconds

    if degrees > 360:
        degrees = degrees - 360

    print("Clockwise angle: %.2f" % (degrees))