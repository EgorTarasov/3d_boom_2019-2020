'''
Module to work with HC-sr04
'''
import time

import RPi.GPIO as GPIO


class UltraSonic:
    '''
    class to work with hc-sr04s
    '''
    def __init__(self):
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        # set GPIO Pins
        self.gpio_trigger = 18
        self.gpio_echo = 24

        # set GPIO direction (IN / OUT)
        GPIO.setup(self.gpio_trigger, GPIO.OUT)
        GPIO.setup(self.gpio_echo, GPIO.IN)

    def get_mesurement(self):
        '''
        gets measurement from hc-sr04
        :return: distance
        '''
        GPIO.output(self.gpio_trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.gpio_trigger, False)

        while GPIO.input(self.gpio_echo) == 0:
            start_time = time.time()

        while GPIO.input(self.gpio_echo) == 1:
            stop_time = time.time()

        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2
        distance = round(distance, 2)

        return distance

    def middle_value(self):
        '''
        Sorting values from hc-sr04
        by taking 5 measurements
        and gives middle one
        :return: correct value
        '''
        values = list()
        number = 0
        while number < 5:
            values.append(self.get_mesurement())
            time.sleep(0.5)
            number += 1
        values.sort()
        return values[2]

    def __del__(self):
        GPIO.cleanup()
