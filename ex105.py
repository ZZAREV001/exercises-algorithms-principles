# Determine if numbers (actually, we are building a finite state machine)
# note the importance of data structures like enum and the 2 hashmaps that will organize the input data.
from enum import Enum


class DigitState(Enum):
    BEGIN = 0
    NEGATIVE1 = 1
    DIGIT1 = 2
    DOT = 3
    DIGIT2 = 4
    E = 5
    NEGATIVE2 = 6
    DIGIT3 = 7


STATE_VALIDATOR = {
    DigitState.BEGIN: lambda x: True,
    DigitState.DIGIT1: lambda x: x.isdigit(),
    DigitState.NEGATIVE1: lambda x: x == '-',
    DigitState.DIGIT2: lambda x: x.isdigit(),
    DigitState.DOT: lambda x: x == '.',
    DigitState.E: lambda x: x == 'e',
    DigitState.NEGATIVE2: lambda x: x == '-',
    DigitState.DIGIT3: lambda x: x.isdigit(),
}

NEXT_STATES_MAP = {
    DigitState.BEGIN: [DigitState.NEGATIVE1, DigitState.DIGIT1],
    DigitState.NEGATIVE1: [DigitState.DIGIT1, DigitState.DOT],
    DigitState.DIGIT1: [DigitState.DIGIT1, DigitState.DOT, DigitState.E],
    DigitState.DOT: [DigitState.DIGIT2],
    DigitState.DIGIT2: [DigitState.DIGIT2, DigitState.E],
    DigitState.NEGATIVE2: [DigitState.DIGIT3],
    DigitState.DIGIT3: [DigitState.DIGIT3],
}


PATHS = {
    DigitState.BEGIN: [DigitState.NEGATIVE1, DigitState.DIGIT1],
    DigitState.NEGATIVE1: [DigitState.DIGIT1, DigitState.DOT],
    DigitState.DIGIT1: [DigitState.DIGIT1, DigitState.DOT, DigitState.E],
    DigitState.DOT: [DigitState.DIGIT2],
    DigitState.NEGATIVE2: [DigitState.DIGIT3],
    DigitState.DIGIT3: [DigitState.DIGIT3]
}


class Solution:
    @staticmethod
    def parseNumber(str):
        state = DigitState.BEGIN

        for c in str:
            found = False
            for next_state in NEXT_STATES_MAP[state]:
                if STATE_VALIDATOR[next_state](c):
                    state = next_state
                    found = True
                    break
            if not found:
                return False

        return state in [DigitState.DIGIT1, DigitState.DIGIT2, DigitState.DIGIT3]


print(Solution().parseNumber("12.3"))
# expect True
print(Solution().parseNumber("12a"))
# expect False (this is not a number of any type