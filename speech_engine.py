import asyncio
import edge_tts
import pygame
import os

async def speak_edge(text):
    tts = edge_tts.Communicate(
        text=text,
        voice="hi-IN-MadhurNeural"  # Indian male voice
    )
    await tts.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def speak(text):
    asyncio.run(speak_edge(text))
