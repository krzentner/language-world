# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put the gripper above the puck
    #  2. Push the gripper into the top of the puck
    #  3. Move the gripper to the wall
    #  4. Push up against the wall to lift the puck
    #  5. Slide the puck past the wall
    #  6. Move the gripper back to the puck and push the gripper into the puck again
    #  7. Slide the puck to the target location
    # To push the puck past the wall, we need to lift it over the wall.
    # Start by lining up the gripper with the puck as usual.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # Try to push into the top of the puck to trap it.
    if check("the robot's gripper is near the puck and the robot's gripper is not pushing into the puck"):
        robot.push("the gripper into the puck")
    # Once we have the puck trapped, move the gripper to the wall.
    if check("the robot's gripper is pushing into the puck and the robot's gripper is not aligned with the wall"):
        robot.move("gripper to the wall")
    # Once the gripper is at the wall, push up on the wall to lift the puck.
    if check("the robot's gripper is aligned with the wall and is not pushing upwards against the wall"):
        robot.push("up against the wall")
    # The gripper is now pushing up against the wall, so slide the puck to the other side of the wall.
    # Since the gripper is pushing up, it will lift the puck over the wall and allow us to slide it to the other side.
    if check("the robot's gripper is pushing up against the wall and the puck is not at the target location"):
        robot.slide("the puck past the wall")
    # Once the puck is past the wall, move the gripper back to the puck and push into it again.
    if check("the puck is at the target location and the robot's gripper is not at the puck"):
        robot.move("gripper to the puck")
    if check("the robot's gripper is not pushing into the puck"):
        robot.push("the gripper into the puck")
    # Finally, we can slide the puck to the target location using the same technique as before.
    if check("the robot's gripper is pushing into the puck and the puck is not at the target location"):
        robot.slide("the puck to the goal")