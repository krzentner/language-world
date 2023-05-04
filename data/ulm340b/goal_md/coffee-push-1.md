
    <input>

The task `drawer-close` requires the robot to push the drawer closed.
To push the drawer closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Grab drawer handle  3. Push the drawer closed
    Because this is a drawer, the robot should make sure to put its gripper above the drawer handle to grab it.
    - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle
    When the gripper is vertically aligned with the drawer handle and the robot's gripper is not around drawer handle, the robot should try to grab the drawer handle with its gripper.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle
    Finally, when the robot's gripper is around drawer handle the robot should push the drawer closed by moving its gripper to the drawer handle.
    - When the robot's gripper is around drawer handle, move the robot's gripper until the robot's gripper is horizontally aligned with drawer handle

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    -