
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above the puck"):
        robot.grab("puck")
    if check("the robot's gripper is closed and the puck is in the robot's gripper"):
        robot.move("puck to goal")

# hand-insert-side: grab the peg and insert it into the hole from the side
def hand_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is above the peg"):
        robot.grab("peg")
    if check("the robot's gripper is closed and the peg is in the robot's gripper"):
        robot.insert("peg into hole")

# push-pick-place: push the puck to the target location, pick it up, and hold it at the target location
def push_pick_place(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")
    if check("the robot's gripper is above puck"):
        robot.grab("puck")
    if check("the robot's gripper is below the goal"):
        robot.move("puck to goal")

# push-reach-pick-place: push the puck to the target location, reach to the target location, pick up the puck, and hold it at the target location
def push_reach_pick_place(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")
    if check("the robot'