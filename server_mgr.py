import paths as PATH
import subprocess

class ServerMgr(object):
    '''This class managers the jade server process.  It starts the server, stops
    it, and can report whether or not it is still running.
    '''
    def __init__(self, logging_function):
        self.log = logging_function
        self.proc = None
        
    def start_server(self):
        if self.proc == None:
            self.log("Starting web server")
            self.proc = subprocess.Popen(["python", PATH.JADE_SERVER_MODULE])
        else:
            self.log("Web server should already be started")
            
    def log_status(self):
        if self.proc == None:
            self.log("Server not started")
        else:
            self.log("Not sure what's going on TODO")
        
    def stop_server(self):
        if self.proc != None:
            try: self.log("Shutting down server")
            except: pass
            
            self.proc.kill()
            self.proc = None
        else:
            try: self.log("Server is already down")
            except: pass
