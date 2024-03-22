from typing import List
from entity import Appointment
class HospitalService(IHospitalService):
    def getAppointmentById(self, appointmentId: int) -> Appointment:
        pass
    def getAppointmentsForPatient(self, patientId: int) -> List[Appointment]:
        pass
    def getAppointmentsForDoctor(self, doctorId: int) -> List[Appointment]:
        pass
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        pass
    def updateAppointment(self, appointment: Appointment) -> bool:
      pass
    def cancelAppointment(self, appointmentId: int) -> bool:
        pass
