import time
import pandas as pd
import customtkinter as ctk


class Automation:
    def __init__(self, root):
        self.root = root

        self.main_content = self.root.main_content
        self.appearance_manager = self.root.appearance_manager

        self.interface()

    def interface(self):
        # Configuração do layout
        self.main_content.grid_rowconfigure(0, weight=0)
        self.main_content.grid_rowconfigure(1, weight=0)
        self.main_content.grid_rowconfigure(2, weight=0)
        self.main_content.grid_rowconfigure(3, weight=0)
        self.main_content.grid_columnconfigure(0, weight=1)

        # Título
        label_titulo = ctk.CTkLabel(
            self.main_content,
            text=f"AUTOMAÇÃO",
            fg_color="transparent",
            font=self.appearance_manager.get_font_title(),
            corner_radius=6,
            anchor="w",
        )
        label_titulo.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
