
    Steps:  1. Put gripper above stick  2. Drop gripper around stick  3. Grab stick and line it up with the thermos  4. Push the thermos to the target location
    First, put the gripper above the stick.
    - When the robot's gripper is not above stick, move the robot's gripper until the robot's gripper is above the stick
    Now that the gripper is lined up above the stick, put the gripper around the stick.
    - When the robot's gripper is above stick and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the stick and the robot's gripper is closed
    Now that the gripper is around the stick, line up the stick with the thermos.
    - When stick is not horizontally aligned with thermos, move the robot's gripper until stick is forward aligned with the robot's gripper
    Now that the gripper and the stick are lined up, we can try pushing the thermos.
    - When stick is not around the thermos, move the robot's gripper until stick is vertically aligned with thermos

The task `block-orient-side` requires the robot to orient the block into the goal area.
To orient the block into the goal area reliably, what steps the robot should perform?
    Steps:  1. Put gripper above block  2. Grab block  3. Put gripper below block  4. Insert block into the goal
    We need to put the gripper above the block before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not above block, move the robot's gripper until the robot's gripper is above block
    If the gripper is around the block, try closing the gripper to grab it.
    - When the robot's gripper is above block, move the robot's gripper until the robot's gripper is around block and the robot's gripper is closed
    Now that the gripper is around the block, put the gripper below the block.
    - When the robot's gripper is not vertically aligned with block and the robot's gripper is closed, move the robot's gripper until the robot's gripper is vertically aligned with block
    Now we can just insert the block into the goal by dropping the gripper into the goal.
    - When block is below goal, move the robot's gripper until block is vertically aligned with goal

The task `peg-un