
class ServiceRecord:

    def __init__(self, reg, owner, vehicle, service):
        self.reg = reg
        self.owner = owner
        self.vehicle = vehicle
        self.service = service
        self.status = "Pending"

    def calculate_cost(self):
        prices = {
            "Oil Change": 1500,
            "Wheel Alignment": 800,
            "Full Service": 4500,
            "Brake Repair": 2200
        }

        return prices[self.service] * 1.18

    def display(self):
        print("Registration:", self.reg)
        print("Owner:", self.owner)
        print("Vehicle:", self.vehicle)
        print("Service:", self.service)
        print("Cost with GST: Rs.", self.calculate_cost())
        print("Status:", self.status)


services = {}


while True:

    print("\n--- VEHICLE SERVICE MANAGEMENT SYSTEM ---")
    print("1. Add Record")
    print("2. View Record")
    print("3. Update Status")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Record
    if choice == "1":

        reg = input("Enter Registration Number: ")
        owner = input("Enter Owner Name: ")
        vehicle = input("Enter Vehicle Type: ")
        service = input("Enter Service Type: ")

        if service not in ["Oil Change", "Wheel Alignment",
                           "Full Service", "Brake Repair"]:
            print("Invalid service type!")
            continue

        if reg in services:
            print("Record already exists!")
            continue

        record = ServiceRecord(reg, owner, vehicle, service)

        services[reg] = record

        print("Record Added Successfully!")

    # View Record
    elif choice == "2":

        if len(services) == 0:
            print("No records found!")

        for reg in services:
            services[reg].display()

    # Update Status
    elif choice == "3":

        reg = input("Enter Registration Number: ")

        if reg in services:

            status = input("Enter New Status: ")

            if status in ["Pending", "In Progress", "Completed"]:
                services[reg].status = status
                print("Status Updated Successfully!")
            else:
                print("Invalid Status!")

        else:
            print("No record found!")

    # Delete Record
    elif choice == "4":

        reg = input("Enter Registration Number: ")

        if reg in services:
            del services[reg]
            print("Record Deleted Successfully!")
        else:
            print("No record found!")

    # Exit
    elif choice == "5":

        break

    else:
        print("Invalid Choice!")