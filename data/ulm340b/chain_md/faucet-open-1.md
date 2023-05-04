
We don't know the steps yet. But maybe we can figure out how to turn the faucet left reliably while you are doing the task. For this task, you can give instructions to the robot by clicking on what you want it to do in the top right. Try to think of a set of steps you want to repeat and give them to the robot with the click actions in the top right. The robot will try to learn what you want to repeat and repeat it automatically.

The task `peg-insert-topdown` requires the robot to insert the peg in the hole.
To insert the peg in the hole reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Insert the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    As long as the gripper is vertically aligned with the peg and not yet around it, we can put the gripper around it.
    - When the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole to the side, insert it.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, the robot should perform the following steps:
    Steps:  1. Put gripper right of the window handle  2. Start pushing against the window handle to open the window  3. Push the window open harder
    If the robot's gripper is not vertically lined up with the window handle, we should move the gripper near the window handle to start pushing
    - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
    If the robot's gripper is near the window handle we can probably slide the window open now by moving the gripper left.
    - When the robot's gripper is near the window