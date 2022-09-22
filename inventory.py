# The class below reads data and allows user to search for data and also present data in a table format.

from tabulate import tabulate


class Shoe:
    """Shoe class"""

    # File name
    data_file_txt = 'inventory.txt'

    @classmethod
    def read_data(cls):
        """Reading data"""
        while True:
            try:
                with open(Shoe.data_file_txt, 'r') as inventory_file:

                    # Lists
                    shoe_code_list = []
                    shoe_quantity = []
                    cost_list = []
                    product_type = []

                    # Reading data
                    for content in inventory_file:
                        country = content.split(',')[0]
                        code = content.split(',')[1]
                        product = content.split(',')[2]
                        cost = content.split(',')[3]
                        quantity = content.split(',')[4]

                        # Adding to a list
                        shoe_code_list.append(code.strip())
                        shoe_quantity.append(quantity.strip())
                        cost_list.append(cost.strip())
                        product_type.append(product.strip())

                    # Creating five shoe list
                    five_shoes_code = shoe_code_list[1:6]

                    # Searching shoes by code
                    search_shoe = str(input("Search shoe by code:  \n"))
                    if search_shoe in five_shoes_code:
                        print(search_shoe)
                    else:
                        print(f"The code {search_shoe} does not exist, try again")
                        continue

                    # Slicing the first five items of the list
                    five_shoe_quantity = shoe_quantity[1:6]

                    # sorting the list in ascending order
                    five_shoe_quantity_sorted = sorted(five_shoe_quantity)

                    # Determining the product with the lowest quantity
                    lowest_quantity = min(five_shoe_quantity_sorted)
                    if lowest_quantity == five_shoe_quantity_sorted[0]:
                        # Adding new stock of item with the lowest stock
                        new_stock_quantity = 50 + int(five_shoe_quantity_sorted[0])
                        five_shoe_quantity_sorted.append(str(new_stock_quantity))

                        # # Finding the product with the lowest quantity
                        my_index = min(five_shoe_quantity)
                        lowest_quantity_index = five_shoe_quantity.index(my_index)
                        the_lowest_quantity = product_type[1:6]
                        print(f"{the_lowest_quantity[lowest_quantity_index]} has lowest quantity of stock, "
                              f"{new_stock_quantity} units is now being restocked.")

                    # Finding the product with the highest quantity
                    highest_quantity = max(five_shoe_quantity)

                    # Finding the product name of the product with the highest quantity
                    highest_quantity_index = five_shoe_quantity.index(highest_quantity)
                    five_product_types_list = product_type[1:6]

                    # Printing out the results
                    print(
                        f"{five_product_types_list[highest_quantity_index]} has {highest_quantity} units, it's now on "
                        f"SALE!!! \n")

                    break

            except FileNotFoundError:
                print(f"The file {Shoe.data_file_txt} is not found,")

    @classmethod
    def value_per_item(cls):
        """ This method calculates the value or total worth of each product"""
        while True:
            try:
                with open(Shoe.data_file_txt, 'r') as inventory_file:
                    contents = inventory_file.readlines()
                    # Lists
                    cost_list = []
                    quantity_list = []

                    # Reading data
                    for content in contents[1:]:
                        country = content.split(',')[0].strip()
                        code = content.split(',')[1].strip()
                        product = content.split(',')[2].strip()
                        cost = content.split(',')[3].strip()
                        quantity = content.split(',')[4].strip()

                        # Adding to lists
                        cost_list.append(int(cost))
                        quantity_list.append(int(quantity))

                    # Calculating the total worth
                    value = []
                    for i in range(0, len(cost_list)):
                        value.append(cost_list[i] * quantity_list[i])

                # Reading data, so it can be presented in a tabular format
                with open(Shoe.data_file_txt, 'r') as inventory_tabulate:
                    contents = inventory_tabulate.readlines()
                    formatted_data = []
                    for each_element in contents[1:]:
                        each_element_split = each_element.split(',')
                        formatted_data.append(each_element_split)

                    formatted_data.append(value)

                    # Headers for the table
                    headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity']

                    # Printing out the results in a table format
                    print(tabulate(formatted_data, headers=headers, showindex=range(1, len(contents[1:]) + 2),
                                   tablefmt='fancy grid'))

                    break

            except FileNotFoundError:
                print(f"The file {Shoe.data_file_txt} is not found,")


if __name__ == '__main__':
    Shoe().read_data()
    Shoe().value_per_item()
