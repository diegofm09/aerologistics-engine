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
                suboption = input(" Vehicle Fleet Management:\n 1.1) Check Current Vehicle List\n 1.2) Add New Vehicle\n 1.3) Change Vehicle Strategy\n 1.4) Calculate Vehicle Shipping Cost\n 1.5) Close Vehicle Fleet Management\n")
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
                        break                    
                    case _:
                        print("Error that option is not avaiable")




        case "2":
            while True:
                print("-----------------------")
                suboption = input(" Package Management:\n 2.1) Add New Package\n 2.2) Delete Package\n 2.3) Extract Packages\n 2.4) Close Package Management\n")
                print("-----------------------")
                match suboption:
                    case "2.1":
                        pass
                    case "2.2":
                        pass
                    case "2.3":
                        pass
                    case "2.4":
                        break                 
                    case _:
                        print("Error that option is not avaiable")

        case "3":
            while True:
                print("-----------------------")
                suboption = input(" Data Persistence Menu:\n 3.1) Save Actual Fleet\n 3.2) Load Fleet\n 3.3) Check System Configuration\n 3.4) Close Data Persistence\n")
                print("-----------------------")
                match suboption:
                    case "3.1":
                        pass
                    case "3.2":
                        pass
                    case "3.3":
                        pass
                    case "3.4":
                        break                 
                    case _:
                        print("Error that option is not avaiable")

        case "4":
            while True:
                print("-----------------------")
                suboption = input(" Analysis and Reports Panel:\n 4.1) Fleet Weight Summary\n 4.2) Filter Packages by Weight\n 4.3) Check Express Packages Zipcodes\n 4.4) Check All Zipcodes\n 4.5) Generate Fast Consult Map\n 4.6) Close Analysis and Reports Panel\n")
                print("-----------------------")
                match suboption:
                    case "4.1":
                        pass
                    case "4.2":
                        pass
                    case "4.3":
                        pass
                    case "4.4":
                        pass
                    case "4.5":
                        pass   
                    case "4.6":
                        break                 
                    case _:
                        print("Error that option is not avaiable")

        case "5":
            while True:
                print("-----------------------")
                suboption = input(" Waybill Management and Exportation:\n 5.1) Create Waybill\n 5.2) Export Waybill\n 5.3) Close Waybill Management and Exportation\n")
                print("-----------------------")
                match suboption:
                    case "5.1":
                        pass
                    case "5.2":
                        pass
                    case "5.3":
                        break                    
                    case _:
                        print("Error that option is not avaiable")

        case "6":
            while True:
                print("-----------------------")
                suboption = input(" Events and Audit System:\n 6.1) Try Notifications System\n 6.2) Check Events Register\n 6.3) Close Events and Audit System\n")
                print("-----------------------")
                match suboption:
                    case "6.1":
                        pass
                    case "6.2":
                        pass
                    case "6.3":
                        break               
                    case _:
                        print("Error that option is not avaiable")

        case "7":
            print("-----------------------\n Exiting the system, Goodbye!")
            exit()


        case _:
            print("Error that option is not avaiable")