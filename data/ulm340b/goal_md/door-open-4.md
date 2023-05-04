
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    We need to put the gripper above the door handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with door handle, move the robot's gripper until the robot's gripper is vertically aligned with the door handle
    Once the gripper is lined up above the door handle, we should be able to grab the door handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle, move the robot's gripper until the robot's gripper is around the door handle
    Once the gripper is around the door handle, we can just pull the door open.
    - When the robot's gripper is around door handle, move the robot's gripper until the robot's gripper is horizontally aligned with the door handle

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, what steps the robot should perform?
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, move the robot's gripper until the robot's gripper is near the door handle
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, move the robot's gripper until the robot's gripper is around the door handle

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?
    Steps:  1. Line up gripper from the side  2. Push button down from the side
    Because this is "side", we need to line up the robot's gripper from the side before pushing.
    - When the robot's gripper is not horizontally aligned with button, move the robot's gripper until the robot's gripper is horizontally aligned with the button and the robot's gripper is closed
    Then push down with the gripper