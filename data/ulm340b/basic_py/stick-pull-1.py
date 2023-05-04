
    if check("the robot's gripper is not near stick and the robot's gripper is open"):
        robot.grab("stick")
    if check("the robot's gripper is near stick and the robot's gripper is not closed"):
        robot.close("gripper around stick")
    if check("the robot's gripper is near stick and the robot's gripper is closed and the stick is not in the thermos"):
        robot.put("stick into thermos")
    if check("stick is in thermos"):
        robot.pull("thermos to goal")

# pick-place-wall: pick the puck up from the table and place it against the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is not around puck and the robot's gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.put("puck against wall")

# pour-into-pot: pour the water from the cup into the pot
def pour_into_pot(robot):
    if check("the robot's gripper is not near cup and the robot's gripper is open"):
        robot.grab("cup")
    if check("the robot's gripper is near cup and the robot's gripper is open"):
        robot.close("gripper around cup")
    if check("the robot's gripper is near cup and the robot's gripper is closed"):
        robot.pour("water into pot")

# push-multi-step: use the spoon to push the button
def push_multi_step(robot):
    if check("the robot's gripper is not near spoon and the robot's gripper is open"):
        robot.grab("spoon")
    if check("the robot's gripper is near spoon and the robot's gripper is open"):
        robot.close("gripper around spoon")
    if check("the robot's gripper is near spoon and the robot's gripper is closed"):
       