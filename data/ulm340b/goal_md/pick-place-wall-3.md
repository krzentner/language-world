

"""

if __name__ == "__main__":
    print(
        dedent(
            """
        The task `window-close` requires the robot to slide the window closed to the right.
        To slide the window closed to the right reliably, the robot should perform the following steps:
            Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
            If the the window handle is right of the robot's gripper, we should move the gripper near the window handle to start pushing
            - When the robot's gripper is in front of the window handle, move the robot's gripper until the robot's gripper is right of the window handle
            If the robot's gripper is near the window handle we can probably slide the window close now by moving the gripper right.
            - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, move the robot's gripper until the robot's gripper is almost vertically aligned with the window handle
            If the robot's gripper is starting to be in front of the window handle, push harder.
            - When the robot's gripper is near the window handle, move the robot's gripper until the robot's gripper is forward aligned with the window handle

        The task `window-open` requires the robot to slide the window open to the left.
        To slide the window open to the left reliably, the robot should perform the following steps:
            Steps:  1. Put gripper right of the window handle  2. Start pushing against the window handle to open the window  3. Push the window open harder
            If the robot's gripper is not vertically lined up with the window handle, we should move the gripper near the window handle to start pushing
            - When the robot's gripper is near the window handle, move the robot's gripper until the robot's gripper is forward aligned with the window handle
            If the robot's gripper is near the window handle we can probably slide the window open now by moving the gripper left.
            - When the robot's gripper is in front of the window handle, move the robot's gripper until the robot's gripper is vertically aligned with the window handle

        The task `drawer-open` requires the robot to pull the drawer open.
        To pull the drawer open reliably, the robot should perform the following steps:
            Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the