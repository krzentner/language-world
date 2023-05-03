

The Steps:
 1. Put the gripper above and to the side of the hole
 2. Angle the gripper downwards
 3. Reach into the hole
 4. Grab the peg with the gripper
 5. Lift the gripper out of the hole, with the peg
 6. Move the peg to the target location

if check("the robot's gripper is not above the hole and to the side of the hole"):
    robot.put("gripper above and to the side of the hole")

if check("the robot's gripper is above the hole and to the side of the hole"):   
    robot.angle("gripper downwards")

if check("the robot's gripper is angled downwards towards the hole"):
    robot.reach("into the hole")

if check("the robot's gripper is near the peg in the hole"):
    robot.grab("peg with the gripper")

if check("the peg is in the robot's gripper"):
    robot.lift("gripper out of hole, with the peg")

if check("the robot's gripper is out of the hole with the peg"):
    robot.place("peg at target location")