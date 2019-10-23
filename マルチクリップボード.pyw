#! python3
# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save <keyword> -クリップボードをキーワードに紐付けて保存
# py.exe mcb.pyw <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
# py.exe mcb.pyw list - 全キーワードをクリップボードにコピー
# py.exe mcb.pyw delete <keyword> - キーワードに紐付けられたテキストを削除
# py.exe mcb.pyw delete - すべてのキーワードを削除

import shelve,pyperclip,sys

mcb_shelf = shelve.open("mcb")

#TODO クリップボードの内容を保存
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    #キーワード一覧と内容の読み込み
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == "delete":
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
