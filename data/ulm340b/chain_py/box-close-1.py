
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move lid to box
    # Put gripper above box lid
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    # Drop the gripper around the box lid
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # Close gripper around box lid
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # Move lid to box
    if check("the robot's gripper is near the box lid and the robot's gripper is closed"):
        robot.put("lid on box")

# box-open: pick up the box lid and move it away from the box
def box_open(robot):
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move lid away from box
    # Put gripper above box lid
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    # Drop the gripper around the box lid
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # Close gripper around box lid
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # Move lid away from box
    if check("the robot's gripper is above the box lid and the robot's gripper is closed"):
        robot.put("lid far from box")

# pick-place-wall: pick up the puck and hold it at the target location against
# the wall
def pick_place_wall(robot):
    # Steps: