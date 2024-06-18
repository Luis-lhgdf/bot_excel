import time
import pandas as pd
import customtkinter as ctk


class Automation:
    def __init__(self, root):
        self.root = root

        self.main_content = self.root.main_content
        self.appearance_manager = self.root.appearance_manager
        self.dataframe = ""

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

        painel_1 = ctk.CTkButton(
            self.main_content,
            text="Upload/Iniciar",
            text_color=("black", "white"),
            font=self.appearance_manager.get_font_title(),
            width=900,
            height=150,
            border_width=1,
            fg_color="transparent",
            hover=False,
            anchor="nw",
        )

        painel_1.grid(row=1, column=0, sticky="nsew", padx=10, pady=(45, 5))

        self.bt_search_database = ctk.CTkButton(
            painel_1,
            text="Procurar",
            command=self.search_database_dialog,
        )
        self.bt_search_database.place(x=10, y=50)

        self.text_local_database = ctk.CTkLabel(
            painel_1,
            text="Local do arquivo: ",
            font=self.appearance_manager.get_font_title(),
        )
        self.text_local_database.place(x=200, y=50)

        self.bt_play = ctk.CTkButton(
            painel_1,
            text="Play",
            corner_radius=10,
            fg_color="#006837",
            hover_color="#033B21",
            anchor="center",
            command=self.start,
        )
        self.bt_play.place(x=10, y=100)

        painel_2 = ctk.CTkButton(
            self.main_content,
            text="Status:",
            text_color=("black", "white"),
            font=self.appearance_manager.get_font_title(),
            width=900,
            height=100,
            border_width=1,
            fg_color="transparent",
            hover=False,
            anchor="nw",
        )
        painel_2.grid(row=2, column=0, sticky="nsew", padx=10, pady=(45, 5))

        painel_3 = ctk.CTkButton(
            self.main_content,
            text="Download",
            text_color=("black", "white"),
            font=self.appearance_manager.get_font_title(),
            width=900,
            height=100,
            border_width=1,
            fg_color="transparent",
            hover=False,
            anchor="nw",
        )
        painel_3.grid(row=3, column=0, sticky="nsew", padx=10, pady=(45, 5))

        self.bt_download = ctk.CTkButton(
            painel_3,
            text="Download",
            corner_radius=10,
            fg_color="#006837",
            hover_color="#033B21",
            anchor="center",
            command=self.save_database,
        )
        self.bt_download.place(x=10, y=50)

    def search_database_dialog(self):

        db_path = ctk.filedialog.askopenfilename(
            defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")]
        )

        if db_path:
            self.text_local_database.configure(text=db_path)

    def save_database(self):
        # Abrir o diálogo para escolher o local e o nome do arquivo
        file_path = ctk.filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
        )
        if file_path:
            self.dataframe.to_excel(file_path, index=False)
            print(f"Arquivo salvo em: {file_path}")
        else:
            print("Operação de salvamento cancelada")

    def start(self):
        print("INICIANDO AUTOMAÇÃO")
