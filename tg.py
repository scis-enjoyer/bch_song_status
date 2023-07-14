from pyrogram import Client
import asyncio, time
from env import token
from sp import current_track_name, current_track_artist


#### Telegram Auth

bch = Client(
    name ="",
    api_id=,
    api_hash=""
)

#### Getting info from spotify

track = current_track_name(token)
artist = current_track_artist(token)
res_spot = 'listening: '+ artist+' - ' + track

#### Telegram's bio editor


async def bio_changer(res_spot):
    await bch.start()
    await bch.update_profile(bio=res_spot)
    await bch.stop()


##### 

while True:
    try:
        
        track = current_track_name(token)
        artist = current_track_artist(token)
        res_spot = 'listening: '+ artist+' - ' + track
#        print(res_spot)
        bch.run(bio_changer(res_spot))
        time.sleep(10)
        if track or artist == 'error':
            res_spot = ''
            bch.run(bio_changer(res_spot))

    except(RuntimeWarning):
        pass

