

and then write a sequence of `if`/`check` statements to perform this task. For example, an early step should be `if check("the robot's gripper is not above the puck"): robot.put("gripper above the puck")`. After you are finished, press the button below and write in the answer field the sequence of commands you wrote for this task.
'''

task2_solution = """
# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and the robot's gripper is not in front of wall"):
        robot.slide("the puck to the goal")
    if check("the robot's gripper is in front of wall"):
        robot.drop("the puck near the goal")
    if check("the robot's gripper is not above the puck"):
        robot.grab("the puck")
    if check("the robot's gripper is above the puck"):
        robot.place("the puck at the goal")
"""

task3_desc = '''
## Task 3
In [this paper](http://arxiv.org/abs/1502.05705), we showed that people can write the above robot code very efficiently,
as if the code had been written before. One reason may be because human beings can describe tasks in language and we can reuse such descriptions to write the code. Here's an example of a task description that we showed people before they wrote the above code:

```
The goal of the robot is to grab the peg and insert it into the hole from the side.

First, put the gripper above the peg.

Next, if the peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, then grab the peg.

Next, if the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole,
then align peg to hole.

Next, if peg is horizontally aligned with hole, then insert peg into hole.
```

We found that showing people descriptions of the goal of each task, like the one above, helped them to write code more efficiently.

Here'