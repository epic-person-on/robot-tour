# Default libraries
import sys
import machine

# Libraries located in ./lib
sys.path.append('./lib')
import imu
import motordriver

# Setup Motor Driver
m = motordriver.MotorDriver()

# Setup i2c interface
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))

# Setup MPU6050
mpu = imu.MPU6050(i2c)

# Wake up mpu
mpu.wake()

def forward(distance, time):
  distanceMultiplier = 1.0
  timeMultiplier = 1.0
  

def backward(distance, time):
  distanceMultiplier = 1.0
  timeMultiplier = 1.0
  

def left(distance, time):
  distanceMultiplier = 1.0
  timeMultiplier = 1.0

def right(distance, time):
  distanceMultiplier = 1.0
  timeMultiplier = 1.0

def turn(degrees):
  pass

if __name__ == "__main__":
  print("Hello from the robot")



