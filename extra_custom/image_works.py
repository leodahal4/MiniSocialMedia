# Import the randint module for generating the random numbers
from random import randint
# All the modules which are used for image processing and working with images
from PIL import ImageTk, Image, ImageOps, ImageDraw, ImageFilter
from PIL import *


class Image_work:
    """Image_work
        This class contains the functions which are used for processing the
        images for the user avatar
    """
    def crop_center(self, pil_img, crop_width, crop_height):
        """crop_center(self, pil_img, crop_width, crop_height)
                This function is used to crop the central area of the image
        """
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))

    def crop_max_square(self, pil_img):
        return self.crop_center(pil_img, min(pil_img.size), min(pil_img.size))

    def mask_circle_transparent(self, pil_img, blur_radius, offset=0):
        """mask_circle_transparent(self, pil_img, blur_radius, offset = 0)
                This function creates the background as transparent
                i.e same as the back color.
        """
        offset = blur_radius * 2 + offset
        mask = Image.new("L", pil_img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse(
            (
                offset,
                offset,
                pil_img.size[0] - offset,
                pil_img.size[1] - offset
            ),
            fill=255
        )
        mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
        result = pil_img.copy()
        result.putalpha(mask)
        return result

    def crop_image(self, path):
        """crop_image(self, path)
                This function takes the path of the image as the argument and
                than works in the specific image provided.
        """
        name_for_file = ["avatar", "user_avatar", "user_image", "user_img"]
        for i in range(1):
            pointer = randint(0, 3)
            name = name_for_file[pointer]
            name += str(randint(0, 10000))
        for_try = Image.open(path)
        im_square = self.crop_max_square(for_try).resize(
            (100, 100), Image.LANCZOS
        )
        im_thumb = self.mask_circle_transparent(im_square, 4)
        im_thumb.save('assets/' + name + '.png')

        # return the saved path of the processed image
        return "assets/" + name + ".png"
