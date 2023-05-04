
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# push-back: slide the puck backwards to the target location
def push_front(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# push-side: push the puck to the target location from the side
def push_side(robot):
    if check("the robot's gripper is not left of puck"):
        robot.put("gripper to left of puck")
    if check("the robot's gripper is not near puck"):
        robot.place("gripper near puck")
    if check("the robot's gripper is left of puck"):
        robot.push("the puck to the goal")

# push-side-back: push the puck to the target location from the side
def push_side_back(robot):
    if check("the robot's gripper is not left of puck"):
        robot.put("gripper to left of puck")
    if check("the robot's gripper is not near puck"):
        robot.place("gripper near puck")
    if check("the robot's gripper is left of puck"):
        robot.push("the puck to the goal")

# slide-back: slide the puck backwards to the target location
def slide_back(robot):
    if check("the robot's gripper is not below puck and the robot's gripper is not behind puck"):
        robot.put("the gripper behind the puck")
  