import os
from PIL import Image
from flask import current_app

def add_featured_image(upload_image):
    image_filename = upload_image.filename
    filepath = os.path.join(current_app.root_path, f'static/featured_image', image_filename)
    image_size = (800, 800)
    image = Image.open(upload_image)
    image.thumbnail(image_size)
    image.save(filepath)
    return image_filename
