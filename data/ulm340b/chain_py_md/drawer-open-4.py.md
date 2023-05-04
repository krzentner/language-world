

... and then write an `if` statement for each step.
You can look at the code above to see examples of if statements and which ones
are common to use.

You need to write two if statements.
Each of the if statements will need a check and an action.
You can choose the exact words from a list of options.

The first if statement has the following options:
```
if check("the robot's gripper is not near drawer handle"):
    robot.put("gripper above drawer handle")
```

And the second if statement has these options:
```
if check("the robot's gripper is not near drawer handle"):
    robot.put("gripper below drawer handle")
```

Make sure your if statements come after the line `def drawer_open(robot):`,
and make sure they line up, for example:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")

    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")

    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")

    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")
```

(Don't worry, we'll