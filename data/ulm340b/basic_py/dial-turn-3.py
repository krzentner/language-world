
    if check("the robot's gripper is not forward aligned with dial and the robot's gripper is not around dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is forward aligned with dial and the robot's gripper is not around dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is forward aligned with dial and the robot's gripper is around dial"):
        robot.twist("dial")

def push(robot):
    if check("the puck is not below the robot's gripper"):
        robot.put("the robot's gripper above the puck")
    if check("the puck is below the robot's gripper and the puck is not in front of the robot's gripper"):
        robot.push("the robot's gripper into the puck")
    if check("the puck is in front of the robot's gripper"):
        robot.push("the puck towards goal")

def peg_insert_side_v1(robot):
    if check("the peg is not vertically aligned with the robot's gripper"):
        robot.place("gripper above peg")
    if check("the peg is vertically aligned with the robot's gripper and the peg is not below the robot's gripper"):
        robot.push("gripper into peg")
    if check("the peg is below the robot's gripper and the peg is not in front of the robot's gripper"):
        robot.push("peg towards hole")
    if check("the peg is in front of the robot's gripper and the peg is not below the hole"):
        robot.push("peg towards hole")
    if check("the peg is below the hole"):
        robot.insert("peg into hole")

# push: slide the puck to the target location
def push_v2(robot):
    if check("the robot's gripper is not below puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is below puck and the robot's gripper is not in front of puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is in front of puck and the robot's gripper is not below the puck"):
        robot.push("puck toward goal")
    if check("the puck is below the robot's gripper"):