import customtkinter as ctk

from app.services.contact_service import add_contact


class AddContactFrame(ctk.CTkFrame):

    def __init__(self, parent, on_saved=None):
        super().__init__(
            parent,
            corner_radius=0,
            fg_color="transparent"
        )

        self.on_saved = on_saved

        self.create_form()

    def create_form(self):

        # Title
        title = ctk.CTkLabel(
            self,
            text="Add New Contact",
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(30, 20)
        )

        # Form container
        form = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        form.pack(
            fill="x",
            padx=30,
            pady=10
        )

        # First Name
        self.first_name = ctk.CTkEntry(
            form,
            placeholder_text="First Name *",
            height=42
        )

        self.first_name.pack(
            fill="x",
            padx=25,
            pady=(25, 10)
        )

        # Last Name
        self.last_name = ctk.CTkEntry(
            form,
            placeholder_text="Last Name",
            height=42
        )

        self.last_name.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # Phone
        self.phone = ctk.CTkEntry(
            form,
            placeholder_text="Phone Number",
            height=42
        )

        self.phone.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # Email
        self.email = ctk.CTkEntry(
            form,
            placeholder_text="Email",
            height=42
        )

        self.email.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # Company
        self.company = ctk.CTkEntry(
            form,
            placeholder_text="Company",
            height=42
        )

        self.company.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # Designation
        self.designation = ctk.CTkEntry(
            form,
            placeholder_text="Designation",
            height=42
        )

        self.designation.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # Notes
        self.notes = ctk.CTkTextbox(
            form,
            height=100
        )

        self.notes.pack(
            fill="x",
            padx=25,
            pady=10
        )

        self.notes.insert(
            "1.0",
            ""
        )

        # Save button
        save_button = ctk.CTkButton(
            form,
            text="Save Contact",
            height=45,
            corner_radius=8,
            command=self.save_contact
        )

        save_button.pack(
            padx=25,
            pady=(15, 25),
            fill="x"
        )

    def save_contact(self):

        first_name = self.first_name.get().strip()
        last_name = self.last_name.get().strip()
        phone = self.phone.get().strip()
        email = self.email.get().strip()
        company = self.company.get().strip()
        designation = self.designation.get().strip()
        notes = self.notes.get(
            "1.0",
            "end"
        ).strip()

        if not first_name:

            error = ctk.CTkLabel(
                self,
                text="First name is required!",
                text_color="red"
            )

            error.pack(
                pady=10
            )

            return

        add_contact(
            first_name=first_name,
            last_name=last_name or None,
            phone=phone or None,
            email=email or None,
            company=company or None,
            designation=designation or None,
            notes=notes or None
        )

        success = ctk.CTkLabel(
            self,
            text="Contact saved successfully!",
            text_color="green"
        )

        success.pack(
            pady=10
        )

        if self.on_saved:
            self.on_saved()