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

szPathToVLC = r'C:\Program Files\VideoLAN\VLC'
szPathToVLCAddons = os.path.join(szPathToVLC, 'lua')
szPlaylistFolder = os.path.join(szPathToVLCAddons, 'playlist')
szModulesFolder = os.path.join(szPathToVLCAddons, 'modules')

assertTrue(os.path.isdir(szPathToVLC))
assertTrue(os.path.isdir(szPathToVLCAddons))
assertTrue(os.path.isdir(szPlaylistFolder))
assertTrue(os.path.isdir(szModulesFolder))

# Install json.lua to modules.
jsonLUA = urlrequest.urlopen('https://gist.githubusercontent.com/tylerneylon/59f4bcf316be525b30ab/raw/7f69cc2cea38bf68298ed3dbfc39d197d53c80de/json.lua').read().decode('utf8')
with open(os.path.join(szModulesFolder, 'json.lua'), 'w+') as target:
  target.write(jsonLUA)

# Install youtube-dl.exe to playlist.
youtubeDLBinary = urlrequest.urlopen('https://youtube-dl.org/downloads/latest/youtube-dl.exe').read()
with open(os.path.join(szPlaylistFolder, 'youtube-dl.exe'), 'wb') as target:
  target.write(youtubeDLBinary)

with open('../../playlist/template_youtube-dl.lua', 'r') as szLUACode:
  code = szLUACode.read().replace('@ytdl_binary_path@', os.path.join(szPlaylistFolder, 'youtube-dl.exe'))
  with open(os.path.join(szPlaylistFolder, 'youtube-dl.lua'), 'w+') as target:
    target.write(code)

