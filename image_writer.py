from PIL import Image, ImageDraw, ImageFont
import argparse
import random 
def generate_meme(text: str):
    # Open the default image
    img = Image.open('meme.jpg')

    font = ImageFont.truetype("arial.ttf", 35)
    # Create ImageDraw object
    draw = ImageDraw.Draw(img)
    randomx = random.randint(0, img.size[0])
    randomy = random.randint(0, img.size[1])
    draw.text((randomx, randomy), text, fill=(255, 0, 0), font=font)
    # Save the image in a new file
    img.save('meme_with_text.jpg')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a meme with text.')
    parser.add_argument('-t', '--text', type=str, required=True, help='The text to add to the meme.')
    args = parser.parse_args()
    generate_meme(args.text)