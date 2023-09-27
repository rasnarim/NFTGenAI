from PIL import Image, ImageDraw
import random

# Define the color scheme for each emotion
emotion_colors = {
    "happiness": [(255, 255, 0), (255, 215, 0), (255, 192, 203)], # yellow, gold, pink
    "sadness": [(70, 130, 180), (135, 206, 235), (240, 248, 255)], # steel blue, sky blue, alice blue
    "anger": [(255, 0, 0), (178, 34, 34), (139, 0, 0)], # red, firebrick, dark red
    # Add more emotions and their associated colors here
}

random.seed(42)

# Size of the image
WIDTH = 600
HEIGHT = 600

# Number of images to be generated for each emotion
num_images = 1000

for emotion, colors in emotion_colors.items():
    for i in range(num_images):
        # Create a new image with white background
        img = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
        d = ImageDraw.Draw(img)

        # Draw random rectangles with colors associated with the emotion
        for _ in range(1000):  # Increase this for more complex images
            x1 = random.randint(0, WIDTH)
            y1 = random.randint(0, HEIGHT)
            x2 = x1 + random.randint(50, 100)
            y2 = y1 + random.randint(50, 100)
            d.rectangle([x1, y1, x2, y2], fill=random.choice(colors))

        # Save the image
        img.save(f"./emotion_space/{emotion}_{i}.png")
