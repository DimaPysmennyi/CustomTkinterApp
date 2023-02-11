import customtkinter
import PIL
import modules.find_path as f_p

class Project_app(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.title("Project №1")
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{self.SCREEN_HEIGHT-200}")
        self.PROJECT_IMAGE = customtkinter.CTkImage(light_image = PIL.Image.open(f_p.find_path_file("images\\1.jpg")), size = (self.APP_WIDTH, self.APP_HEIGHT))
        self.IMAGE_LABEL1 = customtkinter.CTkLabel(master=self, text = "Моя перша практична робота з customtkinter", image = self.PROJECT_IMAGE, bg_color='black')
        self.IMAGE_LABEL2 = customtkinter.CTkLabel(master=self, text = "Кнопка натиснута", image = self.PROJECT_IMAGE, bg_color='black')
        self.BUTTON = customtkinter.CTkButton(master=self, text="Button", command=self.button_pressed, border_width=0, corner_radius=8, fg_color="white", text_color="black", hover_color="gray")
        # , width=120, height=32, border_width=0, corner_radius=8
        
        # self.BUTTON.pack(padx=20, pady=10,anchor=customtkinter.CENTER)
        self.IMAGE_LABEL1.grid(row= 5, column= 5)
        # self.BUTTON.grid(row=3, column=5)
        self.BUTTON.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        # self.IMAGE_LABEL.grid(row= 5, column= 5)
        
    
    def button_pressed(self):
        self.IMAGE_LABEL2.grid(row=5, column=4)
        
project_app = Project_app(app_width= 400, app_height= 400)     

