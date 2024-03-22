class Doctor:
    def __init__(self, doctor_id=None, first_name=None, last_name=None, specialization=None, contact_number=None):
        self.__doctor_id = doctor_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__specialization = specialization
        self.__contact_number = contact_number

    def get_doctor_id(self):
        return self.__doctor_id

    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def print_details(self):
        print(f"Doctor ID: {self.__doctor_id}")
        print(f"First Name: {self.__first_name}")
        print(f"Last Name: {self.__last_name}")
        print(f"Specialization: {self.__specialization}")
        print(f"Contact Number: {self.__contact_number}")
