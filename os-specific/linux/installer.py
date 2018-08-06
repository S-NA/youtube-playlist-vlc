#!/usr/bin/env nix-shell
#!nix-shell -i python -p python27Packages.python

# START: Python 2.x and 3.x support use for urllib.
try:
  import urllib.request as urlrequest
except ImportError:
  import urllib as urlrequest
# END: Python 2.x and 3.x support use for urllib.

import os

def assertTrue(exp):
  if (not exp):
    exit('Inconsistency detected in VLC installation...')

szPathToVLC = os.path.join(os.getenv('XDG_DATA_HOME', '$HOME/.local/share'), 'vlc')
szPathToVLCAddons = os.path.join(szPathToVLC, 'lua')
szPlaylistFolder = os.path.join(szPathToVLCAddons, 'playlist')
szModulesFolder = os.path.join(szPathToVLCAddons, 'modules')

assertTrue(os.path.isdir(szPathToVLC))
assertTrue(os.path.isdir(szPathToVLCAddons))
assertTrue(os.path.isdir(szPlaylistFolder))
assertTrue(os.path.isdir(szModulesFolder))


if (os.system('command -v youtube-dl &> /dev/null') != 0):
  exit('youtube-dl is not installed... (you must install this through your package manager)')

# Install json.lua to modules.
jsonLUA = urlrequest.urlopen('https://gist.githubusercontent.com/tylerneylon/59f4bcf316be525b30ab/raw/7f69cc2cea38bf68298ed3dbfc39d197d53c80de/json.lua').read().decode('utf8')
with open(os.path.join(szModulesFolder, 'json.lua'), 'w+') as target:
  target.write(jsonLUA)

with open('../../playlist/template_youtube-dl.lua', 'r') as szLUACode:
  code = szLUACode.read().replace('@ytdl_binary_path@', 'youtube-dl')
  with open(os.path.join(szPlaylistFolder, 'youtube-dl.lua'), 'w+') as target:
    target.write(code)

