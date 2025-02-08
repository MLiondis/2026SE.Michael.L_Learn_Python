def main():
    time = input("What is the time? ")
    ftime = convert(time)

    if 7.0 <= ftime <= 8.0:
        print("Breakfast time!")
    elif 12.0 <= ftime <= 13.0:
        print("Lunch time!")
    elif 18.0 <= ftime <= 19.0:
        print("Dinner time!")
    else:
        print("eat later")

def convert(time):
    h, m = (time.split(":"))
    h = int(h)
    m = int(m)
    return h + (m / 60)

if __name__ == "__main__":
    main()