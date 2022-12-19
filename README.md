# Sailboat
___

All that is need to run this application is Python and access to the terminal. This project was written using Python
3.8.2, I recommend the same is used to run it.

Python installation via Homebrew on Mac:

`brew install python@3.8`

Usage:

- From the root directory of the project, run `python3 main.py`.
- Follow the prompts in the terminal

Testing:

- From the root directory of the project, run `python3 calculator_test.py`.  This will run the tests for the Calculator
class.  You should see `'All tests passed!'` in the console on success.

Note:  The requirements say that the program should have a method named `average_minutes` which takes in a list of
strings, `times: List[str]`.  I originally had this method as described, taking in a `times` argument.  However, once I
started writing tests, I realized I could move a lot of validation logic to the `Calculator` class where it was more
easily testable, and in my opinion, where it should belong.  This was all made possible by allowing the
`average_minutes` method to read from the instance variable `self.times` directly.  I hope this was ok for me to do.