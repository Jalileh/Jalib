import JB_utils as jb
import re

def PWD():
    return os.path.dirname(os.path.abspath(__file__))

def GetBashProfileDir():
   bashdir = ""
   env = jb.JALIB_ENV();
   paths = env.Get()['PATH']
  # Regular expression to match the desired path
   match = re.search(r"C:\\Program Files\\Git", paths)
   if match:
       return match.group(0) +  "\\etc\\profile.d"  # Extract and return the matched path
   
   return None

os = jb.os

def SetupFakeName():
    profileDir = ""
    if bashdir := GetBashProfileDir():
     profileDir = bashdir
    else: 
       jb.throwUWSError("unable to find bash home dir in ENVs")

    
    git_prompt_file = profileDir + "/git-prompt.sh"
    if os.path.exists(git_prompt_file  ):
        os.remove(git_prompt_file)
    
    
   
    current_pwd = PWD()
    preset_file_path = os.path.join(current_pwd, "media", "presetgit_profile.d")

    if not os.path.exists(preset_file_path):
        jb.throwUWSError(f"Preset file not found: {preset_file_path}")
        return

    try:
        content = ""
        with open(preset_file_path, 'r') as preset_file:
            content = preset_file.read()
            preset_file.close()
        
        print(content, "\n", git_prompt_file)
        with open(git_prompt_file, 'w') as new_file:
            new_file.write(content)
            new_file.close()

    except Exception as e:
        jb.throwUWSError(f"Error while creating git-prompt.sh: {str(e)}")

    print("CUSTOM SHELL BASH NAME SETUP DONE!")
SetupFakeName()