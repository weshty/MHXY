import time
import asyncio

async def shi_men(name):
    print(f"{name}师门任务")
    await asyncio.sleep(3)
    print(f"{name}师门任务3")

async def bao_tu(name):
    print(f"{name}宝图任务")
    await asyncio.sleep(3)
    print(f"{name}宝图任务3")

async def start_task(name):
    print(f"{name}师门任务开始")
    await shi_men(name)
    print(f"{name}宝图任务开始")
    await bao_tu(name)


# 启动
if __name__ == "__main__":

    print("开始异步方法")

    print("异步方法继续执行")

    async def main():
        tasks = []
        i = 0
        while(i < 3):
            i = i+1
            print(f"第{i}个窗口")
            name = f"第{i}个窗口"
            tasks.append(asyncio.create_task(start_task(name)))
        await asyncio.gather(*tasks)
    asyncio.run(main())