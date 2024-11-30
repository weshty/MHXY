
import common
import time
import mhxy
import win32api, win32gui
import asyncio

# 宝图任务
def bao_tu(window_size):
    global is_start
    is_start = True
    ##1、查找宝图任务是否存在，存在则点击执行，1分钟循环一次，判断宝图任务是否执行完成
    ## 宝图任务完成判断条件20分钟完成宝图任务
    if common.findpng("baotu_1.png") is not None:
        common.get_rw("baotu_1")
        time.sleep(1)
        print("宝图任务进行中")
        mhxy.button_baotu["text"] = "宝图（执行中）"
        time.sleep(30)
        mhxy.button_baotu["text"] = "宝图（已完成）"
        return
    ## 无进行中的宝图任务，则打开活动，点击宝图任务，到店小二处，触发宝图任务，开始任务，执行20分钟后完成宝图任务
    common.open_huodong()
    if not common.get_rw("baotu_rw"):
        print("宝图任务已完成")
        mhxy.button_baotu["text"] = "宝图（已完成）"
        return
    mhxy.button_baotu["text"] = "宝图（执行中）"
    common.get_rw("choice_do")     # 选择任务
    time.sleep(1)
    common.get_rw("baotu_1")     # 查找并点击宝图任务
    time.sleep(30)
    mhxy.button_baotu["text"] = "宝图（已完成）"

async def wa_baotu(window_size):
    global is_start
    is_start = True
    ##1、打开包裹，触发整理，找到宝图，点击使用，等待10s后，判断是否有使用按钮，点击使用，触发挖宝图
    # 后续30s检查一次，是否存在挖宝图按钮，连续6次未找到则退出挖宝图
    common.get_rw("baoguo",window_size)
    await asyncio.sleep(3)
    if common.findpng("wabaotu_baotu.png",window_size) is not None:
        common.get_rw("wabaotu_baotu",window_size)
        await asyncio.sleep(3)
        common.get_rw("wabaotu_shiyong",window_size)
        print("挖宝图进行中")
        await asyncio.sleep(10)
        index = 1
        count = 0
        while(is_start):

            if common.findpng("wabaotu_shiyong2.png",window_size) is not None:
                count = count + 1
                common.get_rw("wabaotu_shiyong2",window_size)
                print(f"挖宝图次数：{count}")
                await asyncio.sleep(20)
                index = 1
                continue
            if index == 6:
                is_start = False
            print(f"未到达宝图地点：{index}")
            await asyncio.sleep(20)
            index = index + 1
    print("挖宝图结束")
    return



# 运镖任务
def yun_biao(window_size):
    is_start = True
    # mhxy.button_yunbiao["text"] = "运镖（进行中）"
    print("运镖（进行中）")
    index = 1
    count = 0
    while count < 3:
        common.open_huodong(window_size)
        time.sleep(1)
        if common.get_rw("yunbiao_rw",window_size):
            count = count + 1
            time.sleep(3)
            common.get_rw("yasong",window_size)
            time.sleep(3)
            common.get_rw("yasong_qd",window_size)
            time.sleep(30)
        else:
            index = index + 1
            time.sleep(30)
            if index > 3 :
                count = 3

    # mhxy.button_yunbiao["text"] = "运镖（已完成）"
    print("运镖（已完成）")
    return None

# 抓鬼
def zhua_gui(window_size,):
    #创建队伍方式 1、打开活动，点击抓鬼任务，创建队伍，自动匹配，关闭窗口，点击抓鬼任务，等待10s,点击钟馗抓鬼任务
    #匹配队伍 1、打开活动，点击抓鬼任务，自动匹配，关闭窗口，等待60s组队成功
    # 循环判断当前是否在进行打鬼中，看是否找到任务，任务中有无抓鬼，等待次数，超过3次则退出组队，进行重新匹配

    is_start = True
    while is_start:
        if common.findpng("renwu.png",window_size) and not common.get_rw("zhuogui",window_size):
            print("打开活动")
            common.open_huodong(window_size)
            common.get_rw("zhuogui_rw",window_size)
            common.get_rw("zudui",window_size)     # 自动组队
            common.get_rw("guanbi",window_size)     # 关闭窗口
            print("组队抓鬼")
        time.sleep(60)
    return

def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)


# 启动
if __name__ == "__main__":
    #global window_region
    screen_resolution = resolution()
    print(screen_resolution)

    new_width = 600  # 新的宽度
    global is_start
    hwnd1,window_size1 = common.get_window_info(u'雷电模拟器')
    # hwnd2,window_size2 = common.get_window_info(u'雷电模拟器-1')
    # hwnd3,window_size3 = common.get_window_info(u'雷电模拟器-2')
    #
    # common.resize_window(hwnd1, new_width)
    # common.resize_window(hwnd2, new_width)
    # common.resize_window(hwnd3, new_width)

    # yun_biao(window_size1)
    zhua_gui(window_size1)


    # wa_baotu(window_size)
    # if window_size1 or window_size2 or window_size3:
    #     print("异步任务")
    #     async def main():
    #         tasks = []
    #         if window_size1:
    #             tasks.append(asyncio.create_task(wa_baotu(window_size1)))
    #         if window_size2:
    #             tasks.append(asyncio.create_task(wa_baotu(window_size2)))
    #         if window_size3:
    #             tasks.append(asyncio.create_task(wa_baotu(window_size3)))
    #         await asyncio.gather(*tasks)
    #     asyncio.run(main())