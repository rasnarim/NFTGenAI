import os
from PIL import Image, ImageDraw
import random

random.seed(1)
# Set the dimensions of the image
width = 512
height = 512

# Create a folder named 'ArtGenia' if it doesn't exist
folder_name = 'ArtGenia'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Generate and save multiple images
num_images = 1000  # Specify the number of images to generate
for i in range(num_images):
    # Create a new blank image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Generate random colors for the background and foreground
    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    foreground_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Set the background color
    draw.rectangle([(0, 0), (width, height)], fill=background_color)

    # Draw some random shapes or patterns
    for _ in range(10):
        shape_type = random.choice(["rectangle", "ellipse"])
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(x1, width)
        y2 = random.randint(y1, height)

        if shape_type == "rectangle":
            draw.rectangle([(x1, y1), (x2, y2)], fill=foreground_color)
        else:
            draw.ellipse([(x1, y1), (x2, y2)], fill=foreground_color)

    # Save the generated image under 'ArtGenia' folder
    image_name = f"{i+1}.png"
    image_path = os.path.join(folder_name, image_name)
    image.save(image_path)
    print(f"Generated image saved: {image_path}")
