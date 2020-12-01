# Customer who choose Take-out option gets 10% discount on total order
from Deliverable_Final.discount import Discount

def test_discount_ten_percent():
    takeout_discount = Discount()
    calculated_discount = takeout_discount.VerifyDiscount(0.1)

    assert calculated_discount == 0.1 #discount should be 10%!