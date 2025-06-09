import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time

class EscapeRoomGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Escape Room - Nuclear Conspiracy")
        self.root.configure(bg='#000000')
        self.root.geometry("1000x700")
        
        # Colors
        self.bg_color = '#000000'
        self.neon_orange = '#FF6600'
        self.text_color = '#D3D3D3'
        
        # Game state
        self.inventory = []
        self.found_items = {
            "cog": False,
            "safe_combination": False,
            "lock_box": False,
            "emblem": False,
            "key": False,
            "combination_code": False
        }
        
        self.game_started = False
        self.room_clue = (
            "This room is disheveled. You see a big **door**, a white **board** "
            "full of sticky notes, a **desk**, a pile of **books**, and a "
            "peculiar **safe**."
        )
        
        self.setup_ui()
        self.show_title_screen()
    
    def setup_ui(self):
        # Main frame with neon border
        main_frame = tk.Frame(self.root, bg=self.bg_color, highlightbackground=self.neon_orange, 
                             highlightthickness=3, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Text display area
        self.text_display = scrolledtext.ScrolledText(
            main_frame, 
            wrap=tk.WORD, 
            width=100, 
            height=35,
            bg=self.bg_color,
            fg=self.text_color,
            font=('Courier New', 13),
            insertbackground=self.neon_orange,
            selectbackground=self.neon_orange,
            selectforeground=self.bg_color,
            highlightbackground=self.neon_orange,
            highlightthickness=2
        )
        self.text_display.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.text_display.tag_configure("bold", font=('Courier New', 11, 'bold'), foreground=self.neon_orange)
        self.text_display.tag_configure("italic", font=('Courier New', 11, 'italic'), foreground=self.text_color)
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg=self.bg_color)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Input label
        input_label = tk.Label(input_frame, text="What do you want to do? ", 
                              bg=self.bg_color, fg=self.text_color, 
                              font=('Courier New', 11, 'bold'))
        input_label.pack(side=tk.LEFT)
        
        # Input entry
        self.input_entry = tk.Entry(
            input_frame, 
            bg=self.bg_color, 
            fg=self.text_color, 
            font=('Courier New', 11),
            insertbackground=self.neon_orange,
            highlightbackground=self.neon_orange,
            highlightthickness=2,
            width=60
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10))
        self.input_entry.bind('<Return>', self.process_input)
        
        # Submit button
        self.submit_button = tk.Button(
            input_frame, 
            text="EXECUTE", 
            command=self.process_input,
            bg=self.bg_color,
            fg=self.neon_orange,
            font=('Courier New', 10, 'bold'),
            highlightbackground=self.neon_orange,
            highlightthickness=2,
            activebackground=self.neon_orange,
            activeforeground=self.bg_color,
            relief=tk.FLAT,
            bd=2
        )
        self.submit_button.pack(side=tk.RIGHT)
        
        # Initially disable input
        self.input_entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        self.is_typing = False
        self.typing_queue = []
    
    def show_title_screen(self):
        title_art = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     ██████╗ ██████╗ ██╗     ██████╗     ██████╗  ██████╗  ██████╗ ███╗   ███╗ ║
║    ██╔════╝██╔═══██╗██║     ██╔══██╗    ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║ ║
║    ██║     ██║   ██║██║     ██║  ██║    ██████╔╝██║   ██║██║   ██║██╔████╔██║ ║
║    ██║     ██║   ██║██║     ██║  ██║    ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║ ║
║    ╚██████╗╚██████╔╝███████╗██████╔╝    ██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║ ║
║     ╚═════╝ ╚═════╝ ╚══════╝╚═════╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

>> PRESS ANY KEY TO BEGIN <<
>> THE TRUTH AWAITS OUTSIDE <
        """
        
            # Configure center alignment tag
        self.text_display.tag_configure("center", justify='center')
        
        # Insert title with center tag
        start_pos = self.text_display.index(tk.INSERT)
        self.text_display.insert(tk.END, title_art)
        end_pos = self.text_display.index(tk.INSERT)
        self.text_display.tag_add("center", start_pos, end_pos)
        self.text_display.config(state='disabled')
        
        # Bind any key press to start game
        self.root.bind('<Key>', self.start_game)
        self.root.focus_set()
    
    def start_game(self, event=None):
        if not self.game_started:
            self.game_started = True
            self.root.unbind('<Key>')
            self.text_display.config(state='normal')
            self.text_display.delete(1.0, tk.END)
            
            # Enable input
            self.input_entry.config(state='normal')
            self.submit_button.config(state='normal')
            self.input_entry.focus_set()
            
            # Start the game
            self.slow_print("You're awakened and find yourself inside an unfamiliar room.\n"
                           "You're having difficulty remembering how you got here or any details about yourself\n"
                           "You feel a massive headache, blood drippping from your chin.\n "
                           "There's an empty handgun on the floor. You're Very confused right now, \n "
                           "but one thing is for sure: this room is unfamiliar to you.\n"
                           "Type 'check surrounding' to search the room for clues, \n "
                           "'check [item]' to inspect an item, 'use [inventory item] on [item]' to use an item, \n"
                           "or 'exit' to quit the game.\n\n")
    
    def slow_print(self, text, delay=0.03):
        self.is_typing = True
        self.input_entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        
        def print_chars():
            try:
                # Parse the text to identify formatting
                i = 0
                while i < len(text):
                    if hasattr(self, 'root') and not self.root.winfo_exists():
                        break
                        
                    # Check for bold formatting **text**
                    if text[i:i+2] == '**':
                        # Find the closing **
                        end_bold = text.find('**', i+2)
                        if end_bold != -1:
                            # Insert the bold text
                            bold_text = text[i+2:end_bold]
                            self.root.after(0, lambda t=bold_text: self.insert_bold_text(t))
                            i = end_bold + 2
                            time.sleep(len(bold_text) * delay)
                            continue
                    
                    # Check for italic formatting *text*
                    if text[i] == '*' and (i == 0 or text[i-1] != '*') and (i+1 >= len(text) or text[i+1] != '*'):
                        # Find the closing *
                        end_italic = text.find('*', i+1)
                        if end_italic != -1:
                            # Insert the italic text
                            italic_text = text[i+1:end_italic]
                            self.root.after(0, lambda t=italic_text: self.insert_italic_text(t))
                            i = end_italic + 1
                            time.sleep(len(italic_text) * delay)
                            continue
                    
                    # Regular character
                    char = text[i]
                    self.root.after(0, lambda c=char: self.text_display.insert(tk.END, c))
                    self.root.after(0, lambda: self.text_display.see(tk.END))
                    i += 1
                    time.sleep(delay)
                
                # Add final newline
                self.root.after(0, lambda: self.text_display.insert(tk.END, "\n"))
                self.root.after(0, lambda: self.text_display.see(tk.END))
                
            finally:
                if hasattr(self, 'root') and self.root.winfo_exists():
                    self.root.after(0, self.enable_input)
        
        thread = threading.Thread(target=print_chars)
        thread.daemon = True
        thread.start()

    def insert_bold_text(self, text):
        """Insert bold text character by character"""
        for char in text:
            start_index = self.text_display.index(tk.INSERT)
            self.text_display.insert(tk.END, char)
            end_index = self.text_display.index(tk.INSERT)
            self.text_display.tag_add("bold", start_index, end_index)
            self.text_display.see(tk.END)

    def insert_italic_text(self, text):
        """Insert italic text character by character"""
        for char in text:
            start_index = self.text_display.index(tk.INSERT)
            self.text_display.insert(tk.END, char)
            end_index = self.text_display.index(tk.INSERT)
            self.text_display.tag_add("italic", start_index, end_index)
            self.text_display.see(tk.END)

    def enable_input(self):
        """Re-enable input after typing is complete"""
        self.is_typing = False
        self.input_entry.config(state='normal')
        self.submit_button.config(state='normal')
        self.input_entry.focus_set()
        
    def insert_formatted_text(self, text):
        """Insert text with **bold** and *italic* formatting"""
        parts = text.split('**')
        for i, part in enumerate(parts):
            if i % 2 == 0:  # Regular text
                # Check for italic in regular text
                italic_parts = part.split('*')
                for j, italic_part in enumerate(italic_parts):
                    if j % 2 == 0:  # Regular text
                        self.text_display.insert(tk.END, italic_part)
                    else:  # Italic text
                        start_index = self.text_display.index(tk.INSERT)
                        self.text_display.insert(tk.END, italic_part)
                        end_index = self.text_display.index(tk.INSERT)
                        self.text_display.tag_add("italic", start_index, end_index)
            else:  # Bold text
                start_index = self.text_display.index(tk.INSERT)
                self.text_display.insert(tk.END, part)
                end_index = self.text_display.index(tk.INSERT)
                self.text_display.tag_add("bold", start_index, end_index)
            
    # Replace your process_input method with this:
    def process_input(self, event=None):
        if not self.game_started or self.is_typing:
            return
            
        action = self.input_entry.get().strip().lower()
        if not action:  # Don't process empty input
            return
            
        self.input_entry.delete(0, tk.END)
        
        # Display user input
        self.text_display.insert(tk.END, f"> {action}\n")
        self.text_display.see(tk.END)
        
        # Process the action
        if action == "check surrounding":
            self.slow_print(self.check_surrounding())

        elif action == "check door":
            self.slow_print("A big cold metal door with a keyhole, you tried to push it with no avail.\n"
                           "The door is not budging.")

        elif action == "check desk":
            self.slow_print(self.check_desk())

        elif action == "check books":
            self.slow_print(self.check_books())

        elif action == "check safe":
            self.check_safe()

        elif action == "check board":
            self.check_board()
        
        elif action == "check lock box":
            self.check_lock_box()

        elif action == "use cog on safe":
            self.use_cog_on_safe()

        elif action == "use combination code on safe":
            self.use_combination_code_on_safe()

        elif action == "use emblem on lock box":
            self.use_emblem_on_lock_box()

        elif action == "use key on door":
            if self.use_key_on_door():
                self.end_game()

        elif action == "check inventory":
            self.check_inventory()
            
        elif action == "check letter":
            self.check_letter()

        elif action == "exit":
            self.slow_print(
                "With no clue for opening the door, you let yourself remain trapped in this room.\n"
                "With a lot of books and ample provisions, you think you can survive here for a long time.\n"
                "The door remains locked, you're still trapped.\n"
                "END"
            )
            self.end_game()

        else:
            self.slow_print(
                "Invalid action. Try 'check surrounding' to look around, 'check [item]' to inspect an item, \n "
                "'use [inventory item] on [item]' to use an item, or 'exit' to quit the game."
            )
    
    def check_surrounding(self):
        return self.room_clue

    def check_desk(self):
        if not self.found_items["emblem"]:
            self.found_items["emblem"] = True
            self.inventory.append("emblem")
            return "As you search the desk, you find document related to defence prime minister of Indonesia \n" \
                   "In the last document titled '*Rencana Besar Negara Guna Menghadapi Perang Nuklir*', " \
                   "an **emblem** falls out.\nYou're intrigued by the emblem. You keep it on your inventory"
        return "You already found the emblem."

    def check_books(self):
        if not self.found_items["cog"]:
            self.found_items["cog"] = True
            self.inventory.append("cog")
            return "As you scoured on the pile of book, you noticed that there's a lot books \n" \
                   "Document related to doomsday and Nuclear Warfare. I think Whoever owning this \n" \
                   "room is a to too deep reading conspiracy theories. Under the pile of the \n" \
                   "books, you find a **cog**. You keep it on your inventory, you have a \n" \
                   "gut feeling it's useful for something, so you keep it on your inventory."
        return "You already found the cog."

    def check_safe(self):
        if "cog" in self.inventory and "combination code" in self.inventory:
            if not self.found_items["lock_box"]:
                self.slow_print("You enter the combination, and the safe opens to reveal a small **lock box**.")
                self.found_items["lock_box"] = True
                self.inventory.append("lock box")
            else:
                self.slow_print("The safe is already open, and the lock box has been taken.")
        elif "cog" in self.inventory:
            self.slow_print("The safe has an exposed mechanism with a missing cog slot.")
        else:
            self.slow_print("Its a large safe with part of its mechanism exposed. It seems to be missing something.")
    
    def check_lock_box(self):
        if not self.found_items["emblem"]:
            self.slow_print("its a small lockbox with a missing part on its top, maybe saothing on this room can fit on this")
        else:
            self.slow_print("its a small lockbox with a missing part on its top, it shaped like **emblem** you found before")

    def check_board(self):
        if not self.found_items["combination_code"]:
            self.slow_print(
                "You examine the whiteboard covered in notes. You read each note curiously:\n"
                "26/01/2045. Perselisihan Kubu Barat dan Timur semakin intens, \n"
                "Peerebutan sumber daya menjadi masalah utama. Indonesia yang berada di antara \n"
                "kedua kubu tersebut bisa menjadi korban.\n"
                "03/02/2045. Saya menduga bahwa Ada pihak asing yang berperan akan merenggangnya \n"
                "kedua kubu, mereka terlalu buta untuk melihat bahwa mereka dikendalikan oleh pihak \n"
                "lain untuk saling terpecah belah.\n"
                "05/02/2045. Saya berusaha memberitahu informasi terkait dengan perselisihan kubu \n"
                "barat dan timur tapi presiden tidak mengindahkan, dia hanya terfokus pada pengelolaan \n"
                "sumber daya energi baru di Sulawesi Tenggara.\n"
                "21/05/2045. Saya mendapatkan intel bahwa kalahnya Pihak timur dalam perebutan titik \n"
                "sumber daya terbaru yang ditemukan di pusat Sahara dikarenakan ada intervensi pihak \n"
                "yang tidak dikenal oleh masing-masing kubu.\n"
                "14/08/2045. Situasi makin kacau, rudal nuklir yang tidak diketahui asal usulnya \n"
                "mengenai gedung Pentagon. Tidak ada pihak dari kubu timur yang mengakui serangan \n"
                "tersebut dari mereka.\n"
                "16/08/2045. Amerika membabi buta, Mereka menembakkan rudal mereka ke masing-masing \n"
                "negara dari kubu timur dengan bantuan dari kubu barat.\n"
                "17/08/2045. Perang Tidak terelakkan, republik akan hancur terkena efek perang dari \n"
                "kedua kubu tersebut. Saya akan tetap di sini sampai situasi lebih aman, entah sampai kapan.\n"
                "The last note only says 17081945, which might be the combination code for something.\n"
                "So you keep the **combination code** note on your inventory"
            )
            self.found_items["combination_code"] = True
            self.inventory.append("combination code")
        else:
            self.slow_print("You've already found the combination code on the whiteboard.")

    def use_cog_on_safe(self):
        if "cog" in self.inventory and not self.found_items["combination_code"]:
            self.slow_print("You insert the cog into the safe mechanism. A small panel reveals a combination code. the combination code is around here")
        elif "cog" in self.inventory:
            self.slow_print("The cog has already been inserted.")
        else:
            self.slow_print("You don't have a cog to use.")

    def use_combination_code_on_safe(self):
        if "cog" in self.inventory and "combination code" in self.inventory:
            self.check_safe()
        elif "combination code" not in self.inventory:
            self.slow_print("You don't have the combination code to use on the safe.")
        else:
            self.slow_print("The cog hasn't been placed in the safe mechanism yet.")

    def use_emblem_on_lock_box(self):
        if "lock box" in self.inventory and "emblem" in self.inventory and not self.found_items["key"]:
            self.slow_print(
                "You insert the emblem into the lock box, and it clicks open. Inside, you find a **letter** and a **key**.\n"
                "You keep the key and the letter in your inventory."
            )
            self.found_items["key"] = True
            self.inventory.append("key")
            self.found_items["letter"] = True
            self.inventory.append("letter")
        elif "lock box" not in self.inventory:
            self.slow_print("You need a lock box to use the emblem on.")
        else:
            self.slow_print("The lock box is already open.")

    def use_key_on_door(self):
        if "key" in self.inventory:
            self.slow_print(
                "You insert the key into the door's keyhole. With a satisfying click, the door unlocks and opens.\n"
                "You've managed to escape the room!"
            )
            return True
        else:
            self.slow_print("You don't have the key to use on the door.")
        return False

    def check_letter(self):
        if letter in self.inventory:
            self.slow_print(f"Aku telah gagal melindungi Indonesia dari ancaman perang, suaraku tidak didengar sama sekali.\n"
                            "Diam di sini pun rasanya percuma, aku hanya melindungi diriku sendiri sedangkan di luar sana telah hancur,\n"
                            "Persediaan makanan juga sudah mau habis. Daripada aku mati kelaparan, lebih baik aku akhiri diriku lebih dahulu.\n"
                            "Buat siapapun yang membaca pesan ini dan apapun yang ada di ruangan ini, aku harap kamu akhirnya kamu tahu \n"
                            "yang menciptakan neraka ini.\n \n"
                            "You realized something as you read this, you take a deep beath and put the letter on your pocket")
            
    def check_inventory(self):
        self.slow_print("Inventory: " + (", ".join(self.inventory) if self.inventory else "Your inventory is empty."))
    
    def end_game(self):
        self.input_entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        
        # Add restart option
        restart_button = tk.Button(
            self.root,
            text="RESTART GAME",
            command=self.restart_game,
            bg=self.bg_color,
            fg=self.neon_orange,
            font=('Courier New', 12, 'bold'),
            highlightbackground=self.neon_orange,
            highlightthickness=2,
            activebackground=self.neon_orange,
            activeforeground=self.bg_color,
            relief=tk.FLAT,
            bd=2
        )
        restart_button.pack(pady=10)
    
    def restart_game(self):
        self.root.destroy()
        new_game = EscapeRoomGUI()
        new_game.run()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = EscapeRoomGUI()
    game.run()