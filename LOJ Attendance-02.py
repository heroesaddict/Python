from tkinter import * 

class LE(Frame): 
 def __init__(self, master, text): 
     Frame.__init__(self, master) 
     self.label = Label(self, text=text, font=("Courier New", 10)) 
     self.label.pack(side=LEFT) 
     self.entry = Entry(self) 
     self.entry.pack(side=LEFT) 

class LE2(Frame): 
 def __init__(self, master, text): 
     Frame.__init__(self, master) 
     self.label = Label(self, text=text, font=("Courier New", 10)) 
     self.label.pack(side=LEFT) 
     self.entry = Entry(self) 
     self.entry.pack(side=LEFT) 
     self.pack() 

class Win1(Frame): 
 def __init__(self, master=None): 
     Frame.__init__(self, master) 
     LE(self, 'name:Win1').pack() 
     LE(self, ' age:').pack() 
     self.pack() 

class Win2(Frame): 
 def __init__(self, master=None): 
     Frame.__init__(self, master) 
     LE(self, 'name:Win2').pack(side=LEFT) 
     LE(self, ' age:').pack(side=LEFT) 
     self.pack() 

class Win3(Frame): 
 def __init__(self, master=None): 
     Frame.__init__(self, master) 
     LE2(self, 'name:Win3') 
     LE2(self, ' age:') 
     self.pack() 

w1 = Win1() 
w1.mainloop() 
w2 = Win2() 
w2.mainloop() 
w3 = Win3() 
w3.mainloop() 

#-- this time use root --# 
root = Tk() 
LE(root, 'name:Last').pack(side=LEFT) 
LE(root, 'age:').pack(side=LEFT) 
root.mainloop() 
