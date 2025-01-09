# TRANSACTION CREATION

class new:

    # CREATE TRANSACTION

    '''

    format for data
    
    Data = {
        Merchant : str
        Total : double
        Date : str
        Purchase Type : str

            - Food
            - Entertainment
            - Bills
            - Wire Transaction
            - ATM Transactions

        MiscData : {}
        PurchaseBv : True | False
        ProcessStatus : True | False
    }
    
    '''

    # CONSTRUCTOR

    def __init__(self, data):
        self.Merchant = data["Merchant"]
        self.Total = data["Total"]
        self.Date = data["Date"]
        self.MiscData = data["MiscData"]
        self.Purchase = data["PurchaseBv"]
        self.Processed = data["ProcessStatus"]

        return self

    # METHODS

    #self.Total -> newtotal
    def change_Total(self,new_total):
        self.Total = new_total

    #self -x-> none
    def Destroy(self):
        self = None
        