from PIL import Image, ImageDraw, ImageFont
import argparse

def generate_meme(text: str):
    # Open the default image
    img = Image.open('meme.jpg')

    # Create ImageDraw object
    draw = ImageDraw.Draw(img)

    draw.text((15, 100), text, fill=(255, 0, 0))
    # Save the image in a new file
    img.save('meme_with_text.jpg')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a meme with text.')
    parser.add_argument('-t', '--text', type=str, required=True, help='The text to add to the meme.')
    args = parser.parse_args()
    generate_meme(args.text)