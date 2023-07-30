def qwer(n):
    draw = [
        "    _~_   ",
        "   (o o)  ",
        "  /  V  \ ",
        " /(  _  )\\",
        "   ^^ ^^  "
    ]

    for _ in range(n):
        for line in draw:
            print(line, end="  ")
        print()

if __name__ == "__main__":
    n = int(input("Type the quantity of penguins (from 1 to 9): "))
    if 1 <= n <= 9:
        qwer(n)
    else:
        print("Incorrect number! Type the right one in range from 1 to 9.")