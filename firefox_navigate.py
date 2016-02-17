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
from urlparse import urlparse 

URL = str(sys.argv[1])
Host = urlparse(URL).netloc


fp = webdriver.FirefoxProfile()

fp.add_extension(extension='/opt/annabe/har_export_trigger-0.5.0-beta.7-fx.xpi');

fp.set_preference("devtools.netmonitor.enabled", True);
fp.set_preference("devtools.netmonitor.har.defaultLogDir", "/tmp/har");
fp.set_preference("devtools.netmonitor.har.defaultFileName", Host+"_%y-%m-%d_%H-%M-%S");
fp.set_preference("devtools.netmonitor.har.enableAutoExportToFile", True);
fp.set_preference("devtools.netmonitor.har.forceExport", True);
fp.set_preference("devtools.netmonitor.har.includeResponseBodies", False)
fp.set_preference("devtools.toolbox.selectedTool", "netmonitor");
fp.set_preference("extensions.netmonitor.har.autoConnect", True);
fp.set_preference("extensions.netmonitor.har.enableAutomation", True);

browser = webdriver.Firefox(firefox_profile=fp)
browser.get(URL)
time.sleep(5)
browser.close()
