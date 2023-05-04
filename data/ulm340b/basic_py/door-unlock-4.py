
    if check("the robot's gripper is not almost vertically aligned with dial"):
        robot.place("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is open"):
        robot.put("gripper around dial")
    if check("the robot's gripper is vertically aligned with dial"):
        robot.spin("dial to goal")

# lever-pull: grab the lever and pull it down
def lever_pull(robot):
    if check("the robot's gripper is not around lever"):
        robot.grab("lever")
    if check("the robot's gripper is around lever and the robot's gripper is above the lever"):
        robot.push("lever down")

# peg-unplug-side: remove the peg from the hole by pulling it out
def peg_unplug_side(robot):
    if check("the robot's gripper is not around the peg"):
        robot.grab("peg")
    if check("the robot's gripper is around the peg and the peg is in the hole"):
        robot.pull("peg out of hole")

# slide-back: slide the object back to the target location
def slide_back(robot):
    if check("the robot's gripper is not above the object"):
        robot.move("gripper above object")
    if check("the robot's gripper is almost above the object and the robot's gripper is forward aligned with the object"):
        robot.slide("object back to goal")

# pick-place-wall: pick up the block and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above the object"):
        robot.place("gripper above object")
    if check("the robot's gripper is above the object and the object is in the room and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is near object and the object is in the room and the robot's gripper is open"):
        robot.close("gripper around object")
    if check("the robot's gripper is around object and the object is in the room and the robot's gripper is closed"):
        robot.place("object at goal")

# stack: place the top block on the bottom block
def stack(robot):
