from dao.hospitalservice import implemetation
from util.db_connection_util import DBConnection
from entity.appointment import Appointment
from typing import List
from mysql.connector import Error
from exception.myexceptions import PatientNumberNotFoundException


def get_connection():
    return DBConnection.get_connection('D:/Hexaware/Hospital_Management_System/util/db.properties')


def close_connection(cursor, connection):
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()


class HospitalServiceImpl(IHospitalService):

    def getAppointmentById(self, appointmentId: int) -> Appointment | None:
        connection = None
        cursor = None
        try:
            connection = get_connection()
            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM appointment WHERE appointmentId = %s"
                cursor.execute(query, (appointmentId,))
                appointment_data = cursor.fetchone()
                if appointment_data:
                    appointment = Appointment(*appointment_data)
                    return appointment
                else:
                    print(f"No appointment found with ID {appointmentId}")
                    return None
            else:
                print("Failed to establish database connection")
                return None
        except Error as e:
            print(f"Error retrieving appointment: {e}")
            return None
        finally:
            close_connection(cursor, connection)

    def getAppointmentsForPatient(self, patientId: int) -> List[str]:
        connection = None
        cursor = None
        appointments = []

        try:
            connection = get_connection()

            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM appointment WHERE patientId = %s"
                cursor.execute(query, (patientId,))
                appointment_data = cursor.fetchall()
                if not appointment_data:
                    # Raise PatientNumberNotFoundException if no appointments are found for the patient
                    raise PatientNumberNotFoundException(f"No appointments found for patient with ID {patientId}")

                for data in appointment_data:
                    appointment = Appointment(*data)
                    appointments.append(str(appointment).replace('\n', ', '))

            return appointments

        except Exception as e:
            print(f"Error retrieving appointments for patient: {e}")
            return []

        finally:
            close_connection(cursor, connection)

    def getAppointmentsForDoctor(self, doctorId: int) -> List[str]:
        connection = None
        cursor = None
        appointments = []

        try:
            connection = get_connection()
            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM appointment WHERE doctorId = %s"
                cursor.execute(query, (doctorId,))
                appointment_data = cursor.fetchall()
                for data in appointment_data:
                    appointment = Appointment(*data)
                    appointments.append(str(appointment).replace('\n', ', '))

            return appointments

        except Exception as e:
            print(f"Error retrieving appointments for doctor: {e}")
            return []

        finally:
            close_connection(cursor, connection)

    def scheduleAppointment(self, appointment: Appointment) -> bool:
        connection = None
        cursor = None

        try:
            connection = get_connection()
            if connection:
                cursor = connection.cursor()
                query = ("INSERT INTO appointment (appointmentId,patientId, doctorId, appointmentDate, description) "
                         "VALUES (%s,%s, %s, %s, %s)")
                data = (
                    appointment.get_appointment_id(), appointment.get_patient_id(), appointment.get_doctor_id(),
                    appointment.get_appointment_date(), appointment.get_description())
                cursor.execute(query, data)
                connection.commit()
                return True

        except Exception as e:
            print(f"Error scheduling appointment: {e}")
            return False

        finally:
            close_connection(cursor, connection)

    def updateAppointment(self, appointment: Appointment) -> bool:
        connection = None
        cursor = None

        try:
            connection = get_connection()

            if connection:
                cursor = connection.cursor()
                query = ("UPDATE appointment SET patientId = %s, doctorId = %s, appointmentDate = %s, description = %s "
                         "WHERE appointmentId = %s")
                data = (
                    appointment.get_patient_id(), appointment.get_doctor_id(), appointment.get_appointment_date(),
                    appointment.get_description(), appointment.get_appointment_id())
                cursor.execute(query, data)
                connection.commit()

                return True

        except Exception as e:
            print(f"Error updating appointment: {e}")
            return False

        finally:
            close_connection(cursor, connection)

    def cancelAppointment(self, appointmentId: int) -> bool:
        connection = None
        cursor = None

        try:
            connection = get_connection()

            if connection:
                cursor = connection.cursor()
                query = "DELETE FROM appointment WHERE appointmentId = %s"
                cursor.execute(query, (appointmentId,))
                connection.commit()

                return True

        except Exception as e:
            print(f"Error canceling appointment: {e}")
            return False

        finally:
            close_connection(cursor, connection)
