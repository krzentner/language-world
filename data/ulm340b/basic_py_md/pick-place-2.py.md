

You will need to use `robot.grab("puck")` and `robot.put("the puck at the goal")`.

---

{
    "metadata": {
        "name": "robot-pick-place",
        "description": "demonstrate the ability to follow directions from a simple instruction manual to program the movement of a robot arm"
    },
    "type": "off-policy",
    "input": "text",
    "context": "text",
    "add_special_tokens": ["<s>"],
    "add_start_token": "<s>",
    "max_tokens": 250,
    "num_samples": 1
}

(add_special_tokens="<s>" means the input will have a special start token "<s>" prepended to it)
(add_start_token="" means the desired output has no prefix)



<details>
<summary>Task-specific Input</summary>
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")

# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper