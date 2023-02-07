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


def dictionarydatabase(filename):
    """
    This function is aimed to read the data in the file and make data into the type "dictionary in dictionary"
    For example database = {123456:{name:..., category:...,...}, 234567:{name:..., category:...,...},...}
    # type of data k = {444444:{name: kkk, category : ""}}
    """
    filelist = []  # List of each new line
    u1 = []  # Variable to get the beginning and the ending of the product
    variable = 0
    dictionary1 = {}
    dictionary2 = {}
    dictionary3 = {}
    dictionary4 = {}
    filelistwithenter = open(filename).readlines()  # Open the file and make the data of the file into the list
    # remove \n from the data
    for i in filelistwithenter:
        i = i.strip('\n')
        filelist.append(i)
    # finding the position from the CODE line to the last information line
    for i in range(0, len(filelist), 1):
        if filelist[i] == "BEGIN PRODUCT":
            u1.append(i + 1)
        elif filelist[i] == "END PRODUCT":
            u1.append(i - 1)
    u1.sort()  # After finishing, we can get the odd number as the beginning, the even number as the ending
    # of the data that we need to import to class Product
    for i in range(0, len(u1), 2):  # variable to get the beginning and the ending of the data
        for z in range(u1[i], u1[i + 1] + 1, 1):  # we can get the line number to get the data with t
            u3 = []  # Get the list of variable without command
            u = filelist[z].split()  # list the word of the list into small list
            for m in range(0, len(u), 1):
                if u[m] == "#":
                    for t in range(m, len(u), 1):
                        u3.append(u[t])
                    break
            for x in u3:
                u.remove(x)

            # Make a list into 2 variables
            if len(u) > 2:
                k = ' '.join(u[1:len(u)])
                utemporary = [u[0], k]
                u = utemporary
            dictionary1[u[0]] = u[1]
            # Join the list into dictionary
            if len(dictionary2) < (u1[i + 1] - u1[i] + 1):
                dictionary2.update(dictionary1)

            if len(dictionary2) == (u1[i + 1] - u1[i] + 1):
                dictionary3.update(dictionary2)
                # print(dictionary3)
                # print(dictionary4)
                a = -1
                for y in range(0, len(dictionary4), 1):
                    if dictionary4[f'Data {y}']['CODE'] == dictionary3['CODE'] and dictionary4[f'Data {y}']['PRICE'] == \
                            dictionary3['PRICE'] and dictionary4[f'Data {y}']['CATEGORY'] == dictionary3['CATEGORY'] and \
                            dictionary4[f'Data {y}']['NAME'] == dictionary3['NAME']:
                        dictionary4[f'Data {y}']['STOCK'] = int(dictionary4[f'Data {y}']['STOCK']) + int(
                            dictionary3['STOCK'])
                        a = 0
                        variable -= 1
                        break

                if a == -1:
                    dictionary4[f"Data {variable}"] = dictionary3
                dictionary3 = dictionary1 = dictionary2 = {}
                variable += 1
    # print(u1)
    # print(dictionary4)
    return dictionary4


def printwholedata(dictionary4):
    """Docstring to bla bla bla"""
    dictionaryn = dictionary4.copy()
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


def printonlyadata(dictionary4, parameters):
    """Docstring to bla bla bla"""
    i = -1

    for k in range(0, len(dictionary4), 1):
        if dictionary4[f'Data {k}']['CODE'] == parameters:
            i = k
            break
    if i != -1:
        code = dictionary4[f'Data {i}']['CODE']
        name = dictionary4[f'Data {i}']['NAME']
        category = dictionary4[f'Data {i}']['CATEGORY']
        price = float(dictionary4[f'Data {i}']['PRICE'])
        stock = dictionary4[f'Data {i}']['STOCK']
        print(Product(code, name, category, price, stock))
    else:
        print(f"Error: product '{parameters}' can not be printed as it does not exist.")


def main():
    filename = input("Enter database name: ")
    # filename = "productsx.txt"
    # filename = "simpleproducts.txt"
    dictionary4 = dictionarydatabase(filename)

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
            printwholedata(dictionary4)
        elif "print".startswith(command) and parameters != "":
            # TODO: Implement print command to print a single
            #       product when the product code is given.
            ...
            printonlyadata(dictionary4, parameters)
        elif "delete".startswith(command) and parameters != "":
            # TODO: Implement delete command for removing
            #       a product from the inventory.
            ...
            i = -1
            parameters_split = parameters.split()
            if len(parameters_split) != 1:
                print(f"Error: product '{parameters}' can not be deleted as it does not exist.")
            else:
                for k in range(0, len(dictionary4), 1):
                    if dictionary4[f'Data {k}']['CODE'] == parameters_split[0]:
                        i = k
                        break
                if i == -1:
                    print(f"Error: product '{parameters}' can not be deleted as it does not exist.")
                else:
                    if int(dictionary4[f'Data {i}']['STOCK']) > 0:
                        print(f"Error: product '{parameters}' can not be deleted as stock remains.")
                    else:
                        dictionary4[f'Data {i}']['CODE'] = ""
                        dictionary4[f'Data {i}']['NAME'] = ""
                        dictionary4[f'Data {i}']['CATEGORY'] = ""
                        dictionary4[f'Data {i}']['PRICE'] = ""
                        dictionary4[f'Data {i}']['STOCK'] = ""

        elif "change".startswith(command) and parameters != "":
            # TODO: Implement change command which allows
            #       the user to modify the amount of a product
            #       in stock.
            ...
            i = -1
            parameters_split = parameters.split()
            if len(parameters_split) != 2:
                print(f"Error: bad parameters '{parameters}' for change command.")
            else:
                try:
                    int(parameters_split[0])
                    for k in range(0, len(dictionary4), 1):
                        if dictionary4[f'Data {k}']['CODE'] == parameters_split[0]:
                            i = k
                            break
                    if i != -1:
                        ...
                        dictionary4[f'Data {i}']['STOCK'] = int(dictionary4[f'Data {i}']['STOCK']) + int(
                            parameters_split[1])
                    else:
                        print(f"Error: stock for '{parameters_split[0]}' can not be changed as it does not exist.")
                except ValueError:
                    print(f"Error: bad parameters '{parameters}' for change command.")
        elif "low".startswith(command) and parameters == "":
            # TODO: Implement low command which can be used to
            #       alert the user when the amount of items
            #       drop below <LOW_STOCK_LIMIT> i.e. 30.
            ...
            u = []
            k = 0
            smalldictionary = {}
            for i in range(0, len(dictionary4), 1):
                if dictionary4[f'Data {i}']['CODE'] != "":
                    if int(dictionary4[f'Data {i}']['STOCK']) < LOW_STOCK_LIMIT:
                        u.append(i)
            if u:
                for i in u:
                    smalldictionary[f'Data {k}'] = dictionary4[f'Data {i}']
                    k += 1
                if len(smalldictionary) == 1:
                    printonlyadata(dictionary4, dictionary4[f'Data {u[0]}']['CODE'])
                else:
                    printwholedata(smalldictionary)
        elif "combine".startswith(command) and parameters != "":
            # TODO: Implement combine command which allows
            #       the combining of two products into one.
            ...
            i1 = -1
            i2 = -2
            parameters_split = parameters.split()
            if len(parameters_split) != 2:
                print(f"Error: bad command line '{parameters}' for combine command.")
            else:
                for k in range(0, len(dictionary4), 1):
                    if dictionary4[f'Data {k}']['CODE'] == parameters_split[0]:
                        i1 = k
                        break
                for k in range(0, len(dictionary4), 1):
                    if dictionary4[f'Data {k}']['CODE'] == parameters_split[1]:
                        i2 = k
                        break
                if i1 != -1 and i2 != -2 and i1 != i2:
                    if dictionary4[f'Data {i1}']['CATEGORY'] == dictionary4[f'Data {i2}']['CATEGORY']:
                        if dictionary4[f'Data {i1}']['PRICE'] == dictionary4[f'Data {i2}']['PRICE']:
                            dictionary4[f'Data {i1}']['STOCK'] = int(dictionary4[f'Data {i1}']['STOCK']) + int(
                                dictionary4[f'Data {i2}']['STOCK'])
                            dictionary4[f'Data {i2}']['CODE'] = ""
                            dictionary4[f'Data {i2}']['NAME'] = ""
                            dictionary4[f'Data {i2}']['CATEGORY'] = ""
                            dictionary4[f'Data {i2}']['PRICE'] = ""
                            dictionary4[f'Data {i2}']['STOCK'] = ""
                        else:
                            print(
                                f"Error: combining items with different prices {dictionary4[f'Data {i1}']['PRICE']}€ and {dictionary4[f'Data {i2}']['PRICE']}€.")
                    else:
                        print(
                            f"Error: combining items of different categories '{dictionary4[f'Data {i1}']['CATEGORY']}' and '{dictionary4[f'Data {i2}']['CATEGORY']}'.")
                elif i1 == i2:
                    print(f"Error: bad parameters '{parameters}' for combine command.")
                else:
                    print(f"Error: bad parameters '{parameters}' for combine command.")
        elif "sale".startswith(command) and parameters != "":
            # TODO: Implement sale command which allows the user to set
            #       a sale price for all the products in a specific category.
            ...
            parameters_split = parameters.split()
            i = []

            t = 0
            if len(parameters_split) != 2:
                print(f"Error: bad parameters '{parameters}' for sale command.")
            else:
                for k in range(0, len(dictionary4), 1):
                    if dictionary4[f'Data {k}']['CATEGORY'] == parameters_split[0]:
                        i.append(k)
                if not i:
                    print(f"Sale price set for 0 items.")
                else:
                    try:
                        float(parameters_split[1])
                        if float(parameters_split[1]) != 0.0:
                            for k in i:
                                dictionary4[f'Data {k}']['PRICE'] = (100 - float(parameters_split[1])) / 100 * \
                                                                    float(dictionarydatabase(filename)[f'Data {k}'][
                                                                              'PRICE'])
                        else:
                            if float(parameters_split[1]) == 0.0:
                                for k in i:
                                    dictionary4[f'Data {k}']['PRICE'] = dictionarydatabase(filename)[f'Data {k}'][
                                        'PRICE']

                        print(f"Sale price set for {len(i)} items.")
                    except ValueError:
                        print(f"Error: bad parameters '{parameters}' for sale command.")
                t += 1



        else:
            print(f"Error: bad command line '{command_line}'.")


if __name__ == "__main__":
    main()
