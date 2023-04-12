try:
    # 有可能發生例外的程式碼
    x = int(input("請輸入一個正整數: "))
    y = int(input("請輸入一個正整數: "))
    result = x / y
    print(f"{x}/{y} = {result}")
except ValueError as ve:
    # 處理使用者輸入非數字的例外
    print(f"輸入錯誤: {ve}")
except ZeroDivisionError:
    # 處理除以0的例外
    print("除以0錯誤")
except Exception as e:
    # 處理其他未知的例外
    print(f"發生未知例外: {e}")
else:
    # 當try區塊內程式碼沒有發生例外時，會執行else區塊內的程式碼
    print("程式執行完畢，沒有發生例外")
finally:
    # 無論try區塊內程式碼是否發生例外，都會執行finally區塊內的程式碼
    print("程式結束")
