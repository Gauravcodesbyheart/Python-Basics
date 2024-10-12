class account:
    def __init__(self,account_no,account_password):
        self.account_no = account_no
        self.__account_password = account_password 
          # here password is made private so it wont work publicly means nothing printed in the loop
    
    
    def reset_password(self):
        print(self.__account_password)


account1 = account(12345,"abcde")
print(account1.account_no,"\n")
print(account1.reset_password())
print(account1.__account_password)