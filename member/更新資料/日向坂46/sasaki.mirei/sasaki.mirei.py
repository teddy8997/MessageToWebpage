import xlwt #写入文件
import xlrd #打开excel文件
import os

path = "G:\\MessageProject\\member\\message\\日向坂46\\佐々木美玲\\"
#新建一个excel文件
file=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet1=file.add_sheet('sub')
sheet1.write(0,0,"year")
sheet1.write(0,1,"month")

sheet = file.add_sheet('data')
sheet.write(0,0,"date")
sheet.write(0,1,"fileName")
sheet.write(0,2,"cate")
sheet.write(0,3,"content")
sheet.write(0,4,"month")
sheet.write(0,5,"time")
i = 1
j = 1
for f_name in os.listdir(path):
    if os.path.isdir(path + f_name):
        sheet1.write(i, 0, f_name[0:4])
        sheet1.write(i, 1, f_name[5:])
        for f in os.listdir(path + f_name):
            if f[24:] == "txt":
                date = f[0:6]
                sheet.write(j, 0, date)
               
                fileName = f[0:23]
                sheet.write(j, 1, fileName)
               
                cate = f[24:]
                sheet.write(j, 2, cate)
               
                with open(path + f_name + "\\" + f ,'r', encoding="utf-8") as fp:
                  all_lines = fp.readlines()
                sheet.write(j, 3, all_lines)

                fileMonth = f[4:8]
                sheet.write(j, 4, fileMonth)

                fileTime = f[8:10] + ":" + f[10:12]
                sheet.write(j, 5 , fileTime)
            elif f[24:] == "jpg" or f[24:] == "mp4":
                date = f[0:6]
                sheet.write(j, 0, date)
                
                fileName = f[0:23]
                sheet.write(j, 1, fileName)
                
                cate = f[24:]
                sheet.write(j, 2, cate)
                
                sheet.write(j, 3, "x")

                fileMonth = f[4:8]
                sheet.write(j, 4, fileMonth)
                
                fileTime = f[8:10] + ":" + f[10:12]
                sheet.write(j, 5 , fileTime)
            j = j+1
        i = i + 1    
file.save('member.xls')




