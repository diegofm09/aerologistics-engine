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
    option = input(" Aerologistics Engine:\n 1) Vehicle Fleet Management\n 2) Package Management\n 3) Data Persistence Menu\n 4) Analysis and Reports Panel\n 5) Waybill Management and Exportation\n 6) Events and Audit System\n 7) Exit System\n")
    match option:


        case "1":
            while True:
                print("-----------------------")
                suboption = input(" Vehicle Fleet Management:\n 1.1) X\n 1.2) X\n 1.3) X\n 1.4) X\n 1.5) Close Vehicle Fleet Management\n")
                print("-----------------------")
                match suboption:
                    case "1.1":
                        pass
                    case "1.2":
                        pass
                    case "1.3":
                        pass
                    case "1.4":
                        pass
                    case "1.5":
                        pass                    
                    case _:
                        pass




        case "2":
            while True:
                print("-----------------------")
                suboption = input(" Package Management:\n 2.1) X\n 2.2) X\n 2.3) X\n 2.4) Close Package Management\n")
                print("-----------------------")


        case "3":
            while True:
                print("-----------------------")
                suboption = input(" Data Persistence Menu:\n 3.1) X\n 3.2) X\n 3.3) X\n 3.4) Close Data Persistence\n")
                print("-----------------------")


        case "4":
            while True:
                print("-----------------------")
                suboption = input(" Analysis and Reports Panel:\n 4.1) X\n 4.2) X\n 4.3) X\n 4.4) X\n 4.5) X\n 4.6) Close Analysis and Reports Panel\n")
                print("-----------------------")


        case "5":
            while True:
                print("-----------------------")
                suboption = input(" Waybill Management and Exportation:\n 5.1) X\n 5.2) X\n 5.3) Close Waybill Management and Exportation\n")
                print("-----------------------")


        case "6":
            while True:
                print("-----------------------")
                suboption = input(" Events and Audit System:\n 6.1) X\n 6.2) X\n 6.3) Close Events and Audit System\n")
                print("-----------------------")


        case "7":
            print("-----------------------\n Exiting the system, Goodbye!")
            exit()


        case _:
            print("Error that option is not avaiable")