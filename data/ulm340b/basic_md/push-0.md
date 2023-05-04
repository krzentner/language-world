

To solve `button-press-topdown`, you can use the following actions:
    - place gripper above button: The robot's gripper will be above the button, but the robot will no longer be holding the button.
    - push down on button: The robot's gripper will be on the button, but the robot will no longer be above the button.

To solve `drawer-open`, you can use the following actions:
    - put gripper above drawer handle: The robot's gripper will be above the drawer handle, but the robot will no longer be holding the drawer handle.
    - put gripper around drawer handle: The robot's gripper will be holding the drawer handle, but the robot will no longer be above the drawer handle.
    - pull away from drawer: The robot's gripper will be above the drawer handle, but the robot will no longer be holding the drawer handle.

To solve `peg-insert-side`, you can use the following actions:
    - put gripper above peg: The robot's gripper will be above the peg, but the robot will no longer be holding the peg.
    - grab peg: The robot's gripper will be holding the peg, but the robot will no longer be above the peg.
    - align peg to hole: The robot's gripper will be forward aligned with the peg, but the robot will no longer be aligned with the hole.
    - insert peg into hole: The robot's gripper will be horizontally aligned with the peg, but the robot will no longer be holding the peg.

To solve `door-open`, you can use the following actions:
    - put gripper above door handle: The robot's gripper will be above the door handle, but the robot will no longer be holding the door handle.
    - put gripper around door handle: The robot's gripper will be holding the door handle, but the robot will no longer be above the door handle.
    - pull door open: The robot's gripper will be holding the door handle, but the robot will no longer be above the door handle.

To solve `drawer-close`, you can use the following actions:
    - grab drawer handle: The robot's gripper will be holding the drawer handle, but the robot will no longer be above the drawer handle.
    - push drawer closed: The robot's gripper will be above the drawer handle, but the robot will no longer be holding the drawer handle.

To solve `window-close`, you can use the following actions:
    - move gripper to left of window handle: The robot's gripper will be below the window handle, but the robot will no longer be above the window handle.
    