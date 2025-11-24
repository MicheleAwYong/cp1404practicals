"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
class Car:
    """Mock Car class for demonstration purposes."""
    def __init__(self, fuel=0):
        self._odometer = 0
        if fuel > 0:
            self._fuel = fuel
        else:
            self._fuel = 0

# Original function (fixed in TODO 1)
def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    # TODO 1: fix the repeat_string function so that it passes the failing test
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    # TODO 4: Fix the failing is_long_word function
    return len(word) >= length


# TODO 5: Write and test a function to format a phrase as a sentence
def format_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('a quick brown fox')
    'A quick brown fox.'
    """
    sentence = phrase.capitalize()
    if sentence.endswith('.'):
        sentence = sentence.rstrip('.') + '.'
    else:

        sentence += '.'

    return sentence


def run_tests():
    print("--- Running Assert Tests ---")
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # TODO 2: write assert statements to show if Car sets the fuel correctly
    default_car = Car()
    assert default_car._fuel == 0, "Car does not set default fuel (0) correctly"
    fuel_car = Car(fuel=10)
    assert fuel_car._fuel == 10, "Car does not set specified fuel (10) correctly"

    print("All assert tests passed successfully!")
    print("------------------------------------")

run_tests()

print("--- Running Doctests ---")
doctest.testmod(verbose=True)
print("------------------------")