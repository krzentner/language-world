# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    # 1. Move the gripper to the left side of the lever
    # 2. Grab the lever handle from above
    # 3. Rotate the lever up
    # First, align the gripper to the left of the lever
    if check("the robot's gripper is not left of the lever handle"):
        robot.move("gripper left of lever handle")
    # Once aligned, grab the lever handle from above
    if check("the robot's gripper is left of the lever handle and the robot's gripper is not above the lever handle"):
        robot.put("gripper over lever handle")
        robot.grab("lever handle")
    # Once the gripper has grabbed the lever handle, start rotating the lever up.
    if check("the robot's gripper is holding the lever handle"):
        robot.push("lever handle up")