from PIL import Image, ImageDraw, ImageFont

# Create blank image
img = Image.new('RGB', (1920, 1080), color=(30, 30, 60))
draw = ImageDraw.Draw(img)

# Add title
font = ImageFont.truetype("arial.ttf", 80)
draw.text((960, 400), "Learn NLP with Python:", fill=(255, 255, 255), font=font, anchor="mm")
draw.text((960, 520), "A Step-by-Step Tutorial for Beginners", fill=(200, 200, 255), font=font, anchor="mm")

# Add Python logo (would need to download one)
# python_logo = Image.open("python_logo.png")
# img.paste(python_logo, (100, 100))

img.save("nlp_tutorial_banner.png")