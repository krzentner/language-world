
"""

def drawer_open(robot):
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.pull("drawer open")
    [eod] [code]"""
WSGI config for s_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s_app.settings")

application = get_wsgi_application()
[eod] [code]import pandas as pd
import numpy as np

def parse_csv(filename, header_names):
    df = pd.read_csv(filename, names=header_names)
    return df

def remove_null(df):
    df = df.dropna(axis=0, how='any')
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

def add_missing_attributes(df):
    df["Cylinders"] = df["Engine Size"].str[0]
    df["FuelType"] = df["Transmission"] + df["Cylinders"]
    df["MileageGroup"] = np.where(df["FuelType"] == "P", "Petrol", "Diesel")
    return df

def group_by(df, col, grp_col):
    df_grouped = df.groupby(grp_col).mean().reset_index()
    return df_grouped

def calculate_cost(df):
    df_cost = df[["Price", "Mileage"]]
    df_cost["Cost"] = df_cost["Price"]/df_cost["Mileage"]
    df_cost = df_cost.groupby("MileageGroup").mean().reset_index()
    return df_