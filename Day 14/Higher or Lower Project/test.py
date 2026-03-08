import pytest
from main import generate_a_comparison_candidate, generate_a_random_num_in_range, format_dict_into_string
from unittest.mock import patch
import random
from game_data import data


# Arrange
@pytest.fixture
def mock_random():
    """Fixture that provides a mocked random.randint"""
    with patch('random.randint') as mock:
        yield mock

def test_random_num_is_int():
    """Property-based test: roll_dice always returns a value between 1 and 6.

    This test doesn't use mocking - it tests the actual random behavior.
    By running many iterations, we verify the function always produces
    valid output regardless of the random values generated.
    """
    # Arrange
    num_trials = 1000
    results = [(generate_a_random_num_in_range()) for _ in range(num_trials)]
    # Check all the results are integers
    assert all((isinstance(result, int)) for result in results)
    # Check all results are in the correct range, from 0 to list_length - 1
    # assert all(0 >= result <= list_length_ranged for result in results)

def test_random_int_in_correct_range():
    # Arrange
    list_length_ranged = len(data) - 1
    num_trials = 1000
    results = [(generate_a_random_num_in_range()) for _ in range(num_trials)]
    # Assert
    assert all(0 <= result <= list_length_ranged for result in results)

def test_dict_formatting_to_str():
    # Arrange
    profile = {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    }
    # Act
    result = "Maluma, Musician from Colombia"
    # Assert
    assert format_dict_into_string(profile) == result
    ...



# def test_generating_a_single_random_dict_from_list(mock_random):
#     mock_random.return_value = 0
#     # Act
#     result = generate_a_comparison_candidate()
#     # Assert
#     assert result == {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     }
#     pass

def test_returning_a_dict_from_a_list():
    # Arrange
    index_num = 1
    # Act
    result = generate_a_comparison_candidate(index_num)
    # Assert
    assert result == {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    }


