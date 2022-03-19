from PIL import Image

# Path for your image where it is
image_1 = Image.open(
    r'C:/Users/Darshil Shukla/Desktop/Python/20CE137_Sem3.jpeg')

# Converting it into pdf
im_1 = image_1.convert('RGB')

# Path where your PDF file will bw saved
im_1.save(r'C:/Users/Darshil Shukla\Desktop/Python/Sem3.pdf')