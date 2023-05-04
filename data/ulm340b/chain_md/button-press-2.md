
    Steps: 1. Line up the gripper as viewed from the front  2. Close the gripper on the button  3. Push the button in
    Because this is "front", we need to line up the gripper from in front. Line up the robot's gripper from the front.
    - When the robot's gripper is not forward aligned with button, the robot should put gripper above button.
    Once the gripper is lined up, we can grab the button and start moving.
    - When the robot's gripper is forward aligned with button and the robot's gripper is not near button, the robot should put gripper around button.
    Once the gripper is around the button, we can push in on the button.
    - When the robot's gripper is forward aligned with button and the robot's gripper is near button, the robot should press button.

The task `pull-side` requires the robot to pull open the drawer from the side.
To pull open the drawer from the side reliably, what steps the robot should perform?
    Steps: 1. Move gripper roughly near the drawer handle  2. Start grabbing the drawer handle
    The side task has a small margin for error. If the robot's gripper is not near the drawer handle, move it in the direction of the drawer handle.
    - When the robot's gripper is not near drawer handle, the robot should move gripper near drawer handle.
    If the robot's gripper is near the drawer handle, start grabbing it.
    - When the robot's gripper is near drawer handle and the robot's gripper is open, the robot should start grabbing drawer handle.

The task `drawer-side` requires the robot to slide the drawer closed from the side.
To slide the drawer closed from the side reliably, what steps the robot should perform?
    Steps: 1. Move gripper roughly near the drawer handle  2. Start pushing the drawer handle in
    The side task has a small margin for error. If the robot's gripper is not near the drawer handle, move it in the direction of the drawer handle.
    - When the robot's gripper is not near drawer handle, the robot should move gripper near drawer handle.
    If the robot's gripper is near the drawer handle, start pushing it in.
    - When the robot's gripper is near drawer handle and the robot's gripper is open, the robot should start pushing drawer handle in.

The task `door-side` requires the robot to pull open the door from the side.
To pull open the door from the side reliably