from calculator import Calculator
from errors import IncorrectTimeFormatError, MaximumEntriesError, MinimumEntriesError


if __name__ == '__main__':
    print(
        """
        Please enter your times, one at a time. At least 1 time is required to make a calculation, and you are limited
        to 50. Times are expected to be in the format "hh:mm xM, DAY n" where where hh is exactly 2 digits giving the
        hour, mm is exactly 2 digits giving the minute, x is either 'A' or 'P', and n is a positive integer less than
        100 with no leading zeros. If this format is not followed, your entry will be omitted. Enter "done" to signify
        that you have no more times to enter, and to execute the average calculation. 
        """
    )

    calculator = Calculator()
    while True:
        user_input = input()
        if user_input == 'done':
            break
        try:
            calculator.add_time(user_input)
        except (IncorrectTimeFormatError, MaximumEntriesError) as e:
            print(e)

    try:
        average = calculator.average_minutes()
        print(f"The average time is {average} minutes.")
    except MinimumEntriesError as e:
        print(e)
