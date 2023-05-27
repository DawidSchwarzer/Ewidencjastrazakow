

class Rescuer:
    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position

    def display_details(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")


class RescuerRegistry:
    def __init__(self):
        self.rescuers = []

    def add_rescuer(self, rescuer):
        self.rescuers.append(rescuer)
        print("Rescuer added successfully.")

    def remove_rescuer(self, first_name, last_name):
        for rescuer in self.rescuers:
            if rescuer.first_name == first_name and rescuer.last_name == last_name:
                self.rescuers.remove(rescuer)
                print(f"Rescuer {first_name} {last_name} removed.")
                return
        print(f"Rescuer {first_name} {last_name} not found.")

    def display_all_rescuers(self):
        if not self.rescuers:
            print("No rescuers found.")
        else:
            print("All Rescuers:")
            for rescuer in self.rescuers:
                rescuer.display_details()

    def display_rescuers_by_age_range(self, start_age, end_age):
        filtered_rescuers = [rescuer for rescuer in self.rescuers if start_age <= rescuer.age <= end_age]

        if not filtered_rescuers:
            print(f"No rescuers found in age range {start_age}-{end_age}.")
        else:
            print(f"Rescuers in age range {start_age}-{end_age}:")
            for rescuer in filtered_rescuers:
                rescuer.display_details()

    def display_rescuers_by_position(self, position):
        filtered_rescuers = [rescuer for rescuer in self.rescuers if rescuer.position == position]

        if not filtered_rescuers:
            print(f"Nie znaleziono ratownika {position}.")
        else:
            print(f"Rescuers with position {position}:")
            for rescuer in filtered_rescuers:
                rescuer.display_details()


def main():
    rescuer_registry = RescuerRegistry()

    while True:
        print("\n===== Ewidencja ratowników OSP Katowice Szopienice =====")
        print("1. Dodaj ratownika")
        print("2. Usuń ratownika")
        print("3. Wyświetl cały podział bojowy")
        print("4. Wyswietl wg wieku")
        print("5. Wyświetl wg stanowiska")
        print("6. Wyjście")

        choice = input("Wpisz swój wybór (1-6): ")

        if choice == '1':
            first_name = input("Podaj imię: ")
            last_name = input("Podaj nazwisko: ")
            age = int(input("Podaj wiek: "))
            position = input("Podaj stanowisko: ")
            rescuer = Rescuer(first_name, last_name, age, position)
            rescuer_registry.add_rescuer(rescuer)

        elif choice == '2':
            first_name = input("Enter First Name of Rescuer to remove: ")
            last_name = input("Enter Last Name of Rescuer to remove: ")
            rescuer_registry.remove_rescuer(first_name, last_name)

        elif choice == '3':
            rescuer_registry.display_all_rescuers()

        elif choice == '4':
            print("Wybierz przedział wiekowy")
            print("1. 18-30")
            print("2. 31-45")
            print("3. 46-65")

            age_choice = input("Wprowadź wybór przedziału wiekowego (1-3): ")

            age_ranges = {
                '1': (18, 30),
                '2': (31, 45),
                '3': (46, 65)
            }

            if age_choice in age_ranges:
                start_age, end_age = age_ranges[age_choice]
                rescuer_registry.display_rescuers_by_age_range(start_age, end_age)
            else:
                print("Nieprawidłowy wybór przedziału wiekowego. Proszę spróbuj ponownie.")
                continue

        elif choice == '5':
            print("Wybierz stanowisko:")
            print("1. Strażak")
            print("2. Starszy strażak")
            print("3. Młodszy ratownik")
            print("4. Ratownik")
            print("5. Starszy Ratownik")
            print("6. Ratownik specjalista")
            print("7. Dowódca zastępu")
            print("8. Dowódca sekcji")
            print("9. Zastępca Naczelnika")
            print("10. Naczelnik")

            position_choice = input("Wprowadź wybór stanowiska(1-10): ")

            positions = {
                '1': 'Strażak',
                '2': 'Starszy strażak',
                '3': 'Młodszy ratownik',
                '4': 'Ratownik',
                '5': 'Starszy Ratownik',
                '6': 'Ratownik specjalista',
                '7': 'Dowódca zastępu',
                '8': 'Dowódca sekcji',
                '9': 'Zastępca Naczelnika',
                '10': 'Naczelnik'
            }

            if position_choice in positions:
                position = positions[position_choice]
                rescuer_registry.display_rescuers_by_position(position)
            else:
                print("Nieprawidłowy wybór stanowiska. Spróbuj ponownie.")
                continue

        elif choice == '6':
            print("Wyjście...")
            break

        else:
            print("Nieprawidłowy wybór. Prosze spórbuj ponownie.")


if __name__ == "__main__":
    main()