'''This code generate 10800 NFTs as parallel universes'''


from PIL import Image, ImageDraw
import random
import os

# Ensure the output directory exists
output_dir = './SpectralMandala'
os.makedirs(output_dir, exist_ok=True)
random.seed(42)
# Parameters
num_images = 10800  # Number of images to generate
width, height = 800, 800  # Dimensions of the image
num_elements = 100  # Number of elements (lines and circles) per image

# Function to generate a color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to generate a random position
def random_position():
    return (random.randint(0, width), random.randint(0, height))

# Generate the images
for i in range(num_images):
    # Create a new image with a white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Draw the elements
    for _ in range(num_elements):
        if random.random() < 0.5:
            # Draw a line
            draw.line([random_position(), random_position()], fill=random_color())
        else:
            # Draw a circle
            pos = random_position()
            r = random.randint(10, 100)
            draw.ellipse([pos[0]-r, pos[1]-r, pos[0]+r, pos[1]+r], fill=random_color())

    # Save the image
    image.save(os.path.join(output_dir, f'{i + 1}.png'))

