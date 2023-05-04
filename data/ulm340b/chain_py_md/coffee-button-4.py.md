

For reference, here is a list of the things that the robot can do:

```
    Robot object methods:
        robot.move(where): moves the robot's gripper to <where>
        robot.place(where): places the robot's gripper at <where>
        robot.put(where): puts the robot's gripper at <where>
        robot.grab(what): grabs <what>
        robot.drop(what): drops <what>
        robot.push(what): pushes <what>
        robot.pull(what): pulls <what>
        robot.insert(what): inserts <what>
        robot.slide(what): slides <what>
        robot.close(what): closes <what>
        robot.open(what): opens <what>
        robot.align(what): aligns <what>
        robot.around(what): arounds <what>
        robot.near(what): nears <what>
        robot.on(what): ons <what>
        robot.above(what): aboves <what>
        robot.vertically-aligned(what): vertically-aligns <what>
        robot.forward-aligned(what): forward-aligns <what>
        robot.horizontally-aligned(what): horizontally-aligns <what>
        robot.vertically-aligned(what): vertically-aligns <what>

    True/false conditions:
        robot.gripper.is-open: True if the gripper is open
        robot.gripper.is-closed: True if the gripper is closed
        robot.gripper.is-holding: True if the gripper is holding something
        robot.gripper.is-touching: True if the gripper is touching something
        robot.gripper.is-above: True if the gripper is above something
        robot.gripper.is-below: True if the gripper is below something
        robot.gripper.is-near: True if the gripper is near something
        robot.gripper.is-forward-aligned: True if the gripper is forward aligned with something
        robot.gripper.is-horizontally-aligned: True if the gripper is horizontally aligned with something
        robot.gripper.is-vertically-aligned: True if the gripper is vertically aligned with something
        robot.gripper.is-on-top-of: True if the gripper is on top of something
        robot.gripper.is-on-bottom-of: True if the gripper is on bottom of something
        robot.gripper.is-on-left-side-of: True if the gripper is on