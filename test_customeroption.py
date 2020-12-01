from Deliverable_Final.customeroption import dine_in
from Deliverable_Final.customeroption import take_out
from Deliverable_Final.customeroption import delivery
from Deliverable_Final.discount import Discount
def test_dinein_selection():
    dinein_option_selected = dine_in().VerifyDineinSelection("Dine-in")
    assert dinein_option_selected == "Dine-in"

def test_takeout_selection():
    takeout_option_selected = take_out().VerifyTakeOutSelection("Take-out")
    assert takeout_option_selected == "Take-out"

def test_delivery_selection():
    delivery_option_selected = delivery().VerifyDeliverySelection("Delivery")
    assert delivery_option_selected == "Delivery"

