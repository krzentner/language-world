
    Steps:  1. Line up the gripper as viewed from the front  2. Push the button down
    Because this is the "front", we just need to line up the gripper from the front. Line up the robot's gripper from the front.
    - When the robot's gripper is not forward aligned with button, the robot should put gripper in front of button.
    Now that the gripper is lined up, push the button down.
    - When the robot's gripper is forward aligned with button, the robot should push down on button.
"""



INSTRUCTION_DEMO = """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, the robot should reach to goal.

We'll give you a demonstration of how the task should be accomplished:




The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the the window handle is right of the robot's gripper, we should move the gripper near the window handle to start pushing
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    If the robot's gripper is near the window handle we can probably slide the window close now by moving the gripper right.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

We'll give you a demonstration of how the task should be accomplished:




The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the