from tkinter import *

# 🎨 تنظیم رنگ‌ها
BG_COLOR = "#2c3e50"
FG_COLOR = "#ecf0f1"
BTN_COLOR = "#1abc9c"
DEL_COLOR = "#e74c3c"
FONT = ("Vazirmatn", 12)

# 🪟 ساخت پنجره اصلی
root = Tk()
root.title("📝 لیست کارهای زیزی")
root.geometry("400x500")
root.config(bg=BG_COLOR)

# 🧠 لیست کارها
tasks = []

# 🎯 توابع اصلی
def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

def add_task():
    task = entry.get()
    if task.strip():
        tasks.append(task)
        update_listbox()
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()

def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                tasks.append(line.strip())
        update_listbox()
    except FileNotFoundError:
        pass

# 📦 UI Elements
entry = Entry(root, width=25, font=FONT)
entry.pack(pady=10)

btn_add = Button(root, text="➕ اضافه کردن", bg=BTN_COLOR, fg="white", font=FONT, command=add_task)
btn_add.pack(pady=5)

btn_delete = Button(root, text="🗑️ حذف کار انتخاب‌شده", bg=DEL_COLOR, fg="white", font=FONT, command=delete_task)
btn_delete.pack(pady=5)

btn_save = Button(root, text="💾 ذخیره در فایل", bg="#3498db", fg="white", font=FONT, command=save_tasks)
btn_save.pack(pady=5)

listbox = Listbox(root, width=35, height=15, font=FONT, bg=FG_COLOR, fg="black", selectbackground="#95a5a6")
listbox.pack(pady=20)

load_tasks()

root.mainloop()
