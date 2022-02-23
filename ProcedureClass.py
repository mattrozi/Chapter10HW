'''
write a class named Procedure that represents a medical procedure that has been performed on a patient. 
The Procedure class should have the following attributes - Name of the procedure, Date of the procedure, 
Name of the practitioner who performed the procedure, Charges for the procedure and patient ID. 
The Procedure class’s __init__ method should accept an argument for each attribute. 
The Procedure class should have accessor methods only for each attribute.


'''
class Procedure:
    def __init__(self, procedure_name, dateProcedure, practioner,charges_for_procedure,patientID):
        self.__nameProcedure=procedure_name
        self.__procedureDate=dateProcedure
        self.__practioner=practioner
        self.__charges=charges_for_procedure
        self.__id=patientID


    def get_procedure_name(self):
        return self.__nameProcedure

    def get_date(self):
        return self.__procedureDate

    def get_charges(self):
        return self.__charges

    def get_id(self):
        return self.__id
