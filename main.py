from tkinter import messagebox,simpledialog,Tk

def get_task():
    task=simpledialog.askstring('Task', 'Do you want to encrypt or decrypt')
    return task


def get_message():
    message=simpledialog.askstring('Message','Enter the secret message: ')
    return message

root=Tk()

while True:
    task=get_task()
    if task=='encrypt':
        message=get_message()
        messagebox.showinfo('Message to encrypt is: ',message)
    
    elif task=='decrypt':
        message=get_message()
        messagebox.showinfo('Message to decrypt is: ',message)

    else:
        break
