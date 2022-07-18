import errno
import os
import re
import time

# root_path=r"C:\Users\ch\Desktop\新建文件夹 (2)"
root_path=r"C:\Users\ch\Desktop\手机相册"

os.chdir(root_path)

dir = os.listdir(root_path)

for filename in dir:
    oldname = filename
    if filename.find("jpg")>0 :
        tmpTimes = re.compile(r"[0-9]{13}\(1\)\.jpg").findall(filename)
        if len(tmpTimes)>0 :
            tmpTime=tmpTimes[0]
            newTmpTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(int(tmpTime[0:10])))
            newname = "IMG_"+newTmpTime+".jpg"

            try:
                os.rename(filename,newname)
                print(filename + "->" + newname + "->" + newTmpTime)
            except OSError as e:
                if e.errno == errno.EEXIST:
                    os.remove(filename)
                    print("remove->"+newname)



            # # newname = ("IMG_201"+filename[1:]).replace("-","_")
            # newname = filename.replace("jpg",".jpg")
            # try:
            #     os.rename(filename,newname)
            #     print(oldname+"->"+newname)
            # except OSError as e:
            #     if e.errno == errno.EEXIST:
            #         os.remove(filename)
            #         print("remove->"+newname)
