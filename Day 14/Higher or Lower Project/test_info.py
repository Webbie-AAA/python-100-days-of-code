import random
import pytest
from unittest.mock import patch, MagicMock


# ============================================================================
# DICE ROLL FUNCTION TO TEST
# ============================================================================

def roll_dice() -> int:
    """Roll a single six-sided die and return the result.

    Returns:
        int: A random number between 1 and 6 (inclusive)
    """
    return random.randint(1, 6)


# ============================================================================
# TEST 1: Verify the function calls random.randint with correct arguments
# ============================================================================
# Use this approach when you want to verify that your function calls
# a dependency with the correct parameters, without caring about the return value.

def test_roll_dice_calls_randint_with_correct_args():
    """Test that roll_dice calls random.randint with arguments (1, 6)."""
    with patch('random.randint') as mock_randint:
        # Set a return value so the function works
        mock_randint.return_value = 4

        # return_value = 4 - This makes the mock pretend to be
        # random.randint() and return 4. So when your roll_dice()
        # function calls random.randint(1, 6), instead of getting
        # a random number, it gets 4.
        # This let you test: "Does my function correctly return
        # whatever random.randint() gives it?"

        # Call the function
        roll_dice()

        # assert_called_once_with(1, 6) - checks you called
        # the dependency correctly assert result == mocked_value
        # - checks your function returns what it should

        # Verify random.randint was called exactly once with args (1, 6)
        mock_randint.assert_called_once_with(1, 6)


# ============================================================================
# TEST 2: Control what random.randint returns and verify function output
# ============================================================================
# Use this approach when you want to test your function's behavior with
# specific, predictable inputs. This makes tests deterministic and reliable.

def test_roll_dice_returns_mocked_value():
    """Test that roll_dice returns the value from random.randint."""
    with patch('random.randint') as mock_randint:
        # Control what random.randint returns
        mock_randint.return_value = 3

        # Call the function and verify it returns the mocked value
        result = roll_dice()
        assert result == 3

        # Test with a different value
        mock_randint.return_value = 6
        result = roll_dice()
        assert result == 6


# ============================================================================
# TEST 3: Test multiple scenarios with parametrize
# ============================================================================
# Use parametrize to test multiple mocked return values efficiently

@pytest.mark.parametrize("mocked_value", [1, 2, 3, 4, 5, 6])
#This allows running the same test multiple times with different values
def test_roll_dice_with_all_possible_values(mocked_value):
    """Test that roll_dice correctly returns each possible dice value."""
    with patch('random.randint', return_value=mocked_value):
        result = roll_dice()
        assert result == mocked_value


# ============================================================================
# TEST 4: Property-based test - verify output is always in valid range
# ============================================================================
# Use this approach to test the actual behavior of the function without mocking.
# This verifies that the function works correctly in real-world conditions.
# Run it many times to gain confidence in the implementation.

def test_roll_dice_always_returns_valid_range():
    """Property-based test: roll_dice always returns a value between 1 and 6.

    This test doesn't use mocking - it tests the actual random behavior.
    By running many iterations, we verify the function always produces
    valid output regardless of the random values generated.
    """
    # Run the function many times
    # Property based testing instead of controlling the randomness
    # with mocks, it runs the real random function 1000 times
    # and checks that certain properties always hold true.
    num_trials = 1000
    results = [roll_dice() for _ in range(num_trials)]

    # Property 1: All results should be integers
    assert all(isinstance(result, int) for result in results)

    # Property 2: All results should be in the valid range [1, 6]
    assert all(1 <= result <= 6 for result in results)

    # Property 3: Over many trials, we should see all possible values
    # (This could theoretically fail due to randomness, but probability is very low)
    unique_values = set(results)
    assert len(unique_values) >= 4, f"Expected at least 4 different values in {num_trials} rolls"


# ============================================================================
# TEST 5: Statistical property test (optional advanced test)
# ============================================================================
# Verify that the distribution is roughly uniform over many trials

def test_roll_dice_distribution_is_roughly_uniform():
    """Test that dice rolls are roughly uniformly distributed.

    This is a statistical test that verifies the randomness quality.
    Each value (1-6) should appear approximately 1/6 of the time.
    """
    num_trials = 6000
    results = [roll_dice() for _ in range(num_trials)]

    # Count occurrences of each value
    from collections import Counter
    counts = Counter(results)

    # Each value should appear roughly num_trials/6 times
    expected_count = num_trials / 6
    tolerance = 0.15  # Allow 15% deviation

    for value in range(1, 7):
        count = counts[value]
        # Check that count is within tolerance of expected
        assert abs(count - expected_count) / expected_count < tolerance, \
            f"Value {value} appeared {count} times, expected ~{expected_count}"


# ============================================================================
# BONUS: Testing with pytest fixtures for cleaner code
# ============================================================================

# A fixture is a reusable setup that pytest can inject into tests.
# Instead of writing patch('random.randint') in every test, you
# write it once in the fixture and pytest handles it.

# Fixtures are defined once and then passed as arguments to test functions.

@pytest.fixture
def mock_random():
    """Fixture that provides a mocked random.randint."""
    with patch('random.randint') as mock:
        yield mock


def test_roll_dice_using_fixture(mock_random):
    """Example of using a fixture to reduce boilerplate code."""
    mock_random.return_value = 5
    result = roll_dice()
    assert result == 5
    mock_random.assert_called_once_with(1, 6)

# ============================================================================
# SUMMARY OF TESTING APPROACHES
# ============================================================================
#
# 1. MOCK TO VERIFY CALLS: Use when you need to ensure your function
#    calls dependencies with correct arguments.
#    Example: test_roll_dice_calls_randint_with_correct_args()
#
# 2. MOCK TO CONTROL BEHAVIOR: Use when you need deterministic tests
#    that don't depend on randomness or external factors.
#    Example: test_roll_dice_returns_mocked_value()
#
# 3. PARAMETRIZED TESTS: Use to test multiple scenarios efficiently
#    without duplicating test code.
#    Example: test_roll_dice_with_all_possible_values()
#
# 4. PROPERTY-BASED TESTS: Use to verify invariants that should always
#    hold true, regardless of random inputs.
#    Example: test_roll_dice_always_returns_valid_range()
#
# 5. STATISTICAL TESTS: Use to verify probabilistic properties over
#    many trials (use with caution - can be flaky).
#    Example: test_roll_dice_distribution_is_roughly_uniform()
#
# ============================================================================

# Pytest tests are for developers to verify that code works correctly.

