#定義類別 與類別屬性(封裝在類別中的變數和函式)
#定義一個類別 IO, 有兩個屬性 SupportedSrcs 和 read
class IO: #input output
    supportedSrcs=["console","file"] #來源=終端機 , 檔案
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported") #不支援
        else:
            print("Read from",src)
        # print("Read from", src)
#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")