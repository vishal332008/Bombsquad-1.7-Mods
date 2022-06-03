
# ba_meta require api 6
from __future__ import annotations
import copy
import time
from typing import TYPE_CHECKING
import os
import _ba
import ba
import shutil
import time
import threading
from enum import Enum
from dataclasses import dataclass
if TYPE_CHECKING:
    from typing import Any, Optional, Dict, List, Tuple,Type
    import ba
    from bastd.ui.gather import GatherWindow



#  https://discord.gg/CbxhJTrRta    join for mmore mods updates     BOMBSPOT 

# CHARACTER PACK1  -PLUGIN BY MRSMOOTHY   ( CHARACTERS BY  byANG3L)

#    contains 4 sub plugins    set1 ,set 2, set 3 ,restore original

#    enable required sets only    to avoid game lag on VERY LOW end devices ( <= 1gb ram )-  will work on most of the devices tho 

#   SET 1  CHARACTERS 
  #     alien > bowser
#       butch > Koopa paratrropa
#       gladiator > Mario
#       gretel   >   peach

#     SET 2 CHARACTERS
#       lee      >  yoshi
#       middle-man  > deadpool
#         oldlady  >  CTCD courage
#           robot    >   S-117

#      SET 3 CHARACTERS
#         todd mcbuton  > Pikachu
#        warrior  > Black panther
#        witch > broly
#      wrestler  > ash ketchum
#        zola > Bendy


#  ENABLE ONLY SETS REQUIRED ..OR ALL   YOUR WISH 

#  =========== TO UNINSTALL CHARACTER  ==================== 
#              DISABLE ALL SETS CHECKBOXS
#              ENABLE RESTORETOORIGINAL PLUGIN 
#               restart game .
# if not help !! uninstall game   .rip 


#only you will be able to see them ...... not other players (if they not installed this mod)

#so share this mod with all of  your frinds ..and enjoy 
from bastd.ui.confirm import ConfirmWindow
# discord @mr.smoothy#5824


#character by byAng3L
import bastd.ui.mainmenu as bastd_ui_mainmenu




#  All characters ..made by byAngel and team , I (mr.smoothy) just made this characters installer to make  them USABLE  online  with bs 1.5 + :;  with permission from character owner (byAng3l)

# All charactes rights hold by byANG3L  @ ! JoseANG3LYT#0268   

# This script rights hold by @Mr.Smoothy#5824 

# to use another set of characters .. take permission from character owner  byANG3L
# if releasing this script with another characters set take permission from Mr.Smoothy 


# YOU WILL BE SENTENCED TO DEATH IF TRY TO MODIFY SCRIPT , CREDITS , CHARACTERS 

#join bombspot discord group ...for more mods/plugins

#mode set of characters will be released on bombspot #mods  
newfilesdir=os.path.join(_ba.env()["python_directory_user"],"characterpack1" + os.sep)
mdo=_ba.env()["python_directory_user"]

def copy3():
    global newfilesdir
    
    filesdir=os.path.join(newfilesdir,"set3" + os.sep)
    files=os.listdir(filesdir)
    print("doing set3")
    for file in files:
        if file.endswith('.ktx') or file.endswith('.dds'):
            copytexture(file,filesdir)
        if file.endswith('.bob') or file.endswith('cob'):
            copymodel(file,filesdir)
        if file.endswith('.ogg'):
            copysounds(file,filesdir)
def copy2():
    global newfilesdir
    
    filesdir=os.path.join(newfilesdir,"set2" + os.sep)
    files=os.listdir(filesdir)
    print("doing set2")
    for file in files:
        if file.endswith('.ktx') or file.endswith('.dds'):
            copytexture(file,filesdir)
        if file.endswith('.bob') or file.endswith('cob'):
            copymodel(file,filesdir)
        if file.endswith('.ogg'):
            copysounds(file,filesdir)
    
def copy1():
    global newfilesdir
    filesdir= os.path.join(newfilesdir,"set1" + os.sep)
    ba.screenmessage("hi copying files")
    files=os.listdir(filesdir)
    print("doing set1")
    for file in files:
        if file.endswith('.ktx') or file.endswith('.dds'):
            copytexture(file,filesdir)
        if file.endswith('.bob') or file.endswith('cob'):
            copymodel(file,filesdir)
        if file.endswith('.ogg'):
            copysounds(file,filesdir)  
    

def copymodel(src,dirct):
    
        
    shutil.copyfile(dirct+src, "ba_data/models/"+src)

def copytexture(src,dirct):
    shutil.copyfile(dirct+src, "ba_data/textures/"+src)

def copysounds(src,dirct):
    shutil.copyfile(dirct+src, "ba_data/audio/"+src)

def install1():
    copy1()
    if os.path.isfile(os.path.join(_ba.env()["python_directory_user"],"c1set1.txt")):
        
        if open(os.path.join(_ba.env()["python_directory_user"],"c1set1.txt"),"r").read()== "True":
            print("set 1 already installed skipping")
        else:
            copy1()
            open(os.path.join(_ba.env()["python_directory_user"],"c1set1.txt"),"w").write("True")

    else:

        copy1()
        open(os.path.join(_ba.env()["python_directory_user"],"c1set1.txt"),"w").write("True")
def install2():
    if os.path.isfile(os.path.join(_ba.env()["python_directory_user"],"c1set2.txt")):
        
        if open(os.path.join(_ba.env()["python_directory_user"],"c1set2.txt"),"r").read()== "True":
            print(" set 2 already installed skipping")
        else:
            copy2()
            open(os.path.join(_ba.env()["python_directory_user"],"c1set2.txt"),"w").write("True")

    else:

        copy2()
        open(os.path.join(_ba.env()["python_directory_user"],"c1set2.txt"),"w").write("True")

def install3():
    if os.path.isfile(os.path.join(_ba.env()["python_directory_user"],"c1set3.txt")):
        
        if open(os.path.join(_ba.env()["python_directory_user"],"c1set3.txt"),"r").read()== "True":
            print("set 3 already installed skipping")
        else:
            copy3()
            open(os.path.join(_ba.env()["python_directory_user"],"c1set3.txt"),"w").write("True")

    else:

        copy3()
        open(os.path.join(_ba.env()["python_directory_user"],"c1set3.txt"),"w").write("True")
def restoreset1():
    global newfilesdir
    
    filesdir=os.path.join(newfilesdir,"org" + os.sep)
    files=os.listdir(filesdir)
    print("restoring set 1")
    set1=['alien','cowboy','gladiator','operaSinger']
    for cname in set1:
        for file in files:
            if file.endswith('.ktx') or file.endswith('.dds'):
                shutil.copyfile(filesdir+file, "ba_data/textures/"+file.replace("neoSpaz",cname))
            if file.endswith('.bob') or file.endswith('cob'):
                shutil.copyfile(filesdir+file, "ba_data/models/"+file.replace("neoSpaz",cname))
            if file.endswith('.ogg'):
                shutil.copyfile(filesdir+file, "ba_data/audio/"+file.replace("neoSpaz",cname))
def restoreset2():
    global newfilesdir
    
    filesdir=os.path.join(newfilesdir,"org" + os.sep)
    files=os.listdir(filesdir)
    print("restoring set 2")
    set2=['jumpsuit','oldLady','robot','superhero']
    for cname in set2:
        for file in files:
            if file.endswith('.ktx') or file.endswith('.dds'):
                shutil.copyfile(filesdir+file, "ba_data/textures/"+file.replace("neoSpaz",cname))
            if file.endswith('.bob') or file.endswith('cob'):
                shutil.copyfile(filesdir+file, "ba_data/models/"+file.replace("neoSpaz",cname))
            if file.endswith('.ogg'):
                shutil.copyfile(filesdir+file, "ba_data/audio/"+file.replace("neoSpaz",cname))

def restoreset3():
    global newfilesdir
    
    filesdir=os.path.join(newfilesdir,"org" + os.sep)
    files=os.listdir(filesdir)
    print("restoring set 3")
    set1=['actionHero','assassin','warrior','witch','wrestler']
    for cname in set1:
        for file in files:
            if file.endswith('.ktx') or file.endswith('.dds'):
                shutil.copyfile(filesdir+file, "ba_data/textures/"+file.replace("neoSpaz",cname))
            if file.endswith('.bob') or file.endswith('cob'):
                shutil.copyfile(filesdir+file, "ba_data/models/"+file.replace("neoSpaz",cname))
            if file.endswith('.ogg'):
                shutil.copyfile(filesdir+file, "ba_data/audio/"+file.replace("neoSpaz",cname))

def restore1():
    if os.path.isfile(os.path.join(_ba.env()["python_directory_user"],"c1set1.txt")):
        if open(os.path.join(_ba.env()["python_directory_user"],"c1set1.txt")).read()=="False":
            print("already original")
        else:
            restoreset1()
            open(os.path.join(_ba.env()["python_directory_user"],"c1set1.txt"),"w").write("False")
    else:
        restoreset1()
        open(os.path.join(_ba.env()["python_directory_user"],"c1set1.txt"),"w").write("False")
def restore2():
    if os.path.isfile(os.path.join(_ba.env()["python_directory_user"],"c1set2.txt")):
        if open(os.path.join(_ba.env()["python_directory_user"],"c1set2.txt")).read()=="False":
            print("already original")
        else:
            restoreset2()
            open(os.path.join(_ba.env()["python_directory_user"],"c1set2.txt"),"w").write("False")
    else:
        restoreset2()
        open(os.path.join(_ba.env()["python_directory_user"],"c1set2.txt"),"w").write("False")
def restore3():
    if os.path.isfile(os.path.join(_ba.env()["python_directory_user"],"c2set3.txt")):
        if open(os.path.join(_ba.env()["python_directory_user"],"c1set3.txt")).read()=="False":
            print("already original")
        else:
            restoreset3()
            open(os.path.join(_ba.env()["python_directory_user"],"c1set3.txt"),"w").write("False")
    else:
        restoreset3()
        open(os.path.join(_ba.env()["python_directory_user"],"c1set3.txt"),"w").write("False")

# ba_meta export plugin
class set1(ba.Plugin):
    
    def __init__(self):
        
        if _ba.env().get("build_number",0) >= 20124:
            install1()
             
        else:print("workon 1.5 and above ... ")

# ba_meta export plugin
class set2(ba.Plugin):
    
    def __init__(self):
        
        if _ba.env().get("build_number",0) >= 20124:
            install2()
              
        else:print("workon 1.5 and above ... ")

# ba_meta export plugin
class set3(ba.Plugin):
    
    def __init__(self):
        
        if _ba.env().get("build_number",0) >= 20124:
            install3()
              
        else:print("workon 1.5 and above ... ")

# ba_meta export plugin
class restoreToOriginal(ba.Plugin):
    
    def __init__(self):
        
        if _ba.env().get("build_number",0) >= 20124:
            restore1()
            restore2()
            restore3()
              
        else:print("workon 1.5 and above ... ")
