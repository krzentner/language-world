```
# push-back: slide the puck backwards to the target location
# def push_back(robot):
    # Steps:
    # 1. Put gripper above the puck
    # 2. Push gripper into the puck
    # 3. Move gripper and puck backwards to the target
    # The robot will slide the puck backwards by trapping it with its gripper and
    # moving the gripper and puck backwards.
    # If the puck is not vertically aligned with the gripper, move the gripper
    # above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above the puck")
    # If the gripper is not around the puck, move the gripper down and around
    # the puck.
    if check("the robot's gripper is not around the puck"):
        robot.drop("gripper around the puck")
    # If the gripper is around the puck, move the gripper and puck backwards
    # towards the target.
    if check("the robot's gripper is around the puck"):
        robot.push_back("the gripper and puck towards the target")