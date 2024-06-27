import random


def main():
    level = get_level()
    score = 10
    for i in range(10):
        x, y = generate_integer(level)
        while True:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == (x + y):
                    break
                else:
                    print("EEE")
                    score -= 1
            except ValueError:
                pass
    print(f"Score: {score}")        


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
