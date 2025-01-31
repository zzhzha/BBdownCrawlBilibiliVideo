import requests
from bs4 import BeautifulSoup
import re
import time
import os
import json




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Referer': 'https://space.bilibili.com/192243/search/dynamic?keyword=happy',
    'cookie': 'buvid3=1374B366-3546-B2B4-C030-E16B0E99C90213855infoc; b_nut=1725269413; _uuid=5DDFDFE8-525C-F37A-C6D5-1C4AB8A310101E15885infoc; header_theme_version=CLOSE; enable_web_push=DISABLE; DedeUserID=397283120; DedeUserID__ckMd5=eadd20c51c17fa49; rpdid=0zbfVGnVgF|1gvdZ6if0|44|3w1SL56M; buvid_fp_plain=undefined; buvid4=6739F451-B96A-CA1B-4E59-F376BC6024B313855-024090209-URdscrtfPt2bbwJ8muFQgfWTT8k0z3vgkvTC7Sr%2BEdSPPt8A9JG%2FegkG%2FzvwuTq%2F; hit-dyn-v2=1; is-2022-channel=1; LIVE_BUVID=AUTO4917256462768324; CURRENT_BLACKGAP=0; opus-goback=1; CURRENT_QUALITY=112; home_feed_column=5; PVID=6; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzYzOTA0NjQsImlhdCI6MTczNjEzMTIwNCwicGx0IjotMX0.QZnhBvWECmNjsldVKrDMsdtzzcaFmwNK7bhNZvUPNUs; bili_ticket_expires=1736390404; SESSDATA=6ae448e1%2C1751691413%2C2f814%2A11CjA2KNNjpFP9KZ_gq9C6pzCebYFbBpDTllN861SrP9eSZVPvqKUSdLw7IJZsx3cZiEQSVnpKSnRjNG5zLTNkcHpIN1ZPSGs0dkZGejZzQkk3SnBNUFphVTE5NVZCNGpnb0hQTGhCcWlTTk1BRXY2WF9oVXJldGIwREVJYkEtYjJTeEY1R3d2WWt3IIEC; bili_jct=5e7433e8815ca9a4a4f68131e0a6f57e; sid=6nblu4po; bsource=search_bing; browser_resolution=1897-998; bp_t_offset_397283120=1019587693761265664; fingerprint=abc5413b2be4240c9ba96f4439f2d907; CURRENT_FNVAL=4048; buvid_fp=abc5413b2be4240c9ba96f4439f2d907; b_lsid=88D9398C_1943F842C1A',


}
