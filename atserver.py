
import socket
import threading
import SocketServer
from athandle import *
from atdb import *


class ATMyHandle(ATHandle):

    def  __init__(self, request):
        self.request = request
        self.db = ATDB("chafer")
        self.regdevs = {}
        self.commdevs = {}

    def do_at_s_reg_set(self, params):
        """P1-SIM, P2-Device ID, P2-Battery Voltage, P3-GPRS Signal Value, P4-DateTime"""
        self.regdevs[params[0]] = params
        comm_id = params[0]
        if self.commdevs.has_key(comm_id):
            self.request
        pass

    def do_at_s_unreg_set(self, params):
        print params
        pass

    def do__s_pant_notify(self, params):
        print params
        pass

    def do__s_warn_notify(self, params):
        print params
        pass

class ATServerRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        _data = self.request.recv(1024)
        print _data
        a = ATMyHandle(self.request)
        print a.execute(_data)

class ATServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 9009

    server = ATServer((HOST, PORT), ATServerRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    import time
    while(1):
        time.sleep(1000)

    server.shutdown()