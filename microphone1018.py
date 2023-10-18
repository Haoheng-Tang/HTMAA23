import machine
import utime
from machine import Pin

# Define LED pins
led_pins = [machine.Pin(pin, machine.Pin.OUT) for pin in [28, 29, 6, 7, 0]]
# Define Microphone pins
digital_pin = machine.Pin(26, machine.Pin.IN)   # D0 is GPIO 26
analog_pin = machine.ADC(27)  # D1 is GPIO 27


# Function to turn on an LED
def turn_on_led(led):
    led.value(1)

# Function to turn off an LED
def turn_off_led(led):
    led.value(0)

# Function to read analog signal
def read_analog():
    return analog_pin.read_u16()

# Function to read digital signal
def read_digital():
    return digital_pin.value()

# Main loop
while True:

    digital_value = read_digital()
    analog_value = read_analog()
    print("Digital Value:", digital_value)
    print("Analog Value:", analog_value)
    
    for led in led_pins:
        if analog_value>3000:
            turn_on_led(led)
        else:
            turn_off_led(led)
        
    utime.sleep_ms(100)  # Adjust delay as needed

