import os
import time

from common import gui


def export(file_path: str):
    if os.path.exists(file_path):  # 先判断文件是否存在
        os.remove(file_path)
    gui.click(*gui.locate("./imgs/tonghuashun.png"))
    time.sleep(3)
    gui.click(*gui.locate("./imgs/home.png"))
    gui.click(*gui.locate("./imgs/individual_stock.png"))
    gui.click(200, 300, button="right")
    gui.hover(*gui.wait("./imgs/export_data.png"))
    gui.click(*gui.wait("./imgs/export_all_data.png"))
    gui.input(os.path.abspath(file_path))
    gui.enter()
    gui.enter()
    gui.wait("./imgs/operation_finished.png")
    gui.enter()
