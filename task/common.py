
import time
import pyautogui
import win32api, win32gui
import win32con
import random
import mhxy





# 获取梦幻西游窗口信息吗，返回一个矩形窗口四个坐标
def get_window_info(wdname):
    global handle
    # wdname = u'雷电模拟器'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:
        # text.insert('end', '提示：请打开梦幻西游\n')
        # text.see('end')  # 自动显示底部
        window_region = (0, 0, 800, 600)
        return None,None
    else:
        window_size = win32gui.GetWindowRect(handle)
        print(f"window_size:{window_size}")
        return handle,window_size

def get_window_region(window_size):
    window_region = (window_size[0], window_size[1], window_size[2] - window_size[0], window_size[3] - window_size[1])
    return window_region

##重置窗口大小
def resize_window(hwnd, new_width, height_ratio=0.58):
    """
    调整窗口大小，高度为宽度的指定比例
    :param hwnd: 窗口句柄
    :param new_width: 新的宽度
    :param height_ratio: 高度与宽度的比例
    """
    if not hwnd:
        print("未找到窗口")
        return

    rect = win32gui.GetWindowRect(hwnd)
    left, top, right, bottom = rect
    current_width = right - left
    current_height = bottom - top

    new_height = int(new_width * height_ratio)

    win32gui.MoveWindow(hwnd, left, top, new_width, new_height, True)


# 找指定任务
def findpng(Pngfile,window_size):
    myConfidence = 0.80
    try:
        result = pyautogui.locateOnScreen('img\\'+Pngfile, region=get_window_region(window_size), confidence=myConfidence)
        return result
    except pyautogui.ImageNotFoundException:
        print("ImageNotFoundException: Image could not be located. image:"+Pngfile)
    return None


def move_click(x, y, t=0):  # 移动鼠标并点击左键
    win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                         win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
    if t == 0:
        time.sleep(random.random()*2+1)  # sleep一下
    else:
        time.sleep(t)
    return 0


# 单击指定位置
def click(x,y,window_size):
    move_click(x,y,0.1)
    pyautogui.moveTo(x=window_size[0]+10,y=window_size[1]+10,duration=0.1)  #鼠标移至窗口左上角

# 接任务
def get_rw(rwm,window_size):
    pos=findpng(rwm+".png",window_size)
    print(rwm,pos)
    if pos is not None:
        click(pos[0]+pos[2]-6,pos[1]+pos[3]-6,window_size)
        time.sleep(0.5)
        return True
    else:
        return False

# 等待直到打开活动界面
def open_huodong(window_size):
    global is_start
    is_start = True
    window_region = get_window_region(window_size)
    time.sleep(1)   # 等待1秒
    print(window_region[0]+window_region[2]/2,window_region[1]+window_region[3]/2,window_region)
    click(window_region[0]+int(window_region[2]/2),window_region[1]+int(window_region[3]/2))  #移到窗口中间，点击以激活窗口
    while is_start:
        if get_rw("huodong",window_size):
            break
        else:
            time.sleep(3)
