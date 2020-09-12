import autocopier

obj = autocopier.AutoCopier()

#if method return 0 it means operation is done no error occured duing execution
#if method return -1 or -2 means invalid file name or address provided, no files copied or deleted.

#In both methods source is optional
obj.copyFiles("Destination", "LogFile.txt")
obj.deleteFiles("LogFile.txt")

#with source
obj.copyFiles("Destination", "LogFile.txt", source="Source")
obj.deleteFiles("LogFile.txt", source="Source")