
    Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.
    
    
    The task `coffee-button` requires the robot to push the button on the coffee machine.
    To push the button on the coffee machine reliably, the robot should perform the following steps:
    Steps:  1. Put gripper in front of the button  2. Push down on the button from the top
    
    Because this is a "topdown" task, line up the robot's gripper from above with the button.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Once the gripper is lined up, push down on the button.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button
    """,

    "drawer-close-train":
    """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the the window handle is right of the robot's gripper, we should move the gripper near the window handle to start pushing
    - When the robot's gripper is in front of the window handle, move the robot's gripper until the robot's gripper is right of the window handle
    If the robot's gripper is near the window handle we can probably slide the window close now by moving the gripper right.
    - When the window handle is right of the robot's gripper and the robot's gripper