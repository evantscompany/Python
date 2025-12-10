class BankAccount: # 간단한 은행 계좌 클래스
    def _init_(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount<=0:
            print('입금액은 0보다 커야 합니다.')
            return
        self.balance +=amount
        print(f"{amount}원 입금 완료! 현재 잔액 : {self.balance}원" )

    def withdraw(self,amount):
        if amount<=0:
            print("출금액은 0보다 커야 합니다.")
            return
        if amount>self.balance:
            print("잔액 부족!") 
            return
        self.balance -=amount
        print(f"amount원 출금 완료! 현재 잔액 : {self.balance}")

    def show_balance(self):
        print(f" 현재잔액 : {self.balance}원")    


def main():
    name =input("계좌 소유자 이름을 입력하세요:")
    account = BankAccount(name)

    while True:
        print("\n===== 은행 메뉴 =====")
        print("1. 입금")
        print("2. 출금")
        print("3. 잔액 조회")
        print("4. 종료")
        menu = input("메뉴선택 : ")

    if menu == "1" :
        money = int(input("입금할 금액 : "))
        account.deposit(money)

    elif menu =="2":
        money = int(input("출금할 금액 : "))
        account.withdraw(money)

    elif menu == "3":
        account.show_balance()

    elif menu == "4":
        print("프로그램 종료")
        
    
    
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")



if __name__=="__main__":
    main()




