
# ba_meta require api 7


'''
Copy Profile info to clipboard 

Mod by : Mr.Smoothy 

discord : mr.smoothy#5824

Downloaded from https://www.youtube.com/c/heysmoothy  

Subscribe now for more amazing mods 

join Discord    https://discord.gg/ucyaesh


'''


from __future__ import annotations
import copy
import time
from typing import TYPE_CHECKING

import weakref
import _ba
import ba
import bastd.ui.mainmenu as bastd_mainmenu
if TYPE_CHECKING:
    from typing import Any, Optional, Dict, List, Tuple,Type
    import ba
import bastd.mainmenu as bas_main
import random

from bastd.ui.account import settings
refresh=settings.AccountSettingsWindow._refresh

def new_refresh(self):
  refresh(self)
  if (_ba.get_v1_account_state() == 'signed_in'):

    self.copyprofile = btn = ba.buttonwidget(
                  parent=self._subcontainer,
                  position=((self._sub_width - 250) * 0.5, -20),
                  size=(250, 60),
                  label="Get account id",
                  color=(0.55, 0.5, 0.6),
                  textcolor=(0.75, 0.7, 0.8),
                  autoselect=True,
                  on_activate_call=copyprofileinfo)

def copyprofileinfo():
  accounts= _ba.get_v1_account_misc_read_val_2('linkedAccounts', [])
  displaystr=_ba.get_v1_account_display_string()
  pbid=_ba.get_v1_account_misc_read_val_2('resolvedAccountID','UNKNOWN')
  mem={"pbid":pbid,"id":displaystr,"linked":accounts}
  if ba.clipboard_is_supported():
    ba.clipboard_set_text(str(mem))
    ba.screenmessage("copied to clipboard")
  else:
    ba.screenmessage("clipboard not supported")


# ba_meta export plugin
class bySmoothy(ba.Plugin):
    """My last ballistica plugin!"""
    def __init__(self):
        
        if _ba.env().get("build_number",0) >= 20124:
            settings.AccountSettingsWindow._refresh=new_refresh
