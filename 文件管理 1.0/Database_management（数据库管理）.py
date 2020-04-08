import json, time, easygui, os

usual_ext = {'图像文件': ['.png', '.jpg', '.JPG', '.Png', '.bmp', '.jpeg', '.gif', '.pcx', '.tiff', '.tif', '.dxf', '.ico', '.cgm', '.cdr', '.wmf', '.eps', '.emf', '.pict', '.ai', '.psd', '.pdd', '.flc', '.fli', '.tga'],
             '音频文件': ['.cd', '.wave', '.aiff', '.au', '.mp3', '.mid', '.wma', '.ra', '.rmx', '.vqf', '.avi', '.mpg', '.amr', '.ape', '.flac', 'aac', '.tak'],
             '视频文件': ['.avi', '.mp4', '.mpeg-4', '.mpg-4', '.mov', '.qt', '.asf', '.rm', '.navi', '.divx', '.mpeg', '.mpg', '.dat', '.rmvb', '.ogg', '.3gp', '.mod', '.flv', '.mkv', '.mts', '.MTS', '.swf'],
             'Word文档': ['.doc', '.docx'],
             'Excel表格': ['.xls', '.xlsx'],
             'PPT演示': ['.ppt', '.pptx'],
             'WPS文档': ['.wps'],
             'PDF文件': ['.pdf'],
             'Publisher出版物': ['.pub'],
             'Access数据库': ['.mdb', '.accdb'],
             '应用程序（附件）': ['.exe', '.ipa', '.dll', '.inf', 'Config'],
             '程序源文件（附件）': ['.c', '.cpp', '.py', '.java', '.bcm', '.r', '.h', '.lib', '.dsp', '.dsw', '.cs', '.asp', '.aspx', '.php', '.jsp', '.e', '.ec', '.edb', '.js', '.pas', '.pyc'],
             '文本和json文件': ['.json', '.txt', '.rtf'],
             '网页文件': ['.html', '.htm', '.jsp', '.phtml', '.xml'],
             '字体文件': ['.eot', '.otf', '.fon', '.font', '.ttf', '.ttc', '.woff', '.woff2', '.fng', '.fog'],
             '压缩文件': ['.rar', '.zip', '.arj', '.z', '.cab', '.lzh', '.ace', '.tar', '.gz', '.uue', '.bz2', '.jar', '.isz', '.7z', '.pal'],
             '快捷方式':['.lnk','.pif','.url']}


def find():
    while True:
        name = easygui.enterbox('请输入一个文件扩展名（如“.doc”，退出程序点击cancel）：', '文件管理--数据库管理')
        if name == None:
            stop_running()
        if len(name) == 0:
            easygui.msgbox('您还未输入' '文件管理--数据库管理', '重试')
            break
        if not '.' in name:
            easygui.msgbox('输入不是扩展名，扩展名格式:“.letters”', '文件管理--数据库管理', '重试')
            break
        for i in name:
            if u'\u4e00' <= i <= u'\u9fff':
                easygui.msgbox('输入不是扩展名，扩展名格式:“.letters”', '文件管理--数据库管理', '重试')
                _break = True
                break
            else:
                _break = False
        if _break:
            break
        find_out = False
        for key in usual_ext:
            if name in usual_ext[key]:
                easygui.msgbox('{} 属于{}'.format(name, key), '文件管理--数据库管理', '好的')
                find_out = True
        if not find_out:
            easygui.msgbox('没有找到{}'.format(name), '文件管理--数据库管理', '好的')
    find()


def import_data():
    try:
        time.sleep(1)
        with open('usual_ext.json', 'w') as f:
            json.dump(usual_ext, f)
        easygui.msgbox('加载完成', '文件管理--数据库管理', '好的')
        _class = list(usual_ext.keys())
        ext = []
        txt = '最新数据库：\n'
        for key in usual_ext:
            ext.append(', '.join(usual_ext[key]))
        for i in range(len(_class)):
            txt += '{}:{}\n'.format(_class[i],ext[i])
        easygui.msgbox(txt, '文件管理--数据库管理', '好的')
        stop_running()
    except:
        again = easygui.ynbox('加载失败，是否重试', '文件管理--数据库管理', ('重新加载', '退出程序'))
        if again == None:
            easygui.msgbox('您未选择，默认为直接退出', '文件管理--数据库管理', '好的')
            stop_running()
        elif again:
            import_data()
        else:
            stop_running()


def stop_running():
    easygui.msgbox('程序即将关闭', '文件管理--数据库管理', '关闭')
    os._exit(0)


def main_program():
    way = easygui.ynbox('您需要以下哪项操作？', '文件管理--数据库管理', ('重新加载数据库', '手动查找文件扩展名'))
    if way == None:
        stop_running()
    elif way:
        import_data()
    else:
        find()

main_program()