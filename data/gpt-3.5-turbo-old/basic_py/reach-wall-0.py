if check("the robot's gripper is not near reach target"):
        if check("there is a short wall between the robot and the reach target"):
            # move the gripper to a position above the wall
            robot.move("gripper to position above wall")
            # raise the gripper to clear the wall
            robot.lift("gripper above wall")
            # move the gripper to the target location
            robot.move("gripper to reach target")
            # lower the gripper to the target location
            robot.lower("gripper to reach target")
        else:
            # no wall in the way, simply reach to the target location
            robot.reach("to goal")