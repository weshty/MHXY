import win32gui


def get_window_info(window_title):
    """
    获取指定窗口的句柄和当前矩形区域
    :param window_title: 窗口标题
    :return: 窗口的句柄、矩形区域 (left, top, right, bottom)
    """
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        return hwnd, rect
    else:
        return None, None


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


def main():
    window_title = u'雷电模拟器-2'  # 替换为你要调整的窗口标题
    hwnd, rect = get_window_info(window_title)

    if hwnd and rect:
        new_width = 600  # 新的宽度
        resize_window(hwnd, new_width)
        print(f"窗口 {window_title} 的大小已调整为 {new_width} 像素宽，高度为 {int(new_width * 0.58)} 像素")
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