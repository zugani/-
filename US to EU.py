#! python3
# renameDAtes.py - 米国式MM-DD-YYYYのファイル名を欧州式DD-MM-YYYYに書き換える

import shutil,os,re

# 米国式日付のファイル名にマッチする正規表現を作る
date_pattern = re.compile(r"""
    ^(.*?)         # 日付の前の全テキスト
    ((0|1)?\d)-    # 月を表す1,2桁の数字
    ((0|1|2|3)?\d)-# 日を表す1,2桁の数字
    ((19|20)\d\d)  # 年を表す4桁の数字
    (.*?)$         # 日付の後の全テキスト
    """,re.VERBOSE)

# カレントディレクトリの全ファイルをループする
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # 日付のないファイルをスキップする
    if mo == None:
        continue

    # ファイル名を部分分解する
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # 欧州式の日付のファイル名を作る
    euro_filename = before_part + day_part +'-'+ month_part +'-'+\
                    year_part +after_part

    # ファイルのフルパス（絶対パス）を取得する
    print("renaming'{}'to'{}'...".format(amer_filename,euro_filename))
    shutil.move(amer_filename,euro_filename)    
