import customtkinter as ctk
from app.ui.contacts import ContactsFrame


class Dashboard:

    def __init__(self, parent):
        self.parent = parent

        self.create_sidebar()
        self.create_main_content()

    # =========================
    # SIDEBAR
    # =========================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.parent,
            width=230,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Application title
        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="NEXA",
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            )
        )

        self.logo.pack(
            padx=20,
            pady=(35, 5)
        )

        self.subtitle = ctk.CTkLabel(
            self.sidebar,
            text="Smart Contact Manager",
            font=ctk.CTkFont(size=12)
        )

        self.subtitle.pack(
            padx=20,
            pady=(0, 30)
        )

        # Navigation buttons
        navigation = [
            "Dashboard",
            "Contacts",
            "Favorites",
            "Groups",
            "Reminders",
            "Analytics",
            "AI Assistant"
        ]

        for item in navigation:

            button = ctk.CTkButton(
                self.sidebar,
                text=item,
                height=42,
                corner_radius=8,
                anchor="w",

                # Navigation
                command=lambda name=item: self.navigate(name)
            )

            button.pack(
                padx=18,
                pady=5,
                fill="x"
            )

        # Settings
        self.settings_button = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            height=42,
            corner_radius=8,
            anchor="w",
            command=lambda: self.navigate("Settings")
        )

        self.settings_button.pack(
            side="bottom",
            padx=18,
            pady=25,
            fill="x"
        )

    # =========================
    # MAIN CONTENT
    # =========================

    def create_main_content(self):

        self.main = ctk.CTkFrame(
            self.parent,
            corner_radius=0,
            fg_color="transparent"
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Header
        self.header = ctk.CTkFrame(
            self.main,
            height=80,
            corner_radius=0,
            fg_color="transparent"
        )

        self.header.pack(
            fill="x",
            padx=30,
            pady=(20, 0)
        )

        self.heading = ctk.CTkLabel(
            self.header,
            text="Dashboard",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        self.heading.pack(
            side="left"
        )

        self.welcome = ctk.CTkLabel(
            self.header,
            text="Welcome back 👋",
            font=ctk.CTkFont(size=14)
        )

        self.welcome.pack(
            side="right",
            pady=10
        )

        # Statistics
        self.create_stat_cards()

    # =========================
    # STAT CARDS
    # =========================

    def create_stat_cards(self):

        self.stats_frame = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.stats_frame.pack(
            fill="x",
            padx=30,
            pady=20
        )

        stats = [
            ("Total Contacts", "0"),
            ("Favorites", "0"),
            ("Groups", "0"),
            ("Follow-ups", "0")
        ]

        for title, value in stats:

            card = ctk.CTkFrame(
                self.stats_frame,
                height=130,
                corner_radius=15
            )

            card.pack(
                side="left",
                expand=True,
                fill="both",
                padx=7
            )

            label = ctk.CTkLabel(
                card,
                text=title,
                font=ctk.CTkFont(size=14)
            )

            label.pack(
                anchor="w",
                padx=20,
                pady=(20, 5)
            )

            number = ctk.CTkLabel(
                card,
                text=value,
                font=ctk.CTkFont(
                    size=30,
                    weight="bold"
                )
            )

            number.pack(
                anchor="w",
                padx=20
            )

    # =========================
    # NAVIGATION
    # =========================

    def navigate(self, page):

        # Remove current content
        for widget in self.main.winfo_children():
            widget.destroy()

        if page == "Contacts":

            contacts_page = ContactsFrame(self.main)

            contacts_page.pack(
                fill="both",
                expand=True
            )

        else:

            label = ctk.CTkLabel(
                self.main,
                text=f"{page} Page",
                font=ctk.CTkFont(
                    size=30,
                    weight="bold"
                )
            )

            label.pack(
                padx=30,
                pady=30,
                anchor="w"
            )