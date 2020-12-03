from Deliverable_Final.customeroption import dine_in
from Deliverable_Final.customeroption import take_out
from Deliverable_Final.customeroption import delivery
from Deliverable_Final.discount import Discount
def test_dinein_selection():   # Checks if the customer selected Dine-in option
    dinein_option_selected = dine_in().VerifyDineinSelection("Dine-in")
    assert dinein_option_selected == "Dine-in"

def test_takeout_selection():  #Checks if the customer selected takeout option
    takeout_option_selected = take_out().VerifyTakeOutSelection("Take-out")
    assert takeout_option_selected == "Take-out"

def test_delivery_selection():   # Checks if the customer selected delivery option
    delivery_option_selected = delivery().VerifyDeliverySelection("Delivery")
    assert delivery_option_selected == "Delivery"

