import threading
from tkinter import *
from tkinter.ttk import *
from tkinter import Scale
from tkinter.scrolledtext import ScrolledText


class MainTableFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tree = self.create_table()
        self.xscroll, self.yscroll = self.create_scrollbars(self.tree)

    def create_table(self):
        # columns = {"图片文件夹名称": 120, "路径": 319}
        tk_table = Treeview(self, show="headings", columns=("标题", "BV号/分p号"))

        tk_table.column("标题", anchor="center", stretch=False)
        tk_table.heading("标题", text="标题", anchor=CENTER)

        tk_table.column("BV号/分p号", anchor="center", stretch=True)
        tk_table.heading("BV号/分p号", text="BV号/分p号", anchor='center')

        return tk_table

    def create_scrollbars(self, tree):
        xscroll = Scrollbar(self, orient=HORIZONTAL)
        yscroll = Scrollbar(self, orient=VERTICAL)
        tree.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.config(command=tree.xview)
        yscroll.config(command=tree.yview)
        return xscroll, yscroll

    def pack_children(self):
        self.xscroll.pack(side=BOTTOM, fill=X, expand=False)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.tree.pack(fill=BOTH, expand=1)

    def pack(self, cnf={}, **kw):
        super().pack(cnf, **kw)
        self.pack_children()


class StartButtonFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.start_button = self.create_start_button()

    def create_start_button(self):
        button = Button(self, text="开始")
        return button

    def pack_children(self):
        self.start_button.pack(side=LEFT, pady=3, ipadx=5, ipady=3, anchor=CENTER, expand=1)

    def pack(self, cnf={}, **kw):
        super().pack(cnf, **kw)
        self.pack_children()


class StateFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.state_label = self.create_state_label()
        self.loginButton = self.create_login_button()

    def create_state_label(self):
        label = Label(self, text="状态：未登录")
        return label

    def create_login_button(self):
        button = Button(self)
        button.config(text="登录",width=4)
        return button

    def pack_children(self):
        self.state_label.pack(side=LEFT, padx=8, pady=3, ipadx=5, ipady=3, anchor=W, expand=1, fill=BOTH)
        self.loginButton.pack(side=RIGHT, padx=8, pady=3, ipadx=5, ipady=3, expand=False, anchor=E, fill=BOTH)

    def pack(self, cnf={}, **kw):
        super().pack(cnf, **kw)
        self.pack_children()


class EntryFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tips_label = self.create_tips_label()
        self.entry = self.create_entry()
        self.check_button = self.create_check_button()

    def create_tips_label(self):
        label = Label(self, text="手动输入：")
        return label

    def create_entry(self):
        entry = Entry(self)
        entry.config(width=10)
        return entry

    def create_check_button(self):
        button = Button(self, text="检查",width=4)
        return button

    def grid_children(self):
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.entry.grid(row=1, column=0, padx=8, pady=3, ipadx=5, ipady=3, sticky=N + W + S + E)
        self.check_button.grid(row=1, column=1, padx=8, pady=3, ipadx=5, ipady=3, sticky=W+E)
        self.tips_label.grid(row=0, column=0, rowspan=1, padx=8, pady=3, ipadx=5, ipady=3, sticky=W+E)

    def pack(self, cnf={}, **kw):
        super().pack(cnf, **kw)
        self.grid_children()


class SecondTableFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tree = self.create_table()

    def create_table(self):
        # columns = {"图片文件夹名称": 120, "路径": 319}
        tk_table = Treeview(self, show="headings", columns="清晰度")

        tk_table.column("清晰度", anchor="center", stretch=True,width=70)
        tk_table.heading("清晰度", text="清晰度", anchor=CENTER)

        tk_table.insert("", "end", text="8K 超高清", values=["8K 超高清"])
        tk_table.insert("", "end", text="4K 超清", values=["4K 超清"])
        tk_table.insert("", "end", text="1080P 高码率", values=["1080P 高码率"])
        tk_table.insert("", "end", text="1080P 60帧", values=["1080P 60帧"])
        tk_table.insert("", "end", text="1080P 高清", values=["1080P 高清"])
        tk_table.insert("", "end", text="720P 高清", values=["720P 高清"])
        tk_table.insert("", "end", text="480P 清晰", values=["480P 清晰"])
        tk_table.insert("", "end", text="360P 流畅", values=["360P 流畅"])

        tk_table.config(height=8)

        return tk_table

    def pack_children(self):
        self.tree.pack(fill=BOTH, expand=1, padx=8, pady=3, ipadx=5, ipady=3)

    def pack(self, cnf={}, **kw):
        super().pack(cnf, **kw)
        self.pack_children()


class PriorityFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.table_frame = self.create_table_frame()
        self.up_button = self.create_up_button()
        self.down_button = self.create_down_button()

    def create_table_frame(self):
        table_frame = SecondTableFrame(self)
        return table_frame

    def create_up_button(self):
        button = Button(self, text="🔼",width=2)
        return button

    def create_down_button(self):
        button = Button(self, text="🔽",width=2)
        return button

    def pack_children(self):
        self.table_frame.pack(side=LEFT, fill=BOTH)
        self.up_button.pack(side=TOP, padx=8, pady=3, ipadx=5, ipady=3, anchor=N)
        self.down_button.pack(side=BOTTOM, padx=8, pady=3, ipadx=5, ipady=3, anchor=S)

    def pack(self, cnf={}, **kw):
        super().pack(cnf, **kw)
        self.pack_children()


class CheckbuttonsFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.check_danmu_button = self.create_check_danmu_button()
        self.check_audio_button = self.create_check_audio_button()

    def create_check_danmu_button(self):
        button = Checkbutton(self, text="是否要下载弹幕", variable=IntVar(), onvalue=1, offvalue=0)
        return button

    def create_check_audio_button(self):
        button = Checkbutton(self, text="是否只下载音频", variable=IntVar(), onvalue=1, offvalue=0)
        return button

    def pack_children(self):
        self.check_danmu_button.pack(side=TOP, padx=8, pady=6, ipadx=5, ipady=3, anchor=W, expand=1)
        self.check_audio_button.pack(side=TOP, padx=8, pady=10, ipadx=5, ipady=3, anchor=W, expand=1)

    def pack(self, cnf={}, **kw):
        super().pack(cnf, **kw)
        self.pack_children()


class ExceptTableFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.start_button_frame = self.create_start_button_frame()
        self.state_frame = self.create_state_frame()
        self.entry_frame = self.create_entry_frame()
        self.priority_frame = self.create_priority_frame()
        self.checkbuttons_frame = self.create_checkbuttons_frame()

    def create_start_button_frame(self):
        frame = StartButtonFrame(self)
        return frame

    def create_state_frame(self):
        frame = StateFrame(self)
        return frame

    def create_entry_frame(self):
        frame = EntryFrame(self)
        return frame

    def create_priority_frame(self):
        frame = PriorityFrame(self)
        return frame

    def create_checkbuttons_frame(self):
        frame = CheckbuttonsFrame(self)
        return frame

    def pack_children(self):
        self.start_button_frame.pack(side=TOP, fill=Y, expand=1)
        self.state_frame.pack(side=TOP, fill=Y)
        self.entry_frame.pack(side=TOP, fill=Y)
        self.priority_frame.pack(side=TOP, fill=Y,anchor=W)
        self.checkbuttons_frame.pack(side=TOP, fill=Y,anchor=W)

    def pack(self, cnf={}, **kw):
        super().pack(cnf, **kw)
        self.pack_children()


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.table_frame = self.__table_frame()
        self.except_table_frame = self.__except_table_frame()

    def __win(self):
        self.title("微信自动添加表情包助手")
        # self.geometry("700x600")
        self.minsize(600, 450)
        # self.iconbitmap("icon.ico")
        # self.resizable(width=False, height=False)

    def __table_frame(self):
        table_frame = MainTableFrame(self)
        table_frame.pack(side=LEFT, fill=BOTH, expand=1)
        return table_frame

    def __except_table_frame(self):
        except_table_frame = ExceptTableFrame(self)
        except_table_frame.pack(side=RIGHT,fill=Y)
        return except_table_frame


class Win(WinGUI):
    def __init__(self, controller):
        # self.ctl = controller
        super().__init__()
        # self.__event_bind()
        # self.__style_config()
        # self.ctl.init(self)
        # self.except_table_frame.main_function_frame.image_config_frame.inquire_enlarge_pic_config_checkbutton.config(
        #     variable=self.ctl.ENLARGE_STATE)
        # self.iconphoto(True, self.ctl.get_icon())


#     def __event_bind(self):
#         self.bind("<Configure>", self.ctl.fix_tree_column_width)
#
#         self.table_frame.tree.bind('<Double-Button-1>', self.ctl.show_image)
#         self.table_frame.tree.bind('<Delete>', self.ctl.multi_delete_image)
#         self.table_frame.tree.bind("<ButtonRelease-1>", self.ctl.fix_tree_column_width)
#
#         self.except_table_frame.introduction_frame.about_scroll_text.bind('<Double-Button-1>',
#                                                                           self.ctl.show_introduction_toplevel)
#         self.except_table_frame.main_function_frame.buttons_frame.start_button.bind('<Button-1>',
#                                                                                     lambda _: thread_it(
#                                                                                         self.ctl.start_add_image))
#         # self.except_table_frame.main_function_frame.buttons_frame.start_button.bind('<Button-1>',
#         #                                                                             self.ctl.start_add_image)
#         self.except_table_frame.main_function_frame.buttons_frame.select_emoji_folder_button.bind('<Button-1>',
#                                                                                                   self.ctl.select_image_folder)
#         self.except_table_frame.main_function_frame.image_config_frame.max_image_length_config_scale.bind('<B1-Motion>',
#                                                                                                           self.ctl.set_max_length)
#
#     def __style_config(self):
#         pass
#
#
# def thread_it(func, *args, daemon: bool = True):
#     t = threading.Thread(target=func, args=args)
#     t.daemon = daemon  # 当daemon为True时，该线程为守护线程，效果为主程序结束时不等待子线程结束，立即结束子线程
#     t.start()
#     return t


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
