

In writing the program, use the following actions:

 - `check(condition)`, where `condition` is a string like
   `"the robot's gripper is not vertically aligned with button"`
 - `robot.put("gripper above button")`
 - `robot.push("down on button")`
 - `robot.grab("drawer handle")`
 - `robot.pull("away from drawer")`
 - `robot.put("gripper above door handle")`
 - `robot.put("gripper around door handle")`
 - `robot.pull("door open")`
 - `robot.grab("drawer handle")`
 - `robot.push("drawer closed")`
 - `robot.put("gripper above peg")`
 - `robot.grab("peg")`
 - `robot.align("peg to hole")`
 - `robot.insert("peg into hole")`
 - `robot.move("gripper to left of window handle")`
 - `robot.slide("window right")`
 - `robot.push("window right harder")`
 - `robot.move("gripper to right of window handle")`
 - `robot.slide("window left")`
 - `robot.push("window left harder")`
 - `robot.place("gripper above puck")`
 - `robot.drop("gripper around puck")`
 - `robot.close("gripper around puck")`
 - `robot.place("puck at goal")`
 - `robot.reach("to goal")`
 - `robot.put("the gripper above the puck")`
 - `robot.push("the gripper into the puck")`
 - `robot.slide("the puck to the goal")`

To test your code, press the "Submit" button and check your score.

For a hint, press the "Hint" button.

Your program must pass all test cases to be accepted.

### Hints

 - The robot can move around the gripper to perform tasks. Use actions such
   as `robot.put("gripper above button")` to move the gripper.
 - To perform a task, you will need to perform a number of these small
   operations in the right order.
 - A simple example is pressing a button from above:
   ```
   # button-press-topdown: push the button down from above
   def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "top