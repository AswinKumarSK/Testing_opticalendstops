import pyfirmata # Import the PyFirmata library
import serial 
import time

board = pyfirmata.Arduino('COM5', baudrate=57600) # Define the serial port for the Arduino
endstop_pin = board.get_pin('d:7:i') # Define the pins for the optical endstop
it = pyfirmata.util.Iterator(board) # Enable the iterator
it.start()
pul_pin = 2
dir_pin = 3
ena_pin = 4
delay_time = 0.01
def move_motor(direction, steps):
    if direction == 'cw':
        board.digital[dir_pin].write(0)
    else:
        board.digital[dir_pin].write(1)
    for i in range(steps):
        board.digital[pul_pin].write(1)
        time.sleep(delay_time)
        board.digital[pul_pin].write(0)
        time.sleep(delay_time)
    

while True:
    move_motor('cw', 100)
    if endstop_pin.read() == True: # Check if the endstop is triggered
        print("Endstop triggered!") # Print a message if the endstop is triggered
        move_motor('ccw', 100000)
    elif endstop_pin.read() == False:
        print("Not triggered")

board.exit()