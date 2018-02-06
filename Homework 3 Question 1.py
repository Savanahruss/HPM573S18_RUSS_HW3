class Patient:
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be defined in the subclasses")

class Hospital:
    def __init__(self):
        """ cost is the cost that the admitted and later discharged patient will incur for the hospital"""
        self.cost = 0
        self.patient = []
    def admit(self, patient):
        self.patient.append(patient)

    def discharge_all(self):
        for patient in self.patient:
            patient.discharge()
            self.cost += patient.expectedcost


    def get_total_cost(self):
        return self.cost


class HospitalizedPatient:
    def __init__(self, name):
        Patient.__init__(self, name)
        self.expectedcost = 2000

    def discharge(self):
        print(self.name, "HospitalizedPatient")


class EmergencyPatient:
    def __init__(self, name):
        Patient.__init__(self, name)
        self.expectedcost = 1000

    def discharge(self):
        print(self.name, "EmergencyPatient")


P1 = HospitalizedPatient("P1")
P2 = HospitalizedPatient("P2")
P3 = EmergencyPatient("P3")
P4 = EmergencyPatient("P4")
P5 = EmergencyPatient("P5")

YNHH = Hospital()
YNHH.admit(P1)
YNHH.admit(P2)
YNHH.admit(P3)
YNHH.admit(P4)
YNHH.admit(P5)

#Then discharge all patients
YNHH.discharge_all()

print(YNHH.get_total_cost())




