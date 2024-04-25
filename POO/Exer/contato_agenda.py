class ContactBook:
    def __init__(self) -> None:
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    def remove_contact(self, contact):
        self.contacts.remove(contact)
        
    def display_contact(self, contact):
        self.contacts.remove(contact)
    
    def display_contact(self):
        if not self.contacts:
            print ("Lista de contatos está Vazia")
        else:
            for contact in self.contacts:
                print(contact)
                print("---------------------")
                
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contanto nao foi encontrado")