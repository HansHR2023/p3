import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO 
import base64

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
 
    return remove(image)
 

my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

counter = 0

for img in my_upload:
    fixed_img = fix_image(img)
    counter += 1
    fixed_img.save(f"./proefcropper/fixed{counter}.png")

# pad = "./proefcropper"