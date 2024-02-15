import os
from PIL import Image, ImageDraw, ImageFont
import sys

font = ImageFont.truetype('comic-sans.ttf', size=48)

text = sys.argv[1]

if len(text) > 1000: 
  text = "Too long!"

width, height = 512, 562
img = Image.new('RGB', (width, height), color=(255, 255, 255))
canvas = ImageDraw.Draw(img)
chunks = []

chunk = ""
# print(canvas.textlength(text, font=font))
for char in text:
  chunk += char
  text_width = canvas.textlength(chunk, font=font) 
  if text_width >= (width-20):
    chunks.append(chunk[:-1])
    chunk = char

if len(chunks) == 0:
  chunks.append(chunk)

if chunks[-1] != chunk:
  chunks.append(chunk)
  
for i,chunk in enumerate(chunks):
  text_width = canvas.textlength(chunk, font=font)
  x_pos = int((width - text_width) / 2) + 10
  y_pos = 15 + i * 100
  canvas.text((x_pos, y_pos), chunk, font=font, fill='#000000')

img2 = Image.open('static/VinMeme-Small.png')
img.paste(img2, (0, 0), img2.convert('RGBA'))
img.save("meme_with_text.png")