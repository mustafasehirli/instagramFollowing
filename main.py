import art
import random
import game_data


print(art.logo)


def random_number():
    """random number return"""
    return random.choice(game_data.data)


def compare_two_values(v1, v2):
    if v1["follower_count"] > v2["follower_count"]:
        follower = 'A'
    else:
        follower = 'B'
    return follower


current_score = 0
start = True
while start:
    value1 = random_number()
    value2 = random_number()
    big = compare_two_values(value1, value2)
    while start:
        value1 = value2
        value2 = random_number()

        print(f"Current Score : {current_score}")
        print(f"Compare A : {value1['name']},{value1['description']},{value1['country']}")
        print(art.vs)
        print(f"Against B : {value2['name']},{value2['description']},{value2['country']}")
        result = input("Who has more followers? Type 'A' or 'B' : ")

        if big == result:
            current_score += 1
            b_variable = value2
            continue
        else:
            print(f"Game Over {current_score}")
            start = False

