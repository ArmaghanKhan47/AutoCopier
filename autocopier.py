# Problem Statement: When you move files from one device to another, such as videos or photos from your memory card to your pc. you often forget which files you already have copied and not.
# This program automatically move the files from folder in which its placed to the destination folder and know which files to copy and which are files are already copied 
# with the help of LogFile.txt.
# This program is really helpful when you want to move files and forgot which files have been copied which are not.
# This program is helpful for video / photo editors who constantly copy files from one device to another.
# Place this program in Source Folder or provide SourFolder Address, Provide Destination Folder Full Address and LogFile.txt Full Address after that let the program do the magic
import os, shutil, copy

# Private Classes and Functions Definition Area Start

class __LogFile__:
    #LogFile Class helps in performing the operations on logfile.txt
    def __init__(self, logFileName):
        self.__logFileName__ = logFileName
        self.__isEmpty__ = True
        
    def filesInLog(self):
        # List : Provide list of files recorded in log | returns None when log file is empty
        logFile = open(self.__logFileName__, "r")
        lines = logFile.readlines()
        logFile.close()
        if lines != []:
            self.__isEmpty__ = False
            return lines
        else:
            return None
    
    def filesNotInLog(self, fileList):
        # List : returns list of file which are not recorded in log file
        # param: fileList = names of file to check
        logFileData = self.filesInLog()
        if logFileData != None and fileList != None:
            
            for x in range(len(logFileData)):
                logFileData[x] = logFileData[x].strip('\n')
            
            logFileData, fileList = set(logFileData), set(fileList)
            copyList = list(set.difference(set.union(logFileData, fileList), logFileData))
            return copyList
        else:
            return list(fileList)
        
    def commonFiles(self, fileList):
        logFileData = self.filesInLog()
        if logFileData != None and fileList != None:
            
            for x in range(len(logFileData)):
                logFileData[x] = logFileData[x].strip('\n')
                
            logFileData, fileList = set(logFileData), set(fileList)
            deleteList = list(set.intersection(logFileData, fileList))
            return deleteList if deleteList != [] else None
        else:
            return None
    
    def updateLogFile(self, fileList):
        # Function to update logfile
        logFile = open(self.__logFileName__, "a")
        if fileList != None:
            for name in fileList:
                logFile.write(name)
                logFile.write('\n')
        logFile.close()
        
    def checkLogFileExist(self):
        return os.path.exists(self.__logFileName__)  

def __fileExtensionCheck__(name):
    # Function to check that file is of required extension : Boolean
    extension = os.path.splitext(name)[1]
    # change the extension or add more extension so program know which files are needed to be copied are not on the basis of extension.
    if extension == ".mp4" or extension == ".jpg":
        return True
    else:
        return False
    
def __copyFile__(fileList, destination):
    # This function just copy files from one location to another without messing with the meta of files.
    if fileList != []:
        for fil in fileList:
            try:
                shutil.copy2(fil, destination)
                if __name__ == "__main__":
                    print("[+] Copied {} to {}".format(fil, destination))
            except FileNotFoundError:
                fileList.remove(fil)
                print("[!] Couldn't find {}".format(fil))
        return fileList if fileList != [] else None
    else:
        if __name__ == "__main__":
            print("[!] No File Copied")
        return None
        
# Private Classes and Functions Definition Area End

# API Area Start

class AutoCopier:
    def __init__(self):
        pass
    
    def copyFiles(self, destination, logFile, source = None):
        if (source is not None) and (not os.path.isdir(source)):
            return -1
        elif source is not None:
            os.chdir(source)
        if not os.path.isdir(destination):
            return -1
        
        logFileObj = __LogFile__(logFile)
        if not logFileObj.checkLogFileExist():
            return -1
        
        fileNames = os.listdir()
        # Filtering the files on the basis of extensions
        fileNames = [fi for fi in fileNames if __fileExtensionCheck__(fi)]

        # Getting list of files needed to be copied
        listt = logFileObj.filesNotInLog(fileNames)
        # Files are being copied
        copied = __copyFile__(listt, destination)
        # Log File being updated
        logFileObj.updateLogFile(copied)
        if copied is None:
            return -2
        else:
            return 0
    
    def deleteFiles(self, logFile, source = None):
        if (source is not None) and (not os.path.isdir(source)):
            return -1
        elif source is not None:
            os.chdir(source)
        
        logfile = __LogFile__(logFile)
        if not logfile.checkLogFileExist():
            return -1
        
        files = os.listdir()
        files = [fi for fi in files if __fileExtensionCheck__(fi)]
        deletList = logfile.commonFiles(files)
        if deletList != None:
            for x in deletList:
                os.remove(x)
            return 0
        else:
            return -1
        
# API Area End
       
# Actual Program Execution happens here
if __name__ == "__main__":
    print("""      ___           ___                         ___           ___           ___           ___                     ___           ___     
     /\  \         /\  \                       /\  \         /\__\         /\  \         /\  \                   /\__\         /\  \    
    /::\  \        \:\  \         ___         /::\  \       /:/  /        /::\  \       /::\  \     ___         /:/ _/_       /::\  \   
   /:/\:\  \        \:\  \       /\__\       /:/\:\  \     /:/  /        /:/\:\  \     /:/\:\__\   /\__\       /:/ /\__\     /:/\:\__\  
  /:/ /::\  \   ___  \:\  \     /:/  /      /:/  \:\  \   /:/  /  ___   /:/  \:\  \   /:/ /:/  /  /:/__/      /:/ /:/ _/_   /:/ /:/  /  
 /:/_/:/\:\__\ /\  \  \:\__\   /:/__/      /:/__/ \:\__\ /:/__/  /\__\ /:/__/ \:\__\ /:/_/:/  /  /::\  \     /:/_/:/ /\__\ /:/_/:/__/___
 \:\/:/  \/__/ \:\  \ /:/  /  /::\  \      \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  / \:\/:/  /   \/\:\  \__  \:\/:/ /:/  / \:\/:::::/  /
  \::/__/       \:\  /:/  /  /:/\:\  \      \:\  /:/  /   \:\  /:/  /   \:\  /:/  /   \::/__/     ~~\:\/\__\  \::/_/:/  /   \::/~~/~~~~ 
   \:\  \        \:\/:/  /   \/__\:\  \      \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\  \        \::/  /   \:\/:/  /     \:\~~\     
    \:\__\        \::/  /         \:\__\      \::/  /       \::/  /       \::/  /       \:\__\       /:/  /     \::/  /       \:\__\    
     \/__/         \/__/           \/__/       \/__/         \/__/         \/__/         \/__/       \/__/       \/__/         \/__/     
     __                               _           _                         
    /   __ _  _ _|_ _  _|   |_  \/   |_| ____  _ (_||_  _ __    |/ |_  _ __ 
    \__ | (/_(_| |_(/_(_|   |_) /    | | | |||(_|__|| |(_|| |   |\ | |(_|| |                                                                                                                                  
                                                                                                                                        """)
    operation = input("[>] Do you want to Copy Files(copy) or Delete Files(del): ")
    if operation == "copy":
        destinationFolder = input("[>] Enter Destination Folder Name: ")
        sourceFolder = input("[>] Enter Source Folder | Leave Empty if program placed in Source Folder: ")
        if not os.path.isdir(destinationFolder):
            print("[!] Please Provide Valid Directory Name / Address")
            exit()
        logFileAddress = input("[>] Enter Log File Name / Address if in different Directory: ")
        print("[+] Copying Files to : {}".format(destinationFolder))
        print("[+] Picking Up Log File : {}".format(logFileAddress))

        if sourceFolder != "":
            if not os.path.isdir(sourceFolder):
                print("[!] Please Provide Valid Directory Name / Address")
                exit()
            os.chdir(sourceFolder)
            print('[+] Source Provided')

        fileNames = os.listdir()
        # Filtering the files on the basis of extensions
        fileNames = [fi for fi in fileNames if __fileExtensionCheck__(fi)]

        logFileObj = __LogFile__(logFileAddress)
        if not logFileObj.checkLogFileExist():
            print("[!] Please Enter Valid Log File Name / Address")
            exit()
        # Getting list of files needed to be copied
        listt = logFileObj.filesNotInLog(fileNames)
        # Files are being copied
        copied = __copyFile__(listt, destinationFolder)
        # Log File being updated
        logFileObj.updateLogFile(copied)

        input("[>] Operation Completed | Press Enter Key to terminate")
    
    elif operation == "del":
        sourceFolder = input("[>] Enter Source Folder | Leave Empty if program placed in Source Folder: ")
        sourceBool = False
        if sourceFolder != "":
            if not os.path.isdir(sourceFolder):
                print("[!] Please Provide Valid Directory Name / Address")
                exit()
            os.chdir(sourceFolder)
            sourceBool = True
            print('[+] Source Provided')
        logFileAddress = input("[>] Enter Log File Name / Address if in different Directory: ")
        print("[+] Picking Up Log File : {}".format(logFileAddress))
        logFileObj = __LogFile__(logFileAddress)
        if not logFileObj.checkLogFileExist():
            print("[!] Please Enter Valid Log File Name / Address")
            exit()
        if sourceBool:
            print("[+] Deleting Files from : {}".format(sourceFolder))
        else:
            print("[+] Deleting Files from : {}".format(os.getcwd()))
        
        files = os.listdir()
        files = [fi for fi in files if __fileExtensionCheck__(fi)]
        deletList = logFileObj.commonFiles(files)
        
        if deletList != None:
            for x in deletList:
                os.remove(x)
                print("[+] Deleted {}".format(x))
        else:
            print("[!] No File(s) Deleted")
            
        input("[>] Operation Completed | Press Enter Key to terminate")
        
        
