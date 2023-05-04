

(Hint: The task `faucet-open`, which is the opposite of `faucet-close`, looks like this:

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not vertically aligned with faucet and faucet is below the robot's gripper"):
        robot.place("gripper above faucet")
    if check("the robot's gripper is vertically aligned with faucet and faucet is below the robot's gripper"):
        robot.grab("faucet")
    if check("the robot's gripper is vertically aligned with faucet"):
        robot.turn("faucet to the left")
```
)

**Do you have any questions?** [Yes](dialog:training/tasks/task008_faucet_close_yesno_0) | [No](dialog:training/tasks/task008_faucet_close_yesno_1)

## [Task009](https://github.com/chris-chris/Elicit-Response/blob/main/src/tasks/task009_faucet_open.yml) faucet-open

* * * * *

### Script

The task: `faucet-open`

Description: `turn the faucet left`

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not vertically aligned with faucet and faucet is below the robot's gripper"):
        robot.place("gripper above faucet")
    if check("the robot's gripper is vertically aligned with faucet and faucet is below the robot's gripper"):
        robot.grab("faucet")
    if check("the robot's gripper is vertically aligned with faucet"):
        robot.turn("faucet to the left")
```

**Do you have any questions?** [Yes](dialog:training/tasks/task009_faucet_open_yesno_0) | [No](dialog:training/tasks/task009_faucet_open_yesno_1)

## [Task010](https://github.com/chris-chris/Elicit-Response/blob/main/src/tasks/task010_door_open.yml) door-open

* * * * *

### Script

The task: `door-open`

Description: `pull the door open`

```
# door-open: pull the door open
def door_open(robot):
  