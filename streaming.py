import asyncio
import random
from data.mock_data import SONG_DATABASE

async def search_song(song_name: str):

    print(f"กำลังค้นหาเพลง: {song_name} ...")
    await asyncio.sleep(random.uniform(1, 2))
    song = next((s for s in SONG_DATABASE if s["title"].lower() == song_name.lower()), None)
    
    if song:
        song_url = f"https://music.example.com/{song_name.replace(' ', '_')}.mp3"
        print(f"พบเพลง: {song['title']} - {song['artist']} ({song['duration']} นาที) ({song_url})")
        return song_url
    else:
        print(f"ไม่พบเพลง: {song_name}")
        return None

async def download_sample(song_url: str):
    print(f"กำลังดาวน์โหลดเพลงจาก {song_url} ...")
    await asyncio.sleep(random.randint(2, 5))
    print(f"ดาวน์โหลดเพลงจาก {song_url} สำเร็จ!")

async def play_sample(song_url: str):
    print(f"กำลังเล่นเพลงจาก {song_url} ...")
    await asyncio.sleep(3)  
    print(f"หยุดเล่นเพลงจาก {song_url}")

async def main():
    song_list = ["The Middle", "Wonderwall", "Smells Like Teen Spirit","14 อีกครั้ง", "Ocean Avenue",]
    search_tasks = [search_song(song) for song in song_list]
    song_urls = await asyncio.gather(*search_tasks)
    song_urls = [url for url in song_urls if url is not None]
    download_tasks = [download_sample(url) for url in song_urls]
    await asyncio.gather(*download_tasks)
    for url in song_urls:
        await play_sample(url)

    print("------จบการทำงานของโปรแกรมเพลง------")


asyncio.run(main())
