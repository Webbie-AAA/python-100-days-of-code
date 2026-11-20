import pytest
import random


# ============================================================================
# FUNCTION TO TEST: A dice rolling function with error handling
# ============================================================================

def roll_dice(num_sides):
    """
    Simulate rolling a dice with a specified number of sides.

    Args:
        num_sides: Number of sides on the dice (must be a positive integer)

    Returns:
        int: Random number between 1 and num_sides (inclusive)

    Raises:
        TypeError: If num_sides is not an integer
        ValueError: If num_sides is less than 1
    """
    # Check if input is an integer
    if not isinstance(num_sides, int):
        raise TypeError(f"num_sides must be an integer, got {type(num_sides).__name__}")

    # Check if input is positive
    if num_sides < 1:
        raise ValueError(f"num_sides must be at least 1, got {num_sides}")

    return random.randint(1, num_sides)


# ============================================================================
# TEST 1: Basic error raising with pytest.raises()
# ============================================================================

def test_roll_dice_raises_value_error_for_zero():
    """
    Test that ValueError is raised when num_sides is 0.

    pytest.raises() is a context manager that catches the expected exception.
    If the exception is NOT raised, the test fails.
    """
    with pytest.raises(ValueError):
        roll_dice(0)


def test_roll_dice_raises_value_error_for_negative():
    """
    Test that ValueError is raised when num_sides is negative.
    """
    with pytest.raises(ValueError):
        roll_dice(-5)


# ============================================================================
# TEST 2: Testing TypeError for wrong input types
# ============================================================================

def test_roll_dice_raises_type_error_for_float():
    """
    Test that TypeError is raised when num_sides is a float.
    """
    with pytest.raises(TypeError):
        roll_dice(6.5)


def test_roll_dice_raises_type_error_for_string():
    """
    Test that TypeError is raised when num_sides is a string.
    """
    with pytest.raises(TypeError):
        roll_dice("six")


# ============================================================================
# TEST 3: Testing error message content
# ============================================================================

def test_value_error_message_content():
    """
    Test that the ValueError contains the expected message.

    We can access the exception object using 'as exc_info' and then
    check its string representation or specific attributes.
    """
    with pytest.raises(ValueError) as exc_info:
        roll_dice(-3)

    # Check the exact error message
    assert str(exc_info.value) == "num_sides must be at least 1, got -3"


def test_type_error_message_contains_type_name():
    """
    Test that the TypeError message contains information about the wrong type.

    Using 'in' allows for partial matching of the error message.
    """
    with pytest.raises(TypeError) as exc_info:
        roll_dice(3.14)

    # Check that the error message contains expected text
    assert "must be an integer" in str(exc_info.value)
    assert "float" in str(exc_info.value)


# ============================================================================
# TEST 4: Testing that valid inputs do NOT raise errors
# ============================================================================

def test_roll_dice_valid_input_no_error():
    """
    Test that valid inputs execute successfully without raising errors.

    This is important to ensure we're not being too strict with validation.
    """
    # These should all work without raising exceptions
    result = roll_dice(6)
    assert 1 <= result <= 6

    result = roll_dice(20)
    assert 1 <= result <= 20

    result = roll_dice(1)  # Edge case: single-sided dice
    assert result == 1


def test_roll_dice_large_number_no_error():
    """
    Test that large valid numbers work correctly.
    """
    result = roll_dice(1000)
    assert 1 <= result <= 1000


# ============================================================================
# TEST 5: Parametrized tests for multiple invalid inputs
# ============================================================================

@pytest.mark.parametrize("invalid_sides,expected_exception", [
    (0, ValueError),  # Zero sides
    (-1, ValueError),  # Negative number
    (-100, ValueError),  # Large negative number
    (3.5, TypeError),  # Float
    ("6", TypeError),  # String
    ([6], TypeError),  # List
    ({"sides": 6}, TypeError),  # Dictionary
    (None, TypeError),  # None
])
def test_roll_dice_invalid_inputs_parametrized(invalid_sides, expected_exception):
    """
    Parametrized test to check multiple invalid inputs in one test.

    This is more efficient than writing separate tests for each case.
    The test will run once for each parameter set.
    """
    with pytest.raises(expected_exception):
        roll_dice(invalid_sides)


# ============================================================================
# TEST 6: Parametrized test with error message validation
# ============================================================================

@pytest.mark.parametrize("invalid_sides,expected_error,message_fragment", [
    (0, ValueError, "must be at least 1"),
    (-5, ValueError, "got -5"),
    (2.5, TypeError, "must be an integer"),
    ("ten", TypeError, "got str"),
])
def test_error_messages_parametrized(invalid_sides, expected_error, message_fragment):
    """
    Parametrized test that validates both the exception type and message content.
    """
    with pytest.raises(expected_error) as exc_info:
        roll_dice(invalid_sides)

    assert message_fragment in str(exc_info.value)


# ============================================================================
# TEST 7: Demonstrating what happens when expected error is NOT raised
# ============================================================================

def test_expecting_error_but_none_raised():
    """
    This test demonstrates what happens when you expect an error but it doesn't occur.

    IMPORTANT: This test is designed to FAIL to show the behavior.
    In real testing, you would NOT write a test like this.

    Uncomment the code below to see pytest.raises() fail when no exception occurs.
    """
    # Uncomment to see the failure:
    # with pytest.raises(ValueError):
    #     roll_dice(6)  # This is valid input, so no ValueError is raised
    #     # pytest will fail with: "DID NOT RAISE <class 'ValueError'>"

    # Instead, we'll show the correct way to test this:
    # If you want to ensure NO exception is raised, just call the function
    result = roll_dice(6)
    assert isinstance(result, int)


# ============================================================================
# TEST 8: Using match parameter to test error message with regex
# ============================================================================

def test_error_message_with_regex_match():
    """
    The 'match' parameter allows regex pattern matching on error messages.

    This is useful when you want to validate the error message format
    without checking the exact text.
    """
    # Match error message using regex
    with pytest.raises(ValueError, match=r"must be at least 1, got -\d+"):
        roll_dice(-42)

    # Match with simpler pattern
    with pytest.raises(TypeError, match="must be an integer"):
        roll_dice("invalid")


# ============================================================================
# TEST 9: Testing exception attributes
# ============================================================================

def test_exception_attributes():
    """
    You can access and test specific attributes of the exception object.
    """
    with pytest.raises(ValueError) as exc_info:
        roll_dice(0)

    # Access the exception object
    exception = exc_info.value

    # Test exception type
    assert isinstance(exception, ValueError)

    # Test exception args
    assert len(exception.args) > 0
    assert "must be at least 1" in exception.args[0]


# ============================================================================
# RUNNING THE TESTS
# ============================================================================

if __name__ == "__main__":
    # To run these tests, use the command:
    # pytest test_dice.py -v
    #
    # Or to run with more details:
    # pytest test_dice.py -v -s
    #
    # To run a specific test:
    # pytest test_dice.py::test_roll_dice_raises_value_error_for_zero -v

    print("Run this file with pytest to execute the tests.")
    print("Example: pytest", __file__, "-v")