

Then add your code in the following box. 

If you want to check what's in the clipboard, you can just type `print(robot.read())` to print it.

If you make a mistake, just press undo.

Please write a program to perform the last task, `handle-press`.
Begin with the text:

```
# handle-press: push down the handle
def handle_press(robot):
```

Then add your code in the following box. 

If you want to check what's in the clipboard, you can just type `print(robot.read())` to print it.

If you make a mistake, just press undo.

```
# handle-press: push down the handle
def handle_press(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```
[eod] [code]from pymongo import MongoClient
from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import config


def connect(server, database_name):
    try:
        client = MongoClient(server)
        client.server_info()
        collection = client[database_name]
        print("Connected to database!")
        return collection
    except:
        sys.exit(1)


def get_collection(collection_name):
    return connect(config.SERVER, config.DATABASE)[collection_name]


def insert_to_database(collection_name, new_article_title, new_article_url):
    collection = get_collection(collection_name)
    if collection.find_one({"_id": new_article_url}) == None:
        collection.insert_one({
            "_id": new_article_url,
            "url": new_article_url,
            "title": new_article_title
        })


def get_from_database(collection_name, article_url):
    return get_collection(collection_name).find_one({"_id": article_url})[eod] [code]from math import gcd, modf, ceil, sqrt
from random import randint


# Returns the gcd of two natural numbers (or Zero)
def natural_gcd(num1: int, num2: int) -> int:
    if not