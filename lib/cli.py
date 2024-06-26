# lib/cli.py
from models.card_type import Card_type
from models.card import Card
from models.ability import Ability
from helpers import (
    exit_program,
    list_cards,
    list_card_types,
    list_card_abilities,
    find_card_by_name,
    find_card_by_id,
    list_cards_of_type,
    list_cards_of_ability,
    create_new_card,
    create_new_card_type,
    create_new_card_ability,
    delete_card,
    delete_card_type,
    delete_card_ability
)

def main():
    Card_type.create_table()
    Card.create_table()
    Ability.create_table()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_cards()
        elif choice == "2":
            list_card_types()
        elif choice == "3":
            list_card_abilities()
        elif choice == "4":
            find_card_by_name()
        elif choice == "5":
            find_card_by_id()
        elif choice == "6":
            list_cards_of_type()
        elif choice == "7":
            list_cards_of_ability()
        elif choice == "8":
            create_new_card()
        elif choice == "9":
            create_new_card_type()
        elif choice == "10":
            create_new_card_ability()
        elif choice == "11":
            delete_card()
        elif choice == "12":
            delete_card_type()
        elif choice == "13":
            delete_card_ability()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all Cards")
    print("2. List all card Types")
    print("3. List all card Abilities")
    print("4. Find card by name")
    print("5. Find card by ID number")
    print("6. List cards by card type")
    print("7. List cards by card ability")
    print("8. Create a new card")
    print("9. Create a new card type")
    print("10. Create a new card ability")
    print("11. Delete a Card")
    print("12. Delete card Type")
    print("13. Delete card Ability")

if __name__ == "__main__":
    main()
