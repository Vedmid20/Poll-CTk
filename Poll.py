from customtkinter import *
from tkinter import *
from tkinter import ttk

root = CTk()
w = root.winfo_screenwidth() / 2 - 250
h = root.winfo_screenheight() / 2 - 175
root.geometry(f'500x350+{int(w)}+{int(h)}')
root.resizable(width=False, height=False)
root.configure(fg_color='grey20')

def forget():
    global l, rdbtn
    l.pack_forget()
    for i in root.winfo_children():
        if isinstance(i, (CTkRadioButton, CTkCheckBox, CTkComboBox, Scale, CTkTextbox, CTkEntry, CTkCanvas, Listbox, Button)):
            i.pack_forget()

def poll1Buttons(btnName):
    forget()
    if btnName == 0:
        v = -1
        root.title(f'Питання 1')
        l.configure(text='Як буде правильно')
        l.pack(pady=30)
        for i in question1:
            v += 1
            rdbtn = CTkRadioButton(root, text=f'{i}', font=('arial', 16), hover_color='lightskyblue', fg_color='lightblue', variable=langRdBtn, value=v)
            rdbtn.pack(pady=8)
        if langRdBtn.get() in trueAnswers:
            pass
        else:
            if langRdBtn.get() == 0:
                trueAnswers.append(langRdBtn.get())
            else:
                pass

    elif btnName == 1:
        v = -1
        root.title(f'Питання 2')
        l.configure(text='Коли був створений Пайтон')
        l.pack(pady=30)
        scale = Scale(root, from_=1920, to=2024, length=250, tickinterval=50, orient='horizontal', background='grey20', foreground='white', variable=langScale)
        scale.pack(pady = 15)
        if langScale.get() in trueAnswers:
            pass
        else:
            if langScale.get() == 1991:
                trueAnswers.append(langScale.get())
            else:
                pass

    elif btnName == 2:
        v = -1
        root.title(f'Питання 3')
        l.configure(text='Які координати відносяться до цієї фігури')
        l.pack(pady=30)
        c = CTkCanvas(root, width=100, height=100)
        c.create_oval((5, 5), (97,95), width=3, )
        c.pack(pady = 2)
        combbox = CTkComboBox(root, values=question3, variable=langCombobox, width=180, fg_color='white', text_color='black', button_hover_color='#C3D9F7',
                              button_color='grey60', dropdown_hover_color='#C3D9F7', dropdown_fg_color='grey50', dropdown_text_color='black', font=('arial', 18), state='readonly')
        combbox.pack(pady = 13)
        if langCombobox.get() in trueAnswers:
            pass
        else:
            if langCombobox.get() == '(5,5),(97,95)':
                trueAnswers.append(str(langCombobox.get()))
            else:
                pass

    elif btnName == 3:
        v = -1
        root.title(f'Питання 4')
        l.configure(text='Що лишнє в цьому списку')
        l.pack(pady=30)
        lst = Listbox(root, listvariable=langListBox, font=('arial', 17), height=5, selectmode=SINGLE)
        lst.pack()
        def listFunc():
            # print(lst.get(lst.curselection()))
            choice = lst.get(lst.curselection())
            if choice == 'def':
                if choice not in trueAnswers:
                    trueAnswers.append(choice)
                else:
                    pass
            else:
                pass
        if len(lst.get('0', 'end')) != 4:
            for i in question4:
                lst.insert(END, i)
        else:
            pass
        btn = Button(root, width=10, background='#C3D9F7', fg='black',
                              font=('arial', 18), borderwidth=2,  command=listFunc, text='Обрати')
        btn.pack(pady = 10)


    elif btnName == 4:
        v = -1
        root.title(f'Питання 5')
        l.configure(text='Оберіть правильні твердження')
        l.pack(pady=30)
        chbox = CTkCheckBox(root, text=f'tkinter був створений раніше пайтона', onvalue=1, offvalue=0, hover_color='#C3D9F7',
                            variable=langCheckButtons1)
        chbox.pack(anchor=CENTER, pady=10)
        chbox = CTkCheckBox(root, text=f'Пайтон динамічна мова програмування', onvalue=1, offvalue=0,
                            hover_color='#C3D9F7',
                            variable=langCheckButtons2)
        chbox.pack(anchor=CENTER, pady=10)
        chbox = CTkCheckBox(root, text=f'tkinter бібліотека для створення GUI', onvalue=1, offvalue=0,
                            hover_color='#C3D9F7',
                            variable=langCheckButtons3)
        chbox.pack(anchor=CENTER, pady=10)
        if langCheckButtons2.get() == 1 and langCheckButtons3.get() == 1 and langCheckButtons1.get() == 0:
            trueAnswers.append(langCheckButtons2.get())
            trueAnswers.append(langCheckButtons3.get())
        else:
            pass

def poll1():
    global questionsFrame
    for i in range(5):
        btn = CTkButton(questionsFrame, text=f'Питання {i + 1}', width=100, text_color='black', font=('arial', 14),
                        fg_color='white', hover_color='#C3D9F7', corner_radius=0)
        btn.configure(command=lambda btnName=i: poll1Buttons(btnName))
        btn.pack(side=LEFT)
    questionsFrame.pack(side=TOP)
    questionsFrame1.pack_forget()

def result():
    load = Toplevel()
    wl = load.winfo_screenwidth() / 2 - 135
    hl = load.winfo_screenheight() / 2 - 40
    load.geometry(f'270x80+{int(wl)}+{int(hl)}')
    load.title('Завантаження')
    prog = ttk.Progressbar(load, orient='horizontal', value=0, maximum=100, length=200)
    prog.pack(pady=20)

    res = len(trueAnswers) - 6

    def loading():
        if prog['value'] < 100:
            prog['value'] += 20
            load.after(500, loading)
        else:
            load.destroy()
            fd = filedialog.asksaveasfilename(parent=root, defaultextension='txt', title='Збереження результату', initialfile='Мій результат', filetypes=[("Текстові файли", "*.txt"), ("Усі файли", "*.*")],)
            if res == 0:
                with open(fd, 'w', encoding='utf-8') as file:
                    file.write('Ви відповіли на все правильно, вітаємо!')
            else:
                with open(fd, 'w', encoding='utf-8') as file:
                    file.write(f'Ви відпивіли правильно лише на {len(trueAnswers)} питань')
    loading()



trueAnswers = []
question1 = ['Python', 'Pithon', 'Payton']
question3 = ['(95,32),(3,5)', '(5,50),(5,50)', '(5,5),(97,95)']
question4 = ['int', 'str', 'float', 'def']
l = CTkLabel(root, text='Як буде правильно?', text_color='ghostwhite', font=('arial', 24))
questionsFrame = CTkFrame(root, height=30 , width=500, corner_radius=0, fg_color='sea green')
questionsFrame1 = CTkFrame(root, height=30 , width=500, corner_radius=0, fg_color='sea green')
langRdBtn = IntVar()
langScale = IntVar()
langCombobox = StringVar()
langListBox = StringVar()
langCheckButtons1 = IntVar()
langCheckButtons2 = IntVar()
langCheckButtons3 = IntVar()
header = Menu(root)
root.configure(menu=header)
header.add_command(label='Опитування', command=poll1)
header.add_command(label='Результат', command=result)

root.mainloop()
