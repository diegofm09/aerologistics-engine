from core.persistence import FleetRepository
from core.observers import DeliverySubject, CustomerSMSListener, LogisticsAuditListener

repository = FleetRepository()
delivery_subject = DeliverySubject()
sms_listener = CustomerSMSListener()
audit_listener = LogisticsAuditListener()
delivery_subject.attach(sms_listener)
delivery_subject.attach(audit_listener)


while True:
    print("--------------------")
    option = input("Aerologistics Engine: ")
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