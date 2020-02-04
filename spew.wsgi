#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/spew/")
sys.path.insert(0,"/var/www/spew/spew/")

import logging
logging.basicConfig(stream=sys.stderr)

from spew import app as application
