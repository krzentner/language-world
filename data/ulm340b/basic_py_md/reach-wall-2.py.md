

You should be able to write the code by adapting code from the other tasks.

---

## Step 2: Adapting a Program to Avoid a Wall

In this section, we will ask you to adapt a program to avoid hitting the wall.
The program can be summarized as follows:

```
# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
```

Here is some feedback on how this could be done:

```
The first thing you might do is to call the function for a previous task.  We
can see this from the following lines:

    def reach_wall(robot):
        reach(robot)
```

The second thing you might do is to handle the case when the robot hits the
wall.  We can see this from the following lines:

    def reach_wall(robot):
        if check("the robot's gripper is above wall"):
            reach(robot)
```

You could try adapting a few other examples, such as `button-press-topdown`.
However, the `reach` program is the simplest example to adapt.

---

## Step 3: Adapting a Program to Put an Object in a Box

In this section, we will ask you to adapt a program to put an object inside a
box.  The program can be summarized as follows:

```
# box-put: put the puck into the box
def box_put(robot):
```

Here is some feedback on how this could be done:

```
The first thing you might do is to call the function for a previous task.  We
can see this from the following lines:

    def box_put(robot):
        if check("the robot's gripper is below puck"):
            pick_place(robot)
```

The second thing you might do is to make sure that the puck is near the box. 
We can see this from the following lines:

    def box_put(robot):
        if check("the robot's gripper is below puck"):
            pick_place(robot)
        if check("the robot's gripper is near box"):
            drop("puck in box")
```

If the puck is not near the box, you could try to call `reach`.
However, the `reach` program is not enough to reach over the box.
We will have to find a different program to call.

---

## Step 4: Adapting a Program to Put an Object in a Box with a Wall in the Way

In this section, we will ask you to adapt a program