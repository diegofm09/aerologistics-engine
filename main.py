from core.persistence import FleetRepository
from core.observers import DeliverySubject, CustomerSMSListener, LogisticsAuditListener
from core.models import DeliveryVehicle, StandardPackage, ExpressPackage, RefrigeratedPackage
from core.strategies import DroneEcoShipping, GroundShipping, AirShipping
from core.factories import PackageFactory

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
                        fleet = repository.load_fleet()
                        for vehicle in fleet:
                            print(f"ID: {vehicle.vehicle_id} SHIPPING STRATEGY: {vehicle.shipping_strategy.__class__.__name__} USED WEIGHT: {vehicle.used_weight}/{vehicle.max_weight_capacity}kg")

                    case "1.2":
                        try:
                            print("--- Add New Vehicle ---")
                            id = input("What will be the id of the new vehicle?: ")
                            while True:
                                strategy = input("What will be its strategy:\n 1) Ground Shipping\n 2) Air Shipping\n 3) Eco Drone Shipping\n")
                                match strategy:
                                    case "1":
                                        strategy = GroundShipping()
                                        break
                                    case "2":
                                        strategy = AirShipping()
                                        break
                                    case "3":
                                        strategy = DroneEcoShipping()
                                        break
                                    case _:
                                        print("Error, please enter 1, 2 or 3")
                            max_weight = float(input("Enter the max weight of the vehicle: "))

                            new = DeliveryVehicle(vehicle_id=id, max_weight_capacity=max_weight, shipping_strategy=strategy)

                            fleet = repository.load_fleet()
                            fleet.append(new)
                            repository.save_fleet(fleet)

                            print(f"Vehicle '{id}' added successfully and saved to JSON!")

                        except ValueError:
                            print("[Error]: Please enter a valid number for the weight capacity.")

                        except Exception as e:
                            print(f"[ERROR]: Could not create vehicle -> {e}")

                    case "1.3":
                        veh_id = input("Introduce the vehicle id: ")
                        fleet = repository.load_fleet()
                        found = False
                        for v in fleet:
                            if v.vehicle_id == veh_id:
                                found = True
                                while True:
                                    strategy = input("What will be its strategy:\n 1) Ground Shipping\n 2) Air Shipping\n 3) Eco Drone Shipping\n")
                                    match strategy:
                                        case "1":
                                            v.shipping_strategy = GroundShipping()
                                            break
                                        case "2":
                                            v.shipping_strategy = AirShipping()
                                            break
                                        case "3":
                                            if v.used_weight <= 3:
                                                v.shipping_strategy = DroneEcoShipping()
                                                break
                                            else:
                                                print("ERROR, the vehicle has more weight than a drone could carry")
                                            
                                        case _:
                                            print("Error, please enter 1, 2 or 3")
                                break
                        if not found:
                            print("Vehicle not found")
                        else:
                            repository.save_fleet(fleet)
                            print("Fleet successfully updated and saved!")
                                    
                        
                    case "1.4":
                        try:
                            print("-- VEHICLE COST CALCULATOR --")
                            fleet = repository.load_fleet()
                            found = False
                            veh_id = input("Enter the vehicle id: ")
                            for v in fleet:
                                if v.vehicle_id == veh_id:
                                    found = True
                                    kms = float(input("Enter the ammount of kms: "))
                                    print(f"Total cost: {v.get_shipping_cost(kms)}$")
                            if not found:
                                print("Vehicle not found")
                        except ValueError:
                            print("Error, the kms must be a number")
                        except Exception as e:
                            print(f"Error: {e}")

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
                        try:
                            print("-- ADD NEW PACKAGE --")
                            id = input("Enter its ID: ")
                            weight = float(input("Enter its weight: "))
                            destination = input("Enter its Destination Zipcode: ")
                            height = float(input("Enter its height: "))
                            length = float(input("Enter its length: "))
                            width = float(input("Enter its width: "))

                            while True:
                                package_type = input("What will be its type (standard, express, refrigerated): ").strip().lower()
                                if package_type in ["standard", "express", "refrigerated"]:
                                    break
                                print("Error, please enter standard, express or refrigerated")

                            package_data = {
                                "package_id": id,
                                "weight_kg": weight,
                                "destination_zip": destination,
                                "length": length,
                                "width": width,
                                "height": height
                            }

                            if package_type == "express":
                                package_data["urgency_level"] = int(float(input("Enter urgency level (1 to 5): ")))
       
                            elif package_type == "refrigerated":
                                package_data["target_temp_celsius"] = float(input("Enter target temperature in Celsius (-50 to 5): "))

                            new_package = PackageFactory.create_package(package_type, **package_data)
                            
                            vehicle_id = input("Enter the vehicle ID to add the package: ")
                            fleet = repository.load_fleet()
                            found = False
                            for v in fleet:
                                if v.vehicle_id == vehicle_id:
                                    found = True
                                    v.add_package(new_package)
                                    repository.save_fleet(fleet)
                            if not found:
                                print("Vehicle not found")         
                        
                        except ValueError:
                            print("Error, the size, weight, temperature target and urgency level parameters must be numbers")
                        except Exception as e:
                            print(f"Error: {e}")

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