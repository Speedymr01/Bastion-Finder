def get_coordinates():
   x_cord = int(input("Enter X cord: "))
   z_cord = int(input("Enter Z cord: "))
   
   start_x = x_cord / 480
   start2_x = round(start_x, None)
   start3_x = start2_x * 480
   
   start_z = z_cord / 480
   start2_z = round(start_z, None)
   start3_z = start2_z * 480
   
   coord104_x = start3_x + 104
   coord208_x = start3_x + 208
   coord312_x = start3_x + 312
   coord104_z = start3_z + 104
   coord208_z = start3_z + 208
   coord312_z = start3_z + 312
   
   print("Here are your coordinates:")
   for i in range(1, 10):
       if i == 1: print(f"1: {coord104_x}, {coord104_z}")
       elif i == 2: print(f"2: {coord104_x}, {coord208_z}")
       elif i == 3: print(f"3: {coord104_x}, {coord312_z}")
       elif i == 4: print(f"4: {coord208_x}, {coord104_z}")
       elif i == 5: print(f"5: {coord208_x}, {coord208_z}")
       elif i == 6: print(f"6: {coord208_x}, {coord312_z}")
       elif i == 7: print(f"7: {coord312_x}, {coord104_z}")
       elif i == 8: print(f"8: {coord312_x}, {coord208_z}")
       elif i == 9: print(f"9: {coord312_x}, {coord312_z}")

get_coordinates()
