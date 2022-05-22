#!/usr/bin/env python
"""Run the car autonomously"""
import time
import sys
from keras.models import load_model
import io
import picamera
import configuration
import numpy as np
import cv2
from predict import predict
import helpers.motor_driver as motor_driver_helper
import helpers.image as image_helper

def autonomous_control(model):
    """Run the car autonomously"""
    with picamera.PiCamera() as camera:
        camera.resolution = configuration.PICAMERA_RESOLUTION
        camera.framerate = configuration.PICAMERA_FRAMERATE
        time.sleep(configuration.PICAMERA_WARM_UP_TIME)
        pwm = motor_driver_helper.get_pwm_imstance()
        motor_driver_helper.start_pwm(pwm)
        should_brake = False
        while True:
            stream = io.BytesIO()
            camera.capture(stream, format='jpeg', use_video_port=True)
            stream.seek(0)
            file_bytes = np.asarray(bytearray(stream.read()),dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            direction_array = predict(model, img)
            direction = [direction for direction, array in configuration.CLASSIFICATION_LABELS_AND_VALUES.items() if array == direction_array]
            image_helper.save_image_with_direction(stream, direction)
            stream.flush()
            if direction == 'forward_right':
                print('forward_right')
                should_brake = True
                motor_driver_helper.set_right_mode()
                motor_driver_helper.set_forward_mode()
            elif direction == 'forward_left':
                print('forward_left')
                should_brake = True
                motor_driver_helper.set_left_mode()
                motor_driver_helper.set_forward_mode()
            elif direction == 'forward':
                print('forward')
                should_brake = True
                motor_driver_helper.set_front_motor_to_idle()
                motor_driver_helper.set_forward_mode()
            elif direction == 'left':
                print('left')
                should_brake = True
                motor_driver_helper.set_back_motor_to_idle()
                motor_driver_helper.set_left_mode()
            elif direction == 'right':
                print('right')
                should_brake = True
                motor_driver_helper.set_back_motor_to_idle()
                motor_driver_helper.set_right_mode()
            else:
                if should_brake:
                    print("braking...")
                    motor_driver_helper.set_reverse_mode()
                    time.sleep(0.2)
                    should_brake = False
                motor_driver_helper.set_idle_mode()
                motor_driver_helper.change_pwm_duty_cycle(pwm, 100)
            print(direction)

def main():
    """Main function"""
    model = load_model("keras_mnist.h5")
    motor_driver_helper.set_gpio_pins()
    autonomous_control(model)

if __name__ == '__main__':
    main()
