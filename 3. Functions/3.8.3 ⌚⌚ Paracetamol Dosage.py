"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""


def calculate_dose(a, b, c):
    """oifsjdoifjoiejfoijweoifjw"""
    k = 0
    if b >= 6:
        t = 15 * a
        if c + t > 4000:
            k = 4000 - c
        else:
            k = t
    return k


def main():
    """oifsjdoifjoiejfoijweoifjw"""
    a = int(input("Patient's weight (kg): "))
    b = int(input("How much time has passed from the previous dose (full hours): "))
    c = int(input("The total dose for the last 24 hours (mg): "))
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(a, b, c)}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
    main()
