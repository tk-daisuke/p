import os
import shutil as sl
import datetime
import calendar

dt_now = datetime.datetime.now()
cur_dir = os.getcwd() #実行ファイルのパスを取得しています。
master_name = 'master.xlsx'
mastar_dir = cur_dir +"/"+ master_name

def safe_copy(copy_dir):
    """
    ファイルをコピーする。すでにあったら上書き確認
    """
    if os.path.exists(copy_dir):
        if input('上書きしますか?(y/n): ') != 'y':
            return
    sl.copyfile(mastar_dir, copy_dir)


if os.path.isfile(mastar_dir):
    input_year = input("年数を入力:")
    input_month = input("月を入力:")
    print(input_month)
    input_year = int(input_year)
    input_month = int(input_month)
    output_path = cur_dir + "/" + str(input_month) +"月/"

    month_length = calendar.monthrange(input_year, input_month)[1]

    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    for i in range(month_length):
        date_convert=  datetime.date(input_year, input_month, i+1)
        date_format = date_convert.strftime("%Y%m%d")

        excel_name = "text"
        excel_copy_file = output_path + excel_name + str(date_format) +".xlsx"
        print(excel_copy_file)
        safe_copy(excel_copy_file)

else: 
    print(mastar_dir+"マスターファイルの名前が違う")





