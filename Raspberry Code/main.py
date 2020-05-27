'''
The main entrance of the program
'''
import time

from logger import Logger
from network import Connection
from sonic import UltraSonic

SONIC = UltraSonic()
LOGGER = Logger()
CONNECTION = Connection()


def main(working_time):
    '''
    main function to SmartBin to work
    :param working_time:
    :return: status
    '''
    while working_time > 0:
        command, dist = 'measure', SONIC.middle_value()
        LOGGER.write(command, dist)
        # logger.write(CONNECTION.send_data(dist))
        time.sleep(10)
        working_time -= 10


if __name__ == '__main__':
    main(40)
