from PIL import ImageTk,Image
import tkinter as tk
class CardVisuals:
    cards = None
    playerRow = 0
    dealerRow = 0
    WIDTH = 238
    HEIGHT = 180
    blankLabel = None
    @classmethod
    def initCards(cls, filePath):
        cls.cards = Image.open(filePath)

    def __init__(self, master, deck, card, mode):
        if CardVisuals.cards is None:
            raise RuntimeError("Cards not initiated")
        cards = CardVisuals.cards
        self.image = ImageTk.PhotoImage((cards.crop((deck[card]["x_alignment"], deck[card]["y_alignment"], deck[card]["x_alignment"] + 400, deck[card]["y_alignment"] + 560))).resize((self.HEIGHT,self.WIDTH)))
        self.label = tk.Label(master, image=self.image)
        print(f"Added {card}")
        if mode == "player":
            self.y = "player"
            self.x = CardVisuals.playerRow
            self.label.place(x = 20 + (CardVisuals.playerRow * 0.85*self.WIDTH), y = 1318, )
            CardVisuals.playerRow += 1
        else:
            self.y = "dealer"
            self.x = CardVisuals.dealerRow
            self.label.place(x = 20 + (CardVisuals.dealerRow * 0.85*self.WIDTH), y = -248, )
            CardVisuals.dealerRow += 1
            if card == "Blank":
                CardVisuals.blankLabel = self

    def remove(self):
        self.label.destroy()
    
    def resetAlignment():
        print("alignment reset")
        CardVisuals.playerRow = 0
        CardVisuals.dealerRow = 0

    def attributeSort(card):
        return card.y == "dealer"

    def clearScreen(root,cards,Finished=None):
        sortedCards = sorted(cards, key=CardVisuals.attributeSort)
        CardVisuals.sequentialAnimation(root, sortedCards, 0,Finished)

    def animateHand(root, cards):
        print("triggered card animation")
        for card in cards:
            if card.y == "dealer":
                CardVisuals.animateCard(root, card, "down", 0,None, "in")
            elif card.y == "player":
                CardVisuals.animateCard(root, card, "up", 0,None,  "in")
    def sequentialAnimation(root, cards, index,Finished=None):
        if index >= len(cards):
            if Finished:
                Finished()
                return
        
        card = cards[index]
        direction = "up" if card.y == "dealer" else "down"
        CardVisuals.animateCard(root, card, direction, 2, lambda: CardVisuals.sequentialAnimation(root, cards, index + 1, Finished=Finished), "out")



    def animateCard(root, card, direction, step, callback, mode):
        if not card.label.winfo_exists():
        # Widget destroyed; skip animation and call callback immediately
            callback()
            return
        if mode == "out":
            if step < 258:
                relativeX = 20 + (0.85 * 238 * card.x)
                relativeY = 20 - step if direction == "up" else 980 - 238 + step
                card.label.place(x = relativeX, y = relativeY)
                root.after(2, lambda: CardVisuals.animateCard(root, card, direction, step + 3, callback, "out"))
            else:
                card.label.destroy()
                callback()
        if mode == "in":
            if step < 263:
                relativeX = 20 + (0.85 * 238 * card.x)
                if direction == "down":
                    relativeY = -242 + step  # from above into view
                else:
                    relativeY = root.winfo_screenheight() - 80 - step
                card.label.place(x = relativeX, y = relativeY)
                root.after(2, lambda: CardVisuals.animateCard(root, card, direction, step + 2, callback, "in"))
            else:
                if callback:
                    callback()
                else:
                    return


        


