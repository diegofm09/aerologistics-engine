from core.persistence import FleetRepository
from core.observers import DeliverySubject, CustomerSMSListener, LogisticsAuditListener

repository = FleetRepository()
delivery_subject = DeliverySubject()
sms_listener = CustomerSMSListener()
audit_listener = LogisticsAuditListener()
delivery_subject.attach(sms_listener)
delivery_subject.attach(audit_listener)

print("-----------------------")
while True:
    option = input(" Aerologistics Engine:\n 1) Vehicle Fleet Management\n 2) Package Management\n 3) Data Persistence\n 4) Analysis and Reports Panel\n 5) Waybill Management and Exportation\n 6) Events and Audit System\n 7) Exit System\n")
    match option:

        
        case "1":
            while True:
                print("-----------------------")
                suboption = input(" Vehicle Fleet Management:\n 1) X\n 2) X\n 3) X\n 4) X\n 5) X\n")
                print("-----------------------")


        case "2":
            while True:
                print("-----------------------")
                suboption = input(" Package Management:\n 1) X\n 2) X\n 3) X\n 4) X\n 5) X\n")
                print("-----------------------")


        case "3":
            while True:
                print("-----------------------")
                suboption = input(" Data Persistence:\n 1) X\n 2) X\n 3) X\n 4) X\n 5) X\n")
                print("-----------------------")


        case "4":
            while True:
                print("-----------------------")
                suboption = input(" Analysis and Reports Panel:\n 1) X\n 2) X\n 3) X\n 4) X\n 5) X\n")
                print("-----------------------")


        case "5":
            while True:
                print("-----------------------")
                suboption = input(" Waybill Management and Exportation:\n 1) X\n 2) X\n 3) X\n 4) X\n 5) X\n")
                print("-----------------------")


        case "6":
            while True:
                print("-----------------------")
                suboption = input(" Events and Audit System:\n 1) X\n 2) X\n 3) X\n 4) X\n 5) X\n")
                print("-----------------------")


        case "7":
            print("-----------------------\n Exiting the system, Goodbye!")
            exit()


        case _:
            print("Error that option is not avaiable")