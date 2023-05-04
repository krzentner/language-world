
"""
import pandas as pd

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the faucet handle
    #  3. Turn faucet left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("the gripper above the faucet handle")
    # If the faucet handle is not forward aligned with the robot's gripper,
    # move the robot's gripper to be aligned with the faucet handle
    if check("the robot's gripper is not forward aligned with the faucet handle"):
        robot.put("the gripper around the faucet handle")
    # If the robot's gripper is around the faucet handle, turn the faucet handle left.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("the faucet handle left")[eod] [code]"""Module for building the API routes for the flask application"""
from flask import Blueprint, request
from models.base_model import BaseModel
from models.user import UserModel
from models.item import ItemModel
from models.bid import BidModel

blueprint = Blueprint("api", __name__)


#############################
# GET requests
#############################
# Get all of one type
@blueprint.route("/api/<resource>", methods=["GET"])
def get_all(resource):
    if resource == "users":
        return [user.json() for user in UserModel.query.all()]
    elif resource == "items":
        return [item.json() for item in ItemModel.query.all()]
    elif resource == "bids":
        return [bid.json() for bid in BidModel.query.all()]
    # For other resources that don't yet exist
    return "404"


# Get a specific item
@blueprint.route("/api/<resource>/<id>", methods=["GET"])
def get_single(resource, id):
    if resource == "users":
        # This is how to return a 404 response
        # -> flask will handle it and generate HTML automatically
        return UserModel.query.get(int(id)).json()
    elif resource == "items":
        return ItemModel.query.get(int(id)).json()
