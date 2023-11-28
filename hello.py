from PIL import Image, ImageDraw, ImageFont

MAX_ROW_PIXELS = 340
MAX_ROW_CHARS = 16

def generate(text, output="result.png"):
    text = text.upper()
    if len(text) == 0:
        print("No text entered")
        return
    if len(text) > 24:
        print("Long texts not supported yet")
        return
    
    img = Image.open("assets/city-template.png")
    img_draw = ImageDraw.Draw(img)

    font_size = 2 * round(-1.71*len(text) + 51.43)
    font = ImageFont.truetype("assets/din1451alt.ttf", font_size)
    text_width, text_height = img_draw.textsize(text, font)

    # print(f"Height: {text_height}px")

    while text_width > img.width - 50:
        font_size -= 2
        font = ImageFont.truetype("assets/din1451alt.ttf", font_size)
        text_width, text_height = img_draw.textsize(text, font)

    init_x = (img.width - text_width) // 2
    init_y = (img.height - text_height) // 2 - 10

    img_draw.text((init_x, init_y), text, font=font, fill=(0, 0, 0))
    img.save(output)