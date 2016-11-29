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
        self.log("Starting web server")
        cmd = "python " + PATH.JADE_SERVER_MODULE
        subprocess.run("python", PATH.JADE_SERVER_MODULE)
        
        pass

    def stop_server(self):
        pass
    
