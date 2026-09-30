import customtkinter as ctk

from app.ui.add_contact import AddContactFrame
from app.services.contact_service import (
    get_all_contacts,
    delete_contact
)


class ContactsFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            corner_radius=0,
            fg_color="transparent"
        )

        self.parent = parent

        self.create_header()
        self.create_search_bar()
        self.create_contacts_area()

        self.load_contacts()

    # =========================
    # HEADER
    # =========================

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(30, 10)
        )

        title = ctk.CTkLabel(
            header,
            text="Contacts",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        title.pack(side="left")

        add_button = ctk.CTkButton(
            header,
            text="+ Add Contact",
            width=140,
            height=40,
            corner_radius=8,
            command=self.open_add_contact
        )

        add_button.pack(side="right")

    # =========================
    # SEARCH
    # =========================

    def create_search_bar(self):

        search_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        search_frame.pack(
            fill="x",
            padx=30,
            pady=15
        )

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search contacts...",
            height=42
        )

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        search_button = ctk.CTkButton(
            search_frame,
            text="Search",
            width=100,
            height=42,
            command=self.search_contacts
        )

        search_button.pack(
            side="left",
            padx=(10, 0)
        )

        filter_button = ctk.CTkButton(
            search_frame,
            text="Filters",
            width=100,
            height=42
        )

        filter_button.pack(
            side="left",
            padx=(10, 0)
        )

    # =========================
    # CONTACT AREA
    # =========================

    def create_contacts_area(self):

        self.contacts_area = ctk.CTkScrollableFrame(
            self,
            label_text="Your Contacts"
        )

        self.contacts_area.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(5, 30)
        )

    # =========================
    # LOAD CONTACTS
    # =========================

    def load_contacts(self):

        for widget in self.contacts_area.winfo_children():
            widget.destroy()

        contacts = get_all_contacts()

        if not contacts:

            empty_label = ctk.CTkLabel(
                self.contacts_area,
                text="No contacts found.\nClick '+ Add Contact' to create one.",
                font=ctk.CTkFont(size=16)
            )

            empty_label.pack(pady=80)

            return

        for contact in contacts:

            full_name = contact.first_name

            if contact.last_name:
                full_name += f" {contact.last_name}"

            self.create_contact_card(
                contact.id,
                full_name,
                contact.designation or "No designation",
                contact.email or "No email"
            )

    # =========================
    # CONTACT CARD
    # =========================

    def create_contact_card(
        self,
        contact_id,
        name,
        designation,
        email
    ):

        card = ctk.CTkFrame(
            self.contacts_area,
            height=90,
            corner_radius=12
        )

        card.pack(
            fill="x",
            pady=6
        )

        # Contact information
        info_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        info_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        name_label = ctk.CTkLabel(
            info_frame,
            text=name,
            font=ctk.CTkFont(
                size=17,
                weight="bold"
            )
        )

        name_label.pack(
            anchor="w",
            padx=20,
            pady=(12, 0)
        )

        info = ctk.CTkLabel(
            info_frame,
            text=f"{designation}  •  {email}",
            font=ctk.CTkFont(size=13)
        )

        info.pack(
            anchor="w",
            padx=20,
            pady=(3, 12)
        )

        # Delete button
        delete_button = ctk.CTkButton(
            card,
            text="Delete",
            width=80,
            height=35,
            corner_radius=8,
            fg_color="#C62828",
            hover_color="#8E0000",
            command=lambda: self.delete_contact_from_ui(contact_id)
        )

        delete_button.pack(
            side="right",
            padx=20
        )

    # =========================
    # DELETE CONTACT
    # =========================

    def delete_contact_from_ui(self, contact_id):

        confirm = ctk.CTkToplevel(self)

        confirm.title("Delete Contact")
        confirm.geometry("350x180")
        confirm.resizable(False, False)

        label = ctk.CTkLabel(
            confirm,
            text="Are you sure you want to delete\nthis contact?",
            font=ctk.CTkFont(size=16)
        )

        label.pack(
            pady=(30, 20)
        )

        button_frame = ctk.CTkFrame(
            confirm,
            fg_color="transparent"
        )

        button_frame.pack()

        cancel_button = ctk.CTkButton(
            button_frame,
            text="Cancel",
            width=100,
            command=confirm.destroy
        )

        cancel_button.pack(
            side="left",
            padx=5
        )

        delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            width=100,
            fg_color="#C62828",
            hover_color="#8E0000",
            command=lambda: self.confirm_delete(
                contact_id,
                confirm
            )
        )

        delete_button.pack(
            side="left",
            padx=5
        )

    # =========================
    # CONFIRM DELETE
    # =========================

    def confirm_delete(self, contact_id, window):

        delete_contact(contact_id)

        window.destroy()

        self.load_contacts()

    # =========================
    # ADD CONTACT
    # =========================

    def open_add_contact(self):

        self.destroy()

        add_contact_page = AddContactFrame(
            self.parent,
            on_saved=self.contact_saved
        )

        add_contact_page.pack(
            fill="both",
            expand=True
        )

    # =========================
    # AFTER SAVE
    # =========================

    def contact_saved(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

        contacts_page = ContactsFrame(
            self.parent
        )

        contacts_page.pack(
            fill="both",
            expand=True
        )

    # =========================
    # SEARCH
    # =========================

    def search_contacts(self):

        search_text = self.search_entry.get().strip()

        print(f"Searching for: {search_text}")