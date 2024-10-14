import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="Tawes", database="klasse_und_items"
)

cursor = connection.cursor()


def read_data():
    cursor.execute("Select ID_ITEMSLOT, SLOT, SOURCE From slot_drop")
    result = cursor.fetchall()

    print("\nAltuelle Liste:")
    print(f"{'ID':<5} {"Slot":<15} {"Quelle":<15}")
    print("-" * 35)
    
    for row in result:
        slot_id, slot_name, source = row
        print(f"{slot_id:<5} {slot_name:<15} {source:<15}")
        


def update_source_for_slot(slot_id, source):
    cursor.execute(
        "UPDATE slot_drop SET SOURCE = %s WHERE ID_ITEMSLOT = %s", (source, slot_id)
    )
    connection.commit()


# def insert_data(source):
#    cursor.execute("INSERT INTO slot_drop(SOURCE)VALUES (%s)", (source))
#    connection.commit()

# Hauptprogramm
while True:
    print("\nAktuelle Slots:")
    read_data()
    print("-" * 40)

    slot_id = input(
        "Geben sie die SLOT-ID ein, die Sie ändern möchten (oder 'exit' zum Beenden des Programms)\nSlot: "
    )
    if slot_id.lower() == "exit":
        break

    try:
        slot_id = int(slot_id)
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine gültige Slot ID ein.")
        continue

    new_Source = input(f"Geben Sie den neue Quelle für den Slot {slot_id} ein: ")

    update_source_for_slot(slot_id, new_Source)
    print(f"Slot {slot_id} wurden aktualisiert! Quelle: '{new_Source}'")


# for slot_id in range(1, 15):
#    source_Value = input(f"Quelle für Slot :{slot_id} ")
#    update_source_for_slot(slot_id, source_Value)
#    print(f"Updatet Slot {slot_id}: {source_Value}")
#    read_data()
#    print("-" * 40)


cursor.close
connection.close
