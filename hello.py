from PIL import Image, ImageDraw, ImageFont

MAX_ROW_PIXELS = 340
MAX_ROW_CHARS = 16

def generate(text, output="result.png"):
    text = text.upper()
    if len(text) == 0:
        print("No text entered")
        return
    if len(text) > 16:
        print("Long texts not supported yet")
        return
    
    img = Image.open("assets/city-template.png")
    img_draw = ImageDraw.Draw(img)

    font_size = round(-1.71*len(text) + 51.43)
    font = ImageFont.truetype("assets/din1451alt.ttf", font_size)

    img_draw.text((40, 40), text, font=font, fill=(0, 0, 0))
    img.save(output)