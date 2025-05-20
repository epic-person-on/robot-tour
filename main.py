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
  pass

def backward(distance, time):
  pass

def left(distance, time):
  pass

def right(distance, time):
  pass

def turn(degrees):
  pass

if __name__ == "__main__":
  print("Hello from the robot")



