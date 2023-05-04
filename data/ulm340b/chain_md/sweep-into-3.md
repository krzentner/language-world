

The task `lift` requires the robot to grab the cube and move it up.
To grab the cube and move it up reliably, the robot should perform the following steps:
    Steps:  1. Drop gripper around the cube  2. Lift up the cube
    The robot should lower the gripper to grab the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, the robot should drop gripper around cube.
    As long as the cube stays in the gripper, lifting up the cube should work.
    - When the robot's gripper is around cube, the robot should lift cube up.

The task `push-away` requires the robot to push the cube away from the gripper.
To push the cube away from the gripper reliably, the robot should perform the following steps:
    Steps:  1. Put gripper near cube  2. Push cube away
    As long as the cube is near the gripper, we can just push the cube.
    - When the robot's gripper is not near cube, the robot should push cube away.

The task `press-on` requires the robot to press down on the button.
To press down on the button reliably, the robot should perform the following steps:
    Steps:  1. Line gripper up above button  2. Push gripper down into button
    - When the robot's gripper is not above button, the robot should move gripper above button.
    As long as the button is still below the gripper, the button is being pressed.
    - When the robot's gripper is above button, the robot should press down into button.

The task `move-back` requires the robot to move the gripper back towards the robot without touching anything.
To move the gripper back towards the robot without touching anything reliably, the robot should perform the following steps:
    Steps:  1. Move the robot's gripper backwards towards the robot  2. Keep the robot's gripper far away from any objects
    - When the robot's gripper is not far away from all objects, the robot should move back towards robot.

The task `drop` requires the robot to lower the gripper without hitting anything.
To lower the gripper without hitting anything reliably, the robot should perform the following steps:
    Steps:  1. Keep the robot's gripper far away from any objects  2. Move the robot's gripper downwards
    First, keep the gripper away from anything we might hit.
    - When the robot's gripper is not far away from all objects,