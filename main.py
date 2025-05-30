# Default libraries
import sys
import machine

# Logging helper function
def log(msg):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

# Libraries located in ./lib
sys.path.append('./lib')
try:
    import imu
    import motordriver
    from button import Button
except Exception as e:
    log(f"Import Error: {str(e)}")
    sys.exit()

# Indicator light
led = machine.Pin("LED", machine.Pin.OUT)
led.on()

# Setup Motor Driver
m = motordriver.MotorDriver()
log("MotorDriver initiated")

# Setup i2c interface
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))

# Setup MPU6050
mpu = imu.MPU6050(i2c)

# Wake up mpu
mpu.wake()

log("mpu initiated")

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

    print(
        f"Moving forward: distance={distance}, time={time}, speed={speed}%, duration={motor_time}"
    )
    m.MotorRun('MD', 'forward', speed, motor_time)
    m.MotorRun('MB', 'forward', speed, motor_time)

def backward(distance, time):
    if distance <= 0 or time <= 0:
        print("Distance and time must be greater than zero.")
        return

    factor = 10.0
    speed = min(100, max(0, int((distance / time) * factor)))
    motor_time = int(time * 10)

    print(
        f"Moving backward: distance={distance}, time={time}, speed={speed}%, duration={motor_time}"
    )
    m.MotorRun('MD', 'backward', speed, motor_time)
    m.MotorRun('MB', 'backward', speed, motor_time)

def left(distance, time):
    if distance <= 0 or time <= 0:
        print("Distance and time must be greater than zero.")
        return

    factor = 10.0
    speed = min(100, max(0, int((distance / time) * factor)))
    motor_time = int(time * 10)

    print(
        f"Turning left: distance={distance}, time={time}, speed={speed}%, duration={motor_time}"
    )
    m.MotorRun('MA', 'forward', speed, motor_time)
    m.MotorRun('MC', 'forward', speed, motor_time)

def right(distance, time):
    if distance <= 0 or time <= 0:
        print("Distance and time must be greater than zero.")
        return

    factor = 10.0
    speed = min(100, max(0, int((distance / time) * factor)))
    motor_time = int(time * 10)

    print(
        f"Turning right: distance={distance}, time={time}, speed={speed}%, duration={motor_time}"
    )
    m.MotorRun('MA', 'backward', speed, motor_time)
    m.MotorRun('MC', 'backward', speed, motor_time)

def turn(degrees):
    m.MotorRun('MA', 'forward', 100, 20)
    m.MotorRun('MB', 'forward', 100, 20)
    m.MotorRun('MC', 'backward', 100, 20)
    m.MotorRun('MD', 'backward', 100, 20)

def main():
    pass
    '''
    MAIN FUNCTION:
    MODIFY THIS IN COMPETITION
    Available actions:
    forward(distance,time)
    backward(distance,time)
    left(distance,time)
    right(distance,time)
    turn(degrees)
    '''

def start(button, event):
    if event == Button.RELEASED:
        try:
            main()
        except Exception as e:  # Use Exception for compatibility with MicroPython
            log(f"Runtime Error: {str(e)}")
            sys.exit()

button = Button(17, False, start)

if __name__ == "__main__":
    while True:
        button.update()
