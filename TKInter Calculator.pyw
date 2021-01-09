# IMPORTATIONS
import tkinter as tk
import parser

# ROOT
root = tk.Tk()
root.title("Calculator")
root.configure(background = 'silver')

# VARIABLES
px = 16
py = 16
bx = 10
h1 = 2
w1 = 2
c1 = "light green"
c2 = "gold"
c3 = "light blue"

# DEFINITIONS
def get_operations(operator):
    display.insert('end', operator)

def clear_all():
    display.delete(0, 'end')

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[ : -1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def calculate2(event=None):
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def clear_all2(event=None):
    display.delete(0, 'end')

# Root Binds
root.bind('<Return>', calculate2)
root.bind('<Delete>', clear_all2)
        
# TOPFRAME
topframe = tk.Frame(root)
topframe.pack(side='top')

# Display
display = tk.Entry(topframe, bd=40, bg="black", fg="white", width=30, font=30)
display.pack(side='top')

# FRAME1
frame1 = tk.Frame(root)
frame1.pack(side='top')

# BUTTON FRAME 1
tk.Button(frame1, text="CA", command = lambda :clear_all(), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c3).pack(side='left')
tk.Button(frame1, text="(", command = lambda :get_operations("("), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')
tk.Button(frame1, text=")", command = lambda :get_operations(")"), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')
tk.Button(frame1, text="PI", command = lambda :get_operations("*3.141592"), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')
tk.Button(frame1, text="<-", command = lambda :undo(), padx=px, width=w1, height=h1, pady=py, bd=bx, bg=c3).pack(side='left')

# FRAME2
frame2 = tk.Frame(root)
frame2.pack(side='top')

# BUTTON FRAME 2
tk.Button(frame2, text="7", command = lambda :get_operations(7), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame2, text="8", command = lambda :get_operations(8), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame2, text="9", command = lambda :get_operations(9), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame2, text="*", command = lambda :get_operations("*"), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')
tk.Button(frame2, text="/", command = lambda :get_operations("/"), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')

# FRAME3
frame3 = tk.Frame(root)
frame3.pack(side='top')

# BUTTON FRAME 3
tk.Button(frame3, text="4", command = lambda :get_operations(4), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame3, text="5", command = lambda :get_operations(5), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame3, text="6", command = lambda :get_operations(6), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame3, text="+", command = lambda :get_operations("+"), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')
tk.Button(frame3, text="-", command = lambda :get_operations("-"), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')

# FRAME4
frame4 = tk.Frame(root)
frame4.pack(side='top')

# BUTTON FRAME 4
tk.Button(frame4, text="1", command = lambda :get_operations(1), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame4, text="2", command = lambda :get_operations(2), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame4, text="3", command = lambda :get_operations(3), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame4, text="Sq", command = lambda :get_operations("**2"), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')
tk.Button(frame4, text="SqR", command = lambda :get_operations("**(1/2)"), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c2).pack(side='left')

# FRAME5
frame5 = tk.Frame(root)
frame5.pack(side='top')

# BUTTON FRAME 5
tk.Button(frame5, text=".", command = lambda :get_operations("."), width=w1, height=h1, padx=px, pady=py, bd=bx, bg=c3).pack(side='left')
tk.Button(frame5, text="0", command = lambda :get_operations(0), width=12, height=h1, padx=px, pady=py, bd=bx, bg=c1).pack(side='left')
tk.Button(frame5, text="=", command = lambda :calculate(), width=12, height=h1, padx=px, pady=py, bd=bx, bg=c3).pack(side='left')

root.mainloop()                            
