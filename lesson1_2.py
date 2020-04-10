#quantity_of_seconds = 0
quantity_of_minutes = 0
quantity_of_hours = 0

quantity_of_seconds = input("Введите кол-во секунд \n")

quantity_of_hours = int(quantity_of_seconds) // 3600
seconds_without_hours = int(quantity_of_seconds) % 3600
quantity_of_minutes = seconds_without_hours // 60
seconds_without_h_and_m = seconds_without_hours % 60


print ( quantity_of_hours , ":" , quantity_of_minutes , ":" , seconds_without_h_and_m)
#print(quantity_of_seconds_output)