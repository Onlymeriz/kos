import os
import sys
from pyrogram import Client

from Kyranlibs.Kyran.helper.adminHelpers import *
from Kyranlibs.Kyran.helper.aiohttp_helper import*
from Kyranlibs.Kyran.helper.basic import *
from Kyranlibs.Kyran.helper.cmd import *
from Kyranlibs.Kyran.helper.constants import *
from Kyranlibs.Kyran.helper.data import *
from Kyranlibs.Kyran.helper.inline import *
from Kyranlibs.Kyran.helper.interval import *
from Kyranlibs.Kyran.helper.parser import *
from Kyranlibs.Kyran.helper.PyroHelpers import *
from Kyranlibs.Kyran.helper.utility import *
from Kyranlibs.Kyran.helper.what import *


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Kyran"])

