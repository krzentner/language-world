
"""

instruction = "shelf-place: pick up the block and place it at the target location"
func_name = instruction.split(':')[0].strip()

inputs = []
variables = []

inputs.append("the robot's gripper is not above the block")
inputs.append("the robot's gripper is above the block and the robot's gripper is not around the block")
inputs.append("the robot's gripper is around the block and the robot's gripper is open")
inputs.append("the robot's gripper is not near the block and the robot's gripper is closed")
inputs.append("the robot's gripper is near the block and the robot's gripper is open")
inputs.append("the robot's gripper is around the block and the robot's gripper is closed")
inputs.append("the robot's gripper is not near goal")

variables.append(inputs[0].replace("is not", "is").replace("is", ""))
variables.append(inputs[0].replace("is not", "").replace("is", "").replace("the ", "").replace(" above the ", "-above-").replace(" block", ""))
variables.append(inputs[1].replace("is not", "").replace("is", "").replace("the ", "").replace(" above the ", "-above-").replace(" block", ""))
variables.append(inputs[2].replace("is not", "").replace("is", "").replace("the ", "").replace(" around the ", "-around-").replace(" block", ""))
variables.append(inputs[3].replace("is not", "").replace("is", "").replace("the ", "").replace(" near the ", "-near-").replace(" block", ""))
variables.append(inputs[4].replace("is not", "").replace("is", "").replace("the ", "").replace(" around the ", "-around-").replace(" block", ""))
variables.append(inputs[5].replace("is not", "").replace("is", "").replace("the ", "").replace(" near ", "-near-").replace(" goal", ""))

# print(inputs)
# print(variables)
# 661910
for i in range(len(inputs)):
    print(inputs[i], variables[i], file=open("input.txt", "a", encoding="utf-8"))
[eod] [code]# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:0