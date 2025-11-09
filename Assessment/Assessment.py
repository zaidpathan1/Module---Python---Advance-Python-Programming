import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class User:
    def __init__(self, username):
        self.username = username


class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def save_to_file(self):
        """Save post content to a file"""
        try:
            if not os.path.exists("posts"):
                os.makedirs("posts")

            filename = f"posts/{self.user.username}_{self.title}.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"Author: {self.user.username}\n")
                file.write(f"Title: {self.title}\n\n")
                file.write(self.content)

            messagebox.showinfo("Success", f"Post '{self.title}' saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save post: {e}")


class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog App")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f4f7")

        Label(root, text="MiniBlog", font=("Arial", 20, "bold"), bg="#f0f4f7").pack(pady=10)

        Label(root, text="Your Name:", bg="#f0f4f7", font=("Arial", 12)).pack()
        self.username_entry = Entry(root, width=40)
        self.username_entry.pack(pady=5)

        Label(root, text="Post Title:", bg="#f0f4f7", font=("Arial", 12)).pack()
        self.title_entry = Entry(root, width=40)
        self.title_entry.pack(pady=5)

        Label(root, text="Post Content:", bg="#f0f4f7", font=("Arial", 12)).pack()
        self.content_text = Text(root, width=60, height=10)
        self.content_text.pack(pady=5)

        Button(root, text="Save Post", command=self.save_post, bg="#4CAF50", fg="white", width=15).pack(pady=5)
        Button(root, text="Load Posts", command=self.load_posts, bg="#2196F3", fg="white", width=15).pack(pady=5)

        # Dropdown/Listbox to show posts
        Label(root, text="View Saved Posts:", bg="#f0f4f7", font=("Arial", 12)).pack()
        self.post_listbox = Listbox(root, width=50)
        self.post_listbox.pack(pady=5)
        self.post_listbox.bind("<<ListboxSelect>>", self.view_post)

        # Display area for loaded post
        Label(root, text="Selected Post Content:", bg="#f0f4f7", font=("Arial", 12)).pack()
        self.view_text = Text(root, width=60, height=10, state=DISABLED)
        self.view_text.pack(pady=5)


    def save_post(self):
        username = self.username_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", END).strip()

        
        if not username or not title or not content:
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return

        user = User(username)
        post = Post(user, title, content)
        post.save_to_file()

        
        self.title_entry.delete(0, END)
        self.content_text.delete("1.0", END)
        self.load_posts()

    def load_posts(self):
        """Load saved post filenames into the Listbox"""
        self.post_listbox.delete(0, END)
        try:
            if not os.path.exists("posts"):
                messagebox.showinfo("Info", "No posts found.")
                return

            files = os.listdir("posts")
            for file in files:
                if file.endswith(".txt"):
                    self.post_listbox.insert(END, file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load posts: {e}")

    def view_post(self, event):
        """Display selected post content"""
        try:
            selected = self.post_listbox.get(self.post_listbox.curselection())
            filepath = f"posts/{selected}"
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            self.view_text.config(state=NORMAL)
            self.view_text.delete("1.0", END)
            self.view_text.insert(END, content)
            self.view_text.config(state=DISABLED)

        except IndexError:
           
            pass
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open post: {e}")


if __name__ == "__main__":
    root = Tk()
    app = MiniBlogApp(root)
    root.mainloop()