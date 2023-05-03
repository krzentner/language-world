

Below is the code for the `peg-insert-side` task: 

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    # 1. Put gripper above the peg
    # 2. Drop the gripper around the peg
    # 3. Close the gripper around the peg
    # 4. Move the peg to the goal hole
    # 5. Insert the peg into the hole
    # Put the gripper above the peg so that it can grab the peg without bumping it.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # Once the gripper is lined up above the peg, it should open up and grab it.
    if check("the robot's gripper is above the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # Once the gripper has grabbed the peg, close it.
    if check("the robot's gripper is around the peg"):
        robot.close("gripper around peg")
    # Move the peg to the goal hole.
    if check("the robot's gripper is around the peg and the peg is not near the goal hole"):
        robot.move("peg to goal hole")
    # Once the peg is in position, insert it by pushing away from the hole.
    if check("the peg is near the goal hole and the robot's gripper is around the peg"):
        robot.push("away from the hole")
```