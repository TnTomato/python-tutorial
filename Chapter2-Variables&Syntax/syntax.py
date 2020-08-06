import time


def pause(sec: int):
    time.sleep(sec)


if __name__ == '__main__':
    print('start')
    pause(5)
    print('end')
