
    # Steps:
    #  1. Move gripper above coffee button
    #  2. Push down on coffee button
    #  3. Push harder if coffee button is starting to move
    # First move the gripper above the coffee button.
    # If the robot's gripper is not vertically aligned with the coffee button as
    # seen from above, we need to start by moving the gripper there.
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.move("gripper above coffee button")
    # Once we're lined up, we should be able to push the coffee button down.
    # Because the robot's gripper is at an angle, push from in front rather than
    # from above.
    if check("the robot's gripper is vertically aligned with coffee button and the robot's gripper is vertically aligned with coffee button as seen from in front"):
        robot.push("down on coffee button")
    # If the coffee button is not flat, it is starting to go down, so push
    # harder.
    if check("the coffee button is not flat"):
        robot.push("coffee button down harder")

# push-green: slide the green puck to the target location
def push_green(robot):
    # Steps:
    #  1. Put gripper above green puck
    #  2. Push gripper into top of green puck
    #  3. Slide green puck to goal
    # The robot can slide the green puck by trapping it by pushing down on it
    # from above and moving the gripper.
    # If the green puck isn't below the gripper as seen from above, move the
    # gripper above the green puck.
    if check("the robot's gripper is not above green puck and the robot's gripper is not vertically aligned with the green puck"):
        robot.put("the gripper above the green puck")
    # If the gripper is aligned with the green puck but not near it, move the
    # gripper down to the green puck to slide it.
    if check("the robot's gripper is vertically aligned with the green puck and the robot's gripper is not near green puck"):
        robot.push("the gripper into the green puck")
    # If the gripper is near the green puck, we've