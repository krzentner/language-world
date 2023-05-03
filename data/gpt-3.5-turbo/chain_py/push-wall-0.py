# Steps:
    #  1. Put gripper above the puck
    #  2. Push gripper into top of puck
    #  3. Slide the puck toward the wall
    #  4. Move the gripper to the top of the puck
    #  5. Push the puck over the wall
    #  6. Slide the puck to the goal
    # Follow the same basic steps as with push, but with a modification for the
    # wall.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it toward the wall.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck toward the wall")
    # When the gripper is above the puck and we're at the wall, move the gripper
    # to the top of the puck.
    if check("the robot's gripper is above the puck at the wall"):
        robot.put("gripper on top of the puck")
    # Once the gripper is on top of the puck, push it over the wall.
    if check("the puck is below the gripper at the wall and the gripper is on top of the puck"):
        robot.push("the puck over the wall")
    # Once we're on the other side of the wall, we can slide the puck to the
    # goal location.
    if check("the puck is on the other side of the wall and the gripper is above the puck"):
        robot.slide("the puck to the goal")