from calculator import Calculator
from errors import IncorrectTimeFormatError, MaximumEntriesError, MinimumEntriesError

# Test that the average can be calculated for a time prior to 8 am the following day
c = Calculator()
c.add_time('06:00 AM, DAY 2')
assert c.average_minutes() == 1320

# Test that the average is rounded up to the nearest whole number when calculated
c = Calculator()
c.add_time('12:00 PM, DAY 1')
c.add_time('12:01 PM, DAY 1')
assert c.average_minutes() == 241

# Test that the average is rounded down to the nearest whole number when calculated
c = Calculator()
c.add_time('12:00 PM, DAY 1')
c.add_time('12:00 PM, DAY 1')
c.add_time('12:01 PM, DAY 1')
assert c.average_minutes() == 240

# Test that the calculator knows how to handle midnight
c = Calculator()
c.add_time('12:00 AM, DAY 2')
assert c.average_minutes() == 960

# Test that the calculator can handle calculating for multiple weeks
c = Calculator()
c.add_time('02:00 PM, DAY 19')
c.add_time('02:00 PM, DAY 20')
c.add_time('01:58 PM, DAY 20')
assert c.average_minutes() == 27239

# Test that at least 1 time is needed to calculate and average
c = Calculator()
try:
    c.average_minutes()
    assert False
except MinimumEntriesError as e:
    assert str(e) == 'At least 1 time is needed to calculate the average.'

# Test that no more than 50 times can be calculated at once
c = Calculator()
try:
    for i in range(51):
        c.add_time('12:00 PM, DAY 1')
    assert False
except MaximumEntriesError as e:
    assert str(e) == 'Only 50 times can be calculated at once.'

# Test that the calculator knows what an acceptable time format is
c = Calculator()
for time in ['02:00 PM, DAY 199', '2:00 PM, DAY 19', '02:0 PM, DAY 19', '02:0 A, DAY 19']:
    try:
        c.add_time(time)
        assert False
    except IncorrectTimeFormatError as e:
        assert str(e) == f"\"{time}\" does not match the \"hh:mm xM, DAY n\" format."


print('All tests passed!')
