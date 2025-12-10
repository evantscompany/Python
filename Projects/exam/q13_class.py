
# account 클래스 정의 

class Account :
    def __init__(self,owner):
        self.owner = owner
        self.balance=0

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{self.owner}님 {amount}원 입금 완료.")
        else:
            print("입금 금액은 0원 이상이어야 합니다. ")

    def withdraw(self, amount):
        if amount>self.balance:
            print(f"{self.owner}님 잔액 부족! 현재 잔액 : {self.balance}")
        elif amount<=0:
            print("출금 금액은 0원 이상이어야 합니다.")
        else:
            self.balance-=amount
            print(f"{self.owner}님 {amount}원 출금 완료.")

    def show_balance(self):
        print(f"{self.owner}님의 현재 작액 : {self.balance}원")

    def add_interest(self,rate):
        self.balance*=(1+rate)
        print(f"{self.owner}님 잔액에 이자 적용 완료. 현재 잔액 : {self.balance:.2f}원")

acc1=Account("홍길동")
acc2=Account("김철수")


