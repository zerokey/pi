import RPi.GPIO as GPIO
import time
import morse

data_in = raw_input("What would you like to transmit? ")

red = 18
green = 17
blue = 27
led_time = 1
RUNNING = True

# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for led in red, green, blue:
    GPIO.setup(led, GPIO.OUT)


def led_out(color, sleep_time):
    GPIO.output(color,GPIO.LOW)
    time.sleep(sleep_time)
    GPIO.output(color,GPIO.HIGH)
    time.sleep(sleep_time)
		
words = morse.string_to_morse(data_in)

def lights():
	for signal in range(0, len(words)):
		if '-' in words[signal]: 
			led_out(red, .25)
		
		if '.' in words[signal]: 
			led_out(green, .125)
		
		if ' ' in words[signal]: 
			led_out(blue, .5)

try:
	for i in range(1,10):
		lights()

except KeyboardInterrupt:
    RUNNING = False
    print "Quitting\n"
finally:
	GPIO.cleanup()
