
    Steps:  1. Put gripper above hammer  2. Grab the hammer  3. Line up the hammer  4. Slam the hammer down on the nail  5. Pick up the hammer again


    1. When the robot's gripper is above the hammer move the robot's gripper until the robot's gripper is around the hammer and the robot's gripper is closed
    2. When the robot's gripper is above the nail and the robot's gripper is not open, move the robot's gripper until the robot's gripper is near the nail and the robot's gripper is open
    3. When the robot's gripper is around the hammer and the robot's gripper is closed, move the robot's gripper until the robot's gripper is above the hammer and the robot's gripper is open
    4. When the robot's gripper is around the hammer and the robot's gripper is closed, move the robot's gripper until the robot's gripper is above the nail
    5. When the robot's gripper is above the hammer move the robot's gripper until the robot's gripper is around the hammer and the robot's gripper is closed
"""



"""
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the