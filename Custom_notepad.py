import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
#global __thisTextArea 



  
class Notepad: 
  
  
    __root = Tk()
    __root.resizable(bool(0),bool(0))
    __img=PhotoImage(file='el.png')
    __root.attributes('-alpha',0.6)
    #__root.config(bg='black')
    __thisWidth = 300
    __thisHeight = 300
    __lb=Label(__root,bg='black',image=__img).place(x=0,y=0)
    __thisTextArea = Text(__root,font=('Comic Sans Ms',11,'bold'),width=70,height=30,fg='#2abfc6',bd=0,bg='black',insertbackground='#2abfc6',highlightbackground='#2abfc6',highlightthickness=2,highlightcolor='#2abfc6')
    __thisTextArea.insert(END,'Version: 1.01\nAuthor: HAkUx')
    __thisMenuBar = Menu(__root,background='black', fg='#2abfc6',relief='flat') 
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0,fg='#2abfc6',background='black') 
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0,fg='#2abfc6',background='black') 
    __lb2=Label(__root,bg='black',fg='#2abfc6',font=('Comic Sans Ms',13,'bold'),text='Custom notepad',highlightbackground='#2abfc6',highlightthickness=2,highlightcolor='#2abfc6').place(x=50,y=10)
    #__thisHelpMenu = Menu(__thisMenuBar, tearoff=0,)     
    __thisScrollBar = Scrollbar(__thisTextArea)      
    __file = None
    
    
    '''
    def on_click(e):
        global __thisTextArea 
        __thisTextArea.delete(0,END) 
    
    __thisTextArea.bind('<Button-1>',on_click)
    '''
    
    
    def __init__(self,**kwargs):
  
        
        try: 
                self.__root.wm_iconbitmap("icon2.ico")  
        except: 
                pass      
  
  
  
        try: 
            self.__thisWidth = kwargs['width'] 
        except KeyError: 
            pass
  
  
  
        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass
  
  
        
        self.__root.title("Untitled - Notepad")
  
        
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
      
        
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))  
        
        #self.__root.config(bg='black')
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1) 
  
        
        self.__thisTextArea.place(x=50,y=50) 
          
        
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)     
          
        
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile) 
          
        
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)     
  
        
        #self.__thisFileMenu.add_separator()                                          
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu)      
          
        
        self.__thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut)              
      
        
        self.__thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy)          
          
        
        self.__thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)          
          
        
        self.__thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.__thisEditMenu)      


        
          
        '''
        self.__thisHelpMenu.add_command(label="About Notepad", 
                                        command=self.__showAbout)  
        
        self.__thisMenuBar.add_cascade(label="Help", 
                                       menu=self.__thisHelpMenu) 
        '''



  
        self.__root.config(menu=self.__thisMenuBar) 
  
        #self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
          
        
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)      
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
    
    
      
          
    def __quitApplication(self): 
        for i in self.__root.winfo_children():
            i.destroy() 
        self.__root.destroy()
  
    
    '''
    def __showAbout(self): 
        showinfo("Notepad","Mrinal Verma") 
    '''
    
    
    def __openFile(self): 
          
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 
  
        if self.__file == "": 
              
            
            self.__file = None
        else: 
              
            
            
            self.__root.title(os.path.basename(self.__file) + " - Notepad") 
            self.__thisTextArea.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.__thisTextArea.insert(1.0,file.read()) 
  
            file.close() 
  
          
    def __newFile(self): 
        self.__root.title("Untitled - Notepad") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END) 
  
  
    def __saveFile(self): 
  
        if self.__file == None: 
            
            self.__file = asksaveasfilename(initialfile='filename.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 
  
  
  
  
    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>") 
  
    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>") 
  
    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>") 
  
    def run(self):        
        self.__root.mainloop() 
  
  
  
notepad = Notepad(width=1280,height=743)
notepad.run() 