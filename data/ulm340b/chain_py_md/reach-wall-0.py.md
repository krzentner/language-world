

We have provided you the following code snippets that you can use in your program:

```
# Steps:
#  1. Reach towards the target
#  2. Move over the wall to reach the target
if check("the robot's gripper is not near reach target"):
    robot.reach("to goal")
```
"""

if check("the robot's gripper is not near reach target"):
    robot.reach("to goal")[eod] [code]#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import traceback
from wsgiref.simple_server import make_server
from wsgiref.simple_server import WSGIRequestHandler, WSGIServer

from . import settings
from . import helpers


class _MyWSGIRequestHandler(WSGIRequestHandler):
    def address_string(self):
        # XXX: I'm not sure if this is safe - is 'localhost' the right thing?
        # maybe _bind_address?
        return self.client_address[0]


class _MyWSGIServer(WSGIServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        WSGIServer.__init__(self, server_address, RequestHandlerClass)
        self.bind_and_activate = bind_and_activate

    def server_bind(self):
        if not self.bind_and_activate:
            return
        WSGIServer.server_bind(self)


class _MyWSGIThread(ThreadingMixIn, _MyWSGIServer):
    def serve_forever(self, poll_interval=0.5):
        """Start a thread with the server -- the thread calls serve_forever()
        on the server object.
        """

        self.alive = True
        self.poll_interval = poll_interval

        def serve():
            self.serve_forever()
            self.alive = False

        self.thread = threading.Thread(target=serve)
        self.thread.setDaemon(True)
        self.thread.start()
        return self.thread

    def shutdown(self):
        """Shutdown the WSGI server -- the server and its thread should exit."""

        self.alive = False
        self.shutdown_signal = True
        return _MyWSGIServer.shutdown(self)


class WSGIServerHttpHandler(BaseHTTPRequestHandler):
    #def log_request(self, code="-", size