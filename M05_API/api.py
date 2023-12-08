"""File containing your first REST API!"""

from datacademy.modules import Module05
from fastapi import FastAPI

# DO NOT EDIT: Initialize module and load customers
module = Module05()
customers = module.load_customers()

# DO NOT EDIT: Initialize FastAPI
app = FastAPI()


"""
API GET requests
"""


# Example GET request
@app.get("/get-customer/{customer_id}")
def get_customer(customer_id: int) -> dict[str, str]:
    """Get a customer by its ID.

    Args:
        customer_id (int): Customer ID.

    Returns:
        dict[str, str]: Customer details.
    """
    if customer_id not in customers:
        return {"Error": "Customer does not exists yet."}
    return customers[customer_id]


# TODO: Create GET request with end point: "/get-customer-by-name/{last_name}"



# TODO: Create GET request with end point: "/get-customers/"



"""
API POST requests
"""


# Example POST request
@app.post("/create-customer/{customer_id}")
def create_customer(customer_id: int, first_name: str, last_name: str, address: str) -> dict[str, str]:
    """Create a new customer.

    Args:
        customer_id (int): Customer ID.
        first_name (str): First name.
        last_name (str): Last name.
        address (str): Address.

    Returns:
        dict[str, str]: Customer details.
    """
    if customer_id in customers:
        return {"Error": f"customerId already used, next id available is: {max(customers.keys())+1}."}

    if (customer_id - max(customers.keys())) > 1:
        return {"Error": f"customerId do not fit neatly together, next id available is: {max(customers.keys())+1}."}

    customers[customer_id] = {"first_name": first_name, "last_name": last_name, "address": address}
    return customers[customer_id]


# TODO: Create POST request with end point: "/create-customer-auto-increment/"


"""
API PUT requests
"""

# Example PUT  request
@app.put("/update-customer-address/{customer_id}")
def update_customer_address(customer_id: int, address: str) -> dict[str, str]:
    """Update the address of a customer.

    Args:
        customer_id (int): Customer ID.
        address (str): Customer address.

    Returns:
        dict[str, str]: Updated customer.
    """
    if customer_id not in customers:
        return {"Error": "Customer does not exists."}

    customers[customer_id]["address"] = address
    return customers[customer_id]


# TODO: Create PUT request with end point: "/update-customer-address-by-name/"



"""
API DELETE requests
"""

# Example DELETE  request
@app.delete("/delete-customer/{customer_id}")
def delete_customer(customer_id: int) -> dict[str, str]:
    """Delete a customer.

    Args:
        customer_id (int): Customer ID.

    Returns:
        dict[str, str]: Error or success message.
    """
    if customer_id not in customers:
        return {"Error": "Customer does not exists."}

    del customers[customer_id]
    return {"Message": f"Customer {customer_id} deleted successfully."}


# TODO: Create DELETE request with end point: "/delete-customer-by-name/"