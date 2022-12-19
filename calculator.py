import re

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from errors import IncorrectTimeFormatError, MaximumEntriesError, MinimumEntriesError
from typing import Tuple


class Calculator:
    MINUTES_IN_A_DAY = 1440
    MINUTES_IN_EIGHT_HOURS = 480
    TIME_PATTERN = r'^((0\d|1[0-2]):[0-5]\d (A|P)M, DAY ([1-9]\d?))$'

    def __init__(self):
        self.times = []

    def add_time(self, time: str) -> None:
        if len(self.times) == 50:
            raise MaximumEntriesError("Only 50 times can be calculated at once.")
        if re.match(self.TIME_PATTERN, time):
            self.times.append(time)
        else:
            raise IncorrectTimeFormatError(f"\"{time}\" does not match the \"hh:mm xM, DAY n\" format.")

    def average_minutes(self) -> int:
        number_of_times = len(self.times)
        if not number_of_times:
            raise MinimumEntriesError("At least 1 time is needed to calculate the average.")
        total = 0
        for time in self.times:
            time_string, day_string = self._parse_time_and_day(time=time)
            day = self._get_day(day=day_string)
            minutes = self._get_minutes(time=time_string)
            minutes = self._offset_start_time_minutes(minutes=minutes)
            minutes = self._add_additional_day_minutes(minutes=minutes, day=day)
            total += minutes

        return self._calculate_rounded_average(numerator=total, denominator=number_of_times)

    @classmethod
    def _calculate_rounded_average(cls, numerator: int, denominator: int) -> int:
        return int(Decimal(numerator / denominator).to_integral_value(rounding=ROUND_HALF_UP))

    @classmethod
    def _add_additional_day_minutes(cls, minutes: int, day: int) -> int:
        return minutes + (day - 1) * cls.MINUTES_IN_A_DAY

    @classmethod
    def _offset_start_time_minutes(cls, minutes: int) -> int:
        return minutes - cls.MINUTES_IN_EIGHT_HOURS

    @staticmethod
    def _get_day(day: str) -> int:
        arr = day.split(' ')
        return int(arr[1])

    @staticmethod
    def _get_minutes(time: str) -> int:
        time = datetime.strptime(time, '%I:%M %p')
        hour = time.hour
        minutes = time.minute
        return hour * 60 + minutes

    @staticmethod
    def _parse_time_and_day(time: str) -> Tuple[str, str]:
        arr = time.split(', ')
        return arr[0], arr[1]
