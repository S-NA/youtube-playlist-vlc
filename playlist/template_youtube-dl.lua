-- This code is hereby released into the public domain.
-- To the pedantic, if the public domain is not recognized one can prefer
-- using the ISC license.

local json = require "json"

function probe()
    return ( vlc.access == "http" or vlc.access == "https" )
    and string.match( vlc.path, "www%.youtube%.com/playlist" )
end

function parse()
    vlc.msg.info("YouTube Playlist Support via youtube-dl.")
    local url = vlc.access .. "://" .. vlc.path
    local f = assert (io.popen ([[@ytdl_binary_path@ -f best -j ]] .. url, 'r'))
    ytplaylist = {}
    for line in f:lines() do
        ljson = json.decode(line) -- line json
        table.insert(ytplaylist, { path = ljson.url; name = ljson.fulltitle; arturl = ljson.thumbnail; })
    end
    f:close()
    return ytplaylist
end

