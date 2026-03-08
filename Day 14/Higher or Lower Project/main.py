import random
from zipfile import error

from game_data import data
import art

print(art.logo)

def generate_a_random_num_in_range() -> int:
    length_of_list = len(data)
    index = random.randint(0, length_of_list-1)
    return index


# def generate_two_unique_ints(data: list) -> list[int]:
#     return random.sample(range(len(data)), 2)    For testability

def generate_two_unique_ints() -> list:
    two_unique_ints = []
    while len(two_unique_ints) != 2:
        a_num = generate_a_random_num_in_range()
        if a_num not in two_unique_ints:
            two_unique_ints.append(a_num)
    return two_unique_ints

def format_dict_into_string(choice: dict) -> str:
    return f"{choice['name']}, {choice['description']} from {choice['country']}"

def generate_comparison_candidate_a(two_unique_ints: list) -> str:
    option_a = two_unique_ints[0]
    item_a = data[option_a]
    # formatted_a = format_dict_into_string(item_a)
    return item_a

def generate_comparison_candidate_b(two_unique_ints: list) -> str:
    option_b = two_unique_ints[-1]
    item_b = data[option_b]
    # formatted_b = format_dict_into_string(item_b)
    return item_b

def who_has_more_followers(candidate_a: dict, candidate_b: dict) -> str:
    candidate_a_followers = candidate_a['follower_count']
    candidate_b_followers = candidate_b['follower_count']
    if candidate_a_followers > candidate_b_followers:
        return 'a'
    return 'b'
    ...



if __name__ == "__main__":
    game_play = True
    count = 0
    while game_play:
        two_unique_ints = generate_two_unique_ints()
        a = generate_comparison_candidate_a(two_unique_ints)
        a_format = format_dict_into_string(a)
        b = generate_comparison_candidate_b(two_unique_ints)
        b_format = format_dict_into_string(b)
        answer = who_has_more_followers(a, b)
        print(f"Compare A: {a_format}")
        print(art.vs)
        print(f"Compare B: {b_format}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
        if user_choice == answer:
            count += 1
            print("\n" * 20)
            print(f"You're right! Current score: {count}")
            game_play = True
        else:
            print(f"Sorry, that's wrong. Final score: {count}")
            game_play = False


    pass