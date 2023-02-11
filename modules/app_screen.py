import customtkinter
import PIL
import modules.find_path as f_p

class Project_app(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCRREN_HEIGHT = self.winfo_screenheight()
        self.title("Project №1")
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{self.SCRREN_HEIGHT}")
        self.PROJECT_IMAGE = customtkinter.CTkImage(light_image = PIL.Image.open(f_p.find_path_file("images\\1.jpg")), size = (self.APP_WIDTH, self.APP_HEIGHT))
        self.IMAGE_LABEL = customtkinter.CTkLabel(master=self, text = "Моя перша практична робота з customtkinter", image = self.PROJECT_IMAGE, bg_color='black')
        self.IMAGE_LABEL.grid(row= 5, column= 5)
project_app = Project_app(app_width= 400, app_height= 400)       