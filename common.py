import os
import urllib2 as ur
import zipfile
import shutil
import threading
import paths as PATH
import server_mgr

class Common(object):
    def __init__(self, logging_function):
        self.log = logging_function
        self.server_mgr = server_mgr.ServerMgr(logging_function)
        self.download_busy = False

    def cleanup(self):
        self.server_mgr.stop_server()
        
    def show_paths(self):
        self.log("+------------------------------------------------------")
        self.log("| JADE_UTIL PATHS")
        self.log("| ")
        self.log("| " + PATH.JADE_UTIL)
        self.log("| " + PATH.JADE_ZIP)
        self.log("| " + PATH.JADE_EXTRACT)
        self.log("| " + PATH.JADE_IMPORTS)
        self.log("| " + PATH.JADE_EXPORTS)
        self.log("| " + PATH.JADE_BACKUPS)
        self.log("| ")
        
    def setup_paths(self):
        if not os.path.exists(PATH.JADE_UTIL): os.makedirs(PATH.JADE_UTIL)
        if not os.path.exists(PATH.JADE_IMPORTS): os.makedirs(PATH.JADE_IMPORTS)
        if not os.path.exists(PATH.JADE_EXPORTS): os.makedirs(PATH.JADE_EXPORTS)
        if not os.path.exists(PATH.JADE_BACKUPS): os.makedirs(PATH.JADE_BACKUPS)

    def setup_local_jade(self):
        def worker():
            self.download_busy = True
            self.setup_paths()
            self.download_jade()
            self.unzip_jade()
            self.download_busy = False
        threading.Thread(target=worker).start()
        
    def download_jade(self):
        if os.path.exists(PATH.JADE_ZIP):
            self.log("zipfile exists, skipping download")
            return
        
        self.log("Downloading: " + PATH.JADE_ZIP_URL)
        rsp = ur.urlopen(PATH.JADE_ZIP_URL)
        data = rsp.read()

        outfile = os.path.expanduser(PATH.JADE_ZIP)
        self.log("saving to: " + outfile)
        of = open(outfile, 'wb')
        of.write(data)
        of.close()
        self.log("saving done.")

    def start_server(self):
        os.chdir(PATH.JADE_SERVER_DIR)
        if self.download_busy:
            self.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.log("Jade is busy downloading environment, please wait.") 
            self.log("")
        else:             
            self.server_mgr.start_server()

    def stop_server(self):
        self.server_mgr.stop_server()

            
    def remove_old_jade(self):
        # if old jade is
        if os.path.exists(PATH.JADE_EXTRACT):
            self.log("found and old jade, removing: " + PATH.JADE_EXTRACT)
            shutil.rmtree(PATH.JADE_EXTRACT)

    def unzip_jade(self):
        # pre condition, the zip file must exist.
        self.remove_old_jade()
        self.log("decompressing jade into: " + PATH.JADE_EXTRACT)
        with zipfile.ZipFile(PATH.JADE_ZIP, 'r') as zip_ref:
            zip_ref.extractall(PATH.JADE_EXTRACT)
        self.log("decompressing done.")


        
