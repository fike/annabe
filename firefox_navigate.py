#!/usr/bin/env python
#
__author__ = "Leandro Cassiano and Fernando Ike"
__copyright__ = "Copyright 2015, Annabe"
__credits__ = [""]
__license__ = "Apache-2"
__version__ = "0.1"
__maintainer__ = "Leandro Cassiano"
__email__ = "leandro@wetware.com.br"
__status__ = "Development"

import time
import sys
from selenium import webdriver

fp = webdriver.FirefoxProfile()

#fp.add_extension(extension='/opt/annabe/dns_flusher-3.0.1-fx.xpi')
fp.add_extension(extension='/opt/annabe/firebug-1.12.8b1-fx.xpi');
fp.add_extension(extension='/opt/annabe/netExport-0.9b7.xpi');

fp.set_preference("extensions.firebug.currentVersion", "1.12.8b1"); #Avoid startup screen
fp.set_preference("extensions.firebug.allPagesActivation", "on");
fp.set_preference("extensions.firebug.defaultPanelName", "net");
fp.set_preference("extensions.firebug.net.enableSites", True);
fp.set_preference("extensions.firebug.net.persistent", True);
fp.set_preference("extensions.firebug.net.onByDefault", True);

fp.set_preference("extensions.firebug.netexport.alwaysEnableAutoExport", True);
fp.set_preference("extensions.firebug.netexport.showPreview", False);
fp.set_preference("extensions.firebug.netexport.defaultLogDir", "/tmp");
fp.set_preference("extensions.firebug.netexport.autoExportToFile", True);
fp.set_preference("extensions.firebug.netexport.sendToConfirmation", False);
fp.set_preference("extensions.firebug.netexport.pageLoadedTimeout", 6000);
fp.set_preference("extensions.firebug.netexport.Automation", True);

URL = str(sys.argv[1])

browser = webdriver.Firefox(firefox_profile=fp)
browser.get(URL)
browser.close()
