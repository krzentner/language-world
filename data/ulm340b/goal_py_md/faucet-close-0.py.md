

To make it work, we need a way to tell when the faucet is closed.
One of the things that we can check is:

```
"the robot's gripper is below the faucet"
```

When `check()` is passed this check, it will check if the robot's gripper is below the faucet.
This is because we can tell that the faucet is closed when the gripper is below the faucet.

# Notes

There are five tasks that you must perform in order to accomplish this task:

## Task 1

Steps:

  1. Put gripper right of the faucet
  2. Start pulling against the faucet handle to close the faucet
  3. Pull the faucet handle harder

If the gripper is not near the faucet handle, move the gripper near the faucet handle to start pulling.

If the robot's gripper is roughly near the faucet handle, then the faucet is closed.

First, put the gripper right of the faucet.

If the robot's gripper is above the faucet, move it to the right of the faucet handle.

If the gripper is left of the faucet, go back to putting the gripper above the faucet.

As long as the gripper is still roughly above the faucet and the faucet is not closed, move the gripper to the right of the faucet.

If the faucet is closed, then the robot's gripper is roughly right of the faucet handle.

## Task 2

Steps:

  1. Put gripper left of the faucet
  2. Start pulling against the faucet handle to open the faucet
  3. Pull the faucet open harder

If the gripper is not vertically lined up with the faucet handle, we should move the gripper near the faucet handle to start pushing.

If the robot's gripper is above the faucet handle we can probably slide the window open now by moving the gripper left.

If the faucet becomes right of the gripper, go back to putting the gripper above the faucet.

Because the faucet is a long object, check if the gripper is lined up with it from the front instead of around it.

If check("faucet is below the robot's gripper and faucet is forward aligned with the robot's gripper"):

As long the gripper is still mostly around the faucet and the faucet isn't closed, move the gripper left of the faucet handle.

If the faucet is closed, then the robot's gripper is in front of the faucet handle.

If the gripper is in front of the faucet handle, move it left of the faucet.

## Task 3

Steps:

