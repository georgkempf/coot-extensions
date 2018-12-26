# coot-extensions
Adds additional functionality to the program coot

To add this key binding to coot put this file into your .coot-preferences folder.
This key binding requires coot to write all console output to "logfile.txt" at the path were it is executed.
    
Windows: 
Replace the last line ("START ...") of the file runwincoot.bat (in WinCoot folder; e.g. C:\WinCoot)
with "coot-bin.exe > logfile.txt" and execute the batch file from console.

Linux:
Redirect output to logfile.txt. Coot must be in your path. For example:
coot > logfile.txt & or
coot | tee logfile.txt &
if you still want to get console output in parallel.
