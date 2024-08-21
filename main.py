# Dice sum probability calculator
# Författare: Daniil
# Datum: 2024 Onsdag 21
def main():
    user_input = input("").split(" ")
    max_dice = int(max(user_input))
    min_dice = int(min(user_input))

    for sum in range(min_dice + 1, max_dice + 2):
        print(sum)


if __name__ == "__main__":
    main()