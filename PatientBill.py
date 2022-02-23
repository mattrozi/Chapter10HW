import PatientClass as Patient
import ProcedureClass as Procedure


def main(): 


    my_patient=Patient(1,"Matt Jones","123 Main st, Waco TX 76706",254-555-7415,'TRUE')


    my_Procedure1=Procedure('Physical Exam',2/15/2022,'Dr. Irvine','250',1)
    my_Procedure2=Procedure('MRI',2/15/2022,'Dr. Hamilton','1500',1)
    my_Procedure3=Procedure('CT Scan',2/17/2022,'Dr. Drey','1200',2)


    print('*** Patient Bill *** ')
    print('Name: ') 
    my_patient.get_name()
    print('Address: ')
    my_patient.get_address()
    
    







