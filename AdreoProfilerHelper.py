# By WangXiaoLong

import os
from os import path
import Image



GLEX_VERTEX = "#_glesVertex"
GLEX_NORMAL = "#_glesNormal"
GLEX_TEXCOORD = "#_glesMultiTexCoord0"

OBJ_VERTEX = "v"
OBJ_NORMAL = "vn"
OBJ_UV = "vt"

OUTPUT_DIR = "Output"


def OutputObj(srcObjPath, dstObjPath):       

    fileNewObj = open(dstObjPath, "w+")
    fileObj = open(srcObjPath, "r")
    
    for line in fileObj:                    
        index = line.find(' ')            
        beginStr = line[0:index]
        
        if beginStr == GLEX_VERTEX :
            line = OBJ_VERTEX + line[index:]
        elif beginStr == GLEX_NORMAL:
            line = OBJ_NORMAL + line[index:]
        elif beginStr == GLEX_TEXCOORD:
            line = OBJ_UV + line[index:]
        
        fileNewObj.write(line)        
    
    fileObj.close()
    fileNewObj.flush()
    fileNewObj.close()    
    
    print "-------- " +  dstObjPath    
    
def OutputTex(srcTexPath, dstTexPath):
    im = Image.open(srcTexPath)   
    #newIM = im.rotate(180)
    newIM = im.transpose(Image.FLIP_TOP_BOTTOM)
    newIM.save(dstTexPath)
    print "-------- " + dstTexPath;
                

def ScanDir(curPath, savePath, isRecursive):
    
    listFile = os.listdir(curPath)
    
    for fileName in listFile:
        filePath = path.join(curPath, fileName)
        
        if isRecursive:
            if path.isdir(filePath) and fileName != OUTPUT_DIR:               
                saveDirPath = path.join(savePath, fileName)
                if not path.exists(saveDirPath):
                    os.mkdir(saveDirPath)
                ScanDir(filePath, saveDirPath, isRecursive)                        
                 
        if path.isfile(filePath) and fileName.lower().endswith("obj"):
            strObjPath = path.join(curPath,fileName)
            dstObjPath = path.join(savePath, fileName)            
            OutputObj(strObjPath, dstObjPath)
            
        if path.isfile(filePath) and fileName.lower().endswith(".bmp"):
            strObjPath = path.join(curPath,fileName)
            dstObjPath = path.join(savePath, fileName)   
            OutputTex(strObjPath, dstObjPath)                  
  

def SelectMode():
    print "--------- By JiShuYanFaZhongXin, WangXiaoLong --------- " 
    print "Select Run Mode:\n" \
          "1) Input 1 Means Recurse All The Directory\n" \
          "2) Input 2 Means Just Current Directory\n"
    
    
    mode = int(raw_input())     
    if mode != 1 and mode != 2:
        print mode
        print "Wrong Mode You Has Input, Please Try Again!\n\n"
        SelectMode()
    else:
        curDir = os.getcwd()    
        outputPath = os.path.join(curDir, OUTPUT_DIR)
        #outputPath = curDir
        if not os.path.exists(outputPath):
            os.mkdir(outputPath)   
        
        isRecursive = True
        if mode == 1:
            isRecursive = True
        elif mode == 2:
            isRecursive = False     
            
        ScanDir(curDir, outputPath, isRecursive)
        
        print "\nProcess Complete, Press Enter To Close!"
        raw_input()
   

SelectMode()




            


                
