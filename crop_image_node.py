from PIL import Image
import numpy as np

class VahCropImageNode:  # اضافه کردن vah به نام کلاس
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "crop_top": ("INT", {"default": 0, "min": 0, "max": 10000}),
                "crop_bottom": ("INT", {"default": 0, "min": 0, "max": 10000}),
                "crop_left": ("INT", {"default": 0, "min": 0, "max": 10000}),
                "crop_right": ("INT", {"default": 0, "min": 0, "max": 10000}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "crop_image"

    CATEGORY = "Image Processing"  # دسته‌بندی
    DISPLAY_NAME = "vah - Crop Image"  # نام برای نمایش در ComfyUI

    def crop_image(self, image, crop_top, crop_bottom, crop_left, crop_right):
        # Convert image to a PIL image
        pil_image = Image.fromarray((image * 255).astype(np.uint8))
        
        # Get original dimensions
        width, height = pil_image.size

        # Calculate crop boundaries
        left = crop_left
        right = width - crop_right
        top = crop_top
        bottom = height - crop_bottom

        # Ensure valid crop dimensions
        left = max(0, left)
        right = min(width, right)
        top = max(0, top)
        bottom = min(height, bottom)

        # Perform cropping
        cropped_image = pil_image.crop((left, top, right, bottom))
        
        # Convert back to numpy array (normalized)
        cropped_image = np.asarray(cropped_image).astype(np.float32) / 255.0
        return (cropped_image,)


# Register the node
NODE_CLASS_MAPPINGS = {
    "VahCropImage": VahCropImageNode  # تغییر نام نود برای شناسایی
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VahCropImage": "vah - Crop Image"  # نام برای نمایش
}
