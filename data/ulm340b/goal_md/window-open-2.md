
    Steps:  1. Put gripper near the window handle  2. Push the window open
    If the the window handle is not near the gripper, move the gripper near the window handle to start pulling
    - When the window handle is left of the robot's gripper, move the robot's gripper until the robot's gripper is left of the window handle
    If the window handle is near the gripper we can probably start pulling.
    - When the robot's gripper is right of the window handle, move the robot's gripper until the robot's gripper is almost horizontally aligned with the window handle
    
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, what steps the robot should perform?
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, what steps the robot should perform?
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper