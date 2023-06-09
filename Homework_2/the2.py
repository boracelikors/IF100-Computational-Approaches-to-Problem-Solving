number_checker = "12345678"
letter_checker = "abcdefgh"

knight_horizantal = str(input("Please enter horizontal position of the knight (a,b,c,d,e,f,g,h): ")).lower()
bishop_vertical = 0
bishop_horizantal = 0
knight_vertical = 0




if len(knight_horizantal) != 1 or knight_horizantal.isalpha() == False:
  print("Horizontal input for knight is not a letter")
elif knight_horizantal not in letter_checker:
  print("Horizontal input for knight is not a proper letter")
else:
  knight_vertical = str(input("Please enter vertical position of the knight (1,2,3,4,5,6,7,8): "))
  if knight_vertical.isdigit() == False:
    print("Vertical input for knight is not a number")
  elif len(knight_vertical) != 1:
    print("Vertical input for knight is not a proper number")
  elif knight_vertical not in number_checker:
    print("Vertical input for knight is not a proper number") 
  else:
    bishop_horizantal = str(input("Please enter horizontal position of the bishop (a,b,c,d,e,f,g,h): ")).lower()
    if len(bishop_horizantal) != 1 or bishop_horizantal.isalpha() == False:
      print("Horizontal input for bishop is not a letter")
    elif bishop_horizantal not in letter_checker:
      print("Horizontal input for bishop is not a proper letter")
    else:
      bishop_vertical = str(input("Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): "))
      if bishop_vertical.isdigit() == False:
        print("Vertical input for bishop is not a number")
      elif len(bishop_vertical) != 1:
        print("Vertical input for bishop is not a proper number")
      elif bishop_vertical not in number_checker:
        print("Vertical input for bishop is not a proper number") 
      else:
        if bishop_horizantal == knight_horizantal and bishop_vertical == knight_vertical:
          print("They can't be in the same square")
        else:
          knight_co = knight_horizantal + knight_vertical
          bishop_co = bishop_horizantal + bishop_vertical
          isbishop = True
          isknight= True
          letters = " abcdefgh"
          
          bishop_vertical_co = int(bishop_vertical)
          knight_vertical_co = int(knight_vertical)
          bishop_horizantal_co = letters.find(bishop_horizantal)
          knight_horizantal_co = letters.find(knight_horizantal)
          xlerfarki = bishop_horizantal_co - knight_horizantal_co
          ylerfarki = bishop_vertical_co - knight_vertical_co

          if abs(xlerfarki) == abs(ylerfarki):
            print("Bishop can attack knight")
          elif (abs(ylerfarki) == 2 and abs(xlerfarki) == 1) or (abs(ylerfarki) == 1 and abs(xlerfarki) == 2):
            print("Knight can attack bishop")
          else:
            print("Neither of them can attack each other")



            
            
            
        
            


        
          

        

         
      
    





  
