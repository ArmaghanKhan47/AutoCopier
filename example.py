import autocopier

obj = autocopier.AutoCopier()

#Messages these method can return are following:
#[0, "Operation Performed Successfully"]
#[-1, "Invalid file name or address"]
#[-2, "No Operation were performed"]

#In both methods source is optional
obj.copyFiles("Destination", "LogFile.txt")
obj.deleteFiles("LogFile.txt")

#with source
obj.copyFiles("Destination", "LogFile.txt", source="Source")
obj.deleteFiles("LogFile.txt", source="Source")
