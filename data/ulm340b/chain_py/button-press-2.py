
    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push on the button from the front
    # This is the same as button press topdown, except from the front, because
    # there's no "topdown" in the task name.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move("gripper in front of button")
    # Now that the gripper is lined up, just push on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper below the door handle
    #  2. Put gripper roughly around the door handle
    #  3. Push the door closed
    # First, put the gripper below the door handle as seen from the side.
    if check("the robot's gripper is not vertically aligned with door handle and the robot's gripper is not below the door handle"):
        robot.move("gripper below door handle")
    # Once the gripper is lined up with the door handle, we should be able to
    # grab the door handle by moving the gripper to it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not near door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can just push the door
    # closed.
    if check("the robot's gripper is near door handle"):
        robot.push("door closed")

# pick-place-side: pick up the puck and hold it at the target location
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
