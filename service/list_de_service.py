from model.list_de import ListDE

class ListDEService:
    def __init__(self):
        self.list = ListDE()

    def get_all_linked(self):
        try:
            return self.list.enlist()
        except Exception as e:
            return {"message": str(e)}

    def add(self, ship_distribution):
        self.list.add(ship_distribution)
        return {"message": "Adicionado con éxito."}

    def add_first(self, ship_distribution):
        self.list.add_first(ship_distribution)
        return {"message": "Adicionado con éxito."}
