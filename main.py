from dao.HospitalService import implementation
from entity.Appointment import Appointment
from exception.Exception import PatientNumberNotFoundException

def print_menu():
    print("\nHospital Management System Menu:")
    print("1. Schedule Appointment")
    print("2. Get Appointment by ID")
    print("3. Get Appointments for Patient")
    print("4. Get Appointments for Doctor")
    print("5. Update Appointment")
    print("6. Cancel Appointment")
    print("7. Exit")

def schedule_appointment(HospitalService):
    print("\nSchedule Appointment:")
    appointment_id = int(input("Enter appointment ID: "))
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    description = input("Enter appointment description: ")

    new_appointment = Appointment(appointmentId=appointment_id,patientId=patient_id,doctorId=doctor_id,appointmentDate=appointment_date,description=description)
    new_appointment.set_appointment_id(appointment_id)
    new_appointment.set_patient_id(patient_id)
    new_appointment.set_doctor_id(doctor_id)
    new_appointment.set_appointment_date(appointment_date)
    new_appointment.set_description(description)

    is_scheduled = HospitalService.schedule_appointment(new_appointment)
    if is_scheduled:
        print("Appointment scheduled successfully.")
    else:
        print("Failed to schedule appointment.")

def get_appointment_by_id(HospitalService):
    print("\nGet Appointment by ID:")
    appointment_id = int(input("Enter appointment ID: "))
    appointment = HospitalService.get_appointment_by_id(appointment_id)
    if appointment:
        print(f"Appointment details: \nAppointment ID : {appointment.get_appointment_id()}\nAppointment Date: {appointment.get_appointment_date()}\nAppointment Description: {appointment.get_description()}")
    else:
        print("Appointment not found.")

def get_appointments_for_patient(HospitalService):
    print("\nGet Appointments for Patient:")
    patient_id = int(input("Enter patient ID: "))
    try:
        appointments_for_patient = HospitalService.get_appointments_for_patient(patient_id)
        if appointments_for_patient:
            print("Appointments for patient:")
            for appointment in appointments_for_patient:
                print(f"Appointment details: \nAppointment ID : {appointment.get_appointment_id()}\nAppointment Date: {appointment.get_appointment_date()}\nAppointment Description: {appointment.get_description()}")

        else:
            print("No appointments found for patient.")
    except PatientNumberNotFoundException as e:
        print("Patient not found.")

def get_appointments_for_doctor(HospitalService):
    print("\nGet Appointments for Doctor:")
    doctor_id = int(input("Enter doctor ID: "))
    appointments_for_doctor = HospitalService.get_appointments_for_doctor(doctor_id)
    if appointments_for_doctor:
        print("Appointments for doctor:")
        for appointment in appointments_for_doctor:
            print(f"Appointment details: \nAppointment ID : {appointment.get_appointment_id()}\nAppointment Date: {appointment.get_appointment_date()}\nAppointment Description: {appointment.get_description()}")
    else:
        print("No appointments found for doctor.")

def update_appointment(HospitalService):
    print("\nUpdate Appointment:")
    appointment_id = int(input("Enter appointment ID to update: "))
    appointment_date = input("Enter updated appointment date (YYYY-MM-DD): ")
    description = input("Enter updated appointment description: ")
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    updated_appointment = Appointment(appointmentId=appointment_id, patientId=patient_id,doctorId=doctor_id,appointmentDate=appointment_date,description=description)
    if HospitalService.update_appointment(updated_appointment):
        print("Appointment updated successfully.")
    else:
        print("Failed to update appointment.")

def cancel_appointment(HospitalService):
    print("\nCancel Appointment:")
    appointment_id = int(input("Enter appointment ID to cancel: "))
    if HospitalService.cancel_appointment(appointment_id):
        print("Appointment canceled successfully.")
    else:
        print("Failed to cancel appointment.")

def main():
    HospitalService = HospitalServiceImpl()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            schedule_appointment(HospitalService)
        elif choice == '2':
            get_appointment_by_id(HospitalService)
        elif choice == '3':
            get_appointments_for_patient(HospitalService)
        elif choice == '4':
            get_appointments_for_doctor(HospitalService)
        elif choice == '5':
            update_appointment(HospitalService)
        elif choice == '6':
            cancel_appointment(HospitalService)
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
