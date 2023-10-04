from  tkinter import * 
import tkinter.messagebox
def entertask():
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4,bg='lightblue')
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command=add,bg='lightgreen')
    button_temp.pack()
    root1.mainloop()
def deletetask():
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])

window=Tk()
window.geometry('500x450+500+300')
window.title("TO DO LIST")

frame_task=Frame(window)
frame_task.pack()

listbox_task=Listbox(frame_task,bg="lightblue",fg="black",height=15,width=50)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)
 
entry_button=Button(window,text="Add task",font=('bold',13,'italic'),command=entertask,bg='lime')
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete selected task",font=('bold',13,'italic'),command=deletetask,bg='orange')
delete_button.pack(pady=3)

window.mainloop()


