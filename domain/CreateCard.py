import requests
from PIL import Image, ImageDraw, ImageFont

# Image parameters
width, height = 1748, 2480  # A5 size in pixels at 300 dpi
background_color = (85, 107, 47)  # Landwirtschaftsgrün
text_color = (255, 255, 0)  # Gelb

# Create image
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Load fonts
try:
  font_large = ImageFont.truetype("arial.ttf", 160)
  font_small = ImageFont.truetype("arial.ttf", 120)
except IOError:
  font_large = ImageFont.load_default()
  font_small = ImageFont.load_default()

# Text to be added
text_title = "Lieber Christian alles Gute zum Geburtstag"
text_body = "viel Gesundheit und Glück wünschen Dir\nMatilda, Marian, Jonathan, Linus, Mattis, Florian"

# Calculate text size and position
title_w, title_h = draw.textbbox((0, 0), text_title, font=font_large)[2:]
body_w, body_h = draw.textbbox((0, 0), text_body, font=font_small)[2:]
title_position = ((width - title_w) // 2, height // 6)
body_position = ((width - body_w) // 2, height // 6 + title_h + 20)

# Draw text
draw.text(title_position, text_title, fill=text_color, font=font_large)
draw.text(body_position, text_body, fill=text_color, font=font_small)

# Load the image from the provided URL
tractor_image_url = "https://image.spreadshirtmedia.net/image-server/v1/designs/184909936,width=300,height=300/guellebomber-trecker-mit-guellefass-mistfass.jpg"
tractor_image = Image.open(requests.get(tractor_image_url, stream=True).raw)

# Convert the image to RGB mode (remove transparency)
tractor_image = tractor_image.convert("RGB")

# Resize and position the tractor image
tractor_image = tractor_image.resize((int(width * 0.8), int(height * 0.4)))
tractor_position = ((width - tractor_image.width) // 2, height // 2 + 50)
image.paste(tractor_image, tractor_position)

# Save the image
output_path = "/Users/konrad/geburtstagskarte.png"
image.save(output_path)
