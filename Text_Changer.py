import tkinter as tk

def SetTextColor(l1,color):
    l1.config(fg=color)

def SetBgColor(widget, color):
    widget.config(bg=color)

def main():
    root=tk.Tk()
    root.geometry("400x400")
    l1=tk.Label(root,text="Change my color ",font=('Arial',20))
    # b1=tk.Button(root,text="RED",command=lambda:SetTextColor(l1,'red'))
    # b2=tk.Button(root,text="BLUE",command=lambda:SetTextColor(l1,'blue'))
    # b3=tk.Button(root,text="BLACK",command=lambda:SetTextColor(l1,'black'))
    b4 = tk.Button(root, text="YELLOW BG", command=lambda: SetBgColor(l1, 'yellow'))
    b5 = tk.Button(root, text="GREEN BG", command=lambda: SetBgColor(l1, 'lightgreen'))
    b6 = tk.Button(root, text="GRAY BG", command=lambda: SetBgColor(l1, 'lightgray'))

    l1.pack(pady=10)

    b4.pack()
    b5.pack()
    b6.pack()
    root.mainloop()

if __name__=='__main__':
    main()