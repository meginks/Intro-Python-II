class Item: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
       
    def __str__(self):
        return f"You have the {self.name}. {self.description}"

    def __repr__(self):
        return f"Item({repr(self.name)}, {repr(self.description)})"
    
    def on_take(self):
        return f"You have picked up {self.name}"
    
    def on_drop(self):
        return f"You have dropped {self.name}"
