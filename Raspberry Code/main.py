from sonic import UltraSonic
from logger import Logger
from network import Connection
import time

SONIC = UltraSonic()
LOGGER = Logger()
CONECTION = Connection()

def main(working_time):
    while working_time > 0:
        command, dist = 'measure', SONIC.middle_value()
        LOGGER.write(command, dist)
        #logger.write(CONECTION.send_data(dist))
        time.sleep(10)
        working_time -= 10


if __name__ == '__main__':
    main(40)
