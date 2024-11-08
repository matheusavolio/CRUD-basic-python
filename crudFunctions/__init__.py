from time import sleep
from colors import *
registerList = []
registerDict = {}

def formatting():
    print()
    sleep(0.5)

def sucessMessage(message):
    print(f"{green}{message}{reset}")

def errorMessage(message):
    print(f"{red}{message}{reset}")

def newRegister(id, name, email, password):
        """
    Adds a new record to the `registerList` list.

    The function creates a dictionary containing information about a new user, with the following fields: 
    "Id", "Name", "Email" and "Password", using the values ​​provided as arguments. 
    This dictionary is then added to the `registerList` list.

    After adding the record to the list, the function clears the `registerDict` dictionary (although this step
    there is an error in the method call syntax, as the parentheses are missing). A message from
    success is printed to the user, indicating that the record was added successfully.

    Parameters:
        id (int): The user's unique identifier.
        name (str): The user name.
        email (str): The user's email address.
        password (str): The user's password.

    Return:
        None. The function just modifies the `registerList` list and prints a success message.

    Usage example:
        newRegister(1, "João Silva", "joao@example.com", "123456")
        # Add a new record with Id=1, Name="João Silva", Email="joao@example.com" and Password="123456"
    """
        try:
            registerDict = {"Id":id, "Name":name, "Email":email, "Password":password}
            registerList.append(registerDict)
            sucessMessage("Register added sucessfully!")
        except Exception as e:
            errorMessage(f"{e.__class__}")
        

def viewRegisters():
        """
        Displays the details of each registration in the `registerList` list.

        The function loops through the list `registerList`, which is expected to be a list of dictionaries, and prints
        information for each item, including "Id", "Name", "Email" and "Password". The display is made of 
        formatted form, with each record being printed with its respective fields, followed by a 
        blank line. After displaying each record, the code waits 0.5 seconds before continuing to the next.

        Example output for a record:
        Id: 1
        Name: João Silva
        Email: joao@example.com
        Password: 123456

        If an error occurs during execution, an error is captured and a message is printed on the 
            format: "Error! [error cause] - - [error class]", with information related to the error.

        Exception:
            If any exception occurs, it is caught and its cause and class are printed.

        Parameters:
            None.

        Return:
            None. The function only prints information on the screen.
        """
        if not registerList:
            errorMessage("Error! Record not found, add a record first.")
            formatting()
        else:

            for register in registerList:
                print(f"{blue}-=-=-=-=-=-=-=-=-=-=-=-=-={reset}")
                print (
                f'Id: {register["Id"]}\n'
                f'Name: {register["Name"]}\n'
                f'E-mail: {register["Email"]}\n'
                f'Password: {register["Password"]}'
                )
                print(f"{blue}-=-=-=-=-=-=-=-=-=-=-=-=-={reset}")
                formatting()


    
            
def uptadeRegister(idFound, nameUpdate, emailUpdate, passwordUpdate):
        """
    Updates a user's information in the `registerList` by matching the provided ID.

    This function loops through the `registerList` and searches for a record with the matching 
    "Id". If a match is found, the corresponding "Name", "Email", and "Password" fields are 
    updated with the new values provided. Once the update is successfully made, a success 
    message is printed. If no matching ID is found, an error message is displayed.

    Parameters:
        idFound (int): The ID of the record to be updated.
        nameUpdate (str): The new name to be set for the user.
        emailUpdate (str): The new email to be set for the user.
        passwordUpdate (str): The new password to be set for the user.

    Return:
        None. The function modifies the list `registerList` in place and prints messages.

    Example usage:
        updateRegister(1, "Jane Doe", "jane.doe@example.com", "12345")
    """ 
        for register in registerList:
            if register["Id"] == idFound: 
                register["Name"] = nameUpdate
                register["Email"] = emailUpdate
                register["Password"] = passwordUpdate
                print(f"{green}Register updated successfully{reset}")
                formatting()
                return
        errorMessage("Error! Id not found.")
        formatting
                

def deleteRegister(Id):
    """
    Removes a record from the `registerList` based on the provided ID.

    This function searches for a record with the specified `Id` in the `registerList`.
    If the record is found, it is removed. A success message is printed.
    If the ID is not found, an error message is displayed.

    Parameters:
        Id (int): The ID of the record to be removed.

    Return:
        None. The function modifies the `registerList` in place and prints a message.

    Example usage:
        deleteRegister(1)
        # Removes the record with Id=1 from the `registerList`
    """
    
    for register in registerList:
        if register["Id"] == Id:
            registerList.remove(register)
            print(f"{green}Product removed sucessfully!{reset}")
            formatting()
            return
    errorMessage("Error! Id not found.")