

You can then edit your code while testing with the buttons below.
"""

if check("the robot's gripper is not near handle"):
    robot.put("gripper above handle")

if check("the robot's gripper is vertically aligned with handle"):
    robot.pull("handle")

# the robot's gripper is vertically aligned with handle
# the handle is not below the robot's gripper

if check("the handle is below the robot's gripper"):
    robot.move("gripper around handle")

if check("the robot's gripper is forward aligned with handle"):
    robot.push("handle to the side")

# the handle is almost pressed
# the handle is almost vertically aligned with the robot's gripper

if check("the robot's gripper is above handle"):
    robot.place("gripper above handle")

# the handle is not below the robot's gripper

if check("the handle is below the robot's gripper"):
    robot.place("gripper on top of handle")

if check("the robot's gripper is vertically aligned with handle"):
    robot.slide("handle to the side")

# the handle is almost pressed
# the handle is almost vertically aligned with the robot's gripper

if check("the handle is almost pressed"):
    robot.place("gripper on top of handle")

if check("the handle is almost vertically aligned with the robot's gripper"):
    robot.push("handle to the side")
[eod] [code]class MyList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def insert(self, index, item):
        if index > len(self.items) or index < 0:
            raise IndexError("invalid index")
        else:
            self.items.insert(index, item)

    def __getitem__(self, index):
        if index > len(self.items) or index < 0:
            raise IndexError("invalid index")
        return self.items[index]

    def __len__(self):
        return len(self.items)


mylist = MyList()
mylist.add(4)
mylist.add(5)
mylist.add(6)
print(mylist)
mylist.insert(1, 'c')
print(mylist)
print(