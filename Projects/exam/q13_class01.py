from q13_class import Account

def main ():
    print("===은행 계좌 프로그램 ===")
    owner = input("계좌주 이름을 입력하세요 >>")
    account = Account(owner)

    while True:
        print("\n 원하는 작업을 선택하세요 : ")
        print("1 : 입금")
        print("2 : 출금")
        print("3 : 잔액확인")
        print("4 : 이자적용")
        print("5 : 종료")

        choice = input("선택(1~5) : ")

        if choice =="1":
            amount = int(input(" 입금할 금액을 입력하세요 : "))
            account.deposit(amount)
        elif choice =="2":
            amount = int(input("출금할 금액을 입력하세요 : "))
            account.withdraw(amount)
        elif choice=="3":
            account.show_balance()
        elif choice=="4":
            rate = float(input("이자율을 입력하세요 (예 : 0.03): "))
            account.add_interest(rate)
        elif choice=='5':
            print("프로그램을 종료합니다")
            break
        else:
            print("잘못된 입력 입니다. 1~5 중 선택하세요")

main()