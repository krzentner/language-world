

The task `door-open-doorknob` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above doorknob  2. Drop gripper around doorknob  3. Pull open the door
    First, put the gripper above the doorknob.
    - When the robot's gripper is not vertically aligned with doorknob, move the robot's gripper until the robot's gripper is vertically aligned with the doorknob and the robot's gripper is closed
    Once the gripper is lined up above the doorknob, we should be able to grab the doorknob by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with doorknob and the robot's gripper is not around doorknob, move the robot's gripper until the robot's gripper is around the doorknob
    Once the gripper is around the doorknob, we can just pull the door open.
    - When the robot's gripper is around doorknob, move the robot's gripper until the robot's gripper is horizontally aligned with doorknob

The task `window-open-latch` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, the robot should perform the following steps:
    Steps:  1. Put gripper right of the window latch  2. Start pushing against the window latch to open the window  3. Push the window open harder
    If the robot's gripper is not vertically lined up with the window latch, we should move the gripper near the window latch to start pushing
    - When the robot's gripper is near the window latch, move the robot's gripper until the robot's gripper is forward aligned with the window latch
    If the robot's gripper is near the window latch we can probably slide the window open now by moving the gripper left.
    - When the robot's gripper is in front of the window latch, move the robot's gripper until the robot's gripper is vertically aligned with the window latch

The task `peg-insert-hole` requires the robot to grab the peg and insert it into the hole.
To grab the peg and insert it into the hole reliably, the robot should perform the following steps:
    Steps:  1. Put gripper near the peg  2. Start picking up the peg  3. Bring the peg over the hole  4. Start moving the peg down  5. Insert the peg
    As long as the peg is near the