Please provide a detailed explanation and your own examples.


The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the the window handle is right of the robot's gripper, we should move the gripper near the window handle to start pushing
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    If the robot's gripper is near the window handle we can probably slide the window close now by moving the gripper right.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform? Please provide a detailed explanation and your own examples.

''')


def load_data(splits=['train', 'val', 'test'], max_examples=None):
  '''
  The task `button-press-topdown` requires the robot to push the button down from above.
  To push the button down from above reliably, the robot should perform the following steps:
      Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
      Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
      - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
      Now that the gripper is lined up, just push down on the button.
      - When the robot's gripper is vertically aligned with button, the robot should push down on button.

  The task `button-press-topdown` requires the robot to push the button down from above.
  To push the button down from above reliably, the robot should perform the following steps:
      Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
     