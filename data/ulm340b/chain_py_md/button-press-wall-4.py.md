


# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Line up the robot's gripper with the button as viewed from the front
    #  2. Push forward against the button
    # This time the button is behind a wall, so we have to approach it from
    # the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper in front of button")
    # Once the gripper is aligned, just push.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("into button")
[eod] [code]import os
import csv

base_path = '/Users/andrewliu/Desktop/test_folder/'


def create_dir(dir_name):
    base_path = '/Users/andrewliu/Desktop/test_folder/'
    dir_path = os.path.join(base_path, dir_name)
    os.mkdir(dir_path)

def get_files(path):
    file_names = os.listdir(path)
    return file_names


def csv_to_list(file_path):
    file_name = os.path.basename(file_path)
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader) #skip csv header
        print(next(reader)[0])

def main():
    create_dir('test_folder')
    file_names = get_files(base_path)
    for file_name in file_names:
        file_path = os.path.join(base_path, file_name)
        # csv_to_list(file_path)
        print(file_name)
        pass
        # for item in file_name:
        #     file_name = '/Users/andrewliu/Desktop/{}'.format(item)
        #     print(item)

if __name__ == '__main__':
    main()

[eod] [code]import sys
import time
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ''
port = 12345

server.bind((ip