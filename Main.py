# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# MHamilton,12.12.2021,Modified code to complete assignment 9
# MHamilton,12.13.2021,Major updates
# ------------------------------------------------------------------------ #

# Import modules
if __name__ == "__main__":
    import DataClasses as D                     # data classes
    import ProcessingClasses as P               # processing classes
    from IOClasses import EmployeeIO as Eio     # IO classes
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable = []
for row in lstFileData:
    try:
        e = D.Employee(row[0], row[1], row[2])
        lstTable.append(e)
        print(e.to_string().strip(), type(e))
        print() # for looks
    except:
        print("<Invalid entry found.>")

while (True):
    # Show user a menu of options
    Eio.print_menu_items()
    # Get user's menu option choice
    choice_str = Eio.input_menu_options()

    if choice_str.strip() == '1':
        # Show user current data in the list of employee objects
        Eio.print_current_list_items(lstTable)
        continue

    elif choice_str.strip() == '2':
        # Let user add data to the list of employee objects
        try:
            emp = Eio.input_employee_data()
            lstTable.append(emp)
        except:
            print("Invalid entry. Try again.")
        continue

    elif choice_str.strip() == '3':
        # let user save current data to file
        P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
        print("Data saved to file!")
        continue

    elif choice_str.strip() == '4':
        # Let user exit program
        print("Goodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #

