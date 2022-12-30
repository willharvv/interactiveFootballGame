def start_game():
  # Print the opening message
  print("Welcome to an interactive footy game!")
  print("You are an Arseanl FC player in an attack against Man City.")
  print("You meet John Stones. Do you pass left or right?")
  
  # Get the user's choice
  choice = input("> ")
  
  # Check the user's choice and respond accordingly
  if choice == "left":
    print("You passed left.")
    print("Martinelli now has the ball")
    print("Do you shoot or travel?")
    
    # Get the user's choice
    choice = input("> ")
    
    # Check the user's choice and respond accordingly
    if choice == "shoot":
      print("your shot takes a deflection and goes for a corner")
      print("weldone you won a corner for the arsenal!")
    else:
      print("you push the ball past Walker but he beats you to it and you loose possession.")
  else:
    print("Sakas got the ball!")
    print("he beats one player!")
    print("Do you pass or travel?")
    
    # Get the user's choice
    choice = input("> ")
    
    # Check the user's choice and respond accordingly
    if choice == "pass":
      print("your pass is not controlled")
      print("the ball goes out for a corner:(")
    else:
      print("you dribble past diaz and shoot")
      print("goalaciooooooooo!!!!!")

# Start the game
start_game()
