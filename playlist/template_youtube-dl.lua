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
    local f = assert (io.popen ([[@ytdl_binary_path@ --no-check-certificate -j --flat-playlist "]] .. url .. [["]], 'r'))
    ytplaylist = {}
    for line in f:lines() do
        ljson = json.parse(line) -- line json
        table.insert(ytplaylist, { path = [[http://www.youtube.com/watch?v=]] .. ljson.url; name = ljson.title; arturl = [[http://img.youtube.com/vi/]] .. ljson.url .. [[/maxresdefault.jpg]]; })
    end
    f:close()
    return ytplaylist
end

