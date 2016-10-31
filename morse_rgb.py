import RPi.GPIO as GPIO
import time
# stupid morse library because other stupid morse libraries were stupid/
# or maybe I was just stupid.  Either way, beep.

morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    ':': '---...',
    '?': '..--..',
    '\'': '.----.',
    '-': '-....-',
    '/': '-..-.',
    '\"': '.-..-.',
    '@': '.--.-.',
    '=': '-...-',
    ' ': ' '
}


red = 18
green = 17
blue = 27
led_time = 1

# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for led in red, green, blue:
    GPIO.setup(led, GPIO.OUT)


# blinky function
def led_out(color, sleep_time):
    GPIO.output(color, GPIO.LOW)
    time.sleep(sleep_time)
    GPIO.output(color, GPIO.HIGH)
    time.sleep(sleep_time)


# dits and dahs
def string_to_morse(words):
    out = []
    words = words.upper()
    for i in words:
        for j in morse[i]:
            out.append(j)
    return out


# blinky blinky
def lights():
    for signal in range(0, len(words)):
        if '-' in words[signal]:
            led_out(red, .25)
            print "dah"
        if '.' in words[signal]:
            led_out(green, .125)
            print "dit"
        if ' ' in words[signal]:
            led_out(blue, .5)
            print "---"

# prep for cleanly killing
RUNNING = True

try:
    data_in = raw_input("What would you like to transmit? ")
    words = string_to_morse(data_in)

except KeyboardInterrupt:
    RUNNING = False
    print "Quitting\n"

finally:
    GPIO.cleanup()
