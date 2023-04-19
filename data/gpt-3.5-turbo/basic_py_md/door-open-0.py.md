# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open") 

# Note: The code assumes that there is a function called `check` that returns `True` if the given condition is satisfied and `False` otherwise. Additionally, the robot methods `reach`, `put`, `push`, `slide`, `place`, `drop`, `close`, `grab`, `align`, `insert`, `move`, and `pull` are used to control the gripper. These methods are not defined here and should be replaced with appropriate calls to the actual robot's API.