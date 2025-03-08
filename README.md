# Download Song With Python Asyncio

## ผู้ทำ

นายทนุธรรม ศุภผล 6710110151

## Asyncio คืออะไร?

**`asyncio`** เป็นโมดูลใน Python ที่ช่วยให้เราสามารถเขียนโปรแกรมที่ทำงานหลายๆ อย่างพร้อมกันได้ เช่น การค้นหาเพลง ดาวน์โหลดเพลง และเล่นเพลงพร้อมกัน โดยไม่ต้องรอให้งานหนึ่งเสร็จก่อนจึงจะทำงานถัดไปได้

### ส่วนประกอบหลักของ asyncio:

1. **Event Loop (วงจรการทำงาน)**:

   - เปรียบเสมือนผู้จัดการงานที่คอยดูแลว่างานไหนพร้อมทำ งานไหนต้องรอ
   - จัดการการทำงานของ coroutines และ tasks ต่างๆ
   - ทำให้โปรแกรมสามารถทำงานหลายๆ อย่างพร้อมกันได้อย่างมีประสิทธิภาพ
   - เช่น สามารถค้นหาเพลงหลายๆ เพลงพร้อมกัน โดยไม่ต้องรอให้ค้นหาเพลงแรกเสร็จก่อน

2. **Coroutines (ฟังก์ชันพิเศษ)**:

   - เป็นฟังก์ชันที่สามารถหยุดการทำงานชั่วคราวและกลับมาทำงานต่อได้
   - ใช้คำสั่ง `async def` ในการสร้าง coroutine
   - ใช้คำสั่ง `await` เพื่อบอกว่าต้องรอผลลัพธ์จากการทำงานอื่น
   - ตัวอย่างเช่น:
     ```python
     async def search_song(song_name):
         print(f"กำลังค้นหาเพลง {song_name}")
         await asyncio.sleep(1)
         print(f"ค้นหาเพลง {song_name} เสร็จแล้ว")
     ```

3. **Tasks (งานที่ต้องทำ)**:

   - เป็นตัวแทนของ coroutines ที่ถูกจัดการโดย event loop โดย tasks จะทำหน้าที่รัน coroutines
   - สามารถใช้ `asyncio.create_task` เพื่อสร้าง tasks ใหม่
   - ทำให้สามารถรันหลายๆ งานพร้อมกันได้
   - ตัวอย่างเช่น:
     ```python
     tasks = [
         asyncio.create_task(search_song("เพลง 1")),
         asyncio.create_task(search_song("เพลง 2")),
         asyncio.create_task(search_song("เพลง 3"))
     ]
     ```

4. **Futures (ผลลัพธ์ในอนาคต)**:
   - เป็นตัวแทนของผลลัพธ์ที่ยังไม่เสร็จสิ้น
   - ใช้ในการจัดการผลลัพธ์ของ asynchronous operation
   - สามารถใช้ร่วมกับ coroutines และ tasks ได้

### ความต่างระหว่าง Synchronous และ Asynchronous:

เทียบกับการทำงานในชีวิตจริง:

- **แบบ Synchronous**: ต้องทำทีละขั้นตอน เช่น ต้มน้ำให้เดือด → ใส่บะหมี่ → รอบะหมี่สุก → ทำน้ำซุป
- **แบบ Asynchronous**: ทำหลายอย่างพร้อมกัน เช่น ตั้งน้ำให้เดือด ระหว่างรอก็เตรียมเครื่องปรุง หั่นผัก ทำน้ำซุปไปด้วย

## หลักการโปรแกรมค้นหาเพลงและดาวน์โหลดพร้อมเล่นตัวอย่างโดยใช้ asyncio

### การทำงานของฟังก์ชัน Async ในโปรแกรม:

1. **ฟังก์ชัน search_song**

   ```python
   async def search_song(song_name: str):
   print(f"กำลังค้นหาเพลง: {song_name} ...")
   await asyncio.sleep(random.uniform(1, 2))
   song = next((s for s in SONG_DATABASE if s["title"].lower() == song_name.lower()), None)
   ```

   - ใช้ async ใช้เพื่อบอกว่าเป็นฟังก์ชันที่สามารถทำงานแบบ asynchronous ได้
   - async def ประกาศเป็นฟังก์ชัน async เพื่อให้สามารถใช้ await ได้
   - ใช้ await กับ asyncio.sleep() ใช้เพื่อจำลองการรอผลการค้นหาจาก API โดยไม่บล็อกการทำงานอื่น
   - ระหว่างที่รอ สามารถไปค้นหาเพลงอื่นๆ ได้พร้อมกัน

2. **ฟังก์ชัน download_sample**

   ```python
   async def download_sample(song_url: str):
   print(f"กำลังดาวน์โหลดเพลงจาก {song_url} ...")
   await asyncio.sleep(random.randint(2, 5))
   ```

   - async def ประกาศเป็นฟังก์ชัน async เพื่อให้สามารถใช้ await ได้
   - เป็น async function เพื่อให้สามารถดาวน์โหลดหลายเพลงพร้อมกันได้
   - ใช้ await เพื่อจำลองเวลาในการดาวน์โหลด
   - await asyncio.sleep(random.randint(2, 5)) จำลองการโหลดเพลงแบบซุ่มเวลา โดยไม่บล็อกการทำงานอื่น
   - สามารถดาวน์โหลดเพลงอื่นๆ ได้ในขณะที่กำลังดาวน์โหลดเพลงนี้

3. **ฟังก์ชัน play_sample**

   ```python
   async def play_sample(song_url: str):
   print(f"กำลังเล่นเพลงจาก {song_url} ...")
   await asyncio.sleep(3)
   print(f"หยุดเล่นเพลงจาก {song_url}")
   ```

   - async def ประกาศเป็นฟังก์ชัน async เพื่อให้สามารถใช้ await ได้
   - await asyncio.sleep(3) จำลองการเล่นเพลง 3 วินาที โดยไม่บล็อกการทำงานอื่น

4. **ฟังก์ชัน main**
   ```python
   async def main():
    song_list = ["The Middle", "Wonderwall", "Smells Like Teen Spirit"]
    search_tasks = [search_song(song) for song in song_list]
    song_urls = await asyncio.gather(*search_tasks)
    download_tasks = [download_sample(url) for url in song_urls]
    await asyncio.gather(*download_tasks)
   ```
   - ใช้ asyncio.gather() เพื่อรันหลาย tasks พร้อมกัน
   - สร้าง tasks สำหรับการค้นหาและดาวน์โหลดเพลงทั้งหมด
   - รอให้ทุก tasks เสร็จสิ้นด้วย await

## เหตุผลในการใช้ async

1. **ค้นหาเพลงพร้อมกัน**:
   - สามารถค้นหาเพลงหลายๆ เพลงพร้อมกัน
   - ไม่ต้องรอให้ค้นหาเพลงแรกเสร็จก่อน
2. **ดาวน์โหลดพร้อมกัน**:
   - ดาวน์โหลดเพลงหลายๆ เพลงพร้อมกัน
   - ประหยัดเวลาในการดาวน์โหลด
# SearchAndDownloadSongs
