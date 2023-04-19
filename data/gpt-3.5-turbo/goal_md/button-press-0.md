The task `button-press` requires the robot to push the button from the front. To push the button from the front reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the front  2. Push the button
    Since this is not a `topdown` task, we need to line up the robot's gripper from the front.
    - When the robot's gripper is not horizontally aligned with the button, move the robot's gripper until the robot's gripper is horizontally aligned with the button
    Once the robot's gripper is aligned with the button from the front, we can simply push the button. 
    - When the robot's gripper is horizontally aligned with the button, move the robot's gripper until the robot's gripper is close to the button to push it.