import random

def get_score():
    return float(input("Enter score: "))

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def display_result(score, result):
    print(f"Score: {score}, Result: {result}")

def main():
    user_score = get_score()
    result_for_user = determine_result(user_score)
    display_result(user_score, result_for_user)

    print("-" * 20)

    random_score = random.randint(0, 100)
    result_for_random = determine_result(random_score)
    display_result(random_score, result_for_random)

main()
"This is for the Github"