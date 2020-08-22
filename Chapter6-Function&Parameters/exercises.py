# -*- coding: utf-8 -*-
"""
    There is a credi card. The repayment date is set to the 20th day of
    a month. Interest will be charged for late repayment. 0.01% per day with
    in 30 days, 0.02% per day with in 60 days and 0.03% per day with in 90
    days. If longer than 90 days, the credit card will be cancelled and both
    principal and interest should be paied.

    max interest is: principal * 90 * 0.03%

    Now I have 12500 need to be repaied. I want to know how much in total
    should I repay for different delay.

    Let's calculate for delay days 28, 42, 79, 120
"""
