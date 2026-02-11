#
# Name
# Date
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
import math

people = int(input("Enter the number of people attending: "))
hotdogs_per_person = int(input("Enter the number of hot dogs per person: "))

total_hotdogs = people * hotdogs_per_person

hotdog_packages = math.ceil(total_hotdogs / 10)
bun_packages = math.ceil(total_hotdogs / 8)

leftover_hotdogs = (hotdog_packages * 10) - total_hotdogs
leftover_buns = (bun_packages * 8) - total_hotdogs

print("Minimum packages of hot dogs needed:", hotdog_packages)
print("Minimum packages of hot dog buns needed:", bun_packages)
print("Hot dogs left over:", leftover_hotdogs)

print("Hot dog buns left over:", leftover_buns)