from requests import get
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from math import gcd


IMG_URL = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

try:
    # Checks if the provided URL is an image
    
    response = get(url=IMG_URL) # Get URL response

    content = BytesIO(response.content) # Buffer content

    image = Image.open(content) # Open image with pillow

    # Calculate ratios (gdc it's the Greatest Common Divisor)
    width_ratio = image.width / gcd(image.width, image.height)
    height_ratio = image.height / gcd(image.width, image.height)

    aspect_ratio = f"{width_ratio}:{height_ratio}" #Format output into string

    print(aspect_ratio)

except UnidentifiedImageError:
    print("The provided URL isn't an image")