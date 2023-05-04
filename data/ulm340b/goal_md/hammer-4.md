
    - When the robot's gripper is above nail and the hammer is above nail, the robot's gripper should be opened
    - When the hammer is above nail, move the robot's gripper until the robot's gripper is above nail

The task `block-stack` requires the robot to stack the red block on top of the blue block.
To stack the red block on top of the blue block reliably, what steps the robot should perform?
    - When the robot's gripper is above red block and red block is near blue block, the robot's gripper should be opened
    - When the robot's gripper is above red block, move the robot's gripper until the robot's gripper is above blue block
    - When the robot's gripper is above red block, the red block should be picked up
    - When the robot's gripper is above blue block, the blue block should be picked up
""".strip().split("\n")

TASK_DESC_STRING = """
The task `button-press-side` requires the robot to slide the button to the left.
To slide the button to the left reliably, the robot should perform the following steps:
    Steps:  1. Put gripper below the button  2. Slide the button to the left
    First, put the gripper below the button.
    - When the robot's gripper is not below button, move the robot's gripper until the robot's gripper is below button
    The gripper should now be below the button. Now we can just slide the button to the left.
    - When the robot's gripper is below button, move the robot's gripper until the robot's gripper is almost horizontally aligned with button

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button
