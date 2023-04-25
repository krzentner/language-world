

Steps:
1. Put gripper above the hole
2. Drop gripper around the peg
3. Close gripper around peg
4. Move peg to goal

First, put the gripper above the hole.
if check("the robot's gripper is not above the hole"):
    robot.put("gripper above hole")

Next, drop the gripper around the peg. This can be done by angling the gripper in order to fit in the hole and then lowering it around the peg.
if check("the robot's gripper is not around the peg and the robot's gripper is open"):
    robot.drop("gripper around peg")

Once the gripper is lined up around the peg, close the gripper to grab the peg.
if check("the robot's gripper is around the peg and the robot's gripper is open"):
    robot.close("gripper around peg")

Now that the gripper is securely holding the peg, move it to the goal.
if check("the robot's gripper is around the peg and the robot's gripper is closed"):
    robot.place("peg at goal")