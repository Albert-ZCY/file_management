import easygui
import os
import json
import shutil
import time
import sys
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import *

sys.setrecursionlimit(100000)

def data_preparation():
    global usual_ext
    try:
        with open(r'usual_ext.json', 'r') as f:
            usual_ext = json.load(f)
    except:
        easygui.msgbox('数据库导入失败\n解决方案：\n打开本应用（非快捷方式）所在文件夹，点击运行“数据库管理”，选择重新加载数据库即可（如下图）', '文件管理', '好的', image = 'images\\示例图片.gif')
        os._exit(0)

def clear(_dir, myDir, move=False, keep_dir=False):
    try:
        QApplication.processEvents()
        files = os.listdir(_dir)
        for file in files:
            Dir = _dir+os.sep+file
            ext = os.path.splitext(file)[-1]
            if os.path.isdir(Dir):
                if keep_dir:
                    dirs = myDir+os.sep+'文件夹'
                    if not os.path.exists(dirs):
                        os.mkdir(dirs)
                    main_program.nums['文件夹'] += 1
                    shutil.move(Dir, dirs)
                else:
                    clear(Dir, myDir, move, keep_dir)
            else:
                replace = False
                for key in usual_ext:
                    if ext in usual_ext[key]:
                        subDir = myDir+os.sep+key
                        if not os.path.exists(subDir):
                            os.mkdir(subDir)
                        if not os.path.exists(subDir+os.sep+file):
                            if move:
                                shutil.move(Dir, subDir)
                            else:
                                shutil.copy(Dir, subDir)
                            main_program.nums[key] += 1
                        replace = True
                        break
                if not replace:
                    others = myDir+os.sep+'其他类文件'
                    if not os.path.exists(others):
                        os.mkdir(others)
                    if not os.path.exists(others+os.sep+file):
                        if move:
                            shutil.move(Dir, others)
                        else:
                            shutil.copy(Dir, others)
                        main_program.nums['其他类文件'] += 1
        return(True)
    except:
        return(False)


def Del(_dir, myDir, target_ext, config=1, remove=False):
#config1:传入保留的文件扩展名
#config2:传入删除的文件扩展名
    try:
        QApplication.processEvents()
        files = os.listdir(_dir)
        for file in files:
            Dir = _dir+os.sep+file
            ext = os.path.splitext(file)[-1]
            if os.path.isdir(Dir):
                Del(Dir, myDir, target_ext, config, remove)
            else:
                if config == 1:
                    if not ext in target_ext:
                        if remove:
                            os.remove(Dir)
                        elif not os.path.exists(myDir+os.sep+file):
                            shutil.move(Dir, myDir)
                        main_program.num += 1
                else:
                    if ext in target_ext:
                        if remove:
                            os.remove(Dir)
                        elif not os.path.exists(myDir+os.sep+file):
                            shutil.move(Dir, myDir)
                        main_program.num += 1
        return(True)
    except:
        return(False)


def backup(_dir, myDir, target_ext):
    try:
        QApplication.processEvents()
        files = os.listdir(_dir)
        for file in files:
            Dir = _dir+os.sep+file
            newDir = myDir+os.sep+file
            ext = os.path.splitext(file)[-1]
            if os.path.isdir(Dir):
                backup(Dir, myDir, target_ext)
            else:
                if target_ext == 'all':
                    if not os.path.exists(newDir):
                        shutil.copy(Dir, myDir)
                        main_program.bnum += 1
                else:
                    if ext in target_ext:
                        if not os.path.exists(newDir):
                            shutil.copy(Dir, myDir)
                            main_program.bnum += 1
        return(True)
    except:
        return(False)


def get_dir_path():
    global path
    easygui.msgbox('请选择需要处理的文件夹', '文件管理', '选择')
    path = QFileDialog.getExistingDirectory(caption='请选择需要处理的文件夹')
    if len(path) == 0:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        get_dir_path()
    

def new_name():
    global path2
    dname = easygui.enterbox('请输入文件夹名', '文件管理')
    if dname == None or len(dname) == 0:
        easygui.msgbox('您还未输入', '文件管理--提示', '重试')
        new_name()
    else:
        stop_words = ('\\', '/', ':', '*', '?', '"', '<', '>', '|')
        if dname[0] == '.':
            easygui.msgbox('文件夹名首字不得为.！', '文件管理--警告', '重试')
            new_name()
        else:
            for word in dname:
                if word in stop_words:
                    easygui.msgbox('文件夹命名不得使用系统保留字符！', '文件管理--警告', '重试')
                    new_name()
                    return
            path2 = tpath+os.sep+dname
            if os.path.exists(path2):
                easygui.msgbox('该文件夹已存在！', '文件管理--提示', '重试')
                new_name()
            else:
                try:
                    os.mkdir(path2)
                except:
                    easygui.msgbox('新建文件夹失败，请检查文件夹路径是否正确，文件夹命名是否规范！', '文件管理--警告', '重试')
                    new_name()


def new_dir():
    global tpath
    easygui.msgbox('请选择新建文件夹所在目录', '文件管理', '选择')
    tpath = QFileDialog.getExistingDirectory(caption='请选择新建文件夹所在目录')
    if len(tpath) == 0:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        new_dir()
    else:
        new_name()


def old_dir():
    global path2
    path2 = QFileDialog.getExistingDirectory(caption='请选择保存处理结果的文件夹')
    if len(path2) == 0:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        old_dir()


def get_newdir_path():
    global is_new
    is_new = easygui.ynbox('是否新建文件夹储存处理结果？', '文件管理', ('新建文件夹', '选择已有文件夹'))
    if is_new == None:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        is_new()
    elif is_new:
        new_dir()
    else:
        old_dir()


def get_clear_config():
    global keep_dir
    global move
    temp = easygui.ynbox('您需要对文件进行以下哪种操作？', '文件管理', ('复制', '移动(不推荐)'))
    if temp == None:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        get_clear_config()
    elif temp == False:
        if easygui.ynbox('移动操作可能将应用程序文件夹拆散，使其无法正常运行，另外，还会使文件无法恢复到初始状态，且有可能使信息丢失严重的文件丢失。您还要继续吗？', '文件管理--警告', ('继续', '重新选择')):
            move = True
            easygui.msgbox('为防止可能发生的意外情况，建议您备份您要处理的文件夹！', '文件管理--提示', '好的')
            get_clear_config2()
        else:
            get_clear_config()
    else:
        move = False
        keep_dir = False


def get_clear_config2():
    global keep_dir
    keep_dir = easygui.ynbox('是否保留（不拆开）文件夹中包含的子文件夹？', '文件管理', ('保留', '不保留'))
    if keep_dir == None:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        get_clear_config2()

def get_Del_config1():
    global remove
    temp = easygui.ynbox('您需要对无用的文件进行以下哪种操作？', '文件管理', ('移到文件夹', '删除(不推荐)'))
    if temp == None:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        get_Del_config1()
    elif temp == False:
        if easygui.ynbox('删除操作会使您的文件永久丢失，您还要继续吗？', '文件管理--警告', ('继续', '重新选择')):
            remove = True
            easygui.msgbox('为防止可能发生的意外情况，建议您备份您要处理的文件夹！', '文件管理--提示', '好的')
        else:
            get_Del_config1()
    else:
        remove = False


def get_Del_config5():
    global path2
    if not remove:
        get_newdir_path()


def get_Del_config2():    
    global config
    temp = easygui.ynbox('您希望以下哪种输入模式？', '文件管理', ('输入需要保存的文件或扩展名', '输入不需要的文件或扩展名'))
    if temp == None:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        get_Del_config2()
    elif temp == True:
        config = 1
    else:
        config = 2


def get_Del_config3():
    global fileclass
    fileclass = easygui.ynbox('您要以以下哪种方式输入？', '文件管理', ('文件类型', '文件扩展名'))
    if fileclass == None:
        easygui.msgbox('您还未选择', '文件管理--提示', '重试')
        get_Del_config3()


def get_Del_config4():
    global inpext
    if fileclass:
        typeout = '现有以下文件种类：\n'
        letternums = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        letters = list(letternums.keys())
        Keys = list(usual_ext.keys())
        for i in range(len(Keys)):
            typeout = typeout + letters[i] + '.' + Keys[i] + '  '
        typeout = typeout + '\n请输入您要处理的文件类型序号（区分大小写，多选紧连即可）后按OK'
        inpfiles = easygui.enterbox(typeout, '文件管理')
        if inpfiles == None or len(inpfiles) == 0:
            easygui.msgbox('您还未输入', '文件管理--提示', '重试')
            get_Del_config4()
        else:
            try:
                inpext = []
                for i in inpfiles:
                    for j in usual_ext[Keys[letternums[i]-1]]:
                        inpext.append(j)
            except:
                easygui.msgbox('有无效输入，请重试', '文件管理--提示', '重试')
                get_Del_config4()
    else:
        inpext = easygui.enterbox('请输入需要处理的后缀名（中间用英文逗号隔开，如：.jpg,.pdf,.doc,.pptx）：')
        if inpext == None or len(inpext) == 0  :
            easygui.msgbox('您还未输入', '文件管理--提示', '重试')
            get_Del_config4()
        else:
            inpext = inpext.split(',')
            for ext in inpext:
                if not '.' in ext:
                    easygui.msgbox('输入不是扩展名，扩展名格式:“.letters”', '重试')
                    get_Del_config4()
                else:
                    for ext in inpext:
                        for i in ext:
                            if u'\u4e00' <= i <= u'\u9fff':
                                easygui.msgbox('输入不是扩展名，扩展名格式:“.letters”', '重试')
                                get_Del_config4()


def get_Del_config():
    get_Del_config1()
    get_Del_config5()
    get_Del_config2()
    get_Del_config3()
    get_Del_config4()


def get_backup_config():
    global inpext
    global fileclass
    if fileclass:
        typeout = '现有以下文件种类：\n'
        letternums = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        letters = list(letternums.keys())
        Keys = list(usual_ext.keys())
        for i in range(len(Keys)):
            typeout = typeout + letters[i] + '.' + Keys[i] + '  '
        typeout = typeout + '\n请输入您要处理的文件类型序号（区分大小写，多选紧连即可，全部备份输入‘all’）后按OK'
        inpfiles = easygui.enterbox(typeout, '文件管理')
        if inpfiles == None or len(inpfiles) == 0:
            easygui.msgbox('您还未输入', '文件管理--提示', '重试')
            get_backup_config()
        else:
            try:
                if inpfiles == 'all':
                    inpext = 'all'
                else:
                    inpext = []
                    for i in inpfiles:
                        for j in usual_ext[Keys[letternums[i]-1]]:
                            inpext.append(j)
            except:
                easygui.msgbox('有无效输入，请重试', '文件管理--提示', '重试')
                get_backup_config()
    else:
        inpext = easygui.enterbox('请输入需要处理的后缀名（中间用英文逗号隔开，如：.jpg,.pdf,.doc,.pptx）：')
        if inpext == None or len(inpext) == 0:
            easygui.msgbox('您还未输入', '文件管理--提示', '重试')
            get_backup_config()
        else:
            inpext = inpext.split(',')
            for ext in inpext:
                if not '.' in ext:
                    easygui.msgbox('输入不是扩展名，扩展名格式:“.letters”', '重试')
                    get_backup_config()
                else:
                    for ext in inpext:
                        for i in ext:
                            if u'\u4e00' <= i <= u'\u9fff':
                                easygui.msgbox('输入不是扩展名，扩展名格式:“.letters”', '重试')
                                get_backup_config()


class main_program_1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.run = False
        super().__init__()
        self.setupUi(self)
        self.show()
        self.choice_1.clicked.connect(self.all_clear)
        self.choice_2.clicked.connect(self.all_Del)
        self.choice_3.clicked.connect(self.all_backup)
    def all_clear(self):
        global keep_dir
        global move
        global path
        global path2
        if not self.run:
            self.run = True
            self.way = '分类整理'
            get_dir_path()
            get_newdir_path()
            get_clear_config()
            #初始化clear()
            easygui.msgbox('即将开始分类整理，时间可能较长，请耐心等待，切勿在整理过程中关闭程序！', '文件管理', '开始')
            self.nums = {}
            for key in usual_ext:
                self.nums[key] = 0
            self.nums['其他类文件'] = 0
            if keep_dir:
                self.nums['文件夹'] = 0
            self.mistake = not clear(path, path2, move, keep_dir)
            main_program_2()
            self.run = False
        else:
            easygui.msgbox('已有程序在运行！', '文件管理--提示', '好的')

    def all_Del(self):
        global path
        global path2
        global inpext
        global config
        global remove
        if not self.run:
            self.run = True
            self.way = '文件清理'
            get_dir_path()
            get_Del_config()
            #初始化Del()
            easygui.msgbox('即将开始文件清理，时间不会过长，请勿在整理过程中关闭程序！', '文件管理', '开始')
            self.num = 0
            if remove:
                path2 = '__None__'
            self.mistake = not Del(path, path2, inpext, config, remove)
            main_program_2()
            self.run = False
        else:
            easygui.msgbox('已有程序在运行！', '文件管理--提示', '好的')

    def all_backup(self):
        global path
        global path2
        global inpext
        if not self.run:
            self.run = True
            self.way = '快速备份'
            get_dir_path()
            get_newdir_path()
            get_Del_config3()
            get_backup_config()
            easygui.msgbox('即将开始快速备份，时间可能较长，请耐心等待，切勿在整理过程中关闭程序！', '文件管理', '开始')
            self.bnum = 0
            self.mistake = not backup(path, path2, inpext)
            main_program_2()
            self.run = False
        else:
            easygui.msgbox('已有程序在运行！', '文件管理--提示', '好的')

def main_program_2():
    if main_program.mistake:
        easygui.msgbox('处理失败，建议按照以下步骤清理残留：\n如果您将处理冗余或结果放置在文件夹，请找到此文件夹，您可以按原来的方式将其中的文件还原或删除；\n如果您选择将文件删除，您的文件将永远无法还原，但您可以使用原先提示您备份的文件夹。', '文件管理', '好的')
    else:
        if main_program.way == '分类整理':
            Sum = sum(list(main_program.nums.values()))
            result = ''
            for key in main_program.nums:
                result += key+':'+str(main_program.nums[key])+'个,  '
            easygui.msgbox('处理完成，本次分类整理共为您分类文件{}个，具体结果如下：\n{}'.format(Sum, result), '文件管理', '好的')
        if main_program.way == '文件清理':
            easygui.msgbox('处理完成，本次文件清理共为您清理文件{}个'.format(main_program.num), '文件管理', '好的')
        if main_program.way == '快速备份':
            easygui.msgbox('处理完成，本次快速备份共为您备份文件{}个'.format(main_program.bnum), '文件管理', '好的')


if __name__ == '__main__':
    try:
        data_preparation()
        app = QApplication()
        main_program = main_program_1()
        os._exit(app.exec_())
    except:
        critical_win = QMainWindow()
        QMessageBox.critical(critical_win, '警告', '程序发生严重错误，即将关闭')
        os._exit(0)
