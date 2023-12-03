"""The purpose of this project is to create a shopping budget tool that tracks how much a user has spent and tells them
how much they have left to spend"""

# TODO 1: Opening greeting where the user is asked whether it is a weekly, monthly or yearly budget
print("Welcome to this shopping budget tool! I'm so happy that you've come here for your budgeting needs!")
while True:
    while True:
        choice = input("Would you like to discuss weekly, monthly or yearly budget? Please enter the words, 'week', "
                       "'month' or 'year'\n")
        if choice.lower() not in ['week', 'month', 'year']:
            print("You have made an invalid choice. Please try again.")
        else:
            break

    # TODO 2: Ask what the budget is
    print(f"Great! Ok, the next thing for us to do is set a budget for the {choice}")
    while True:
        try:
            budget = float(input(f"What's your budget for the {choice}? £"))
            break
        except Exception:
            print("You have entered an invalid amount. Try again.")

    # TODO 3: Ask how much they've spent
    print(f"Now let's see if you're on track to stay within your budget of £{budget:.2f} for the {choice}.")
    total_spend = 0
    while True:
        try:
            spend = float(input(f"Please enter an expense for this {choice}: £"))
            total_spend += spend
            new_value = input(f"Do you have another expense for this {choice}? Please enter 'y' or 'n' : ")
            if new_value not in ['y', 'n']:
                print("You have entered an invalid choice. Please try again.")
            elif new_value == 'n':
                break
        except Exception:
            print("You have entered an invalid amount. Try again.")

    # TODO 4: Determine how much is left in their budget
    money_left = budget - total_spend
    if money_left > 0:
        print(f"You have £{money_left:.2f} left for the {choice}")
    elif money_left == 0:
        print(f"You have no more money left in your {choice}ly budget.")
    else:
        print(f"You have exceeded your {choice}ly budget")

    # TODO 5: Loop so that users are able to do it again or leave

    while True:
        stay = input("Would you like to do another budget? Please enter 'y' or 'n': ")
        if stay.lower() not in ['y', 'n']:
            print("You have made an invalid choice. Please try again.")
        else:
            break
    if stay.lower() == 'n':
        print("Thank you for using this shopping budget tool. Have a nice day!")
        break
