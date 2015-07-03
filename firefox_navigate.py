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
from selenium import webdriver

fp = webdriver.FirefoxProfile()

#fp.add_extension(extension='/opt/annabe/dns_flusher-3.0.1-fx.xpi')
fp.add_extension(extension='/opt/annabe/firebug-2.0.11-fx.xpi')
fp.add_extension(extension='/opt/annabe/netExport-0.9b7.xpi')

fp.set_preference("extensions.firebug.currentVersion", "2.0.11") #Avoid startup screen
fp.set_preference("extensions.firebug.allPagesActivation", "on")
fp.set_preference("extensions.firebug.defaultPanelName", "net")
fp.set_preference("extensions.firebug.net.enableSites", True)

fp.set_preference("extensions.firebug.netexport.alwaysEnableAutoExport", True);
fp.set_preference("extensions.firebug.netexport.showPreview", True);
fp.set_preference("extensions.firebug.netexport.defaultLogDir", "/opt/annabe/");

browser = webdriver.Firefox(firefox_profile=fp)
browser.get('http://www.github.com/')
browser.close()
