# autonomous-rc-car

[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg?style=flat-square)](https://gitter.im/autonomous-rc-car/Lobby)

This project aims to build an autonomous rc car using supervised learning of a neural network with a five hidden layers.I have modified a remote controlled car to remove the dependency on the RF remote controller. A Raspberry Pi controls the DC motors via an L293D Motor Driver IC. You can find a post explaining this project in detail [here](http://www.multunus.com/blog/2016/07/autonomous-rc-car-using-raspberry-pi-and-neural-networks/). Here's a video of the car in action.

[![Autonomous RC car](https://img.youtube.com/vi/dCyBvLjW6X0/maxresdefault.jpg)](https://www.youtube.com/watch?v=dCyBvLjW6X0&vq=hd1080)

## Configuration

![Rc car controller circuit diagram](https://s3.amazonaws.com/multunus-images/rc_car_circuit_diagram.png)

We will be referring the DC motor controlling the left/right direction as the front motor and the motor controlling the forward/reverse direction as the back motor. Connect the ```BACK_MOTOR_DATA_ONE``` and ```BACK_MOTOR_DATA_TWO``` GPIO pins(`GPIO17` and `GPIO27`) of the Raspberry Pi to the Input pins for Motor 1(`Input 1`, `Input 2`) and the ```BACK_MOTOR_ENABLE_PIN``` GPIO pin(`GPIO22`) to the Enable pin for Motor 1(`Enable 1,2`) in the L293D Motor Driver IC. Connect the Output pins for Motor 1(`Output 1`, `Output 2`) of the IC to the back motor.

Connect the ```FRONT_MOTOR_DATA_ONE``` and ```FRONT_MOTOR_DATA_TWO``` GPIO pins(`GPIO19` and `GPIO26`) of the Raspberry Pi to the Input pins for Motor 2(`Input 3`, `Input 4`) in the IC. Connect the Output pins for Motor 2(`Output 3`, `Output 4`) of the IC to the front motor.

The ```PWM_FREQUENCY``` and ```INITIAL_PWM_DUTY_CYCLE``` represent the initial frequency and duty cycle of the PWM output.

We have created five class labels namely ```forward```, ```reverse```, ```left```, ```right``` and ```idle``` and assigned their expected values. All class labels would require a folder of the same name to be present in the current directory.

The input images resize to the dimension of the ```IMAGE_DIMENSION``` tuple value during training.

All these values are configurable in ```configuration.py```.

## Setup

The images for training are captured using ```interactive_control_train.py```, the car is controlled using the direction arrows and all the images are recorded in the same folder along with the corresponding key press. At the command prompt, run the following command:

```
python interactive_control_train.py
```
##  Data Cleaning

Data cleaning is done using ```Renaming Images.py``` file.

## Train

After cleaning the data we call ```train.py```. Here I have used 5 Conv2d and one Dense layer for training the model. This will save the model in ```keras_model.h5```

```
python train.py 0.1 100
```
 Here's a sample [dataset](https://s3.amazonaws.com/multunus-machine-learning/autonomous-rc-car-data-set.tar.gz) and [trained model](https://s3.amazonaws.com/multunus-machine-learning/model_2016-07-20_19-38-07_l0.05_h114.pkl) to get you started.

## Run

Once we have the trained model, the RC car is run autonomously using ```autonomous.py```.

```
python autonomous.py
```
