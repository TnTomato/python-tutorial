# -*- coding: utf-8 -*-
from typing import Tuple

debt = 125000


def calculate(delay: int) -> Tuple[float, bool]:
    if delay <= 30:
        interest = debt * 0.0001 * delay
        cancel = False
    elif delay <= 60:
        interest = debt * 0.0002 * delay
        cancel = False
    elif delay <= 90:
        interest = debt * 0.0003 * delay
        cancel = False
    else:
        interest = debt * 0.0003 * 90
        cancel = True
    repay = interest + debt
    return repay, cancel


if __name__ == '__main__':
    print(calculate(28))
    print(calculate(42))
    print(calculate(79))
    print(calculate(120))
