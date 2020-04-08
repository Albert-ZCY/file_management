"""
PySide2 5.14.0版本以下可以导入pyside2uic模块，使用该模块中的compileUi函数
实现ui文件转python代码，该函数接受2个必要参数：ui文件对象或路径，python文件对象

Windows测试情况：
    1. 使用os库，os.system手动安装最新版
        * 版本：5.14.0
        * 位置：C:/Pyblock/resources/app/Python-win63/lib/site-packages/PySide2
        * 转换方法：使用PySide2目录下的uic.exe指令转换
            e.g.: uic <ui_file> -g python -o <output_file>

    2. 使用os库，os.system手动安装
        * 版本：5.11.2
        * 位置：C:/Pyblock/resources/app/Python-win63/lib/site-packages/PySide2
        * 转换方法：使用PySide2.scripts下的uic.py模块转换
            e.g.: python -m PySide2.scripts.uic <ui_file> -o <output_file>

    3. 使用库管理安装最新版
        * 版本：5.14.0
        * 位置：C:/Users/admin/.wood/libs_x64/PySide2
        * 转换方法：使用PySide2目录下的uic.exe指令转换
            e.g.: uic <ui_file> -g python -o <output_file>

    4. 使用os库，os.system手动安装
        * 版本：5.11.2
        * 位置：C:/Users/admin/.wood/libs_x64/PySide2
        * 转换方法：使用PySide2.scripts下的uic.py模块转换
            e.g.: python -m PySide2.scripts.uic <ui_file> -o <output_file>

2020/1/13优化：
    * 文件选择对话框中，文件类型仅限.ui文件，避免选择其他文件导致转换报错
    * 添加标签控件显示当前PySide2版本
    * 高版本中使用空字符串替换已经废弃的Qt字符函数(QString())，保证转换后文件可以运行
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import PySide2


class Qt2Py:
    """A class to convert ui file to Python codes."""
    def __init__(self, src):
        """Full directories of a ui file."""
        self.src = src

    def _is_lower_version(self) -> bool:
        """
        Check if current PySide2 version is lower than 5.14.0.

            :return: comparsion result
        """
        if PySide2.__version__ < "5.14.0":
            return True
        else:
            return False

    def _generate_dst(self) -> str:
        """
        Return a Python file name according to ui file.

            :return: python file name
        """
        src_dir = os.path.dirname(self.src)
        src_name = os.path.basename(self.src)
        return os.path.join(src_dir, f"ui_{os.path.splitext(src_name)[0]}.py")

    def _qt2py_version_higher(self) -> bool:
        """
        Convert higher version ui file to Python codes. Return bool.

            :return: True for successful conversion False for failure.
        """
        # 找到并切换到PySide2所在目录
        os.chdir(os.path.dirname(PySide2.__file__))

        # 生成python文件名
        dst = self._generate_dst()

        # 开始转换
        if os.system(f".{os.sep}uic {self.src} -g python -o {dst}"):
            return False
        else:
            try:
                with open(dst, encoding="utf-8") as f:
                    codes = f.read().replace("QString()", '""')
                with open(dst, "w", encoding="utf-8") as f:
                    f.write(codes)
                return True
            except Exception:
                return False

    def _qt2py_version_lower(self) -> bool:
        """
        Convert lower version ui file to Python codes. Return bool.

            :return: True for successful conversion False for failure.
        """
        # 生成python文件名
        dst = self._generate_dst()

        import pyside2uic

        # 开始转换
        try:
            with open(dst, 'w', encoding='utf-8') as f:
                pyside2uic.compileUi(self.src, f)
        except Exception:
            return False
        else:
            return True

    def qt2py(self) -> bool:
        """
        Convert ui file to Python file according PySide2 version.

            :return: True for successful conversion False for failure.
        """
        if self._is_lower_version():
            return self._qt2py_version_lower()
        else:
            return self._qt2py_version_higher()


class Ui_Qt2Py:
    """A class to create a GUI for file conversion."""

    def __init__(self, master):
        """Set up attributes and GUI widgets."""
        self.master = master

        self.ui_file = ''

        self.setup_Master()
        self.setup_Ui()
        self.bind_Method()

    def setup_Master(self):
        """Adjustments to root window."""
        self.master.resizable(False, False)
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry(f'340x240+{(width-340)//2}+{(height-240)//2}')
        self.master.title('Qt Creator转换器')

    def setup_Ui(self):
        """Add all widgets to root window."""
        ttk.Label(
            self.master, text='Qt Creator转换器', font=('Calibri', 20)
        ).place(anchor='center', relx=0.5, rely=0.15)

        ttk.Label(
            self.master, font=('Arial', 12),
            text=f'PySide2 版本：{PySide2.__version__}'
        ).place(anchor='center', relx=0.5, rely=0.35)

        self.btn_choose_file = ttk.Button(self.master, text='选择ui文件')
        self.btn_choose_file.place(anchor='center', relx=0.275, rely=0.55,
                                   relwidth=0.35, relheight=0.15)

        self.btn_convert = ttk.Button(self.master, text='开始转换')
        self.btn_convert.place(anchor='center', relx=0.725, rely=0.55,
                               relwidth=0.35, relheight=0.15)

        self.file_path = tk.StringVar(value='请选择需要转换的ui文件……')
        ttk.Label(
            self.master, textvariable=self.file_path,
            font=('Arial', 16), wraplength=320, anchor='center'
        ).place(anchor='center', relx=0.5, rely=0.8, relwidth=1)

    def _select_file(self, event=None):
        """Using file-selecting dialog to get ui file path."""
        file_path = filedialog.askopenfilename(
            title='打开文件', filetypes=[('Qt', '*.ui')])
        if file_path:
            self.file_path.set(file_path)
            self.ui_file = file_path

    def _convert_file(self, event=None):
        """Method to convert a ui file to Python codes."""
        if not self.ui_file:
            messagebox.showerror('文件错误', '请至少选择一个ui文件')
        else:
            q = Qt2Py(self.ui_file)
            if q.qt2py():
                messagebox.showinfo('转换结果', '转换成功')
            else:
                messagebox.showinfo('转换结果', '转换出错')

    def bind_Method(self):
        """Bind methods to GUI buttons."""
        self.btn_choose_file['command'] = lambda: self._select_file()
        self.btn_convert['command'] = lambda: self._convert_file()

        self.master.bind_all('<Control-KeyPress-o>', self._select_file)
        self.master.bind_all('<Control-KeyPress-e>', self._convert_file)


def main():
    """Main entrance."""
    root = tk.Tk()
    Ui_Qt2Py(root)
    root.mainloop()


if __name__ == "__main__":
    main()
