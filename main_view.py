import customtkinter as ctk
from CTkXYFrame import *
from icons import *
from automation import Automation
from appearance_manager import AppearanceManager
import ctypes


class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.appearance_manager = AppearanceManager()

        self.protocol("WM_DELETE_WINDOW", self.exit)

        # Configuração inicial da janela principal
        self.title("BOT EXCEL")  # Define o título da janela
        self.geometry("1200x750")
        self.resizable(True, True)

        self.total_width = self.winfo_width()  # Largura total da janela principal
        self.button_width_menu = (18 / 100) * self.total_width

        self.buttons_list = []
        self.buttons_list_text = []

        # Defina o ícone da janela

        # Configura a expansão horizontal da janela principal
        self.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.grid_columnconfigure(1, weight=1)  # Coluna 1 se expandirá

        # Configura a expansão vertical da janela principal
        self.grid_rowconfigure(0, weight=1)

        # Frame para os botões de navegação à esquerda
        self.menu_navigation_frame = ctk.CTkFrame(
            self,
            width=self.button_width_menu,
            corner_radius=0,
            fg_color=["gray80", "gray20"],
        )
        self.menu_navigation_frame.grid(row=0, column=0, sticky="nsew")

        # Frame principal para exibição de conteúdo
        self.main_content = CTkXYFrame(
            self,
            corner_radius=0,
        )
        self.main_content.grid(row=0, column=1, sticky="nsew")

        self.load_module_buttons()
        self.start_interface()

    @staticmethod
    def restart_interface(frame):
        try:
            # Destruir todos os widgets existentes
            for widget in frame.winfo_children():
                widget.destroy()
        except:
            print("erro ao destruir widgets")

    @staticmethod
    def msgbox(title, text, style):
        #  Styles:
        #  0 : OK
        #  1 : OK | Cancel
        #  2 : Abort | Retry | Ignore
        #  3 : Yes | No | Cancel 6, 7, 2
        #  4 : Yes | No
        #  5 : Retry | Cancel
        #  6 : Cancel | Try Again | Continue

        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def start_interface(self):
        self.mainloop()

    def load_module_buttons(self):

        self.menu_navigation_frame.grid_rowconfigure(3, weight=1)

        # Botão para ocultar o menu lateral direito
        self.hide_button = ctk.CTkButton(
            self.menu_navigation_frame,
            text="",
            image=menu_icon,
            anchor="w",
            width=23,
            height=23,
            fg_color="transparent",
            text_color=("black", "white"),
            command=self.hide_menu_navigation,
        )
        self.hide_button.grid(row=0, column=0, pady=10, sticky="w")

        self.automation_button = ctk.CTkButton(
            self.menu_navigation_frame,
            text="Automação",
            image=automation_icon,
            anchor="w",
            fg_color="transparent",
            text_color=("black", "white"),
            width=200,
            height=40,
            corner_radius=0,
            command=self.automation_view,
        )
        self.automation_button.grid(row=1, column=0, pady=10, sticky="w")

        self.buttons_list.append(self.automation_button)
        self.buttons_list_text.append(self.automation_button._text)

        self.your_logo = ctk.CTkLabel(
            self.menu_navigation_frame, text="", image=your_logo2, anchor="center"
        )
        self.your_logo.grid(row=2, column=0, pady=0, sticky="s")

        self.option_menu = ctk.CTkOptionMenu(
            self.menu_navigation_frame,
            font=self.appearance_manager.get_font_body(),
            width=150,
            values=["system", "light", "dark"],
            command=self.appearance_manager.appearance_theme,
        )
        self.option_menu.grid(
            row=4,
            pady=5,
            column=0,
        )

    def hide_menu_navigation(self):
        # Verifica a largura atual do menu_navigation_frame
        current_width = self.menu_navigation_frame.winfo_width()
        self.total_width = self.winfo_width()

        # Calcula a porcentagem atual da largura do menu em relação à largura total da janela
        percentage_width = (current_width / self.total_width) * 100

        try:

            if (
                percentage_width > 5
            ):  # Supondo que 10% seja o limite mínimo antes de ocultar o menu
                # Encolhe o menu
                new_width = 0  # Define a nova largura como 0 para ocultar o menu
                new_button_text = ""

                # Oculta os botões e remove texto
                for button in self.buttons_list:
                    button.configure(width=new_width, text=new_button_text, anchor="w")

                self.hide_button.configure(width=new_width)

                self.your_logo.grid_remove()
                self.option_menu.grid_remove()
            else:
                # Expande o menu
                # Defina a nova largura com base em uma porcentagem desejada da largura total da janela
                desired_percentage_width = 9.4  # Supondo que você deseje que o menu ocupe 8% da largura da janela
                new_width = (desired_percentage_width / 100) * self.total_width

                # Atualiza os botões com largura e texto adequados
                for i, button in enumerate(self.buttons_list):
                    button.configure(
                        width=200, text=self.buttons_list_text[i], anchor="w"
                    )

                self.hide_button.configure(width=1)
                self.your_logo.grid()
                self.option_menu.grid()

            # Atualiza a largura do menu_navigation_frame
            self.menu_navigation_frame.configure(width=new_width)
        except:
            pass

    def automation_view(self):
        try:
            self.restart_interface(self.main_content)
            self.interface_automation = Automation(self)
        except Exception as erro:
            print(f"houve um erro de: {erro}")
            
        

    def exit(self):
        resp = self.msgbox("SAIR", "Deseja realmente encerrar o sistema?", 4)
        if resp == 6:

            self.destroy()
