
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Move puck to goal
    # First, put the gripper above the puck.
    # We don't need to be super careful because the robot's gripper is open.
    if check("the robot's gripper is not above the puck"):
        robot.drop("gripper above puck")
    # If the gripper is vertically aligned with the puck but not near it, put
    # the gripper near the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("puck with gripper")
    # If the gripper is below the puck, we've probably grabbed it and can move
    # it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is below the puck"):
        robot.place("puck at goal")

# insert-side: slide the puck sideways into the hole
def insert_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("gripper into puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check