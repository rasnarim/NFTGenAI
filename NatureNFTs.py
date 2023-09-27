import os
from PIL import Image, ImageDraw, ImageFont
import random


random.seed(1)
# Set the dimensions of the image
width = 512
height = 512

# Create a folder named 'NatureNFTs' if it doesn't exist
folder_name = 'NatureNFTs'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define color palette for nature theme
background_colors = ['#E6F2FF', '#CCF5FF', '#B3F0FF', '#99EBFF']
foreground_colors = ['#00802b', '#006f25', '#005a1f', '#004517']

# Define nature-themed patterns or shapes
patterns = ['tree', 'leaf', 'mountain', 'sun']

# Set font for captions
caption_font = ImageFont.truetype('arial.ttf', 20)

# Generate and save multiple nature-themed NFTs
num_images = 500  # Specify the number of NFTs to generate
for i in range(num_images):
    # Create a new blank image
    image = Image.new("RGB", (width, height), random.choice(background_colors))
    draw = ImageDraw.Draw(image)

    # Generate random nature-themed shapes or patterns
    for _ in range(10):
        shape_type = random.choice(patterns)
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(x1, width)
        y2 = random.randint(y1, height)

        if shape_type == "tree":
            draw.rectangle([(x1, y1), (x2, y2)], fill=random.choice(foreground_colors))
        elif shape_type == "leaf":
            draw.ellipse([(x1, y1), (x2, y2)], fill=random.choice(foreground_colors))
        elif shape_type == "mountain":
            draw.polygon([(x1, y1), (x2, y2), (x1 + random.randint(50, 100), y2)], fill=random.choice(foreground_colors))
        elif shape_type == "sun":
            draw.ellipse([(x1, y1), (x2, y2)], fill='yellow')

    # Add caption text
    caption_text = 'Nature NFT #' + str(i + 1)
    text_bbox = draw.textbbox((0, 0), caption_text, font=caption_font)
    text_position = ((width - text_bbox[2]) // 2, height - text_bbox[3] - 10)
    draw.text(text_position, caption_text, fill='black', font=caption_font)

    # Save the generated NFT image under 'NatureNFTs' folder
    image_name = f"{i+1}.png"
    image_path = os.path.join(folder_name, image_name)
    image.save(image_path)
    print(f"Generated NFT saved: {image_path}")
