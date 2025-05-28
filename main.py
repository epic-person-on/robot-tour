# Default libraries
import sys
import machine

# Libraries located in ./lib
sys.path.append('./lib')
import imu
import motordriver
from button import Button




# Setup Motor Driver
m = motordriver.MotorDriver()

# Setup i2c interface
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))

# Setup MPU6050
mpu = imu.MPU6050(i2c)

# Wake up mpu
mpu.wake()

# Movement functions
def forward(distance, time):
    if distance <= 0 or time <= 0:
        print("Distance and time must be greater than zero.")
        return
   
    # Tune the factor
    factor = 10.0
  
    speed = min(100, max(0, int((distance / time) * factor)))  

    # Convert time (seconds) to the unit used by MotorRun (assumed tenths of a second)
    motor_time = int(time * 10)

    print(f"Moving forward: distance={distance}, time={time}, speed={speed}%, duration={motor_time}")
    m.MotorRun('MD', 'forward', speed, motor_time)
    m.MotorRun('MB', 'forward', speed, motor_time)

def backward(distance, time):
    if distance <= 0 or time <= 0:
        print("Distance and time must be greater than zero.")
        return
   
    # Tune the factor
    factor = 10.0
  
    speed = min(100, max(0, int((distance / time) * factor)))  

    # Convert time (seconds) to the unit used by MotorRun (assumed tenths of a second)
    motor_time = int(time * 10)

    print(f"Moving forward: distance={distance}, time={time}, speed={speed}%, duration={motor_time}")
    m.MotorRun('MD', 'backward', speed, motor_time)
    m.MotorRun('MB', 'backward', speed, motor_time)  

def left(distance, time):
    if distance <= 0 or time <= 0:
        print("Distance and time must be greater than zero.")
        return
   
    # Tune the factor
    factor = 10.0
  
    speed = min(100, max(0, int((distance / time) * factor)))  

    # Convert time (seconds) to the unit used by MotorRun (assumed tenths of a second)
    motor_time = int(time * 10)

    print(f"Moving forward: distance={distance}, time={time}, speed={speed}%, duration={motor_time}")
    m.MotorRun('MA', 'forward', speed, motor_time)
    m.MotorRun('MC', 'forward', speed, motor_time)

def right(distance, time):
    if distance <= 0 or time <= 0:
        print("Distance and time must be greater than zero.")
        return
   
    # Tune the factor
    factor = 10.0
  
    speed = min(100, max(0, int((distance / time) * factor)))  

    # Convert time (seconds) to the unit used by MotorRun (assumed tenths of a second)
    motor_time = int(time * 10)

    print(f"Moving forward: distance={distance}, time={time}, speed={speed}%, duration={motor_time}")
    m.MotorRun('MA', 'backward', speed, motor_time)
    m.MotorRun('MC', 'backward', speed, motor_time)


def turn(degrees):
  pass

"""
MAIN FUNCTION:

MODIFY THIS IN COMPETITION
"""

def main():
    pass
"""
Availible actions

forward(distance,time)
backward(distance,time)
left(distance,time)
right(distance,time)

turn(degrees)

"""
  

def start(button, event):
    if event == Button.RELEASED:
        main()

button = Button(17, False, start)

if __name__ == "__main__":
  while(True):
    button.update()



