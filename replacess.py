import re, sys, getopt, pyperclip

def replace(name):
    name1 = name.group("name1").strip()
    name2 = name.group("name2").strip()

    if '"' not in name1:
        names = f'"{name1}": "{name2}",'
    else:
        names = f'{name1}: {name2}'

    return names + '\n'


def main():
    """
    -c  把替换内容打印到控制台
    -v  把替换内容复制到剪辑版
    -h  帮助文档
    -p  复制到剪切板再粘贴到pycahrm（需要安装第三方库 pyautogui）

    例子1：-m replacess -c "$SelectedText$"
    例子2：-m replacess -v "$SelectedText$"
    例子3：-m replacess -v -c "$SelectedText$"

    作者QQ：2920007919
    """
    c = False
    v = False
    h = False
    p = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "-c-v-h-p", ['console', 'version', 'help', 'paste'])
        if args[0] == '':
            raise Exception('\nError: 你没有选择文本，无法添加引号')
        else:
            t = args[0]
            text = re.sub(r'(?P<name1>.*?)[:|：](?P<name2>.*?)\n', replace, f'{t}\n').strip('\n')
        for o, a in opts:
            if o in ('-c', '--console'):
                c = True
            if o in ('-v', '--version'):
                v = True
            if o in ('-h', '--help'):
                h = True
            if o in ('-p', '--paste'):
                p = True

    except Exception as e:
        print(e)
    else:
        if c:
            print(f'\n\n{text}')
        if v:
            pyperclip.copy(text)
        if h:
            print(main.__doc__, end=' ')
        if p:
            try:
                import pyautogui
            except Exception as e:
                print('-p 需要安装pyautogui: "pip install pyautogui"')
                return 0
            else:
                pyperclip.copy(text)
                pyautogui.hotkey('ctrl', 'v')


if __name__ == "__main__":
    sys.exit(main())
