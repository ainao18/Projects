print("Welcome to UniBuddy!")

name = input("What is your name? ")
age = int(input("How old are you? "))
fav_colour = input("What is your favourite colour? ").lower()

print(f"Hello {name}, nice to meet you! Your favourite colour is {fav_colour}, based on this I have a few clubs I think you'll like!")

if fav_colour == "red":
    print("""
You might like: 
          1. Our red debate team
          2. Our art club
          3. Our wrestling club
For more information on how to join, just ask UniBuddy 'How do I join _ ?'
          """)

elif fav_colour == "blue":
    print("""
You might like: 
          1. Our swimming club
          2. Our cloud watching club
          3. Our public speaking club
For more information on how to join, just ask UniBuddy 'How do I join _ ?'
          """)

elif fav_colour == "green":
    print("""
You might like: 
          1. Our football club
          2. Our origami club
          3. Our gardening club
For more information on how to join, just ask UniBuddy 'How do I join _ ?'
          """)
    
else : 
      print("""
You might like: 
          1. Our nature club
          2. Our graphic design club
          3. Our travel club
For more information on how to join, just ask UniBuddy 'How do I join _ ?'
          """)
      
if age == 18: 
     print ("""
Since you are 18 you might enjoy these events: 
            1. Adulthood 101 on Wednesdays at 7pm in the library
            2. Freshman Mixer on Saturday 8pm in the Main Hall
            """)
     
elif age > 25: 
     print ("""
Based on your age you may enjoy: 
            1. Wine Tasting on Tuesdays at 7pm in the cafeteria
            2. Sip and Paint on Saturday 8pm in the Main Hall
            """)
     
else: 
      print ("""
Based on your age you may enjoy: 
            1. Music and Movement on Thursdays at 7pm in the Main Hall
            2. Cocktail Making on Saturday 8pm in the cafeteria
            """)

while True: 
         
    question = input("Do you have any questions? (type in exit to quit) : ").lower()

    if "how do i join" in question :
     print("To join any of our clubs, please go to your university portal, click on 'Join a Club' and seach for your desired club!")

    if "where" in question :
        print ("If you are lost, please use the map in your university portal! ")
    
    if question == "how are you?":
        print("I'm happy to be helping you!")
    
    if question == "exit": 
        break