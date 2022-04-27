from faker import Faker
fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, first_name, last_name, email_address, tel_priv):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.tel_priv = tel_priv

class BusinessContact:
    def __init__(self, first_name, last_name, email_business, tel_business):
        self.first_name = first_name
        self.last_name = last_name
        self.email_business = email_business
        self.tel_business = tel_business
        
    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name),+1])
  
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}, {self.occupation}, {self.company}"

    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, address_email={self.email_address})"

    def contact(self):
        return f"Wybieram numer domowy: {self.tel_priv} i dzwonię do {self.first_name} {self.last_name}"

    def workcontact(self):
        return f"Wybieram numer służbowy: {self.tel_work} i dzwonię do {self.first_name} {self.last_name}"
    
def create_contacts(quantity):
    names = []
    fake = Faker()
    for i in range(quantity):
        names.append(
            BusinessContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                company=fake.company(), post=fake.job()))

if __name__ == "__main__":
    contacts = create_contacts()
    for contact in contacts:
        print(contact)
