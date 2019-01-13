import os
import time
from datetime import datetime
#ファイル作成日時取得
def file_create_time(file_path):
    epoch=os.path.getctime(file_path)
    return datetime(*time.localtime(epoch)[:6])

#ファイル更新日時取得
def file_update_time(file_path):
    epoch=os.path.getmtime(file_path)
    return datetime(*time.localtime(epoch)[:6])