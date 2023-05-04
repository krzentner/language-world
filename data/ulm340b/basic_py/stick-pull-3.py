
    if check("the robot's gripper is not near thermos"):
        robot.put("gripper above stick")
    if check("the robot's gripper is not forward aligned with stick and the robot's gripper is not around stick"):
        robot.put("gripper around stick")
    if check("the robot's gripper is forward aligned with stick"):
        robot.move("thermos to goal")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not near thermos"):
        robot.put("gripper above stick")
    if check("the robot's gripper is not forward aligned with stick and the robot's gripper is not around stick"):
        robot.put("gripper around stick")
    if check("the robot's gripper is forward aligned with stick"):
        robot.move("thermos to goal")

# pick-place-wall: pick up the puck and hold it at the target location (with a wall blocking the gripper's approach)
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.reach("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.slide("gripper to puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is above puck"):
        robot.place("puck at goal")

# push-wall: slide the puck to the target location (with a wall blocking the gripper's approach)
def push_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.reach("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.slide("gripper to puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
