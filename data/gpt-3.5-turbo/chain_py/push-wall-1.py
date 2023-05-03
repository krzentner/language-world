# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to wall
    #  4. Move gripper over the wall
    #  5. Push gripper into top of puck again
    #  6. Slide puck to goal
    # This action is similar to "push", but with a wall in the way.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the wall")
    # Once we're at the wall, move the gripper over it so we can push the puck
    # on the other side of the wall.
    if check("the gripper is not over the wall"):
        robot.move("the gripper over the wall")
    # Once the gripper is over the wall, we need to push down on the puck
    # again to slide it to the goal.
    if check("the gripper is over the wall and the puck is below the robot's gripper"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck on the other side of the wall, we've
    # trapped the puck and can slide it to the target location.
    if check("the gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")