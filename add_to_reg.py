# Python code to add current script to the registry

# module to edit the windows registry
import winreg as reg
import os
import sys


def AddToRegistry(script_name, value):
    # in python __file__ is the instant of
    # file path where it was executed
    # so if it was executed from desktop,
    # then __file__ will be
    # c:\users\current_user\desktop

    # key we want to change is HKEY_CURRENT_USER
    # key value is Software\Microsoft\Windows\CurrentVersion\Run
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

    # open the key to make changes to
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)

    # modify the opened key
    reg.SetValueEx(open, script_name, 0, reg.REG_SZ, value)

    # now close the opened key
    reg.CloseKey(open)


# Driver Code
if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    python_path = sys.executable

    script_name = 'shortcut_restore2'
    script_path = 'restore_shortcuts.py'

    # joins the file name to end of path address
    value = python_path + ' ' + path + '\\' + script_path
    AddToRegistry(script_name, value)

    cs_reg_name = "cs1.6"
    bat_content = f"reg import {path}\{cs_reg_name}.reg"
    AddToRegistry(cs_reg_name, bat_content)

    