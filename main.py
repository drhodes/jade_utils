import tkinter as tk
from common import Common

def hello(): print("Hello")
    
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        #
        self.text_box = None
        self.config_text_box()

        self.common = Common(self.logger)
        self.create_widgets()
        self.welcome()

    def welcome(self):
        '''This utility aims to help people to use JADE on their desktops
        using a local webserver.  It can find the JADE data in users' browser
        local storage, make backups of it, and 
        '''
        
        self.logger("-------------------------------------------------------")
        self.logger("This is a helper utility for dealing with 6.004x JADE")
        self.logger("")
        self.logger("this window doesn't accept input, but it will tell you")
        self.logger("what's going on under the hood.")
        
    def logger(self, s):
        print(s)
        self.text_box.see(tk.END)
        self.text_box.update_idletasks()
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, " " + s + "\n")
        self.text_box.config(state=tk.DISABLED)
        self.text_box.see(tk.END)
        self.text_box.update_idletasks()
        
    def create_widgets(self):
        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="import jade from edx", command=hello)
        filemenu.add_command(label="import jade from local", command=hello)
        filemenu.add_command(label="export jade to edx", command=hello)
        filemenu.add_command(label="export jade to local", command=hello)
        
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        jademenu = tk.Menu(menubar, tearoff=0)
        jademenu.add_command(label="download and setup JADE",
                             command=self.common.setup_local_jade)
        
        jademenu.add_command(label="start JADE webserver",
                             command=self.common.start_server)

        infomenu = tk.Menu(menubar, tearoff=0)
        infomenu.add_command(label="show JADE paths", command=self.common.show_paths)
        infomenu.add_command(label="thank staff", command=self.thank_staff)
        
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="JADE", menu=jademenu)
        menubar.add_cascade(label="info", menu=infomenu)
        
        self.master.title("JADE Utils")
        self.master.config(menu=menubar)

    def config_text_box(self):
        self.text_box = tk.Text(self.master)
        self.text_box.pack(side="top", fill=tk.BOTH, expand=1)
        
    def thank_staff(self):
        msg = [ " _   _                 _              _         __  __ _ ",
                "| |_| |__   __ _ _ __ | | _____   ___| |_ __ _ / _|/ _| |",
                "| __| '_ \ / _` | '_ \| |/ / __| / __| __/ _` | |_| |_| |",
                "| |_| | | | (_| | | | |   <\__ \ \__ \ || (_| |  _|  _|_|",
                " \__|_| |_|\__,_|_| |_|_|\_\___/ |___/\__\__,_|_| |_| (_)"]
        for m in msg: self.logger(m)


        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
