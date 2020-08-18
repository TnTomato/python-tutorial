# -*- coding: utf-8 -*-
"""
    Let's do some time comparison. If now time is earlier than 8 AM, print
    'sleep'. If now time is during 8 AM and 6 PM, print 'work', If now time
    is later than 6 PM, print 'off work'. Do after the following codes.
"""
from datetime import datetime

now = datetime.now().strftime('%H:%M:%S')  # fmt: 00:00:00

# Just compare the string format of time like
# '2020-08-08 08:00:00' < '2020-08-08 09:00:00'
# for example:
#     if now == '12:00:00':
#         print('eat')
