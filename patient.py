
class Patient:
    def __init__(self, patient_id, first_name, last_name, date_of_birth, gender, contact_number, address):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__contact_number = contact_number
        self.__address = address

    def get_patient_id(self):
        return self.__patient_id

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def print_details(self):
        print(f"Patient ID: {self.__patient_id}")
        print(f"First Name: {self.__first_name}")
        print(f"Last Name: {self.__last_name}")
        print(f"Date of Birth: {self.__date_of_birth}")
        print(f"Gender: {self.__gender}")
        print(f"Contact Number: {self.__contact_number}")
        print(f"Address: {self.__address}")



