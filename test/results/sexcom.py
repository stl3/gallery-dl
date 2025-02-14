# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import sexcom


__tests__ = (
{
    "#url"     : "https://www.sex.com/pin/21241874-sexy-ecchi-girls-166/",
    "#comment" : "picture",
    "#category": ("", "sexcom", "pin"),
    "#class"   : sexcom.SexcomPinExtractor,
    "#pattern"     : "https://cdn.sex.com/images/.+/2014/08/26/7637609.jpg",
    "#sha1_content": "ebe1814dadfebf15d11c6af4f6afb1a50d6c2a1c",

    "comments" : int,
    "date"     : "dt:2014-10-19 15:45:44",
    "extension": "jpg",
    "filename" : "7637609",
    "likes"    : int,
    "pin_id"   : 21241874,
    "repins"   : int,
    "tags"     : list,
    "thumbnail": str,
    "title"    : "Sexy Ecchi Girls 166",
    "type"     : "picture",
    "uploader" : "mangazeta",
    "url"      : str,
},

{
    "#url"     : "https://www.sex.com/pin/55435122-ecchi/",
    "#comment" : "gif",
    "#category": ("", "sexcom", "pin"),
    "#class"   : sexcom.SexcomPinExtractor,
    "#pattern"     : "https://cdn.sex.com/images/.+/2017/12/07/18760842.gif",
    "#sha1_content": "176cc63fa05182cb0438c648230c0f324a5965fe",
},

{
    "#url"     : "https://www.sex.com/pin/55748341/",
    "#comment" : "video",
    "#category": ("", "sexcom", "pin"),
    "#class"   : sexcom.SexcomPinExtractor,
    "#pattern"     : r"https://cdn\.sex\.com/videos/pinporn/2018/02/10/776229_hd\.mp4",
    "#sha1_content": "e1a5834869163e2c4d1ca2677f5b7b367cf8cfff",
},

{
    "#url"     : "https://www.sex.com/pin/55847384-very-nicely-animated/",
    "#comment" : "pornhub embed",
    "#category": ("", "sexcom", "pin"),
    "#class"   : sexcom.SexcomPinExtractor,
    "#pattern" : "ytdl:https://www.pornhub.com/embed/ph56ef24b6750f2",
},

{
    "#url"     : "https://www.sex.com/pin/21241874/#related",
    "#category": ("", "sexcom", "related-pin"),
    "#class"   : sexcom.SexcomRelatedPinExtractor,
    "#count"   : ">= 20",
},

{
    "#url"     : "https://www.sex.com/user/sirjuan79/pins/",
    "#category": ("", "sexcom", "pins"),
    "#class"   : sexcom.SexcomPinsExtractor,
    "#count"   : ">= 15",
},

{
    "#url"     : "https://www.sex.com/user/ronin17/exciting-hentai/",
    "#category": ("", "sexcom", "board"),
    "#class"   : sexcom.SexcomBoardExtractor,
    "#count"   : ">= 15",
},

{
    "#url"     : "https://www.sex.com/search/pics?query=ecchi",
    "#category": ("", "sexcom", "search"),
    "#class"   : sexcom.SexcomSearchExtractor,
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://www.sex.com/videos/hentai/",
    "#category": ("", "sexcom", "search"),
    "#class"   : sexcom.SexcomSearchExtractor,
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://www.sex.com/pics/?sort=popular&sub=all&page=1",
    "#category": ("", "sexcom", "search"),
    "#class"   : sexcom.SexcomSearchExtractor,
},

)
