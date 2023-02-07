"""
Enter the amount of the study benefits: 335.32
If the index raise is 1.17 percent, the study benefit,
after a raise, would be 339.243244 euros
"""

name = input("Enter the amount of the study benefits: ")
print("If the index raise is 1.17 percent, the study benefit,"
      "\nafter a raise, would be",float(name) * 101.17/100, "euros"
                                                        "\nand if there was another index raise, the study"
                                                        "\nbenefits would be as much as", float(name)* 101.17/100* 101.17/100,"euros")
