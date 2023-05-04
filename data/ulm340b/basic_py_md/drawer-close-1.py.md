

Please be sure to indent the rest of the text you write by two spaces.
The robot.put, robot.drop, robot.align, and robot.pull commands have 2 arguments.
The robot.insert, robot.slide, robot.push and robot.grab commands have 1 argument.
The robot.place, robot.move, and robot.reach commands have 2 arguments.
The robot.close command has 1 argument.


# Example output:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle and the drawer is open"):
        robot.put("the robot's gripper above the drawer handle")
    if check("the drawer is open"):
        robot.close("the drawer by pushing the drawer handle down")
```

# Additional notes:

- The `robot.put()` command has a first argument of 'gripper' and the second argument depends on the action described in the text (e.g., if it says the robot is putting the gripper above the puck, use 'above puck' as the second argument)
- The `robot.drop()` command has a first argument of 'gripper' and the second argument depends on the action described in the text (e.g., if it says the robot is dropping the gripper around the puck, use 'around puck' as the second argument)
- The `robot.grab()` command always has the first argument 'the puck', as the robot only ever grabs the puck in this dataset.
- The `robot.insert()` command has the first argument 'the peg' and the second argument depends on the action described in the text (e.g., if it says the robot is inserting the peg into the hole, use 'into hole' as the second argument)
- The `robot.slide()` command has the first argument 'the puck' and the second argument depends on the action described in the text (e.g., if it says the robot is sliding the puck to the target, use 'to target' as the second argument)
- The `robot.push()` command has a first argument of 'the gripper' and the second argument depends on the action described in the text (e.g., if it says the robot is pushing the gripper into the puck, use 'into puck' as the second argument)
- The `robot.pull()` command has a first argument of 'the gripper' and the second argument depends on the action described in the text (e.g., if it says the robot is pulling the gripper away from the drawer, use '