from storage import Storage
from user import User
from todo import Todo

class AppController:
    def __init__(self):
        self.storage = Storage()
        self.users = self.storage.load()
        self.current_user = None

    # ---------------- 사용자 기능 ------------------

    def signup(self):
        username = input("새 사용자 이름: ")
        if username in self.users:
            print("❌ 이미 존재하는 아이디입니다.")
            return

        password = input("비밀번호: ")
        self.users[username] = User(username, password)
        self.storage.save(self.users)
        print("✔ 회원가입 완료!\n")

    def login(self):
        username = input("아이디: ")
        password = input("비밀번호: ")

        user = self.users.get(username)
        if not user or not user.check_password(password):
            print("❌ 로그인 실패\n")
            return

        self.current_user = user
        print(f"✔ {username}님 환영합니다!\n")

    # ---------------- Todo 기능 ------------------

    def add_todo(self):
        title = input("할 일 제목: ")
        priority = input("우선순위 (low/normal/high): ")
        deadline = input("마감일 (YYYY-MM-DD 또는 엔터): ")
        category = input("카테고리: ")

        todo = Todo(title, priority, deadline or None, category)
        self.current_user.todos.append(todo)
        self.storage.save(self.users)
        print("✔ 할 일 추가 완료!\n")

    def list_todos(self):
        todos = self.current_user.todos
        if not todos:
            print("할 일이 없습니다.\n")
            return

        print("\n==== 나의 할 일 목록 ====")
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo}")
        print()

    def complete_todo(self):
        self.list_todos()
        idx = int(input("완료할 번호: ")) - 1

        if 0 <= idx < len(self.current_user.todos):
            self.current_user.todos[idx].complete()
            self.storage.save(self.users)
            print("✔ 완료 처리됨!\n")
        else:
            print("번호 오류!\n")

    def delete_todo(self):
        self.list_todos()
        idx = int(input("삭제할 번호: ")) - 1

        if 0 <= idx < len(self.current_user.todos):
            del self.current_user.todos[idx]
            self.storage.save(self.users)
            print("🗑 삭제 완료!\n")
        else:
            print("번호 오류!\n")

    # ---------------- 메인 루프 ------------------

    def run(self):
        while True:
            if not self.current_user:
                print("\n===== 메인 메뉴 =====")
                print("1. 회원가입")
                print("2. 로그인")
                print("3. 종료")
                menu = input("선택: ")

                if menu == "1": self.signup()
                elif menu == "2": self.login()
                elif menu == "3": break
                else: print("잘못된 입력!\n")

            else:
                print("\n===== Todo 메뉴 =====")
                print("1. 할 일 추가")
                print("2. 할 일 목록 보기")
                print("3. 할 일 완료 처리")
                print("4. 할 일 삭제")
                print("5. 로그아웃")
                menu = input("선택: ")

                if menu == "1": self.add_todo()
                elif menu == "2": self.list_todos()
                elif menu == "3": self.complete_todo()
                elif menu == "4": self.delete_todo()
                elif menu == "5":
                    self.current_user = None
                    print("로그아웃 완료\n")
                else:
                    print("잘못된 입력!\n")
