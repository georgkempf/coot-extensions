def jump_from_symmetry_on_click():
    import re
    import os
    '''
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
    '''
    logfile = 'logfile.txt'
    if not os.path.exists(logfile):
        info_dialog_and_text("No logfile found! Check if coot output is redirected to a logfile. See readme for further instructions.")
    else:
        with open(logfile,'r') as file:
            for line in reversed(file.readlines()):
                if re.match(r'\(\d+\)\s*.+\s*/\d+/chainid=\".+\"/\d+/.+,\s*occ:.*', line):
                    print("yes")
                    groups = re.match(r'\(\d+\)\s*(.+)\s*/\d+/chainid=\"(.+)\"/(\d+)/(.+),\s*occ:.*', line)
                    chain_id = groups.group(2)
                    resno = groups.group(3)
                    atom_name = groups.group(1)
                    
                    print(atom_name)
                    print(resno)
                    print(chain_id)
                    break
                    
            if not chain_id is None or not resno is None or not atom_name is None:        
                set_go_to_atom_chain_residue_atom_name(chain_id, int(resno), atom_name)
            else:
                info_dialog_and_text("Found no atom information. Click on a (symmetry) atom before executing this command!")
 
add_key_binding("Jump from symmetry mate", "s", lambda: jump_from_symmetry_on_click())
