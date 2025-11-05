# Class definition for PersonalData
class PersonalData:
    """A class to hold personal information including name, address, age, and phone number."""
    
    # Constructor method to initialize the personal data attributes
    def __init__(self, name, address, age, phone_number):
        """Initialize a PersonalData object with name, address, age, and phone number."""
        self.__name = name  # Private attribute for name
        self.__address = address  # Private attribute for address
        self.__age = age  # Private attribute for age
        self.__phone_number = phone_number  # Private attribute for phone number
    
    # Accessor (getter) method for name
    def get_name(self):
        """Return the person's name."""
        return self.__name
    
    # Mutator (setter) method for name
    def set_name(self, name):
        """Set the person's name."""
        self.__name = name
    
    # Accessor (getter) method for address
    def get_address(self):
        """Return the person's address."""
        return self.__address
    
    # Mutator (setter) method for address
    def set_address(self, address):
        """Set the person's address."""
        self.__address = address
    
    # Accessor (getter) method for age
    def get_age(self):
        """Return the person's age."""
        return self.__age
    
    # Mutator (setter) method for age
    def set_age(self, age):
        """Set the person's age."""
        self.__age = age
    
    # Accessor (getter) method for phone number
    def get_phone_number(self):
        """Return the person's phone number."""
        return self.__phone_number
    
    # Mutator (setter) method for phone number
    def set_phone_number(self, phone_number):
        """Set the person's phone number."""
        self.__phone_number = phone_number
    
    # String representation method for easy display
    def __str__(self):
        """Return a formatted string representation of the personal data."""
        return (f"Name: {self.__name}\n"
                f"Address: {self.__address}\n"
                f"Age: {self.__age}\n"
                f"Phone Number: {self.__phone_number}")


# Main program starts here
def main():
    """Main function to test the PersonalData class with three instances."""
    
    # Print header for the program output
    print("=" * 60)
    print("Personal Data Management System")
    print("=" * 60)
    print()
    
    # Create the first PersonalData instance with my information
    person1 = PersonalData("Hong Khai Nguyen", "123 Main Street, San Francisco, CA 94102", 25, "555-1234")
    
    # Create the second PersonalData instance with friend's information
    person2 = PersonalData("Sarah Johnson", "456 Oak Avenue, Berkeley, CA 94704", 24, "555-5678")
    
    # Create the third PersonalData instance with family member's information
    person3 = PersonalData("Michael Nguyen", "789 Pine Road, Oakland, CA 94601", 28, "555-9012")
    
    # Display information for Person 1 (Hong Nguyen)
    print("Person 1 - My Information:")
    print("-" * 60)
    # Use the __str__ method to display all information
    print(person1)
    print()
    
    # Display information for Person 2 (Sarah Johnson)
    print("Person 2 - Friend's Information:")
    print("-" * 60)
    # Use the __str__ method to display all information
    print(person2)
    print()
    
    # Display information for Person 3 (Michael Nguyen)
    print("Person 3 - Family Member's Information:")
    print("-" * 60)
    # Use the __str__ method to display all information
    print(person3)
    print()
    
    # Demonstrate the use of accessor methods
    print("=" * 60)
    print("Demonstrating Accessor Methods:")
    print("=" * 60)
    # Use get_name() accessor method to retrieve person1's name
    print(f"Person 1's name (using accessor): {person1.get_name()}")
    # Use get_age() accessor method to retrieve person2's age
    print(f"Person 2's age (using accessor): {person2.get_age()}")
    # Use get_phone_number() accessor method to retrieve person3's phone number
    print(f"Person 3's phone number (using accessor): {person3.get_phone_number()}")
    print()
    
    # Demonstrate the use of mutator methods
    print("=" * 60)
    print("Demonstrating Mutator Methods:")
    print("=" * 60)
    # Use set_age() mutator method to update person1's age
    person1.set_age(26)
    print(f"Person 1's age updated to: {person1.get_age()}")
    
    # Use set_address() mutator method to update person2's address
    person2.set_address("999 Elm Street, San Jose, CA 95112")
    print(f"Person 2's address updated to: {person2.get_address()}")
    
    # Use set_phone_number() mutator method to update person3's phone number
    person3.set_phone_number("555-3456")
    print(f"Person 3's phone number updated to: {person3.get_phone_number()}")
    print()
    
    # Display updated information for all persons
    print("=" * 60)
    print("Updated Information for All Persons:")
    print("=" * 60)
    print()
    
    # Display updated information for Person 1
    print("Person 1 - Updated Information:")
    print("-" * 60)
    print(person1)
    print()
    
    # Display updated information for Person 2
    print("Person 2 - Updated Information:")
    print("-" * 60)
    print(person2)
    print()
    
    # Display updated information for Person 3
    print("Person 3 - Updated Information:")
    print("-" * 60)
    print(person3)
    print()
    
    # Print closing message
    print("=" * 60)
    print("End of Personal Data Management System")
    print("=" * 60)


# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to execute the program
    main()


# Question 2
# Class definition for Employee
class Employee:
    """A class to hold employee information including name, ID number, department, and job title."""

    # Constructor method to initialize the employee attributes
    def __init__(self, name, id_number, department, job_title):
        """Initialize an Employee object with name, ID number, department, and job title."""
        self.__name = name  # Private attribute for employee name
        self.__id_number = id_number  # Private attribute for employee ID number
        self.__department = department  # Private attribute for employee department
        self.__job_title = job_title  # Private attribute for employee job title

    # Accessor (getter) method for name
    def get_name(self):
        """Return the employee's name."""
        return self.__name

    # Mutator (setter) method for name
    def set_name(self, name):
        """Set the employee's name."""
        self.__name = name

    # Accessor (getter) method for ID number
    def get_id_number(self):
        """Return the employee's ID number."""
        return self.__id_number

    # Mutator (setter) method for ID number
    def set_id_number(self, id_number):
        """Set the employee's ID number."""
        self.__id_number = id_number

    # Accessor (getter) method for department
    def get_department(self):
        """Return the employee's department."""
        return self.__department

    # Mutator (setter) method for department
    def set_department(self, department):
        """Set the employee's department."""
        self.__department = department

    # Accessor (getter) method for job title
    def get_job_title(self):
        """Return the employee's job title."""
        return self.__job_title

    # Mutator (setter) method for job title
    def set_job_title(self, job_title):
        """Set the employee's job title."""
        self.__job_title = job_title

    # String representation method for easy display
    def __str__(self):
        """Return a formatted string representation of the employee data."""
        return (f"Name: {self.__name}\n"
                f"ID Number: {self.__id_number}\n"
                f"Department: {self.__department}\n"
                f"Job Title: {self.__job_title}")


# Main program starts here
def main():
    """Main function to test the Employee class with three instances."""

    # Print header for the program output
    print("=" * 70)
    print("Employee Management System")
    print("=" * 70)
    print()

    # Create the first Employee object with John's information
    # Name: John, ID: 1050, Department: Finance, Job Title: Manager
    employee1 = Employee("John", 1050, "Finance", "Manager")

    # Create the second Employee object with Susan's information
    # Name: Susan, ID: 1159, Department: IT, Job Title: Vice President
    employee2 = Employee("Susan", 1159, "IT", "Vice President")

    # Create the third Employee object with Megan's information
    # Name: Megan, ID: 0945, Department: Cyber Security, Job Title: Engineer
    employee3 = Employee("Megan", "0945", "Cyber Security", "Engineer")

    # Display information for Employee 1 (John)
    print("Employee 1 Information:")
    print("-" * 70)
    # Use the __str__ method to display all employee information
    print(employee1)
    print()

    # Display information for Employee 2 (Susan)
    print("Employee 2 Information:")
    print("-" * 70)
    # Use the __str__ method to display all employee information
    print(employee2)
    print()

    # Display information for Employee 3 (Megan)
    print("Employee 3 Information:")
    print("-" * 70)
    # Use the __str__ method to display all employee information
    print(employee3)
    print()

    # Demonstrate the use of accessor methods
    print("=" * 70)
    print("Demonstrating Accessor Methods:")
    print("=" * 70)
    # Use get_name() accessor method to retrieve employee1's name
    print(f"Employee 1's name (using accessor): {employee1.get_name()}")
    # Use get_id_number() accessor method to retrieve employee1's ID number
    print(f"Employee 1's ID number (using accessor): {employee1.get_id_number()}")
    # Use get_department() accessor method to retrieve employee2's department
    print(f"Employee 2's department (using accessor): {employee2.get_department()}")
    # Use get_job_title() accessor method to retrieve employee3's job title
    print(f"Employee 3's job title (using accessor): {employee3.get_job_title()}")
    print()

    # Demonstrate the use of mutator methods
    print("=" * 70)
    print("Demonstrating Mutator Methods:")
    print("=" * 70)
    # Use set_job_title() mutator method to update employee1's job title
    employee1.set_job_title("Senior Manager")
    print(f"Employee 1's job title updated to: {employee1.get_job_title()}")

    # Use set_department() mutator method to update employee2's department
    employee2.set_department("Information Technology")
    print(f"Employee 2's department updated to: {employee2.get_department()}")

    # Use set_id_number() mutator method to update employee3's ID number
    employee3.set_id_number("0946")
    print(f"Employee 3's ID number updated to: {employee3.get_id_number()}")
    print()

    # Display updated information for all employees
    print("=" * 70)
    print("Updated Information for All Employees:")
    print("=" * 70)
    print()

    # Display updated information for Employee 1
    print("Employee 1 - Updated Information:")
    print("-" * 70)
    print(employee1)
    print()

    # Display updated information for Employee 2
    print("Employee 2 - Updated Information:")
    print("-" * 70)
    print(employee2)
    print()

    # Display updated information for Employee 3
    print("Employee 3 - Updated Information:")
    print("-" * 70)
    print(employee3)
    print()

    # Create a summary table displaying all employees
    print("=" * 70)
    print("Employee Summary Table:")
    print("=" * 70)
    # Print table header with column names
    print(f"{'Name':<15} {'ID Number':<15} {'Department':<20} {'Job Title':<20}")
    print("-" * 70)
    # Print employee1's information in table format using accessor methods
    print(f"{employee1.get_name():<15} {employee1.get_id_number():<15} "
          f"{employee1.get_department():<20} {employee1.get_job_title():<20}")
    # Print employee2's information in table format using accessor methods
    print(f"{employee2.get_name():<15} {employee2.get_id_number():<15} "
          f"{employee2.get_department():<20} {employee2.get_job_title():<20}")
    # Print employee3's information in table format using accessor methods
    print(f"{employee3.get_name():<15} {employee3.get_id_number():<15} "
          f"{employee3.get_department():<20} {employee3.get_job_title():<20}")
    print()

    # Print closing message
    print("=" * 70)
    print("End of Employee Management System")
    print("=" * 70)


# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to execute the program
    main()