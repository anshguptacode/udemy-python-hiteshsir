seat_type=input("Enter Seat Typ(sleeper/ac/general?luxury): ").upper()
match seat_type:
    case "sleeper":
        print("NO AC but beds avaliable")
    case "ac":
        print("AC CHOOSEN")
    case "general":
        print("No reservation required")
    case "luxury":
        print("best avaliable")
    case _:
        print("Nt avalibale")