import RPi.GPIO as gpio
import time
import numpy as np


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(31, gpio.OUT)
    gpio.setup(33, gpio.OUT)
    gpio.setup(35, gpio.OUT)
    gpio.setup(37, gpio.OUT)
    gpio.setup(7, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(12, gpio.IN, pull_up_down=gpio.PUD_UP)


def gameover():
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, False)
    gpio.output(37, False)
    gpio.cleanup()


def forward(distance):
    counterFL = np.uint64(0)
    counterBR = np.uint64(0)
    buttonFL = int(0)
    buttonBR = int(0)
    pwml = gpio.PWM(31, 50)  # Backleft motor
    pwmr = gpio.PWM(37, 50)  # Frontright motor
    val = 45
    vall = val
    valr = val
    pwml.start(vall)
    pwmr.start(valr)
    time.sleep(0.1)

    tstart = time.perf_counter()
    errorFLprev = 0
    errorBRprev = 0
    encoderticks = distance * 46.718
    while True:
        print("counterBR = ", counterBR, "counterFL = ", counterFL, "BR state: ", gpio.input(12), "FL state: ",
              gpio.input(7))

        if int(gpio.input(12)) != int(buttonBR):
            buttonBR = int(gpio.input(12))
            counterBR += 1
            # Right.append(buttonBR)
            # endright = time.perf_counter()
            # tright.append(endright)

        if int(gpio.input(7)) != int(buttonFL):
            buttonFL = int(gpio.input(7))
            counterFL += 1
            # Left.append(buttonFL)
            # endleft = time.perf_counter()
            # tleft.append(endleft)

        tend = time.perf_counter()
        tsample = tend - tstart

        if tsample >= 0.02:

            if counterBR > counterFL or counterFL > counterBR:
                errorBR = counterBR - counterFL
                errorFL = counterFL - counterBR
                deltaBR = errorBR - errorBRprev
                deltaBR = deltaBR / tsample
                deltaFL = errorFL - errorFLprev
                deltaFL = deltaFL / tsample
                valr -= 0.009 * errorBR + 0.01 * deltaBR
                valr = max(min(val + 5, valr), val - 5)
                vall -= 0.009 * errorFL + 0.01 * deltaFL
                vall = max(min(val + 5, vall), val - 5)
                pwmr.ChangeDutyCycle(valr)
                pwml.ChangeDutyCycle(vall)
                errorBRprev = errorBR
                errorFLprev = errorFL

            tstart = time.perf_counter()

        if counterBR >= encoderticks and counterFL >= encoderticks:
            pwml.stop()
            pwmr.stop()
            gameover()
            break


def reverse(distance):
    counterFL = np.uint64(0)
    counterBR = np.uint64(0)
    buttonFL = int(0)
    buttonBR = int(0)
    pwml = gpio.PWM(33, 50)  # Backleft motor
    pwmr = gpio.PWM(35, 50)  # Frontright motor
    val = 45
    vall = val
    valr = val
    pwml.start(vall)
    pwmr.start(valr)
    time.sleep(0.1)

    tstart = time.perf_counter()
    errorFLprev = 0
    errorBRprev = 0
    encoderticks = distance * 46.718
    while True:
        print("counterBR = ", counterBR, "counterFL = ", counterFL, "BR state: ", gpio.input(12), "FL state: ",
              gpio.input(7))

        if int(gpio.input(12)) != int(buttonBR):
            buttonBR = int(gpio.input(12))
            counterBR += 1

        if int(gpio.input(7)) != int(buttonFL):
            buttonFL = int(gpio.input(7))
            counterFL += 1

        tend = time.perf_counter()
        tsample = tend - tstart

        if tsample >= 0.02:

            if counterBR > counterFL or counterFL > counterBR:
                errorBR = counterBR - counterFL
                errorFL = counterFL - counterBR
                deltaBR = errorBR - errorBRprev
                deltaBR = deltaBR / tsample
                deltaFL = errorFL - errorFLprev
                deltaFL = deltaFL / tsample
                valr -= 0.009 * errorBR + 0.01 * deltaBR
                valr = max(min(val + 5, valr), val - 5)
                vall -= 0.009 * errorFL + 0.01 * deltaFL
                vall = max(min(val + 5, vall), val - 5)
                pwmr.ChangeDutyCycle(valr)
                pwml.ChangeDutyCycle(vall)
                errorBRprev = errorBR
                errorFLprev = errorFL

            tstart = time.perf_counter()

        if counterBR >= encoderticks and counterFL >= encoderticks:
            pwml.stop()
            pwmr.stop()
            gameover()
            break


def pivotleft(angle):
    counterFL = np.uint64(0)
    counterBR = np.uint64(0)
    buttonFL = int(0)
    buttonBR = int(0)
    pwml = gpio.PWM(33, 50)  # Backleft motor
    pwmr = gpio.PWM(37, 50)  # Frontright motor
    val = 45
    vall = val
    valr = val
    pwml.start(vall)
    pwmr.start(valr)
    time.sleep(0.1)

    tstart = time.perf_counter()
    errorFLprev = 0
    errorBRprev = 0
    encoderticks = angle*8.09244
    while True:
        print("counterBR = ", counterBR, "counterFL = ", counterFL, "BR state: ", gpio.input(12), "FL state: ",
              gpio.input(7))

        if int(gpio.input(12)) != int(buttonBR):
            buttonBR = int(gpio.input(12))
            counterBR += 1

        if int(gpio.input(7)) != int(buttonFL):
            buttonFL = int(gpio.input(7))
            counterFL += 1

        tend = time.perf_counter()
        tsample = tend - tstart

        if tsample >= 0.02:

            if counterBR > counterFL or counterFL > counterBR:
                errorBR = counterBR - counterFL
                errorFL = counterFL - counterBR
                deltaBR = errorBR - errorBRprev
                deltaBR = deltaBR / tsample
                deltaFL = errorFL - errorFLprev
                deltaFL = deltaFL / tsample
                valr -= 0.009 * errorBR + 0.01 * deltaBR
                valr = max(min(val + 5, valr), val - 5)
                vall -= 0.009 * errorFL + 0.01 * deltaFL
                vall = max(min(val + 5, vall), val - 5)
                pwmr.ChangeDutyCycle(valr)
                pwml.ChangeDutyCycle(vall)
                errorBRprev = errorBR
                errorFLprev = errorFL

            tstart = time.perf_counter()

        if counterBR >= encoderticks and counterFL >= encoderticks:
            pwml.stop()
            pwmr.stop()
            gameover()
            break


def pivotright(angle):
    counterFL = np.uint64(0)
    counterBR = np.uint64(0)
    buttonFL = int(0)
    buttonBR = int(0)
    pwml = gpio.PWM(31, 50)  # Backleft motor
    pwmr = gpio.PWM(35, 50)  # Frontright motor
    val = 45
    vall = val
    valr = val
    pwml.start(vall)
    pwmr.start(valr)
    time.sleep(0.1)

    tstart = time.perf_counter()
    errorFLprev = 0
    errorBRprev = 0
    encoderticks = angle * 8.09244
    while True:
        print("counterBR = ", counterBR, "counterFL = ", counterFL, "BR state: ", gpio.input(12), "FL state: ",
              gpio.input(7))

        if int(gpio.input(12)) != int(buttonBR):
            buttonBR = int(gpio.input(12))
            counterBR += 1

        if int(gpio.input(7)) != int(buttonFL):
            buttonFL = int(gpio.input(7))
            counterFL += 1

        tend = time.perf_counter()
        tsample = tend - tstart

        if tsample >= 0.02:

            if counterBR > counterFL or counterFL > counterBR:
                errorBR = counterBR - counterFL
                errorFL = counterFL - counterBR
                deltaBR = errorBR - errorBRprev
                deltaBR = deltaBR / tsample
                deltaFL = errorFL - errorFLprev
                deltaFL = deltaFL / tsample
                valr -= 0.009 * errorBR + 0.01 * deltaBR
                valr = max(min(val + 5, valr), val - 5)
                vall -= 0.009 * errorFL + 0.01 * deltaFL
                vall = max(min(val + 5, vall), val - 5)
                pwmr.ChangeDutyCycle(valr)
                pwml.ChangeDutyCycle(vall)
                errorBRprev = errorBR
                errorFLprev = errorFL

            tstart = time.perf_counter()

        if counterBR >= encoderticks and counterFL >= encoderticks:
            pwml.stop()
            pwmr.stop()
            gameover()
            break


def key_input(event):
    init()
    print("Key: ", event)
    key_press = event
    #tf = 1

    if key_press.lower() == 'w':
        distance = input("Select driving distance(in cm): ")
        forward(distance)
    elif key_press.lower() == 's':
        distance = input("Select driving distance(in cm): ")
        reverse(distance)
    elif key_press.lower() == 'a':
        driving_angle = input("enter driving angle(in degrees)")
        pivotleft(driving_angle)
    elif key_press.lower() == 'd':
        driving_angle = input("enter driving angle( in degrees)")
        pivotright(driving_angle)

    else:
        print("Invalid key pressed")


init()
while True:

    key_press = input("Select driving mode: ")
    if key_press == 'p':
        gameover()
        gpio.cleanup()
        break
    key_input(key_press)
