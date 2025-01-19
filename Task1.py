class Customer:
    def __init__(self, first_name, last_name, address, id_number):

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.id_number = id_number

    def save_to_file(self, file_name):

        with open(file_name, 'a') as file:
            file.write(f"ID Number: {self.id_number}\n")
            file.write(f"First Name: {self.first_name}\n")
            file.write(f"Last Name: {self.last_name}\n")
            file.write(f"Address: {self.address}\n")

            
# Separate function to print the content of the file            
def print_customers(file_name):

    try:
    
        with open(file_name, 'r') as file:
            print('Details of the File :',file.read())
        
    
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    

if __name__ == "__main__":
    # Create a customer instance
    customer = Customer(
        first_name="Nalin",
        last_name="Udaya Kumara",
        address="4 Pilsdon, New Lynn, Auckland",
        id_number="CUST001"
    )

    # Save the customer to a file
    customer.save_to_file("customers.txt")
    print("Customer details saved to file.")

    # Print the contents of the file
    print_customers('customers.txt')
    
