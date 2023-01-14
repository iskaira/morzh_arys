import random
import socket
import os


def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0][-2:]
    except Exception as e:
        print(e)
        randint = random.randint(0, 26)
        print("getting random", randint)
        return randint


ip_address_id = int(get_ip_address())

cs_keys_path = "keys.txt"
with open(cs_keys_path) as f:
    lines = f.readlines()

if ip_address_id > len(lines):
    ip_address_id = ip_address_id - len(lines)

key = lines[ip_address_id].strip()

content = f'''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Valve\Half-Life]

[HKEY_CURRENT_USER\Software\Valve\Half-Life\cstrike]

[HKEY_CURRENT_USER\Software\Valve\Half-Life\cstrike\Settings]
"User Token 2"=""
"User Token 3"=""

[HKEY_CURRENT_USER\Software\Valve\Half-Life\Settings]
"EngineDLL"="hw.dll"
"User Token 2"=""
"User Token 3"=""
"ScreenWindowed"=dword:00000000
"CrashInitializingVideoMode"=dword:00000000
"ScreenWidth"=dword:00000500
"ScreenHeight"=dword:00000400
"ScreenBPP"=dword:00000020
"ValveKey"="{key}"
"EngineD3D"=dword:00000000

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced]
"HideIcons"=dword:00000000

; MOUSE
[HKEY_CURRENT_USER\Control Panel\Mouse]
"ActiveWindowTracking"=dword:00000000
;"Beep"="No"
"DoubleClickHeight"="4"
"DoubleClickSpeed"="500"
"DoubleClickWidth"="4"
"ExtendedSounds"="No"
"MouseHoverHeight"="4"
"MouseHoverTime"="400"
"MouseHoverWidth"="4"
"MouseSensitivity"="10"
"MouseSpeed"="1"
;"MouseThreshold1"="6"
;"MouseThreshold2"="10"
;"MouseTrails"="0"
;"SmoothMouseXCurve"=hex:00,00,00,00,00,00,00,00,15,6e,00,00,00,00,00,00,00,40,\
  01,00,00,00,00,00,29,dc,03,00,00,00,00,00,00,00,28,00,00,00,00,00
;"SmoothMouseYCurve"=hex:00,00,00,00,00,00,00,00,fd,11,01,00,00,00,00,00,00,24,\
  04,00,00,00,00,00,00,fc,12,00,00,00,00,00,00,c0,bb,01,00,00,00,00
;"SnapToDefaultButton"="0"
"SwapMouseButtons"="0"
'''

with open("cs1.6.reg", "w") as file:
    file.write(content)

cs_original_config_path = os.path.dirname(os.path.realpath(__file__))
cs_file_path = f"{cs_original_config_path}\\cs1.6_cfg.bat"
cs_config_file_path = f"{cs_original_config_path}\\config.cfg"
cs_file_path_2 = f"D:\\Games\\Counter-Strike 1.6 LAN NEW\\cstrike_russian\\config.cfg"

content = f'''copy \"{cs_config_file_path}\" \"{cs_file_path_2}\"'''

with open(cs_file_path, "w") as file:
    file.write(content)
