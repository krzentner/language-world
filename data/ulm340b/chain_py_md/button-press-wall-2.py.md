

and fill in code to complete it.
'''

if check("gripper vertically aligned with button"):
    robot.move("gripper to left of button")
elif check("gripper forward aligned with button"):
    robot.push("button")
elif check("gripper horizontally aligned with button"):
    robot.push("button")
[eod] [code]# 1.10

for i in range(0, 5):
    for j in range(0, 3):
        print(i, j)[eod] [code]'''
Created on 31 янв. 2018 г.

@author: user
'''
from flask import Flask,jsonify
from flask_restful import reqparse,abort, Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World'

class User(Resource):
    def get(self):
        return jsonify({'users':[{'id': 1, 'name': 'user1'},
                                  {'id': 2, 'name': 'user2'}]})

api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)
    [eod] [code]"""
https://leetcode.com/problems/linked-list-cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1, p2 = head, head

        while p1 != None and p1.next != None and p2 != None:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True

        return False
[eod] [code]def xor(a, b):
    while len(a) < len(b):
        a += b[0]
    while len(a) > len(b):
        b += a[0]
    a = [x for x in a]
    b = [y for