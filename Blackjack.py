import tkinter as tk
from PIL import ImageTk, Image
from random import randint, sample
from cardVisuals import CardVisuals
import math


# Make the root window

root = tk.Tk(screenName=None, baseName=None, className="Tk", useTk=1)
root.geometry("1920x1080")
root.title("Blackjack v1")
root.configure(bg="#3d6b38")
#bg_image = ImageTk.PhotoImage((Image.open("Blackjack/blackjack/assets/background.jpg")).resize((1920, 1080)))
#backgroundLabel = tk.Label(root, image = bg_image)
#backgroundLabel.place(x = 0, y = 0, relwidth = 1, relheight= 1)
print("Root made")

# Make a list of all cards
allCards = [
    "AS", "AD", "AC", "AH",
    "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
    "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
    "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK",
    "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK"
    ]

# Declares the hands and their initial values

player = []
dealer = []

# Make a list to prevent garbage collection
cardsOnScreen = []

# Create the hand counters on root

dealerCounter = tk.Canvas(root, width=400, height=400, bg="#3d6b38", highlightthickness=0)
dealerCircle = dealerCounter.create_oval(0, 0, 238, 238, fill="white", outline="")
dealerText = dealerCounter.create_text(119, 119, text="0", font=("Arial", 85), fill="black")
playerCounter = tk.Canvas(root, width=350, height=350, bg="#3d6b38", highlightthickness=0)
playerCircle = playerCounter.create_oval(0, 0, 238, 238, fill="white", outline="")
playerText = playerCounter.create_text(119, 119, text="0", font=("Arial", 85), fill="black")


# Place the counters
playerCounter.place(x = 1650, y = 740)
dealerCounter.place(x=1650, y = 20)

#Initialise card assets
CardVisuals.initCards("assets/cards.jpg")
cards = Image.open("assets/cards.jpg")

#Function to sort the hand via the number and faces first

def sortHand(card): #This sorts card by making face and numbers false, while aces true, and as trues are of a higher value are placed at a higher index
    return deck[card]["tag"] == "Ace"

def countHand(deck, hand, mode) -> int: #Adds value of the card to the deck 
    sortedHand = sorted(hand, key=sortHand)
    total = 0
    for card in sortedHand: 
        if deck[card]["tag"] != "Ace": #If the card is not an ace, just add the value
            total += deck[card]["value"]
        else:   #If it is an ace
            if total <= 10: #If the total is less or equal to 10, add 11
                total += 11
            else: # Else add 1 otherwise the player will bust 
                total += deck[card]["value"]
    if mode == "dealer": #This is the dealer visible total, which doesnt include the blank card
        if deck[hand[0]]["tag"] == "Ace":
            return 11, total
        else:
            return deck[hand[0]]["value"], total
    return total

def updateText(playerCanvas, dealerCanvas, playerText, dealerText, playerHand, dealerHand, mode): #updates text
        playerCanvas.itemconfig(playerText, text = str(countHand(deck, playerHand, mode="player")))
        print(f"set player to {(countHand(deck, playerHand, mode='player'))}")
        if mode == "hidden":
            dealerCanvas.itemconfig(dealerText, text = str((countHand(deck, dealerHand, mode="dealer")[0])))
            print(f"set dealer to {(countHand(deck, dealerHand, mode='dealer'))}")
        elif mode == "visible":
            dealerCanvas.itemconfig(dealerText, text = str((countHand(deck, dealerHand, mode="dealer")[1])))
            print(f"set dealer to {(countHand(deck, dealerHand, mode='dealer'))}")

def makeHand(allCards, playerHand, dealerHand): #generates a unique hand
    dealerHand = sample([card for card in allCards if card not in playerHand and card not in dealerHand], 2)
    playerHand = sample([card for card in allCards if card not in playerHand and card not in dealerHand], 2)
    
    return dealerHand, playerHand



# Deck of all cards

deck = {
    "Blank" : {
        "name" : "Blank card, what did you expect?",
        "value" : 0,
        "x_alignment" : 0,
        "y_alignment" : 0,
        "tag" : "Blank"
    },

    #Aces

    "AS" : {
        "name" : "Ace of Spades",
        "value" : 1,
        "x_alignment" : 400,
        "y_alignment" : 0,
        "tag" : "Ace"
    },
    "AD" : {
        "name" : "Ace of Diamonds",
        "value" : 1,
        "x_alignment" : 2800,
        "y_alignment" : 1680,
        "tag" : "Ace"
    },
    "AC" : {
        "name" : "Ace of Clubs",
        "value" : 1,
        "x_alignment" : 2000,
        "y_alignment" : 1120,
        "tag" : "Ace"
    },
    "AH" : {
        "name" : "Ace of Hearts",
        "value" : 1,
        "x_alignment" : 1200,
        "y_alignment" : 560,
        "tag" : "Ace"
    # Suit of Diamonds

    },
    "D2" : {
        "name" : "Two of Diamonds",
        "value" : 2,
        "x_alignment" : 3200,
        "y_alignment" : 1680,
        "tag" : "Number"
    },
    "D3" : {
        "name" : "Three of Diamonds",
        "value" : 3,
        "x_alignment" : 3600,
        "y_alignment" : 1680,
        "tag" : "Number"
    },
    "D4" : {
        "name" : "Four of Diamonds",
        "value" : 4,
        "x_alignment" : 4000,
        "y_alignment" : 1680,
        "tag" : "Number"
    },
    "D5" : {
        "name" : "Five of Diamonds",
        "value" : 5,
        "x_alignment" : 0,
        "y_alignment" : 2240,
        "tag" : "Number"
    },
    "D6" : {
        "name" : "Six of Diamonds",
        "value" : 6,
        "x_alignment" : 400,
        "y_alignment" : 2240,
        "tag" : "Number"
    },
    "D7" : {
        "name" : "Seven of Diamonds",
        "value" : 7,
        "x_alignment" : 800,
        "y_alignment" : 2240,
        "tag" : "Number"
    },
    "D8" : {
        "name" : "Eight of Diamonds",
        "value" : 8,
        "x_alignment" : 1200,
        "y_alignment" : 2240,
        "tag" : "Number"
    },
    "D9" : {
        "name" : "Nine of Diamonds",
        "value" : 9,
        "x_alignment" : 1600,
        "y_alignment" : 2240,
        "tag" : "Number"
    },
    "D10" : {
        "name" : "Ten of Diamonds",
        "value" : 10,
        "x_alignment" : 2000,
        "y_alignment" : 2240,
        "tag" : "Number"
    },
    "DJ" : {
        "name" : "Jack of Diamonds",
        "value" : 10,
        "x_alignment" : 2400,
        "y_alignment" : 2240,
        "tag" : "Face"
    },
    "DQ" : {
        "name" : "Queen of Diamonds",
        "value" : 10,
        "x_alignment" : 2800,
        "y_alignment" : 2240,
        "tag" : "Face"
    },
    "DK" : {
        "name" : "King of Diamonds",
        "value" : 10,
        "x_alignment" : 3200,
        "y_alignment" : 2240,
        "tag" : "Face"
    },
    "H2" : {
        "name" : "Two of Hearts",
        "value" : 2,
        "x_alignment" : 1600,
        "y_alignment" : 560,
        "tag" : "Number"
    },
    "H3" : {
        "name" : "Three of Hearts",
        "value" : 3,
        "x_alignment" : 2000,
        "y_alignment" : 560,
        "tag" : "Number"
    },
    "H4" : {
        "name" : "Four of Hearts",
        "value" : 4,
        "x_alignment" : 2400,
        "y_alignment" : 560,
        "tag" : "Number"
    },
    "H5" : {
        "name" : "Five of Hearts",
        "value" : 5,
        "x_alignment" : 2800,
        "y_alignment" : 560,
        "tag" : "Number"
    },
    "H6" : {
        "name" : "Six of Hearts",
        "value" : 6,
        "x_alignment" : 3200,
        "y_alignment" : 560,
        "tag" : "Number"
    },
    "H7" : {
        "name" : "Seven of Hearts",
        "value" : 7,
        "x_alignment" : 3600,
        "y_alignment" : 560,
        "tag" : "Number"
    },
    "H8" : {
        "name" : "Eight of Hearts",
        "value" : 8,
        "x_alignment" : 4000,
        "y_alignment" : 560,
        "tag" : "Number"
    },
    "H9" : {
        "name" : "Nine of Hearts",
        "value" : 9,
        "x_alignment" : 0,
        "y_alignment" : 1120,
        "tag" : "Number"
    },
    "H10" : {
        "name" : "Ten of Hearts",
        "value" : 10,
        "x_alignment" : 400,
        "y_alignment" : 1120,
        "tag" : "Number"
    },
    "HJ" : {
        "name" : "Jack of Hearts",
        "value" : 10,
        "x_alignment" : 800,
        "y_alignment" : 1120,
        "tag" : "Face"
    },
    "HQ" : {
        "name" : "Queen of Hearts",
        "value" : 10,
        "x_alignment" : 1200,
        "y_alignment" : 1120,
        "tag" : "Face"
    },
    "HK" : {
        "name" : "King of Hearts",
        "value" : 10,
        "x_alignment" : 1600,
        "y_alignment" : 1120,
        "tag" : "Face"
    },
    "C2" : {
        "name" : "Two of Clubs",
        "value" : 2,
        "x_alignment" : 2400,
        "y_alignment" : 1120,
        "tag" : "Number"
    },
    "C3" : {
        "name" : "Three of Clubs",
        "value" : 3,
        "x_alignment" : 2800,
        "y_alignment" : 1120,
        "tag" : "Number"
    },
    "C4" : {
        "name" : "Four of Clubs",
        "value" : 4,
        "x_alignment" : 3200,
        "y_alignment" : 1120,
        "tag" : "Number"
    },
    "C5" : {
        "name" : "Five of Clubs",
        "value" : 5,
        "x_alignment" : 3600,
        "y_alignment" : 1120,
        "tag" : "Number"
    },
    "C6" : {
        "name" : "Six of Clubs",
        "value" : 6,
        "x_alignment" : 4000,
        "y_alignment" : 1120,
        "tag" : "Number"
    },
    "C7" : {
        "name" : "Seven of Clubs",
        "value" : 7,
        "x_alignment" : 0,
        "y_alignment" : 1680,
        "tag" : "Number"
    },
    "C8" : {
        "name" : "Eight of Clubs",
        "value" : 8,
        "x_alignment" : 400,
        "y_alignment" : 1680,
        "tag" : "Number"
    },
    "C9" : {
        "name" : "Nine of Clubs",
        "value" : 9,
        "x_alignment" : 800,
        "y_alignment" : 1680,
        "tag" : "Number"
    },
    "C10" : {
        "name" : "Ten of Clubs",
        "value" : 10,
        "x_alignment" : 1200,
        "y_alignment" : 1680,
        "tag" : "Number"
    },
    "CJ" : {
        "name" : "Jack of Clubs",
        "value" : 10,
        "x_alignment" : 1600,
        "y_alignment" : 1680,
        "tag" : "Face"
    },
    "CQ" : {
        "name" : "Queen of Clubs",
        "value" : 10,
        "x_alignment" : 2000,
        "y_alignment" : 1680,
        "tag" : "Face"
    },
    "CK" : {
        "name" : "King of Clubs",
        "value" : 10,
        "x_alignment" : 2400,
        "y_alignment" : 1680,
        "tag" : "Face"
    },
    "S2" : {
        "name" : "Two of Spades",
        "value" : 2,
        "x_alignment" : 800,
        "y_alignment" : 0,
        "tag" : "Number"
    },
    "S3" : {
        "name" : "Three of Spades",
        "value" : 3,
        "x_alignment" : 1200,
        "y_alignment" : 0,
        "tag" : "Number"
    },
    "S4" : {
        "name" : "Four of Spades",
        "value" : 4,
        "x_alignment" : 1600,
        "y_alignment" : 0,
        "tag" : "Number"
    },
    "S5" : {
        "name" : "Five of Spades",
        "value" : 5,
        "x_alignment" : 2000,
        "y_alignment" : 0,
        "tag" : "Number"
    },
    "S6" : {
        "name" : "Six of Spades",
        "value" : 6,
        "x_alignment" : 2400,
        "y_alignment" : 10,
        "tag" : "Number"
    },
    "S7" : {
        "name" : "Seven of Spades",
        "value" : 7,
        "x_alignment" : 2800,
        "y_alignment" : 0,
        "tag" : "Number"
    },
    "S8" : {
        "name" : "Eight of Spades",
        "value" : 8,
        "x_alignment" : 3200,
        "y_alignment" : 0,
        "tag" : "Number"
    },
    "S9" : {
        "name" : "Nine of Spades",
        "value" : 9,
        "x_alignment" : 3600,
        "y_alignment" : 10,
        "tag" : "Number"
    },
    "S10" : {
        "name" : "Ten of Spades",
        "value" : 10,
        "x_alignment" : 4000,
        "y_alignment" : 0,
        "tag" : "Number"
    },
    "SJ" : {
        "name" : "Jack of Spades",
        "value" : 10,
        "x_alignment" : 0,
        "y_alignment" : 560,
        "tag" : "Face"
    },
    "SQ" : {
        "name" : "Queen of Spades",
        "value" : 10,
        "x_alignment" : 400,
        "y_alignment" : 560,
        "tag" : "Face"
    },
    "SK" : {
        "name" : "King of Spades",
        "value" : 10,
        "x_alignment" : 800,
        "y_alignment" : 560,
        "tag" : "Face"
    },
}

# Debug random card show
#index = randint(0,52)
#card = allCards[index]
#cards = Image.open("Blackjack/blackjack/assets/cards.jpg")
#image1 = cards.crop((deck[card]["x_alignment"], deck[card]["y_alignment"], deck[card]["x_alignment"] + 400, deck[card]["y_alignment"] + 560))
#image1.show()

#def reset():


def start(dealer, player):
    hitLabel.bind("<Button-1>", lambda event: playerHit(player, dealer, allCards, cardsOnScreen))
    standButton.config(state="normal")
    dealer.clear()
    player.clear()
    print(cardsOnScreen)
    for c in cardsOnScreen:
        print(f"Card {c} position: x={c.x}, y={c.y}")
    CardVisuals.clearScreen(root, cardsOnScreen)
    def afterClear():
        print(f"cleared screen cards {cardsOnScreen}")
        cardsOnScreen.clear()
        new_dealer, new_player = makeHand(allCards, [], [])  # generate new hands
        dealer.extend(new_dealer)
        player.extend(new_player)
        print(f"Newly created : dealer [{dealer}]")
        print(f"Newly created : player [{player}]")
        CardVisuals.resetAlignment()

        print(dealer)
        print(player)
        for card in player:
            cardsOnScreen.append(CardVisuals(root, deck, card, mode="player"))

        #Place dealer cards, first is true, second is blank
        cardsOnScreen.append(CardVisuals(root, deck, dealer[0], mode="dealer"))
        cardsOnScreen.append(CardVisuals(root, deck, "Blank", mode="dealer"))

        root.after(1500, lambda: CardVisuals.animateHand(root, cardsOnScreen))
        root.after(2000, lambda : updateText(playerCounter, dealerCounter, playerText, dealerText, player, dealer, "hidden"))
    CardVisuals.clearScreen(root, cardsOnScreen, Finished=afterClear)
    

#flickerCircle(root, playerCanvas, playerItem, "#B0B0B0",5)
def checkWin(root, dealerCanvas, dealerItem, playerCanvas, playerItem, deck, player, dealer):
    dealerScore = (countHand(deck, dealer, "dealer"))[1]
    playerScore = countHand(deck, player, "player")

    if playerScore > 21 and dealerScore <= 21: #If player goes bust
        flickerCircle(root, dealerCanvas, dealerItem, "#FFD700",3)
        flickerCircle(root, playerCanvas, playerItem, "red",3)

    elif dealerScore > 21 and playerScore <= 21: # if dealer goes bust
        flickerCircle(root, dealerCanvas, dealerItem, "red",3)
        flickerCircle(root, playerCanvas, playerItem, "#FFD700",3)

    elif dealerScore > playerScore: #Simply if dealer is more
        flickerCircle(root, dealerCanvas, dealerItem, "#FFD700",3)
        flickerCircle(root, playerCanvas, playerItem, "red",3)
    
    elif playerScore > dealerScore:
        flickerCircle(root, dealerCanvas, dealerItem, "red",3)
        flickerCircle(root, playerCanvas, playerItem, "#FFD700",3)

    elif dealerScore == playerScore:
        flickerCircle(root, dealerCanvas, dealerItem, "#B0B0B0",3)
        flickerCircle(root, playerCanvas, playerItem, "#B0B0B0",3)
    
    root.after(3500, lambda: start(dealer, player))



def playerHit(playerHand,dealerHand,allCards, cardsVisible):
    playerHand.append((sample([card for card in allCards if card not in playerHand and card not in dealerHand], 1))[0])
    cardsVisible.append(CardVisuals(root,deck,player[-1], mode="player"))
    root.after(50, lambda: CardVisuals.animateCard(root, cardsOnScreen[-1],"up", 1, None, "in"))
    root.after(650, lambda : updateText(playerCounter, dealerCounter, playerText, dealerText, player, dealer, "hidden"))
    print(f"Hit occured from {dealer}")
    print(f"Player {playerHand}")
    print(f"Dealer {dealer}")
    total = countHand(deck, player, "player")
    if total > 21:
        root.after(1750, lambda : stand(False))



def dealerHit(playerHand,dealerHand,allCards, cardsVisible):
    dealerHand.append((sample([card for card in allCards if card not in playerHand and card not in dealerHand], 1))[0])
    cardsVisible.append(CardVisuals(root,deck,dealer[-1], mode="dealer"))
    root.after(500, lambda: CardVisuals.animateCard(root, cardsOnScreen[-1],"down", 1, None, "in"))
    root.after(1150, lambda : updateText(playerCounter, dealerCounter, playerText, dealerText, player, dealer, "visible"))
    print(f"Hit occured from {dealer}")
    print(f"Player {playerHand}")
    print(f"Dealer {dealer}")
    total = (countHand(deck, dealer, "dealer"))[1]
    if total < 17:
        root.after(1750, lambda : dealerHit(player, dealer, allCards, cardsOnScreen))
    else:
        print(f"winning as {total} > 17")
        root.after(1500, lambda : checkWin(root, dealerCounter, dealerCircle, playerCounter, playerCircle, deck, player, dealer))

    





def stand(mode):
    hitLabel.bind("<Button-1>", hit_callback_id)
    standButton.config(state="disabled")
    dealerCard = dealer[1]
    cards = Image.open("assets/cards.jpg")
    img = ImageTk.PhotoImage(cards.crop((deck[dealerCard]["x_alignment"], deck[dealerCard]["y_alignment"], deck[dealerCard]["x_alignment"] + 400, deck[dealerCard]["y_alignment"] + 560)).resize((180, 238)))
    #CardVisuals.blankLabel.config(image=img)
    #CardVisuals.blankLabel.image = img
    cardsOnScreen.append(CardVisuals.blankLabel)
    print("Dealer reveal")
    original_width = 180 #Width of card
    fixed_center_x = 220 + original_width // 2  # center of card position at all

    for angle in range(1, 180, 1):
        cosVal = abs(math.cos(math.radians(angle)))
        width = max(1, int(original_width * cosVal))

        if angle > 90: #Get actual image for dealer
            initialImage = cards.crop((
                deck[dealerCard]["x_alignment"],
                deck[dealerCard]["y_alignment"],
                deck[dealerCard]["x_alignment"] + 400,
                deck[dealerCard]["y_alignment"] + 560
            )).resize((original_width, 238))
        else: #Get blank
            initialImage = cards.crop((
                deck["Blank"]["x_alignment"],
                deck["Blank"]["y_alignment"],
                deck["Blank"]["x_alignment"] + 400,
                deck["Blank"]["y_alignment"] + 560
            )).resize((original_width, 238))

        img_resized = initialImage.resize((width, 238))
        img = ImageTk.PhotoImage(img_resized)

        # Calculate new x so card is centered on fixed_center_x
        new_x = fixed_center_x - width // 2

        CardVisuals.blankLabel.label.config(image=img)
        CardVisuals.blankLabel.image = img
        CardVisuals.blankLabel.label.place(x=new_x, y=20)

        CardVisuals.blankLabel.label.update()
        #CardVisuals.blankLabel.after() supposedly doesnt create delay but it does for some reason (supposed to pass in a function to execute lol)
    updateText(playerCounter, dealerCounter, playerText, dealerText, player, dealer, mode = "visible")
    print("Updated dealer score")
    total = (countHand(deck, dealer, "dealer"))[1]
    if mode:
        if total < 17:
            dealerHit(player, dealer, allCards, cardsOnScreen)
        else:
            checkWin(root, dealerCounter, dealerCircle, playerCounter, playerCircle, deck ,player, dealer)
    elif mode == False:
        checkWin(root, dealerCounter, dealerCircle, playerCounter, playerCircle, deck ,player, dealer)
        
    




def flickerCircle(root,canvas, item, colour, frequency, mode=True):
        print("Flicker triggered")
        if frequency == 0:
           return
        if mode:
            canvas.itemconfig(item, fill = colour)
        else:
            canvas.itemconfig(item, fill = "white")
            frequency -= 1
        canvas.after(500, lambda : flickerCircle(root, canvas, item, colour, frequency, not mode))
        








standButton = tk.Button(root, command= lambda: stand(True))
standButton.place(x = 600, y =500)

hitCanvas = tk.Canvas(root,width = 280, height = 200, bg = "#84299b")
# Create the image
hitImage = ImageTk.PhotoImage((Image.open("assets/HitCard.png").rotate(90, expand=True)))

# Assign the same image to both label and .image reference
hitLabel = tk.Label(image=hitImage)
hitLabel.image = hitImage  # Prevent garbage collection
hitLabel.place(x=20, y=345)


hit_callback_id = hitLabel.bind("<Button-1>", lambda event: playerHit(player, dealer, allCards, cardsOnScreen))

#hitButton = tk.Button(root, command= lambda: playerHit(player, dealer, allCards, cardsOnScreen))
#hitButton.place(x = 600, y =500)

clearButton = tk.Button(root, command= lambda event: CardVisuals.clearScreen(root, cardsOnScreen))
clearButton.place(x = 700, y =500)

enterButton = tk.Button(root, command= lambda: CardVisuals.animateHand(root, cardsOnScreen))
enterButton.place(x = 800, y =500)

# Generate hands
print(root.winfo_screenwidth(), root.winfo_screenheight())
dealer, player = makeHand(allCards, player, dealer)

root.after(1050, lambda : updateText(playerCounter, dealerCounter, playerText, dealerText, player, dealer, "hidden"))

#Print the value of your hand

print(f"The dealer's hand is {countHand(deck, dealer, "dealer")}")
print(f"The player's hand is {countHand(deck, player, "player")}")



#Place all the cards in the player's hand
for card in player:
    cardsOnScreen.append(CardVisuals(root, deck, card, mode="player"))

#Place dealer cards, first is true, second is blank
cardsOnScreen.append(CardVisuals(root, deck, dealer[0], mode="dealer"))
cardsOnScreen.append(CardVisuals(root, deck, "Blank", mode="dealer"))

root.after(350, lambda: CardVisuals.animateHand(root, cardsOnScreen))

#Opens root
root.mainloop()




