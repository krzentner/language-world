

### Explanation

The faucet is a long object, so you can use `forward aligned` to check for the direction of the gripper. The goal here is to align the gripper to the right direction and push the faucet handle counter-clockwise to turn it.

### Solution

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet left
    # We need to put the gripper above the faucet handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # Once the gripper is lined up above the faucet handle, we should be able to
    # grab the faucet handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.put("gripper around faucet handle")
    # Once the gripper is around the faucet handle, we can just turn the faucet.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")
```

## Test 3

```
# peg-insert-topdown: insert the peg into the hole as seen from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
       