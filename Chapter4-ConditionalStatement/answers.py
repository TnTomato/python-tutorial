# -*- coding: utf-8 -*-
from datetime import datetime

now = datetime.now().strftime('%H:%M:%S')  # fmt: 00:00:00

if now <= '08:00:00':
    print('sleep')
elif now < '18:00:00':
    print('work')
else:
    print('off work')
