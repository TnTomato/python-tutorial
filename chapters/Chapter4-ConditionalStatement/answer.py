# -*- coding: utf-8 -*-
"""
    Let's do some time comparison. If now time is earlier than 8 AM, print
    'sleep'. If now time is during 8 AM and 6 PM, print 'work', If now time
    is later than 6 PM, print 'off work'. Do after the following codes.
"""
from datetime import datetime

now = datetime.now().strftime('%H:%M:%S')  # fmt: 00:00:00

if now < '08:00:00':
    print('sleep')
elif now < '18:00:00':
    print('work')
else:
    print('off work')
