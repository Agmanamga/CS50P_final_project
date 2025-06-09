import time
import sys

# ANSI escape sequences for styling text
bold = '\033[1m'
italic = '\033[3m'
end = '\033[0m'

# Inventory and items
inventory = []
found_items = {
    "cog": False,
    "safe_combination": False,
    "lock_box": False,
    "emblem": False,
    "key": False,
    "combination_code": False
}

# Room Clue
room_clue = (
    f"This room is disheveled. You see a big {bold}door{end}, a white {bold}board{end} "
    f"full of sticky notes, a {bold}desk{end}, a pile of {bold}books{end}, and a "
    f"peculiar {bold}safe{end}."
)

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    slow_print("You're awakened and find yourself inside an unfamiliar room.\n  "
               "You’re having difficulty remembering how you got here or any details \n "
               "about yourself.\n"
               "One thing is for sure: this room is unfamiliar to you.\n"
               "Type 'check surrounding' to search the room for clues, \n "
               "'check [item]' to inspect an item, 'use [inventory item] on [item]' to use an item, \n  "
               "or 'exit' to quit the game.")

    while True:
        action = input("\nWhat do you want to do? ").strip().lower()

        if action == "check surrounding":
            slow_print(check_surrounding())

        elif action == "check door":
            slow_print("A big cold metal door with a keyhole, you tried to push it with no avail.\n"
                       "The door is not budging.")

        elif action == "check desk":
            slow_print(check_desk())

        elif action == "check books":
            slow_print(check_books())

        elif action == "check safe":
            check_safe()

        elif action == "check board":
            check_board()

        elif action == "use cog on safe":
            use_cog_on_safe()

        elif action == "use combination code on safe":
            use_combination_code_on_safe()

        elif action == "use emblem on lock box":
            use_emblem_on_lock_box()

        elif action == "use key on door":
            if use_key_on_door():
                break

        elif action == "check inventory":
            check_inventory()

        elif action == "exit":
            slow_print(
                "With no clue for opening the door, you let yourself remain trapped in this room.\n"
                "With a lot of books and ample provisions, you think you can survive here for a long time.\n"
                "The door remains locked, you're still trapped.\n"
                "END"
            )
            break

        else:
            slow_print(
                "Invalid action. Try 'check surrounding' to look around, 'check [item]' to inspect an item, \n "
                "'use [inventory item] on [item]' to use an item, or 'exit' to quit the game."
            )

def check_surrounding():
    return room_clue

def check_desk():
    if not found_items["emblem"]:
        found_items["emblem"] = True
        inventory.append("emblem")
        return f"As you search the desk, you find document related to defence prime minister of Indonesia \n" \
               f"In the last document titled '{italic}Rencana Besar Negara Guna Menghadapi Perang Nuklir{end}', " \
               f"an {bold}emblem{end} falls out.\nYou're intrigued by the emblem. You keep it on your inventory"
    return "You already found the emblem."

def check_books():
    if not found_items["cog"]:
        found_items["cog"] = True
        inventory.append("cog")
        return "As you scoured on the pile of book, you noticed that there's a lot books \n" \
               "Document related to doomsday and Nuclear Warfare. I think Whoever owning this \n" \
               "room is a to too deep reading conspiracy theories. Under the pile of the \n" \
               f"books, you find a {bold}cog{end}. You keep it on your inventory, you have a \n" \
               "gut feeling it's useful for something, so you keep it on your inventory."
    return "You already found the cog."

def check_safe():
    if "cog" in inventory and "combination code" in inventory:
        if not found_items["lock_box"]:
            slow_print("You enter the combination, and the safe opens to reveal a small lock box.")
            found_items["lock_box"] = True
            inventory.append("lock box")
        else:
            slow_print("The safe is already open, and the lock box has been taken.")
    elif "cog" in inventory:
        slow_print("The safe has an exposed mechanism with a missing cog slot.")
    else:
        slow_print("Its a large safe with part of its mechanism exposed. It seems to be missing something.")

def check_board():
    if not found_items["combination_code"]:
        slow_print(
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
            "So you keep the combination code note on your inventory"
        )
        found_items["combination_code"] = True
        inventory.append("combination code")
    else:
        slow_print("You've already found the combination code on the whiteboard.")

def use_cog_on_safe():
    if "cog" in inventory and not found_items["combination_code"]:
        slow_print("You insert the cog into the safe mechanism. A small panel reveals a combination code. the combination code is around here")
    elif "cog" in inventory:
        slow_print("The cog has already been inserted.")
    else:
        slow_print("You don't have a cog to use.")

def use_combination_code_on_safe():
    if "cog" in inventory and "combination code" in inventory:
        check_safe()
    elif "combination code" not in inventory:
        slow_print("You don’t have the combination code to use on the safe.")
    else:
        slow_print("The cog hasn't been placed in the safe mechanism yet.")

def use_emblem_on_lock_box():
    if "lock box" in inventory and "emblem" in inventory and not found_items["key"]:
        slow_print(
            f"You insert the emblem into the lock box, and it clicks open. Inside, you find a letter {bold}key{end}.\n"
            "You keep the key in your inventory."
        )
        found_items["key"] = True
        inventory.append("key")
    elif "lock box" not in inventory:
        slow_print("You need a lock box to use the emblem on.")
    else:
        slow_print("The lock box is already open.")

def use_key_on_door():
    if "key" in inventory:
        slow_print(
            "You insert the key into the door’s keyhole. With a satisfying click, the door unlocks and opens.\n"
            "You've managed to escape the room!"
        )
        return True
    else:
        slow_print("You don't have the key to use on the door.")
    return False

def check_inventory():
    slow_print("Inventory: " + (", ".join(inventory) if inventory else "Your inventory is empty."))

if __name__ == "__main__":
    main()
