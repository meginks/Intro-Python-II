# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, room):
        self.room: room   
        self.items = []

    def __str__(self):
        return f"You are in {self.room.name}. {self.room.description}."
    
    def __repr__(self):
        return f"Player({repr(self.room)})" 

