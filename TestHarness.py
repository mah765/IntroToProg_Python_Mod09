# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A test harness script to test other scripts
# ChangeLog (Who,When,What):
# MHamilton,2021.12.12,Created script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as Eio  # employee IO classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
# First test the Person class
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print("Person: ", row.to_string(), type(row))

# Test processing module for the Person objects
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = D.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))

# Now test the Employee class
objE1 = D.Employee(123, objP1.first_name, objP1.last_name)
objE2 = D.Employee(456, objP2.first_name, objP2.last_name)
lstTable = [objE1, objE2]
for row in lstTable:
    print("Employee: ", row.to_string(), type(row))

P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    e = D.Employee(row[0], row[1], row[2])
    print(e.to_string().strip(), type(e))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
