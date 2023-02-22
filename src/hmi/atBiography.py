
from tkinter import *


import customtkinter
from tkintermapview import TkinterMapView
from .databasemain import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties


customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    WIDTH = 1280
    HEIGHT = 1008
    MAX_DATA_LOGGER_VIEW = 16

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.title("ATLab Data Logger Manage Tool")
        # self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.data_logger_index = []

        self.frame_left_bottom = customtkinter.CTkFrame(master=self, width=1000)
        self.frame_left_bottom.grid(row=0, column=0,sticky="nswe",padx=10, pady=5,  rowspan=2)
        self.frame_right_bottom = customtkinter.CTkFrame(master=self)
        self.frame_right_bottom.grid(row=1, column=1,sticky="nswe",padx=10, pady=5)
        self.frame_right_top = customtkinter.CTkFrame(master=self, height=120)
        self.frame_right_top.grid(row=0, column=1,sticky="nswe",padx=10, pady=5)
        self.frame_right_top_1 = customtkinter.CTkFrame(master=self.frame_right_top)
        self.frame_right_top_1.grid(row=0, column=0,sticky="nswe",padx=10, pady=5)
        self.frame_right_top_2 = customtkinter.CTkFrame(master=self.frame_right_top)
        self.frame_right_top_2.grid(row=1, column=0,sticky="nswe",padx=10, pady=5)
        self.frame_right_top_3 = customtkinter.CTkFrame(master=self.frame_right_top)
        self.frame_right_top_3.grid(row=0, rowspan=2, column=1,sticky="nswe",padx=10, pady=5)
        self.frame_right_top_4 = customtkinter.CTkFrame(master=self.frame_right_top)
        self.frame_right_top_4.grid(row=0, rowspan=2, column=3,sticky="nswe",padx=10, pady=5)


        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
       
        self.frame_right_bottom.grid_rowconfigure(1, weight=1)
        self.frame_right_bottom.grid_rowconfigure(0, weight=0)
        self.frame_right_bottom.grid_columnconfigure(0, weight=1)
        self.frame_right_bottom.grid_columnconfigure(1, weight=0)
        self.frame_right_bottom.grid_columnconfigure(2, weight=1)

        self.frame_right_top.grid_rowconfigure(0, weight=0,minsize=30)
        self.frame_right_top.grid_rowconfigure(1, weight=0,minsize=30)
        self.frame_right_top.grid_columnconfigure(0, weight=1, minsize=230)
        self.frame_right_top.grid_columnconfigure(1, weight=0)
        # self.frame_right_top.grid_columnconfigure(2, weight=0, minsize=230)

        self.marker_list = []

        for x in range(App.MAX_DATA_LOGGER_VIEW):
            self.data_logger_index.append(str(x))

        self.map_label = customtkinter.CTkLabel(self.frame_right_top_4, text="Tile Server:", anchor="w")
        self.map_label.grid(row=0, column=2, padx=(10, 10), pady=(20, 0))

        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_right_top_4, 
                                                           values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                           command=self.change_map
                                                           )
        self.map_option_menu.grid(row=0, column=3, padx=(10, 10), pady=(20, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(self.frame_right_top_4, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=1, column=2, padx=(10, 10), pady=(20, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_right_top_4, 
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode
                                                                       )
        self.appearance_mode_optionemenu.grid(row=1, column=3, padx=(10, 10), pady=(20, 0))

        #frame left bottom

        self.information_equidment()
        self.init_page()

        #frame right bottm
        
        self.map_widget = TkinterMapView(self.frame_right_bottom, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_right_bottom, width= 1000,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right_bottom,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 12), pady=12)
        
        # Set default values
        self.map_widget.set_address("21.0049984,105.8416758")
        # self.map_option_menu.set("OpenStreetMap")
        # self.appearance_mode_optionemenu.set("Dark")
        self.marker_list = []

        path_file_database = r'src\hmi\database.xlsx'
        data_equidment = read_latitude_longitude_database(path_file_database)

        for index in range(len(data_equidment)):
            self.marker_list.append(self.map_widget.set_marker(data_equidment[index][0],data_equidment[index][1]))

        self.mat_plot()

        self.show_number_devices()
        


    def information_equidment(self):

        # stt
        self.stt = customtkinter.CTkLabel(
                                    master = self.frame_left_bottom,
                                    text="Ordinal number",
                                    width=10
                                    )
        self.stt.grid(row=0, column= 0,pady=5, padx=10)

        # information equidment
        self.information_equidment = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text="Device name",
                                                width=20
                                                )
        self.information_equidment.grid(row=0, column= 1,pady=5, padx=10)

        # information equidment
        self.information_equidment = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text="Status",
                                                width=20
                                                )
        self.information_equidment.grid(row=0, column= 2,pady=5, padx=10)

        # information equidment
        self.information_equidment = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text="Latitude",
                                                width=20
                                                )
        self.information_equidment.grid(row=0, column= 3,pady=5, padx=10)

        # information equidment
        self.information_equidment = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text="Longitude",
                                                width=20
                                                )
        self.information_equidment.grid(row=0, column= 4,pady=5, padx=10)

    def init_page(self):

        path_file_database = r'src\hmi\database.xlsx'

        rows = read_database_file(path_file_database)

        for index in range(0,App.MAX_DATA_LOGGER_VIEW):

            self.data_logger_index[index] = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text=index+1,
                                                width=20
                                            )
            self.data_logger_index[index].grid(row=index+1, column= 0,pady=5, padx=10)

            self.data_logger_index[index] = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text=rows[index][0],
                                                width=20
                                            )
            self.data_logger_index[index].grid(row=index+1, column= 1,pady=5, padx=10)

            self.data_logger_index[index] = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text=rows[index][1],
                                                width=20
                                            )
            self.data_logger_index[index].grid(row=index+1, column= 2,pady=5, padx=10)

            self.data_logger_index[index] = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text=rows[index][2],
                                                width=20
                                            )
            self.data_logger_index[index].grid(row=index+1, column= 3,pady=5, padx=10)

            self.data_logger_index[index] = customtkinter.CTkLabel(
                                                master = self.frame_left_bottom,
                                                text=rows[index][3],
                                                width=20
                                            )
            self.data_logger_index[index].grid(row=index+1, column= 4,pady=5, padx=10)

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def mat_plot(self):
        #setting font
        font = FontProperties()
        font.set_family('serif')
        font.set_name('Georgia')
        font.set_size(10)

        path_file_database = r'src\hmi\database.xlsx'
        A = read_latitude_longitude_database(path_file_database)
        numer_devices = len(A)


        Labels1 = ['working', 'not working']
        share = [numer_devices, 16-numer_devices]
        colors = ['#127db3', '#063970']

        # create figure
        fig = Figure(figsize=(3, 2), dpi=100, facecolor='#dbdbdb')
        ax = fig.add_subplot(111)
        
        ax.pie(share, labels=Labels1, autopct='%1.1f%%', 
               startangle=90, textprops={'fontproperties': font},  colors=colors)
        ax.axis('equal')
 
        centre_circle = plt.Circle((0,0),0.70,fc='#dbdbdb')
        fig.gca().add_artist(centre_circle)

        Canvas_firgue = FigureCanvasTkAgg(fig, master=self.frame_right_top_3)
        Canvas_firgue.draw()
        Canvas_firgue.get_tk_widget().grid(row=0, column=1,sticky="nswe")

        self.title_chart = customtkinter.CTkLabel(
                                    master = self.frame_right_top_3,
                                    text="Chart: The ratio of working equipment",
                                    width=40,
                                    )
        self.title_chart.grid(row=1, column=1,pady=5, padx=10, sticky="nswe")


    def show_number_devices(self):

        path_file_database = r'src\hmi\database.xlsx'
        A = read_latitude_longitude_database(path_file_database)
        numer_devices = len(A)
        B = "Active equipments: " + str(numer_devices)
        C = "Total equidments: 16"

        # print(f"Số phần tử trong danh sách A là {numer_devices}")

        self.working_equipment = customtkinter.CTkLabel(
                                    master = self.frame_right_top_1,
                                    text=B,
                                    width=20
                                    )
        self.working_equipment.grid(row=0, column=0,pady=5, padx=10, sticky="nswe")
        self.non_working_equipment = customtkinter.CTkLabel(
                                    master = self.frame_right_top_2,
                                    text=C,
                                    width=20,
                                    )
        self.non_working_equipment.grid(row=1, column=0,pady=5, padx=10, sticky="nswe")


    def start(self):
        self.mainloop()  

if __name__ == "__main__":
    app = App()
    app.start()  
