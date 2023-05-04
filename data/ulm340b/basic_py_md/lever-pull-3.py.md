

and follow the examples above.

Use the [function names](function_names.txt), [check templates](check_templates.txt) and [command templates](command_templates.txt) I provide to you.

Your function should have `three` if statements.

I'll demonstrate running the code that you write:
```
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.put("gripper around lever")
    if check("the robot's gripper is around lever"):
        robot.pull("lever up")

if __name__ == "__main__":
    tasks = [task for task in globals().keys() if task.startswith('lever_pull')]
    print([task for task in tasks if check(globals()[task])])

# lever_pull
```

If you make the correct program, you will see `lever_pull` printed. If you don't see that message then you should try to understand why your program failed. I won't judge the details of your program, just whether it is successful or not.

Please note that I do not guarantee that I will follow this procedure when I check your program. I might make the program interact with the robot in an arbitrary fashion.

Good luck!
''',
'seed_task_3_2': '''
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's