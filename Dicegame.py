import random
def main():
    print("What is your name?")
    name = input()
    print("Hello, {}!".format(name))
    print("Rolling dice...")
    total = 0
    for i in range(1,3):
        d = random.randint(1,6)
        print("Die {}: {}".format(i, d))
        total += d
    print("Total value: {}".format(total))
    if total >= 7:
        print("{} won!".format(name))
    else :
        print("{} lost!".format(name))

main()
