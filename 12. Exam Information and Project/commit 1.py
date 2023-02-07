"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
StudentId: 151317891
Name:      Nguyen The Long
Email:     long.nguyen@tuni.fi

StudentId: 151394898
Name:      Vu Dinh Thi
Email:     thi.vu@tuni.fi

Assignment: Using practical tools for fixing, showing the data of the product by code
"""

# +--------------------------------------------------------------+
# | This template file requires at minimum Python version 3.8 to |
# | work correctly. If your Python version is older, you really  |
# | should get yourself a newer version.                         |
# +--------------------------------------------------------------+


LOW_STOCK_LIMIT = 30


class Product:
    """
    This class represent a product i.e. an item available for sale.
    """

    def __init__(self, code, name, category, price, stock):
        self.__code = code
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock

        # TODO (MAYBE): You might want to add more attributes here.

    def __str__(self):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests.
        """

        lines = [
            f"Code:     {self.__code}",
            f"Name:     {self.__name}",
            f"Category: {self.__category}",
            f"Price:    {self.__price:.2f}€",
            f"Stock:    {self.__stock} units",
        ]

        longest_line = len(max(lines, key=len))

        for i in range(len(lines)):
            lines[i] = f"| {lines[i]:{longest_line}} |"

        solid_line = "+" + "-" * (longest_line + 2) + "+"
        lines.insert(0, solid_line)
        lines.append(solid_line)

        return "\n".join(lines)

    def __eq__(self, other):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests since the read_database function will
        stop working correctly.
        """

        return self.__code == other.__code and \
               self.__name == other.__name and \
               self.__category == other.__category and \
               self.__price == other.__price

    def modify_stock_size(self, amount):
        """
        YOU SHOULD NOT MODIFY THIS METHOD since read_database
        relies on its behavior and might stop working as a result.

        Allows the <amount> of items in stock to be modified.
        This is a very simple method: it does not check the
        value of <amount> which could possibly lead to
        a negative amount of items in stock. Caveat emptor.

        :param amount: int, how much to change the amount in stock.
                       Both positive and negative values are accepted:
                       positive value increases the stock and vice versa.
        """

        self.__stock += amount

    # TODO: Multiple methods need to be written here to allow
    #       all the required commands to be implemented.


def _read_lines_until(fd, last_line):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION since read_database
    relies on its behavior and might stop working as a result.

    Reads lines from <fd> until the <last_line> is found.
    Returns a list of all the lines before the <last_line>
    which is not included in the list. Return None if
    file ends bofore <last_line> is found.
    Skips empty lines and comments (i.e. characeter '#'
    and everything after it on a line).

    You don't need to understand this function works as it is
    only used as a helper function for the read_database function.

    :param fd: file, file descriptor the input is read from.
    :param last_line: str, reads lines until <last_line> is found.
    :return: list[str] | None
    """

    lines = []

    while True:
        line = fd.readline()

        if line == "":
            return None

        hashtag_position = line.find("#")
        if hashtag_position != -1:
            line = line[:hashtag_position]

        line = line.strip()

        if line == "":
            continue

        elif line == last_line:
            return lines

        else:
            lines.append(line)


def read_database(filename):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION as it is ready.

    This function reads an input file which must be in the format
    explained in the assignment. Returns a dict containing
    the product code as the key and the corresponding Product
    object as the payload. If an error happens, the return value will be None.

    You don't necessarily need to understand how this function
    works as long as you understand what the return value is.
    You can probably learn something new though, if you examine the
    implementation.

    :param filename: str, name of the file to be read.
    :return: dict[int, Product] | None
    """

    data = {}

    try:
        with open(filename, mode="r", encoding="utf-8") as fd:

            while True:
                lines = _read_lines_until(fd, "BEGIN PRODUCT")
                if lines is None:
                    return data

                lines = _read_lines_until(fd, "END PRODUCT")
                if lines is None:
                    print(f"Error: premature end of file while reading '{filename}'.")
                    return None

                # print(f"TEST: {lines=}")

                collected_product_info = {}

                for line in lines:
                    keyword, value = line.split(maxsplit=1)  # ValueError possible

                    # print(f"TEST: {keyword=} {value=}")

                    if keyword in ("CODE", "STOCK"):
                        value = int(value)  # ValueError possible

                    elif keyword in ("NAME", "CATEGORY"):
                        pass  # No conversion is required for string values.

                    elif keyword == "PRICE":
                        value = float(value)  # ValueError possible

                    else:
                        print(f"Error: an unknown data identifier '{keyword}'.")
                        return None

                    collected_product_info[keyword] = value

                if len(collected_product_info) < 5:
                    print(f"Error: a product block is missing one or more data lines.")
                    return None

                product_code = collected_product_info["CODE"]
                product_name = collected_product_info["NAME"]
                product_category = collected_product_info["CATEGORY"]
                product_price = collected_product_info["PRICE"]
                product_stock = collected_product_info["STOCK"]

                product = Product(code=product_code,
                                  name=product_name,
                                  category=product_category,
                                  price=product_price,
                                  stock=product_stock)

                # print(product)

                if product_code in data:
                    if product == data[product_code]:
                        data[product_code].modify_stock_size(product_stock)

                    else:
                        print(f"Error: product code '{product_code}' conflicting data.")
                        return None

                else:
                    data[product_code] = product

    except OSError:
        print(f"Error: opening the file '{filename}' failed.")
        return None

    except ValueError:
        print(f"Error: something wrong on line '{line}'.")
        return None


def example_function_for_example_purposes(warehouse, parameters):
    """
    This function is an example of how to deal with the extra
    text user entered on the command line after the actual
    command word.

    :param warehouse: dict[int, Product], dict of all known products.
    :param parameters: str, all the text that the user entered after the command word.
    """

    try:
        # Let's try splitting the <parameters> string into two parts.
        # Raises ValueError if there are more or less than exactly two
        # values (in this case there should be one int and one float) in
        # the <parameters> string.
        code, number = parameters.split()

        # First parameter was supposed to be a products code i.e. an integer
        # and the second should be a float. If either of these assumptions fail
        # ValueError will be raised.
        code = int(code)
        number = float(number)

    except ValueError:
        print(f"Error: bad parameters '{parameters}' for example command.")
        return

    # <code> should be an existing product code in the <warehouse>.
    if code not in warehouse:
        print(f"Error: unknown product code '{code}'.")
        return

    # All the errors were checked above, so everything should be
    # smooth sailing from this point onward. Of course, the other
    # commands might require more or less error/sanity checks, this
    # is just a simple example.

    print("Seems like everything is good.")
    print(f"Parameters are: {code=} and {number=}.")


def Import_data_into_dictionary(filename):
    """
    This function is aimed to read the data in the file and make data into the type "dictionary in dictionary"
    For example database = {Data 0:{name:..., category:...,...}, Data 1:{name:..., category:...,...},...}
    """
    # First of all, We have the database from filename with '\n', we need to split the data into the lists without '\n'
    Original_database = open(filename).readlines()  # Open the file and make the data of the file into the list
    List_of_data = []  # The list of data that we need to append
    for i in Original_database:
        i = i.strip('\n')
        List_of_data.append(i)
    # print(List_of_data) # If you want to check type of data, you can remove the "# " in the beginning
    """
    Main idea for making data into the correct type: 
    1) We will make a list of the beginning and the ending lines of the products, with odd values are the beginning, and
    even values are the ending 
    2) Remove comments 
    3) Create lists with 2 variables and import to a small dictionary because the data that we need to achieve is 
    dictionary in dictionary: 
        1. For the type of data that we need to know for each product (Code, Name, Category, Price, Stock) 
        2. For the content that we need to know for each product 4) Add small dictionary into large dictionary - the 
        dictionary that we need to achieve 
    """
    beginning_ending = []  # Variable to get the beginning and the ending of each product
    variable = 0  # Since the type of data is {data 0:{...}, data 1:{...}}, variable as 0,1,... in this case
    small_dictionary = {}  # small dictionary inside large dictionary
    dictionary3 = {}  # Making sure that there are no inspections warning in Pycharm
    dictionary_data = {}  # The data after all that we need to input

    """
    Finding the position from the first line to the last information line From the beginning and the ending of the 
    data, we can see "BEGIN PRODUCT" and "END PRODUCT", we can use these characteristics to find the data of each 
    product 
    """
    for i in range(0, len(List_of_data), 1):
        if List_of_data[i] == "BEGIN PRODUCT":
            beginning_ending.append(i + 1)
        elif List_of_data[i] == "END PRODUCT":
            beginning_ending.append(i - 1)
    # print(beginning_ending) # If you want to check type of data, you can remove the "# " in the beginning
    """
    From this part, we will remove the comments which are in line with the data of the products
    Main idea for removing the comments:
        + Split every word into the list
        + Recognize the "#" symbol
        + Adding data from variable "#" to the end of the list into new lists
        + Using command "remove" for the first and the second lists, we can find the list without comments
    """
    for i in range(0, len(beginning_ending), 2):  # i is the no. number of the beginning of the data
        for z in range(beginning_ending[i], beginning_ending[i + 1] + 1, 1):  # z is the no. number of the beginning -
            # ending of each product
            List_containing_comment_spliting_variable = []
            u = List_of_data[z].split()
            """
            u is list of data without comments - Since we need to use u a lot, using "u" for easier understanding
            From the beginning, u is only a list of data with each line split by word (having comment inside)
            However, after processing data of u, u will be only two variables: type and content of the product 
            """
            for m in range(0, len(u), 1):
                if u[m] == "#":
                    for t in range(m, len(u), 1):
                        List_containing_comment_spliting_variable.append(u[t])
                    break
            for x in List_containing_comment_spliting_variable:
                u.remove(x)
            # print(u) # If you want to check type of data and understand more the next step, you can remove the "# "
            # in the beginning
            """
            In this part, we will make "u" into 2 variables, since the some contents of the product will have more than
            1 word
            """
            if len(u) > 2:
                k = ' '.join(u[1:len(u)])  # Join the content letters of the type of the product
                u = [u[0], k]
            # print(u) # Remove the "# " if you want to see the difference without thinking
            """
            After processing all the data into necessary list, we will add the list into small dictionary first
            We will consider a case that they are the same products, but different stock. In this case, we will make a 
            "for" function to plus all the value of stock together
            Considering the factor: the products have the same name, price, category, code => we will plus the stocks 
            """
            small_dictionary[u[0]] = u[1]
            if len(small_dictionary) == (beginning_ending[i + 1] - beginning_ending[i] + 1):
                dictionary3.update(small_dictionary)  # making sure there are no inspections
                a = -1  # The value for checking that the small dictionary is in the dictionary or not
                for y in range(0, len(dictionary_data), 1):
                    if dictionary_data[f'Data {y}']['CODE'] == small_dictionary['CODE'] and \
                            dictionary_data[f'Data {y}'][
                                'PRICE'] == \
                            small_dictionary['PRICE'] and dictionary_data[f'Data {y}']['CATEGORY'] == small_dictionary[
                        'CATEGORY'] and \
                            dictionary_data[f'Data {y}']['NAME'] == small_dictionary['NAME']:
                        dictionary_data[f'Data {y}']['STOCK'] = int(dictionary_data[f'Data {y}']['STOCK']) + int(
                            small_dictionary['STOCK'])
                        a = 0
                        variable -= 1
                        break

                if a == -1:
                    dictionary_data[f"Data {variable}"] = dictionary3
                dictionary3 = small_dictionary = {}
                variable += 1
    # print(dictionary_data)  # If you want to check type of data, you can remove the "# " in the beginning
    return dictionary_data


def printwholedata(dictionary_data):
    """Docstring to bla bla bla"""
    dictionaryn = dictionary_data.copy()
    for i in range(0, len(dictionaryn) - 1, 1):
        for t in range(i + 1, len(dictionaryn), 1):
            if dictionaryn[f'Data {i}']['CODE'] > dictionaryn[f'Data {t}']['CODE']:
                # change the position of the data in ascending
                changevariable = dictionaryn[f'Data {i}']
                dictionaryn[f'Data {i}'] = dictionaryn[f'Data {t}']
                dictionaryn[f'Data {t}'] = changevariable

    for i in range(0, len(dictionaryn), 1):
        if dictionaryn[f'Data {i}']['CODE'] != "":
            code = dictionaryn[f'Data {i}']['CODE']
            name = dictionaryn[f'Data {i}']['NAME']
            category = dictionaryn[f'Data {i}']['CATEGORY']
            price = float(dictionaryn[f'Data {i}']['PRICE'])
            stock = dictionaryn[f'Data {i}']['STOCK']
            print(Product(code, name, category, price, stock))


def printonlyadata(dictionary_data, parameters):
    """Docstring to bla bla bla"""
    i = -1

    for k in range(0, len(dictionary_data), 1):
        if dictionary_data[f'Data {k}']['CODE'] == parameters:
            i = k
            break
    if i != -1:
        code = dictionary_data[f'Data {i}']['CODE']
        name = dictionary_data[f'Data {i}']['NAME']
        category = dictionary_data[f'Data {i}']['CATEGORY']
        price = float(dictionary_data[f'Data {i}']['PRICE'])
        stock = dictionary_data[f'Data {i}']['STOCK']
        print(Product(code, name, category, price, stock))
    else:
        print(f"Error: product '{parameters}' can not be printed as it does not exist.")


def delete(dictionary_data, parameters):
    i = -1
    parameters_split = parameters.split()
    if len(parameters_split) != 1:
        print(f"Error: product '{parameters}' can not be deleted as it does not exist.")
    else:
        for k in range(0, len(dictionary_data), 1):
            if dictionary_data[f'Data {k}']['CODE'] == parameters_split[0]:
                i = k
                break
        if i == -1:
            print(f"Error: product '{parameters}' can not be deleted as it does not exist.")
        else:
            if int(dictionary_data[f'Data {i}']['STOCK']) > 0:
                print(f"Error: product '{parameters}' can not be deleted as stock remains.")
            else:
                dictionary_data[f'Data {i}']['CODE'] = ""
                dictionary_data[f'Data {i}']['NAME'] = ""
                dictionary_data[f'Data {i}']['CATEGORY'] = ""
                dictionary_data[f'Data {i}']['PRICE'] = ""
                dictionary_data[f'Data {i}']['STOCK'] = ""


def changethestock(dictionary_data, parameters):
    """Docstring to bla bla bla"""
    i = -1
    parameters_split = parameters.split()
    if len(parameters_split) != 2:
        print(f"Error: bad parameters '{parameters}' for change command.")
    else:
        try:
            int(parameters_split[0])
            for k in range(0, len(dictionary_data), 1):
                if dictionary_data[f'Data {k}']['CODE'] == parameters_split[0]:
                    i = k
                    break
            if i != -1:
                ...
                dictionary_data[f'Data {i}']['STOCK'] = int(dictionary_data[f'Data {i}']['STOCK']) + int(
                    parameters_split[1])
            else:
                print(f"Error: stock for '{parameters_split[0]}' can not be changed as it does not exist.")
        except ValueError:
            print(f"Error: bad parameters '{parameters}' for change command.")


def low(dictionary_data):
    """Docstring to bla bla bla"""
    u = []
    k = 0
    smalldictionary = {}
    for i in range(0, len(dictionary_data), 1):
        if dictionary_data[f'Data {i}']['CODE'] != "":
            if int(dictionary_data[f'Data {i}']['STOCK']) < LOW_STOCK_LIMIT:
                u.append(i)
    if u:
        for i in u:
            smalldictionary[f'Data {k}'] = dictionary_data[f'Data {i}']
            k += 1
        if len(smalldictionary) == 1:
            printonlyadata(dictionary_data, dictionary_data[f'Data {u[0]}']['CODE'])
        else:
            printwholedata(smalldictionary)


def combine(dictionary_data, parameters):
    i1 = -1
    i2 = -2
    parameters_split = parameters.split()
    if len(parameters_split) != 2:
        print(f"Error: bad command line '{parameters}' for combine command.")
    else:
        for k in range(0, len(dictionary_data), 1):
            if dictionary_data[f'Data {k}']['CODE'] == parameters_split[0]:
                i1 = k
                break
        for k in range(0, len(dictionary_data), 1):
            if dictionary_data[f'Data {k}']['CODE'] == parameters_split[1]:
                i2 = k
                break
        if i1 != -1 and i2 != -2 and i1 != i2:
            if dictionary_data[f'Data {i1}']['CATEGORY'] == dictionary_data[f'Data {i2}']['CATEGORY']:
                if dictionary_data[f'Data {i1}']['PRICE'] == dictionary_data[f'Data {i2}']['PRICE']:
                    dictionary_data[f'Data {i1}']['STOCK'] = int(dictionary_data[f'Data {i1}']['STOCK']) + int(
                        dictionary_data[f'Data {i2}']['STOCK'])
                    dictionary_data[f'Data {i2}']['CODE'] = ""
                    dictionary_data[f'Data {i2}']['NAME'] = ""
                    dictionary_data[f'Data {i2}']['CATEGORY'] = ""
                    dictionary_data[f'Data {i2}']['PRICE'] = ""
                    dictionary_data[f'Data {i2}']['STOCK'] = ""
                else:
                    print(
                        f"Error: combining items with different prices {dictionary_data[f'Data {i1}']['PRICE']}"
                        f"€ and {dictionary_data[f'Data {i2}']['PRICE']}€.")
            else:
                print(
                    f"Error: combining items of different categories "
                    f"'{dictionary_data[f'Data {i1}']['CATEGORY']}' and "
                    f"'{dictionary_data[f'Data {i2}']['CATEGORY']}'."
                )
        elif i1 == i2:
            print(f"Error: bad parameters '{parameters}' for combine command.")
        else:
            print(f"Error: bad parameters '{parameters}' for combine command.")


def sale(dictionary_data, parameters, filename):
    parameters_split = parameters.split()
    i = []

    t = 0
    if len(parameters_split) != 2:
        print(f"Error: bad parameters '{parameters}' for sale command.")
    else:
        for k in range(0, len(dictionary_data), 1):
            if dictionary_data[f'Data {k}']['CATEGORY'] == parameters_split[0]:
                i.append(k)
        if not i:
            print(f"Sale price set for 0 items.")
        else:
            try:
                float(parameters_split[1])
                if float(parameters_split[1]) != 0.0:
                    for k in i:
                        dictionary_data[f'Data {k}']['PRICE'] = (100 - float(parameters_split[1])) / 100 * \
                                                                float(Import_data_into_dictionary(filename)[
                                                                          f'Data {k}'][
                                                                          'PRICE'])
                else:
                    if float(parameters_split[1]) == 0.0:
                        for k in i:
                            dictionary_data[f'Data {k}']['PRICE'] = \
                                Import_data_into_dictionary(filename)[f'Data {k}'][
                                    'PRICE']

                print(f"Sale price set for {len(i)} items.")
            except ValueError:
                print(f"Error: bad parameters '{parameters}' for sale command.")
        t += 1


def main():
    # filename = input("Enter database name: ")
    filename = "productsx.txt"
    # filename = "simpleproducts.txt"
    dictionary_data = Import_data_into_dictionary(filename)

    warehouse = read_database(filename)
    if warehouse is None:
        return
    while True:
        command_line = input("Enter command: ").strip()

        if command_line == "":
            return

        command, *parameters = command_line.split(maxsplit=1)

        command = command.lower()

        if len(parameters) == 0:
            parameters = ""
        else:
            parameters = parameters[0]

        # If you have trouble understanding what the values
        # in the variables <command> and <parameters> are,
        # remove the '#' comment character from the next line.
        # print(f"TEST: {command=} {parameters=}")

        if "example".startswith(command) and parameters != "":
            """
            'Example' is not an actual command in the program. It is
            implemented only to allow you to get ideas how to handle
            the contents of the variable <parameters>.

            Example command expects user to enter two values after the
            command name: an integer and a float:

                Enter command: example 123456 1.23

            In this case the variable <parameters> would refer to
            the value "123456 1.23". In other words, everything that
            was entered after the actual command name as a single string.
            """

            example_function_for_example_purposes(warehouse, parameters)
        elif "print".startswith(command) and parameters == "":
            # TODO: Implement print command which prints all
            #       known products in the ascending order of
            #       the product codes.

            # In this step, we will make the list into the a dictionary like format {401281:{NAME = ...,...},...}
            printwholedata(dictionary_data)
        elif "print".startswith(command) and parameters != "":
            # TODO: Implement print command to print a single
            #       product when the product code is given.
            ...
            printonlyadata(dictionary_data, parameters)
        elif "delete".startswith(command) and parameters != "":
            # TODO: Implement delete command for removing
            #       a product from the inventory.
            delete(dictionary_data, parameters)
        elif "change".startswith(command) and parameters != "":
            # TODO: Implement change command which allows
            #       the user to modify the amount of a product
            #       in stock.

            changethestock(dictionary_data, parameters)
        elif "low".startswith(command) and parameters == "":
            # TODO: Implement low command which can be used to
            #       alert the user when the amount of items
            #       drop below <LOW_STOCK_LIMIT> i.e. 30.
            low(dictionary_data)
        elif "combine".startswith(command) and parameters != "":
            # TODO: Implement combine command which allows
            #       the combining of two products into one.
            combine(dictionary_data, parameters)
        elif "sale".startswith(command) and parameters != "":
            # TODO: Implement sale command which allows the user to set
            #       a sale price for all the products in a specific category.
            sale(dictionary_data, parameters, filename)
        else:
            print(f"Error: bad command line '{command_line}'.")


if __name__ == "__main__":
    main()
