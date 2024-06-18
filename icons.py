import customtkinter as ctk
from PIL import Image
import os


image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")

automation_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(image_path, "ray_black.png")),
    dark_image=Image.open(os.path.join(image_path, "ray_light.png")),
    size=(20, 20),
)


menu_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(image_path, "menu_black.png")),
    dark_image=Image.open(os.path.join(image_path, "menu_light.png")),
    size=(20, 20),
)

your_logo2 = ctk.CTkImage(
    light_image=Image.open(os.path.join(image_path, "logo2.png")),
    dark_image=Image.open(os.path.join(image_path, "logo2.png")),
    size=(130, 130),
)
