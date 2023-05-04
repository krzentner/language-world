
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck"):
        robot.slide("the puck to the goal")

# pick-place-side: pick up the puck and hold it at the target location from the side
def pick_place_side(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not around puck"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# push-side: slide the puck to the target location from the side
def push_side(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not near puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("puck to goal")

# pick: pick up the object with gripper
def pick(robot):
    if check("the robot's gripper is not above object"):
        robot.put("gripper above object")
    if check("the robot's gripper is above object and the robot's gripper is not vertically aligned with object"):
        robot.align("gripper to object")
    if check("the robot's gripper is vertically aligned with object"):
        robot.close("gripper around object")
    if check("the robot's gripper is near object"):
        robot