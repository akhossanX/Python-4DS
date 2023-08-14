# ft_package

**ft_package** is a Python package that provides a utility function to count occurrences of an item in a list.

## Installation

You can install **ft_package** using `pip`:

```bash
pip install ft_package
```

## Usage

To use the `count_in_list` function from the **ft_package**, follow these steps:

1. Install the package using `pip`:

    ```bash
    pip install ft_package
    ```

2. Import the function in your Python code:

    ```python
    from ft_package import count_in_list
    ```

3. Call the `count_in_list` function with a list and an item you want to count:

    ```python
    lst = ["toto", "tata", "toto"]
    item1 = "toto"
    item2 = "tutu"

    count1 = count_in_list(lst, item1)
    count2 = count_in_list(lst, item2)

    print(f"Count of {item1}: {count1}")  # Output: Count of toto: 2
    print(f"Count of {item2}: {count2}")  # Output: Count of tutu: 0
    ```

The `count_in_list` function returns the number of occurrences of the specified item in the list.

Remember to replace `lst`, `item1`, and `item2` with your own list and item values.

## License
This project is licensed under the MIT License - 
see the **LICENSE.txt** file for details.