
    # Steps:
    #  1. Put gripper near wrench
    #  2. Close gripper around the wrench
    #  3. Wrap the wrench around the peg
    # First, put the gripper near the wrench.
    if check("the robot's gripper is not near the wrench"):
        robot.move_gripper("near the wrench")
    # Once the gripper is near the wrench, just close it.
    # We'll assume it'll find the wrench that way, though it might not.
    # TODO: Find the wrench automatically.
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # If the gripper has the wrench, pull it around the peg.
    if check("the robot's gripper is vertically aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")
[eod] [code]import sys
import pygame
import random
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(settings, screen, stats, ship, aliens, bullets, sb):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.