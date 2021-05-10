import os
import re
import socket
import subprocess

from powerline.lib import add_divider_highlight_group

DEFAULT_PATH = '/sys/class/thermal/thermal_zone0/temp'

@add_divider_highlight_group('background:divider')
def temp(pl, path=DEFAULT_PATH, fmat="{:.2f} °C"):
    with open(path, 'r') as f:
        t = f.read()

    try:
        temp = float(t.strip()) / 1000.0
    except:
        temp = ''

    return fmat.format(temp)

def network(pl):
    try:
        ssid = subprocess.check_output('iwgetid -r'.split()).decode().strip()
    except:
        ssid = ''
    try:    
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = ''
    return ''.join((ssid,' ' , ip))


def hostname(pl):
    return socket.gethostname()


def volume(pl):
    cmd = "awk -F'[][]' '/Left:/ { print $2 }' <(amixer sget Master)"
    vol = subprocess.check_output(cmd, shell=True).decode().strip()
    return vol


def bluetooth(pl):
    cmd = "bluetoothctl info".split()
    try:
        info = subprocess.check_output(cmd).decode()
    except subprocess.CalledProcessError:
        return
    else:
        try:
            dev = re.search(".*Name: (.*)\n", info).group(1).strip()
        except:
            dev = ''

    return dev        

