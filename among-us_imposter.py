#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Probability of being the imposter | ----\n", fg("red")))

def imposter_chance(i, p):
    return 100*(i/p)

# user interaction
i = float(input("What is the imposter count? (1-3 possible)\n"))
p = float(input("What is the player count? (1-10 possible)\n"))

chance = stylize(str(round(imposter_chance(i, p), 2))+"%", fg("red"))
print(f"\nThe chance of becoming an imposter is {chance}.\n")
