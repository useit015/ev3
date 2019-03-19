#!/usr/bin/env python3
import json

import ev3dev.ev3 as ev3

from common.follower import Follower
from common.line_detectors import OneSensorLineDetector
from common.utils import get_json_from_file

color_sensor = ev3.ColorSensor(address='in2')
left_motor = ev3.LargeMotor('outA')
right_motor = ev3.LargeMotor('outD')
calibration = get_json_from_file('./data/calibration_two_sensors.json')

line_detector = OneSensorLineDetector(color_sensor, calibration)

follower = Follower(right_motor, left_motor, line_detector, './data/pid_and_speed_1.json')
follower.follow()
