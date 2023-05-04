
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# pick-place-wall: pick up the puck and hold it at the target location with a wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# hammer: pound the peg into the hole
def hammer(robot):
    if check("the robot's gripper is not above the mallet"):
        robot.put("gripper above the mallet")
    if check("the robot's gripper is above the mallet"):
        robot.pick_up("the mallet")
    if check("the mallet is not vertically aligned with the peg and the peg is below the mallet"):
        robot.put("mallet over the peg")
    if check("the robot's gripper is vertically aligned with the mallet and the mallet is above the peg"):
        robot.push("the mallet into the peg")
    if check("the robot's gripper is near the peg and the mallet is above the peg"):
        robot.pound("the mallet into the peg")

# hammer-side: pound the peg into the hole from the side
def hammer_side(robot):
    if check("the robot's gripper is not above the mallet"):
        robot.put("gripper above the mallet")
    if check("the robot's gripper is above the mallet"):
        robot.pick