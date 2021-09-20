from utils import hash, verify
from db import Db


def login():
    username = input('enter username: ')
    password = input('enter password: ')

    exists, err = Db.user_exists(username)

    if not err:
        if not exists:
            input('no account with given credentials')
        else:
            user, err = Db.get_user(username)
            if not err:
                user = user[0]
                salt = user[2]
                key = user[3]
                status = bool(user[4])

                if status:
                    input('your account was blocked (too many tries)!')
                elif verify(salt, key, password):
                    input('You are welcome!')
                else:
                    success, err = Db.increment_count(username)
                    if not success:
                        print(err)
                    else:
                        input('no account with given credentials (wrong pass)')
            else:
                print(err)
    else:
        print(err)


def register():
    username = input('enter username: ')
    password = input('enter password: ')

    salt, key = hash(password)

    success, err = Db.create_user(username, salt, key)

    if not success:
        print(f'user {username} already exists!')
    else:
        print(f'user {username} was successfully created!')


def start_menu():
    while True:
        print('[1] - login\n[2] - register\n[3] - exit')

        user_input = input('choose option: ')

        while user_input not in ('1', '2', '3'):
            user_input = input('choose option (1 - 3): ')

        if user_input == '1':
            login()
        elif user_input == '2':
            register()
        else:
            exit(0)


def main():
    Db.init()
    start_menu()


if __name__ == '__main__':
    main()
