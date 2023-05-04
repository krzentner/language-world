

Once you start typing, the editor will provide code completion for
valid actions like `robot.move("left")`.
If you need more guidance, please ask a human for help.









# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer closed")





# 27.3 DRAWER CLOSE
#   - drawer-close: push the drawer close
#
#   - Please complete the function `drawer_close` by adding the correct commands
#
#     - You should follow a similar flow as `drawer-open` which was provided

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Push the drawer closed
    #  4. Open gripper to release drawer handle
    #  5. Slide gripper upwards above the drawer handle
    if check("the robot's gripper is not vertically aligned with drawer handle and the robot's gripper is open"):
        robot.place("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is open"):
        robot.close("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer closed")
    if check("the robot's gripper is around drawer handle"):
        robot.open("gripper")
    if check("the robot's gripper is not around drawer handle"):
        robot.slide("gripper upwards above drawer handle")
    return "done"


# 33.3 DRAWER CLOSE
#   - drawer-close: push the drawer close
#
#   - Please complete the function `drawer_close` by adding the correct commands
#
#     - You should follow a similar flow as `drawer-open` which was provided

# drawer-close: push the drawer close
