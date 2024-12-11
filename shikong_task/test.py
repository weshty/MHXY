import time

import win32gui
import common


def get_window_info(window_title):
    """
    获取指定窗口的句柄和当前矩形区域
    :param window_title: 窗口标题
    :return: 窗口的句柄、矩形区域 (left, top, right, bottom)
    """
    hwnd = win32gui.FindWindow(0, window_title)
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        return hwnd, rect
    else:
        return None, None

def get_window_size(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    return rect

def get_windows(window_title):
    """
    获取指定窗口的句柄和当前矩形区域
    :param window_title: 窗口标题
    :return: 窗口的句柄、矩形区域 (left, top, right, bottom)
    """
    def enum_windows_callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            text = win32gui.GetWindowText(hwnd)
            if text == window_title:
                rect = win32gui.GetWindowRect(hwnd)
                windows.append((hwnd, rect))

    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)

    if windows:
        # 如果有多个匹配的窗口，可以选择第一个或根据其他条件选择
        return windows  # 返回第一个匹配的窗口
    else:
        return None


def resize_window(hwnd, new_width, height_ratio=0.8):
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


def main():
    window_title = u'梦幻西游：时空'  # 替换为你要调整的窗口标题
    hwnds = get_windows(window_title)

    for hwnd2 in hwnds:
        rect = hwnd2[1]
        hwnd = hwnd2[0]
        if hwnd and rect:
            new_width = 500  # 新的宽度
            common.resize_window(hwnd, new_width)
            window_size = common.get_window_size(hwnd)
            result = common.findpng("ditu.png",window_size)
            common.click_at_offset(20,45,window_size)
            print(f"地图 {result}" )
            print(f"窗口 {window_size} 的大小")
            time.sleep(2)
        else:
            print(f"未找到标题为 '{window_title}' 的窗口")

        if hwnd and rect:
            left, top, right, bottom = rect
            width = right - left
            height = bottom - top
            print(f"窗口句柄: {hwnd}")
            print(f"窗口位置: ({left}, {top})")
            print(f"窗口大小: {width}x{height}")
        else:
            print(f"未找到标题为 '{window_title}' 的窗口")



if __name__ == "__main__":
    main()