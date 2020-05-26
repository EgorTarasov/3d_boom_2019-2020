import RPi.GPIO as GPIO
import time
 

class UltraSonic:
    def __init__(self):
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
         
        #set GPIO Pins
        self.GPIO_TRIGGER = 18
        self.GPIO_ECHO = 24
         
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
    
    def get_mesurement(self):
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
        
        while GPIO.input(self.GPIO_ECHO) == 0:
            start_time = time.time()
            
        while GPIO.input(self.GPIO_ECHO) == 1:
            stop_time = time.time()
        
        elapsed_time = stop_time - start_time 
        distance = (elapsed_time*34300) / 2
        distance = round(distance, 2)
        
        return distance
    
    def middle_value(self):
        values = list()
        for value in range(5):
            values.append(self.get_mesurement())
            time.sleep(0.5)
        values.sort()
        return values[2]
    
    def __del__(self):
        GPIO.cleanup()
            
        

#if __name__ == '__main__':
#    sonic = UltraSonic()
#    
#    try:
#        while True:
#            dist = sonic.middle_value()
#            #print(*dist)
#            #input()
#            print ("Measured Distance = %.1f cm" % dist)
#            time.sleep(1)
# 
#        # Reset by pressing CTRL + C
#    except KeyboardInterrupt:
#        print("Measurement stopped by User")
#        GPIO.cleanup()