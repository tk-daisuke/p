import os
import shutil as sl
import datetime
import calendar
import tkinter as tk
import tkinter.messagebox as messagebox

# 実行ファイルのパス取得
cur_dir = os.getcwd() 
master_name = 'master.xlsm'
mastar_dir = cur_dir +"/"+ master_name
# copy後のファイル名。
excel_name = "excel_name"


def safe_copy(copy_dir):
    """
    ファイルをコピーする。すでにあったら上書き確認
    """
    # すでにファイルが有るかチェック
    if os.path.exists(copy_dir):
        if input('上書きしますか?(y/n): ') != 'y':
            return
    sl.copyfile(mastar_dir, copy_dir)
        
# masterファイルがあった時
if os.path.isfile(mastar_dir):
    # 年月の入力を求める
    input_year = int(input("年数を入力:"))
    input_month = int(input("月を入力:"))
     # 処理回数を策定
    month_length = calendar.monthrange(input_year, input_month)[1]
    # 出力先を設定
    output_path = cur_dir + "/" + str(input_month) +"月/"

    # 出力先フォルダがあるか確認し、なければ作成
    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    # ファイルコピー　for文
    for i in range(month_length):
        # 入力した年月のフォーマットを変更する。
        date_convert=  datetime.date(input_year, input_month, i+1)
        date_format = date_convert.strftime("%Y%m%d")
        # パスとファイル名を組み合わせる。
        excel_create_path = output_path + excel_name + str(date_format) +".xlsm"
        print(excel_create_path)
        # copy実行
        safe_copy(excel_create_path)
# masterファイルがなかった時
else: 
    # エラー処理
    tk.Tk().withdraw()
    messagebox.showinfo('エラー', 'コピー元のファイル(master.xlsx)を用意してください')





