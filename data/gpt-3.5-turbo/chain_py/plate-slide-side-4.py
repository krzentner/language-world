# Steps:
    #  1. Line up gripper with plate from above
    #  2. Push gripper down onto plate from above
    #  3. Slide gripper and plate sideways to target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Once the gripper is lined up, push down on the plate from above.
    if check("the robot's gripper is vertically aligned with the plate"):
        robot.push("down on plate from above")
    # Once the gripper and plate are in contact and still mostly lined up,
    # slide it sideways to the target location.
    if check("the gripper and plate are aligned and in contact, and not at the target location"):
        robot.slide("the gripper and plate to the target location")