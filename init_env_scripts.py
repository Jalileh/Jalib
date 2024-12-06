#!/usr/bin/env python
import JB_utils as jb   


bashrc_PathName = jb.GetBashrcPath()

scriptPathNames = ['C:/Users/fayar/Desktop/PagefileMon']

def AddShellPaths():
    with open(bashrc_PathName, "a") as f:
        for name in scriptPathNames:
            f.write(f'#PathGen\nexport PATH="${{PATH}}:{name}"')
            

AddShellPaths()
        
    

