import time


def timer():
    '''Countdown timer'''
    secs = int(input('Enter the time in seconds: '))

    while secs:
        m, s = divmod(secs, 60)
        print(f'{m:02d}:{s:02d}\n')
        time.sleep(1)
        secs -= 1
    else:
        print('Time is up!')


if __name__ == '__main__':
    timer()
