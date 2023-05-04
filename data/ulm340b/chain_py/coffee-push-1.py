
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Push mug along table
    # First, put the gripper above the mug handle so we can grab it.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # If the gripper is around the mug handle, we can probably slide the mug
    # closed by pushing on the table.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.put("gripper around mug handle")
    # If the mug is aligned with the gripper as seen from in front, we can
    # push the mug closed.
    if check("the robot's gripper is forward aligned with mug handle"):
        robot.push("mug to goal")

# coffee-pull: grab the mug and move it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Pull mug along table
    # First, put the gripper above the mug handle so we can grab it.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # If the gripper is around the mug handle, we can probably slide the mug
    # closed by pushing on the table.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.put("gripper around mug handle")
    # If the mug is aligned with the gripper as seen from in front, we can
    # push the mug closed.
    if check("the robot's gripper is forward aligned with mug handle"):
        robot.push("mug to goal")

# coffee-press: press the button on the coffee machine
def coffee_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the