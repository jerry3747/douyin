#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'

import sys
import os


def app_path():
    if hasattr(sys, 'frozen'):
    # Handles PyInstaller
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


a = app_path()
print(a)