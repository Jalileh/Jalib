#!/usr/bin/env python
import JB_utils as jb


bashrc_PathName = jb.GetBashrcPath()

 
scriptPathNames = [f"{jb.GetUserProfile()}/Desktop/PagefileMon", 
                   f"{jb.GetUserProfile()}/jalib/bin",
                   f"{jb.GetUserProfile()}//jalib/shell",
                   f"{jb.GetUserProfile()}//jalib/shell/bin",
                   f"{jb.GetUserProfile()}//jalib/shell/pykek",
                   f"{jb.GetUserProfile()}//jalib/shell/processor"
]





def AddShellPaths():
    with open(bashrc_PathName, "a") as f:
        for name in scriptPathNames:
            f.write(f'\n#PathGen\nexport PATH="${{PATH}}:{name}"')


 

BASHRC_DATA = """

alias g="git.sh"
alias g2= "git-automation.sh"
alias pjc="pjconf.sh"
alias pjm="pjm.sh"

alias lg="lazygit"

 
# Set the maximum number of commands to save in history
HISTSIZE=1000

# Set the maximum number of lines in the history file
HISTFILESIZE=2000

# Append history entries instead of overwriting the history file
shopt -s histappend

# Save each command as it's entered
PROMPT_COMMAND='history -a'


alias clearhistory='history -c'

alias cbb='cd "$(findproj.exe)"'
alias cbr='cd "$(findproj.exe)/build/release"'
alias cbd='cd "$(findproj.exe)/build/debug"'

alias bsr='pjc bsr'
alias bsd='pjc bsd'
alias sr='pjc sr'
alias sd='pjc sd'
alias bd='pjc bd'
alias br='pjc br'


alias restart='g restart'

alias nv='startNvim.sh'
alias nvim='startNvim.sh'


alias branch='g branch'
"""


bashrc_PathName = jb.GetBashrcPath()
with open(bashrc_PathName, "w") as f:
    f.write(BASHRC_DATA)

AddShellPaths()
