from tkinter import *

# 🎨 رنگ‌ها و فونت
BG_COLOR = "#2c3e50"
FG_COLOR = "#ecf0f1"
BTN_COLOR = "#1abc9c"
DEL_COLOR = "#e74c3c"
FONT = ("Vazirmatn", 12)

# 🪟 پنجره اصلی
root = Tk()
root.title("📝 لیست کارهای زیزی")
root.geometry("450x550")
root.config(bg=BG_COLOR)

# 🧠 لیست کارها: [(task_text, category)]
tasks = []

# 🎯 توابع
def update_listbox():
    listbox.delete(0, END)
    for task, category in tasks:
        listbox.insert(END, f"{task} 📁 ({category})")

def add_task():
    task = entry.get().strip()
    category = selected_category.get()
    if task:
        tasks.append((task, category))
        update_listbox()
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()

def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as f:
        for task, category in tasks:
            f.write(f"{task}|{category}\n")

def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                if "|" in line:
                    task, category = line.strip().split("|")
                    tasks.append((task, category))
        update_listbox()
    except FileNotFoundError:
        pass

# 📦 ورودی تسک
entry = Entry(root, width=30, font=FONT)
entry.pack(pady=10)

# 📂 انتخاب دسته‌بندی
categories = ["کاری", "شخصی", "خرید", "مطالعه"]
selected_category = StringVar()
selected_category.set(categories[0])
category_menu = OptionMenu(root, selected_category, *categories)
category_menu.config(font=FONT, bg="#34495e", fg="white")
category_menu.pack(pady=5)

# 🧷 دکمه‌ها
btn_add = Button(root, text="➕ اضافه کردن", bg=BTN_COLOR, fg="white", font=FONT, command=add_task)
btn_add.pack(pady=5)

btn_delete = Button(root, text="🗑️ حذف", bg=DEL_COLOR, fg="white", font=FONT, command=delete_task)
btn_delete.pack(pady=5)

btn_save = Button(root, text="💾 ذخیره", bg="#3498db", fg="white", font=FONT, command=save_tasks)
btn_save.pack(pady=5)

# 📋 لیست تسک‌ها
listbox = Listbox(root, width=40, height=15, font=FONT, bg=FG_COLOR, fg="black", selectbackground="#95a5a6")
listbox.pack(pady=20)

# 📥 بارگذاری قبلی
load_tasks()

root.mainloop()
