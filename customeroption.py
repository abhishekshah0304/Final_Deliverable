# Takes customer selection as an input (dine-in, takeout, delivery)
class dine_in:

    def VerifyDineinSelection(self, customerselection):
        covid_form = 13    # All 13 questions in covid assessment form should have an answer 'no' in order to dine-in
        if covid_form != 13:
            print(" You're not allowed to dine-in")
            return False
        else:
            return "Dine-in"


class take_out:

    def VerifyTakeOutSelection(self, customerselection):
        return "Take-out"


class delivery:

    def VerifyDeliverySelection(self, customerselection,driverinfo):
        driver_name = ""
        driver_number = ""
        driver_info = driver_name + driver_name
        return "Delivery" + driver_info
