

The target is at the same location as in `pick-place`, `reach`, and `push`.

*/

# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not above the cube"):
        robot.put("the gripper above the cube")
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.put("the gripper around the cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("the gripper around the cube")
    if check("the robot's gripper is around the cube and the robot's gripper is closed"):
        robot.grab("the cube")
    if check("the robot's gripper is around the cube"):
        robot.push("the gripper forward")
    if check("the robot's gripper is forward aligned with the target"):
        robot.put("the cube on the target")


[eod] [code]def print_me_out():
    print("Hello world")

#print_me_out()

#print("Goodbye world")

def greet_someone(name):
    print("Hello " + name)

#greet_someone("James")

print("Goodbye " + "James")

def print_full_name(first_name, last_name):
    print("Hello " + first_name + " " + last_name)

print_full_name("James", "Bond")

def print_age(age):
    if age >= 18:
        print("You are old enough to drive")
    else:
        print("You are too young to drive")

age = 16
print_age(age)

age = 18
print_age(age)

def print_full_name(first_name, last_name):
    print("Hello " + first_name + " " + last_name)

full_name = print_full_name

print_full_name("James", "Bond")
full_name("Miss", "Moneypenny")[eod] [code]from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user: