import Classes.Event as Event
import datetime as date

# ACCOUNT CLASS

class new:

    # CONSTRUCTOR

    '''
    
        name : str
        Initial_Deposit : double

    '''

    def __init__(self,Name,Inital_Deposit):

        # PROPERTIES
        self.Name = Name
        self.Balance = 0 + Inital_Deposit
        self.AccountID = Name
        self.AccountCreationTime = 0
        self.Date = date.today()

        # CALLBACKS
        onBalanceEvent = Event()
        onTransactionEvent = Event()
        
        # TABLES
        self.Transactions = {}
        self.Balance_History = {}

        # EVENTS

        @onBalanceEvent.on
        def onBalanceChanged(balance):
            print('New Balance: {balance}')

        @onTransactionEvent.on
        def onTransactionCreated(transaction):
            print('New Transaction: {transaction}')


    # METHODS

    #self.bal -> new_bal
    def Set_Bal(self, new_balance):
        self.Balance = new_balance

    #self.bal -+-> new_bal
    def Increment_Bal(self, additional_balance):
        self.Balance += additional_balance

    # insert transaction -> self.Transactions
    def Add_Transaction(self, UnqiueID, transaction):
        self.Transactions[UnqiueID] = transaction
        return self.Transactions[UnqiueID]

    # delete transaction -x-> none
    def Remove_Transaction(self,UnqiueID):
        self.Transactions[UnqiueID] = None

    # withdraw money -> self.Balance - amount
    def Withdraw(self, amount):
        self.Balance -= amount

    # deposit money -> self.Balance + amount
    def Deposit(self, amount):
        self.Balance += amount