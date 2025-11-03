import os
import shutil
from datetime import datetime


def organize():
    current_date_str = datetime.now().strftime("%Y%m%d")
    new_directory_name = current_date_str
    # 目标目录路径
    target_dir = os.path.abspath(new_directory_name)
    files_to_copy = [
        "pg_import_kline.csv",
        "pg_import_stock.csv"
    ]

    os.makedirs(new_directory_name, exist_ok=True)
    print(f"✅ 目录 '{new_directory_name}' 创建成功。")

    # --- 3. 复制文件 ---
    for file_name in files_to_copy:
        source_path = file_name
        # 检查文件是否存在
        if os.path.exists(source_path):
            # 使用 shutil.copy2 保留文件元数据
            shutil.copy2(source_path, target_dir)
            print(f"✅ 文件 '{file_name}' 复制成功。")
        else:
            print(f"❌ 文件 '{file_name}' 不存在，跳过复制。")

    print("\n--- 操作完成 ---")