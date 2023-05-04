
    # Steps:
    #  1. Put gripper near puck
    #  2. Grab puck
    #  3. Hold puck at goal
    # If the puck is not in front of the gripper, move the gripper near the
    # puck.
    if check("the puck is not in front of the robot's gripper and the puck is not vertically aligned with the robot's gripper"):
        robot.put("gripper near puck")
    # If the gripper is near the puck but not closed around it, we should grab
    # it.
    if check("the robot's gripper is near the puck and the puck is not inside the robot's gripper"):
        robot.grab("the puck")
    # If we have a firm grip on the puck, we can lift the gripper to the target
    # location to hold it there.
    if check("the puck is inside the robot's gripper"):
        robot.hold("the puck at the goal")

# pick-place-wall: pick up the puck and hold it at the target location against
# the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper near puck
    #  2. Grab puck
    #  3. Hold puck at goal
    # If the puck is not in front of the gripper, move the gripper near the
    # puck.
    if check("the puck is not in front of the robot's gripper and the puck is not vertically aligned with the robot's gripper"):
        robot.put("gripper near puck")
    # If the gripper is near the puck but not closed around it, we should grab
    # it.
    if check("the robot's gripper is near the puck and the puck is not inside the robot's gripper"):
        robot.grab("the puck")
    # If we have a firm grip on the puck, we can lift the gripper to the target
    # location to hold it there.
    # Check that the gripper is still vertically aligned with the puck (as seen
    # from the side) to ensure the puck stays against the wall.
    if check("the puck is inside the robot's gripper and the robot's gripper is vertically aligned with the puck"):
        robot.hold("the puck at the goal")