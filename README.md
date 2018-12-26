# coot-extensions
Adds additional functionality to the program coot

jump_from_symmetry:
    This key binding allows to jump from a symmetry atom to the atom in the 'original' molecule. Before pressing
    the respective key (default: s) the atom needs to be selected by clicking.

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
