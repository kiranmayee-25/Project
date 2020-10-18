from fields import politics,games,awards,driving,judge,climb_Mt,space,ips



def show_choice():
    print("Great! Want to the know who is the first Indian woman in the fields below....Why late?  Pick one")
    print("1.Politics\n2.Games\n3.Awards\n4.Driving\n5.Judge\n6.Climb Mount Everest\n7.Space\n8.IPS\n9.End this chat\n******")
    try:
        return int(input("Enter your choice [1-9] : "))
    except:
        print("Please choose a appropriate option")
        return 0
def first_woman():
    option4=show_choice()
    while(option4!=9):
        if(option4==1):
            politics()
        elif(option4==2):
            games()
        elif(option4==3):
            awards()
        elif(option4==4):
            driving()
        elif(option4==5):
            judge()
        elif(option4==6):
            climb_Mt()
        elif(option4==7):
            space()
        elif(option4==8):
            ips()
        else:
            print("Choose a appropriate choice")
        option4=show_choice()




        

        
        
        

        
        
        
        

        