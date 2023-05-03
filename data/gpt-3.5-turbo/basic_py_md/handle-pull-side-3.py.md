# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with the handle and the handle is not vertically aligned with the hole"):
        robot.move("gripper above the hole")
        robot.move("gripper to side of handle")
    if check("the robot's gripper is vertically aligned with the hole and the handle is not aligned with hole"):
        robot.move("gripper to align with hole")
        robot.push("handle down into the hole")
    if check("the robot's gripper is near the hole and the handle is aligned with the hole"):
        robot.move("gripper upward")
        robot.move("gripper away from the handle")
        robot.release()