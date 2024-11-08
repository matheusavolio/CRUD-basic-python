from time import sleep
from colors import *
registerList = []
registerDict = {}

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
        registerDict = {"Id":id, "Name":name, "Email":email, "Password":password}
        registerList.append(registerDict)

        print(f"{green}Register added sucessfully!{reset}")
        

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
            print(f"{red}Error! Record not found, add a record first.{reset}")
            sleep(0.5)
        else:
            for register in registerList:
                print (
                f'Id: {register["Id"]}\n'
                f'Name: {register["Name"]}\n'
                f'E-mail: {register["Email"]}\n'
                f'Password: {register["Password"]}'
                )
                print()
                sleep(0.5)


    
            
def uptadeRegister(idFound, nameUpdate, emailUpdate, passwordUpdate):
        for register in registerList:
            if register["Id"] == idFound: 
                register["Name"] = nameUpdate
                register["Email"] = emailUpdate
                register["Password"] = passwordUpdate
                print(f"{green}Register updated successfully{reset}")
                print()
                sleep(1)
            else:
                print(f"{red}Error! Id not found.{reset}")
                sleep(0.5)
        return
                

def delRegister(Id):
            for register in registerList:
                if register["Id"] == Id:
                    registerList.remove(register)
                    print(f"{green}Product removed sucessfully!{reset}")
                    sleep(1)
                    return
                else:
                    print(f"{red}Error! Id not found.{reset}")
            return