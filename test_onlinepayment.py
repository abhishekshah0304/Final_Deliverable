from Deliverable_Final.onlinepayment import MobilePayment
from Deliverable_Final.onlinepayment import OnlinePayment

def test_creditcardnumber():
    creditcard_number = [
                5455789478554125,
                7894587463214587,
                4512567844852387,
                1236547885479658,
                ]
    payment_method = OnlinePayment()

    for creditnumber in creditcard_number:
        assert payment_method.VerifyCardNumber(creditnumber) == True  #Credit card number should be verified as valid

def test_expdate():
    exp_date = [
        '2/23',
        '3/11',
        '4/04',
    ]

    credit_exp_date = OnlinePayment()

    for exdate in exp_date:
        assert credit_exp_date.VerifyExpDate(exdate) == True  # Verify expiry date of credit card


def test_cvc_number():
    cvc_number = [
        123,
        234,
        743,
        895,
    ]

    credit_cvc_number = OnlinePayment()

    for cvcnumber in cvc_number:
        assert credit_cvc_number.VerifyCVCNumber(cvcnumber) == True  # Verify CVC number of credit card


def test_mobile_number():
    mobile_number = [
        9052554787,
        6479589874,
        4165854789,
        4378954123,
    ]

    mobile_phone_number = MobilePayment()

    for mobnumber in mobile_number:
        assert mobile_phone_number.VerifyPhoneNumber(mobnumber) == True   # Checks whether the mobile number in connected to the online payent system


def test_email_address():
    email_address = [
        'fdsei@gmail.com',
        'dan@outlook.com',
        'derek@live.com',
    ]

    mobile_email_address = MobilePayment()
    for emailaddress in email_address:
        assert mobile_email_address.VerifyEmailAddress(emailaddress) == True # Checks whether the email address is right