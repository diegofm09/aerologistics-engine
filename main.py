from core.persistence import FleetRepository
from core.observers import DeliverySubject, CustomerSMSListener, LogisticsAuditListener

repository = FleetRepository()
delivery_subject = DeliverySubject()
sms_listener = CustomerSMSListener()
audit_listener = LogisticsAuditListener()
delivery_subject.attach(sms_listener)
delivery_subject.attach(audit_listener)


while True:
    print("-----------------------")
    option = input(" Aerologistics Engine:\n 1) X\n 2) X\n 3) X\n 4) X\n 5) X\n 6) X\n 7) X\n 8) X\n 9) X\n")
    print("-----------------------")
    match option:
        case "":
            pass
        case "":
            pass
        case "":
            pass
        case "":
            pass
        case "":
            pass
        case "":
            pass
        case "":
            pass
        case "":
            pass
        case "":
            pass
        case _:
            print("Error that option is not avaiable")