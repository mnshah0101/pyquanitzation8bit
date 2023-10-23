import sys
from Image import Image
script_name = sys.argv[0]


# The arguments are sys.argv[1:] (from index 1 onward)
file_path = sys.argv[1]

image = Image(file_path, 8)
image.train_image()
return_boolean = image.create_image(image.smaller_image)
if return_boolean:
    print("Image saved successfully")
else:
    print("Image could not be saved")
