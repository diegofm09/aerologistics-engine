from core.persistence import FleetRepository
from core.observers import DeliverySubject, CustomerSMSListener, LogisticsAuditListener
from core.models import DeliveryVehicle, StandardPackage, ExpressPackage, RefrigeratedPackage
from core.strategies import DroneEcoShipping, GroundShipping, AirShipping
from core.factories import PackageFactory
from core.analytics import packages_extractor
from core.exceptions import MaxFleetError
import json

repository = FleetRepository()
delivery_subject = DeliverySubject()
sms_listener = CustomerSMSListener()
audit_listener = LogisticsAuditListener()
delivery_subject.attach(sms_listener)
delivery_subject.attach(audit_listener)

print("-----------------------")
while True:
    option = input(" Aerologistics Engine:\n 1) Vehicle Fleet Management\n 2) Package Management\n 3) Configurations\n 4) Analysis and Reports Panel\n 5) Waybill Management and Exportation\n 6) Events and Audit System\n 7) Exit System\n")
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
                            with open(repository.config_p, "r") as file9:
                                max_vehicles = json.load(file9)
                            if len(repository.load_fleet()) >= max_vehicles["max_fleet_capacity"]:
                                raise MaxFleetError
                            
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
                        print("-- PACKAGE DELETER --")
                        package_id = input("Enter the package ID: ")
                        fleet = repository.load_fleet()
                        found = False
                        for v in fleet:
                            for p in v.packages:
                                if p.package_id == package_id:
                                    found = True
                                    v.delete_package(package_id)
                                    print("Package Deleted Correctly")
                                    repository.save_fleet(fleet)
                                    break
                        if not found:
                            print("Package not found")

                    case "2.3":
                        found = False
                        while True:
                            vehicle_id = input("Enter the vehicle ID to extract its packages: ")
                            filtered = input("Do you want to filter them?:\n 1) Only standard packages\n 2) Only express packages\n 3) Only refrigerated packages\n 4) NO FILTER\n")
                            match filtered:
                                case "1":
                                    filter = "Standard Package"
                                    break
                                case "2":
                                    filter = "Express Package"
                                    break
                                case "3":
                                    filter = "Refrigerated Package"
                                    break
                                case "4":
                                    filter = None
                                    break
                                case _:
                                    print("Error, please enter 1, 2, 3 or 4")
                        fleet = repository.load_fleet()
                        for v in fleet:
                            if v.vehicle_id == vehicle_id:
                                found = True
                                vehicle = [v]
                                for i in packages_extractor(vehicle, filter):
                                    print("-----------------")
                                    print(f"ID: {i.package_id}")
                                    print(f"Weight: {i.weight_kg}")
                                    print(f"Status: {'Shipped' if i.delivered == False else 'Delivered'} to {i.destination_zip}")
                                    print(f"Dimensions: {i.length}*{i.width}*{i.height}")
                                    if i.get_package_type() == "Express Package":
                                        print(f"Urgency Level: {i.urgency_level}")
                                    if i.get_package_type() == "Refrigerated Package":
                                        print(f"Target Temp Celsius: {i.target_temp_celsius}")
                        if not found:
                            print("Vehicle not found")

                    case "2.4":
                        break                 
                    case _:
                        print("Error that option is not avaiable")

        case "3":
            while True:
                print("-----------------------")
                suboption = input(" Configurations:\n 3.1) Check Current Configuration\n 3.2) Change Configuration\n 3.3) Close Data Persistence\n")
                print("-----------------------")
                match suboption:
                    case "3.1":
                        with open(repository.config_p, "r") as file6:
                            config = json.load(file6)
                        print("-- CURRENT CONFIGURATION --")
                        print(f'Max Fleet Capacity: {config["max_fleet_capacity"]}')
                        print(f'Fuel Price Base: {config["fuel_price_base"]}')
                        print(f'Currency: {config["currency"]}')
                        print(f'System Version: {config["system_version"]}')
                    case "3.2":
                        while True:
                            selection = input("Which Config would you like to change?:\n 1) Max Fleet Capacity\n 2) Fuel Price Base\n 3) Currency ($/€)\n")
                            match selection:
                                case "1":
                                    while True:
                                        try:
                                            new = float(input("Enter the new max fleet capacity: "))
                                            with open(repository.config_p, "r") as file6:
                                                config = json.load(file6)
                                            config["max_fleet_capacity"] = new
                                            with open(repository.config_p, "w") as file6:
                                                json.dump(file6, config, indent=2)
                                            print("Config saved correctly")
                                            break
                                        except ValueError:
                                            print("Error, please enter a number")
                                    break
                                case "2":
                                    while True:
                                        try:
                                            new = float(input("Enter the new fuel price base: "))
                                            with open(repository.config_p, "r") as file7:
                                                config = json.load(file7)
                                            config["fuel_price_base"] = new
                                            with open(repository.config_p, "w") as file7:
                                                json.dump(file7, config, indent=2)
                                            print("Config saved correctly")
                                            break
                                        except ValueError:
                                            print("Error, please enter a number")
                                    break
                                case "3":
                                    with open(repository.config_p, "r") as file8:
                                        config = json.load(file8)
                                    if config["currency"] == "USD":
                                        config["currency"] = "EUR"
                                    else:
                                        config["currency"] = "USD"
                                    with open(repository.config_p, "w") as file8:
                                        json.dump(file8, config, indent=2)
                                    print("Config saved correctly")
                                    break
                                case _:
                                    print("Option not avaiable")

                    case "3.3":
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