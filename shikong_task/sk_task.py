import sys

import common
import time
import win32api, win32gui
import asyncio


# 师门
async def shi_men(name,window_size):
    global is_start
    is_start = True
    #师门任务不需要打开活动，直接在任务中就有
    #本脚本师门任务是基于5次基础已完成的情况触发

    if common.findpng("shimen_rcrw.png",window_size) is not None:
        print(f"{name}点击师门日常任务")
        if common.get_rw("shimen_rcrw",window_size) is True:
            await asyncio.sleep(1)
            print(f"{name}点击去完成")
            common.get_rw("shimen_qwc",window_size)
            await asyncio.sleep(3)
            print(f"{name}请选择")
            common.get_rw("shimen_qxz", window_size)
            await asyncio.sleep(4)
            print(f"{name}点击任意位置(师门)")
            common.get_rw("shimen_rw", window_size)
            await asyncio.sleep(4)
    print(f"{name}点击师门任务")
    if common.get_rw("shimen_rw",window_size) is True:
        while (True):
            common.get_rw("shimen_rw", window_size)
            await asyncio.sleep(5)
            if(common.findpng("zhandouzhong.png",window_size) is not None):
                print(f"{name}师门任务战斗中")
                await asyncio.sleep(5)
                continue
            if(common.get_rw("shimen_qxz",window_size,0.8) is True):
                print(f"{name}师门任务请选择")
                await asyncio.sleep(5)
                continue
            if common.get_rw("shimen_goumai",window_size) is True:
                print(f"{name}师门任务点击购买")
                await asyncio.sleep(10)
                if common.get_rw("shimen_qxz",window_size,0.8) is True:
                    print(f"{name}师门任务点击请选择")
                    await asyncio.sleep(1)
                common.get_rw("shimen_sj",window_size)
                print(f"{name}师门任务点击上交")
                await asyncio.sleep(1)
                common.get_rw("shimen_rw",window_size)
                print(f"{name}师门任务点击任务")
                continue
            if common.get_rw("djrydf",window_size) is True:
                print(f"{name}师门任务点击任意地方继续")
                continue

            if common.findpng("shimen_wc.png",window_size) is not None:
                print(f"{name}师门任务完成")
                common.get_rw("shimen_qd",window_size)
                await asyncio.sleep(1)
                print(f"{name}师门任务关闭")
                common.get_rw("shimen_guanbi",window_size)
                while common.get_rw("shimen_shiyong",window_size) is True:
                    print(f"{name}师门任务奖励使用")
                    await asyncio.sleep(1)
                break
            if common.get_rw("shimen_shiyong",window_size) is True:
                print(f"{name}师门任务点击使用")
                continue


# 宝图任务
async def bao_tu(name,window_size):
    global is_start
    is_start = True
    ## 无进行中的宝图任务，则打开活动，点击宝图任务，到店小二处，触发宝图任务，开始任务，执行20分钟后完成宝图任务
    if common.findpng("baotu_rc.png",window_size) is None:
        common.get_rw("huodong", window_size)
        await asyncio.sleep(3)
        if not common.get_rw("baotu_rw", window_size):
            print(f"{name}宝图任务已完成")
            await asyncio.sleep(1)
            common.get_rw("guanbi", window_size)
            return
        else:
            print(f"{name}宝图任务执行中")
            await asyncio.sleep(20)
            common.get_rw("qingxuanze_rw", window_size)  # 选择任务
            print(f"{name}宝图任务-选择任务执行中")
            await asyncio.sleep(2)
            common.get_rw("baotu_rc", window_size)  # 查找并点击宝图任务
            print(f"{name}宝图任务-查找并点击宝图任务")
            await asyncio.sleep(2)
            common.get_rw("baotu_rc", window_size)

            # 宝图任务进行中
            # 每隔60秒检查一次右侧任务栏是否存在宝图日常，且未在战斗中（天覆阵是否在使用）
            # 检查20次后默认已完成，统计宝图任务完成时间
            i = 1
            baotu_time = 1;
            while(i < 20):
                print(f"{name}宝图任务执行中{i}")
                await asyncio.sleep(60)
                baotu_time = baotu_time + 60
                if common.findpng("zhandouzhong.png", window_size) is None \
                        and common.findpng("baotu_rc.png", window_size) is None:
                    print(f"{name}宝图任务已完成")
                    await asyncio.sleep(1)
                    i = 20
                i = i + 1
            print(f"{name}宝图任务总共花费时间：{baotu_time}")
    else:
    ##1、查找宝图任务是否存在，存在则点击执行，1分钟循环一次，判断宝图任务是否执行完成
    ## 宝图任务完成判断条件20分钟完成宝图任务
        common.get_rw("baotu_rc",window_size)
        print(f"{name}宝图任务进行中")
        i = 1
        baotu_time = 1;
        while (i < 20):
            print(f"{name}宝图任务执行中{i}")
            await asyncio.sleep(60)
            baotu_time = baotu_time + 60
            if common.findpng("zhandouzhong.png", window_size) is None \
                    and common.findpng("baotu_rc.png", window_size) is None:
                print(f"{name}宝图任务已完成")
                await asyncio.sleep(1)
                i = 20
            i = i + 1
        print(f"{name}宝图任务总共花费时间：{baotu_time}")


async def wa_baotu(name,window_size):
    global is_start
    is_start = True
    ##1、打开包裹，触发整理，找到宝图，点击使用，等待10s后，判断是否有使用按钮，点击使用，触发挖宝图
    # 后续30s检查一次，是否存在挖宝图按钮，连续6次未找到则退出挖宝图
    common.get_rw("baoguo",window_size)
    await asyncio.sleep(3)
    if common.findpng("wabaotu_baotu.png",window_size) is not None:
        common.get_rw("wabaotu_baotu",window_size)
        await asyncio.sleep(3)
        common.get_rw("wabaotu_shiyong", window_size)
        count = 0
        while(True):

            print(f"{name}挖宝图进行中")
            await asyncio.sleep(10)
            while(common.findpng("zhandouzhong.png",window_size)) is not None:
                print(f"{name}挖宝图战斗中")
                await asyncio.sleep(5)
            if common.findpng("wabaotu_shiyong2.png",window_size) is None:
                count = count + 1
                print(f"{name}挖宝图进行中未找到使用{count}")
            else:
                print(f"{name}挖宝图点击使用")
                common.get_rw("wabaotu_shiyong2", window_size)
                count = 0
            await asyncio.sleep(1)
            if count > 5 :
                break

    print(f"{name}挖宝图结束")


async def mijing(name,window_size):
    await asyncio.sleep(3)
    name = name + "秘境"
    ##1、判断当前是否正在进行秘境降妖任务，存在这继续，不存在则打开活动
    # 1、打开活动找到秘境降妖任务，点击秘境降妖，选则任务，点击一江风，点击秘境任务
    if common.findpng("mijing_rw2.png",window_size) is False:
        await asyncio.sleep(3)
        print(f"{name}打开活动")
        common.get_rw("huodong",window_size)
        await asyncio.sleep(3)
        print(f"{name}点击秘境任务")
        common.get_rw("mijing_rw",window_size)
        await asyncio.sleep(5)
        print(f"{name}点击请选择")
        common.get_rw("qingxuanze_rw",window_size)
        await asyncio.sleep(3 )
        print(f"{name}点击一江风")
        common.get_rw("mijing_yjf",window_size)
        await asyncio.sleep(2)
        print(f"{name}点击挑战")
        common.get_rw("mijing_tz",window_size)
        await asyncio.sleep(3)
        print(f"{name}点击秘境任务")
        common.get_rw("mijing_rw2", window_size)

        await mijing_flag2(name, window_size)
        print(f"{name}秘境任务结束")
    else:
        await mijing_flag2(name,window_size)
        print(f"{name}秘境任务结束")

async def mijing_flag2(name,window_size):
    print(f"{name}点击秘境任务")
    common.get_rw("mijing_rw2", window_size)
    await asyncio.sleep(3)
    while (True):
        print(f"{name}点击请选择")
        if common.get_rw("qingxuanze_rw", window_size) is True:
            await asyncio.sleep(5)
        while (common.findpng("zhandouzhong.png", window_size) is not None):
            print(f"{name}战斗中。。。")
            await asyncio.sleep(30)
        if common.findpng("mijing_sb.png", window_size) is not None:
            print(f"{name}点击失败")
            common.get_rw("mijing_sb", window_size)
            await asyncio.sleep(5)
            while (common.get_rw("mijing_sy", window_size) is not None):
                print(f"{name}点击秘境使用")
                await asyncio.sleep(5)

            print(f"{name}点击离开")
            common.get_rw("mijing_lk", window_size)
            print(f"{name}秘境任务离开")
            break



# 运镖任务
async def yun_biao(name,window_size):
    is_start = True
    print("运镖（进行中）")
    # 打开活动，点击运镖任务，点击押送，检查活跃度，活跃度不足直接退出
    # 否则点击确定压缩
    common.get_rw("huodong",window_size)
    await asyncio.sleep(3)
    if common.get_rw("yunbiao_rw", window_size):
        await asyncio.sleep(10)
        common.get_rw("yasong", window_size)
        await asyncio.sleep(3)
        if common.findpng("yunbiao_hyjc.png", window_size):
            print(f"{name}运镖（进行中）活跃度检查不足50，先完成其他任务")
            common.get_rw("yasong_qd", window_size)
            await asyncio.sleep(1)
            common.get_rw("guanbi", window_size)
            return
        common.get_rw("yasong_qd", window_size)
        print(f"{name}运镖（进行中）1次")
        await asyncio.sleep(30)

    index = 1
    count = 1
    # 检查第一轮押送是否完成，完成则进行后一轮押送
    while index < 20:
        await asyncio.sleep(60)
        if common.findpng("qingxuanze_rw.png",window_size) is not None:
            count = count +1
            common.get_rw("qingxuanze_rw",window_size)
            await asyncio.sleep(5)
            common.get_rw("yasong_qd", window_size)
            print(f"{name}运镖（进行中）{count}次")
        index = index +1
        if count == 3:
            index = 20
    print(f"{name}运镖（已完成）")

# 抓鬼
async def zhua_gui(name,window_size,):
    #创建队伍方式 1、打开活动，点击抓鬼任务，创建队伍，自动匹配，关闭窗口，点击抓鬼任务，等待10s,点击钟馗抓鬼任务
    #匹配队伍 1、打开活动，点击抓鬼任务，自动匹配，关闭窗口，等待60s组队成功
    # 循环判断当前是否在进行打鬼中，看是否找到任务，任务中有无抓鬼，等待次数，超过3次则退出组队，进行重新匹配

    is_start = True
    while is_start:
        if common.findpng("renwu.png",window_size) and not common.get_rw("zhuogui",window_size):
            print(f"{name}打开活动")
            common.open_huodong(window_size)
            common.get_rw("zhuogui_rw",window_size)
            common.get_rw("zudui",window_size)     # 自动组队
            common.get_rw("guanbi",window_size)     # 关闭窗口
            print(f"{name}组队抓鬼")
        await asyncio.sleep(60)
    return

async def sanjie(name,window_size):
    # 打开活动，从下向上滑动50，查找三界奇缘任务
    common.get_rw("huodong",window_size)
    center_x, center_y = common.get_window_center(window_size)
    if center_x and center_y:
        print(f"{name}窗口中心位置: ({center_x}, {center_y})")
        i = 0
        count = 0
        is_check = False
        while i < 10:
            await asyncio.sleep(3)
            i = i+1
            common.get_move_to_scroll(center_x,center_y)
            print(f"{name}滚轮向下滚动20")
            if common.findpng("sanjie_rw.png",window_size) is not None:
                count = count +1
                if count == 2:
                    common.get_rw("sanjie_rw",window_size)
                    await asyncio.sleep(5)
                    print(f"{name}找到三界任务并点击处理")
                    is_check = True
                    i = 5
    if is_check is True:
        i = 0
        while i < 10:
            pos = common.findpng("sanjie_qz.png", window_size)
            print(f"{name}找到求助坐标，并上移50px点击")
            common.click(pos[0] + pos[2] - 6, pos[1] + pos[3] - 50, window_size)
            await asyncio.sleep(5)
            i = i +1
        common.get_rw("sanjie_gb", window_size)

async def qingkongbeibao(name,window_size):
    print(f"{name} 打开包裹")
    common.get_rw("baoguo",window_size)
    await asyncio.sleep(3)
    while common.findpng("jingtie.png",window_size) is not None:
        print(f"{name} 点击精铁")
        common.get_rw("jingtie",window_size)
        await asyncio.sleep(2)
        print(f"{name} 点击商会出售")
        common.get_rw("shanghuichushou",window_size)
        await asyncio.sleep(2)
        print(f"{name} 点击出售")
        common.get_rw("chushou",window_size)
        await asyncio.sleep(2)

    while common.findpng("zhizaoshu.png",window_size,0.5) is not None:
        print(f"{name} 点击制造书")
        common.get_rw("zhizaoshu",window_size,0.5)
        await asyncio.sleep(2)
        print(f"{name} 点击商会出售")
        common.get_rw("shanghuichushou",window_size)
        await asyncio.sleep(2)
        print(f"{name} 点击出售")
        common.get_rw("chushou",window_size)
        await asyncio.sleep(2)
    print(f"{name} 点击整理")
    common.get_rw("zhengli",window_size)
    print(f"{name} 点击关闭")
    await asyncio.sleep(3)
    common.get_rw("guanbi",window_size)

def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

async def start_task(name,window_size):
    # print(f"{name}点击空白出关闭")
    # common.get_rw("djkbgb",window_size)
    # await asyncio.sleep(1)
    # common.get_rw("djkbgb", window_size)
    #
    #common.click_at_offset(20, 45, window_size)
    #await asyncio.sleep(1)
    #common.get_rw("ditu_changan",window_size)
    #await asyncio.sleep(3)
    #print(f"{name}师门任务开始")
    #await shi_men(name,window_size)
    #print(f"{name}宝图任务开始")
    #await bao_tu(name,window_size)
    print(f"{name}挖宝图任务开始")
    await wa_baotu(name,window_size)
    # print(f"{name}清空包裹开始")
    # await qingkongbeibao(name,window_size)
    # print(f"{name}秘境任务开始")
    # await mijing(name,window_size)
    # print(f"{name}运镖任务开始")
    # await yun_biao(name, window_size)
    # print(f'{name}三界任务开始')
    # await sanjie(name,window_size)
    # print(f"{name}运镖任务开始")
    # await yun_biao(name,window_size)
    # print(f"{name}所有任务结束")


# 启动
if __name__ == "__main__":
    screen_resolution = resolution()
    print(screen_resolution)

    new_width = 470  # 新的宽度
    global is_start
    hwnds = common.get_windows(u'梦幻西游：时空')
    if hwnds is None:
        print("窗口未打开")
        sys.exit()
    print("异步任务")


    async def main():
        tasks = []
        for i, (hwnd, window_size) in enumerate(hwnds, start=1):
            print(f"第{i}个窗口：句柄为 {hwnd}, 矩形区域: {window_size}")
            common.resize_window(hwnd, new_width)
            window_size = common.get_window_size(hwnd)
            print(f"第{i}个窗口：句柄为 {hwnd}, 新的矩形区域: {window_size}")
            name = f"第{i}个窗口"
            tasks.append(asyncio.create_task(start_task(name,window_size)))
        await asyncio.gather(*tasks)
    asyncio.run(main())