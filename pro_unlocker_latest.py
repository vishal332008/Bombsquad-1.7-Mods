# ba_meta require api 6

from __future__ import annotations

import ba
import _ba

hello = "hello"
def completed(hi):
	return True

def main() -> None:
    if _ba.env().get("build_number", 0) >= 20577:
        ba.app.accounts_v1.have_pro = lambda: True
        ba.app.accounts_v1.on_app_launch()
        ba.app.accounts_v2.have_pro = lambda: True
        ba.app.accounts_v2.on_app_launch()
        ba.Level.complete = completed(hello)

# ba_meta export plugin
class by_Someone(ba.Plugin):
    def on_app_launch(self):
        main()