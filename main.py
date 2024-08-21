# Dice sum probability calculator
# Författare: Daniil
# Datum: 2024 Onsdag 21

def main():
    user_input = [int(x) for x in input("").split(" ")]
    min_dice = min(user_input)
    max_dice = max(user_input)

    # EX: min: 4, max: 6
    # Loopen körs från 5 till 7 vilket är våra mest sannolika summorna 
    for sum in range(min_dice + 1, max_dice + 2):
        print(sum)

if __name__ == "__main__":
    main()