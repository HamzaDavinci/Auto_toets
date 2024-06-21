import sqlite3

def list_sahara_cars(destination_name: str) -> list:
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()

    cursor.execute("SELECT distance FROM destinations WHERE name = ?", (destination_name,))
    result = cursor.fetchone()

    if result is None:
        return []

    distance = result[0]

    cursor.execute("SELECT brand, model FROM cars WHERE (usage * tankvolume) >= ?", (distance,))
    cars = cursor.fetchall()

    conn.close()
    return cars

plaatsen = ['Cairo', 'Tunis', 'Tripoli', 'Bamako', 'Khartoum', 'Dordrecht']
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
AQUA = '\033[36m'
RESET = '\033[0m'

for naam in plaatsen:
    cars = list_sahara_cars(naam)
    if cars is None:
        print(f"{RED}Bestemming '{naam}' niet gevonden in de database.{RESET}")
    elif not cars:
        print(f"{RED}Geen auto's gevonden die naar '{naam}' kunnen reizen.{RESET}\n")
    else:
        print(f"{AQUA}Auto's die naar '{naam}' kunnen reizen:{RESET}")
        for brand, model in cars:
            print(f"{GREEN}- {brand} {model}{RESET}")
        print()