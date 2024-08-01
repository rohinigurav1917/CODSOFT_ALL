import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=3, column=0, columnspan=2)

        self.search_label = tk.Label(root, text="Search by Name")
        self.search_label.grid(row=4, column=0)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=4, column=1)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=5, column=0, columnspan=2)

        self.update_label = tk.Label(root, text="Update by Name")
        self.update_label.grid(row=6, column=0)
        self.update_entry = tk.Entry(root)
        self.update_entry.grid(row=6, column=1)
        self.update_button = tk.Button(root, text="Update", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2)

        self.delete_label = tk.Label(root, text="Delete by Name")
        self.delete_label.grid(row=8, column=0)
        self.delete_entry = tk.Entry(root)
        self.delete_entry.grid(row=8, column=1)
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_contact)
        self.delete_button.grid(row=9, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("Success", f"Contact '{name}' added.")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Name and Phone fields cannot be empty.")

    def view_contacts(self):
        if self.contacts:
            contacts_str = '\n'.join(f"{name}: {phone}" for name, phone in self.contacts.items())
            messagebox.showinfo("Contact List", contacts_str)
        else:
            messagebox.showinfo("Contact List", "No contacts found.")

    def search_contact(self):
        name = self.search_entry.get().strip()
        if name in self.contacts:
            phone = self.contacts[name]
            messagebox.showinfo("Search Result", f"{name}: {phone}")
        else:
            messagebox.showinfo("Search Result", "Contact not found.")
        self.search_entry.delete(0, tk.END)

    def update_contact(self):
        name = self.update_entry.get().strip()
        if name in self.contacts:
            new_phone = self.phone_entry.get().strip()
            if new_phone:
                self.contacts[name] = new_phone
                messagebox.showinfo("Success", f"Contact '{name}' updated.")
                self.update_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Error", "Phone field cannot be empty.")
        else:
            messagebox.showinfo("Update Result", "Contact not found.")

    def delete_contact(self):
        name = self.delete_entry.get().strip()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted.")
            self.delete_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Delete Result", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
