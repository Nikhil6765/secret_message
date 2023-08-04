from tkinter import messagebox,simpledialog,Tk

def get_task():
    task=simpledialog.askstring('Task', 'Do you want to encrypt or decrypt')
    return task


def get_message():
    message=