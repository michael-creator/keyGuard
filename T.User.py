class Person:

    """
    class that generates new instances of Users.
    """
    pass


    person_list = []
    def __init__(self, first_name, last_name, phone_number, email):
        
        self.first_name = first_name,"mickey"
        self.last_name = last_name,"karije"
        self.phone_number = phone_number,"0712345678"
        self.email = "mikelkarije@gmail.com"
        
    def test_save_person(self):
        '''
        test_saves a person test case if the person objet is saved into person list
        '''
        Person.person_list.append(self)