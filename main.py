import customtkinter as ctk

from app.database.connection import create_database
from app.ui.dashboard import Dashboard


def main():

    create_database()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.title("Smart Contact Manager")
    app.geometry("1200x700")
    app.minsize(1000, 600)

    Dashboard(app)

    app.mainloop()


if __name__ == "__main__":
    main()