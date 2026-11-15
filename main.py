"""기계설계 기초 퀴즈 게임."""


def show_menu():
    """게임 메뉴를 출력합니다."""
    print("\n" + "=" * 40)
    print("       기계설계 기초 퀴즈 게임")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def main():
    """메뉴를 반복 실행하고 사용자 선택을 처리합니다."""

    while True:
        show_menu()

        try:
            choice = input("메뉴 선택 (1-5): ").strip()

            if not choice:
                print("입력값이 비어 있습니다.")
                continue

            number = int(choice)

            if number == 1:
                print("퀴즈 풀기 기능은 구현 예정입니다.")

            elif number == 2:
                print("퀴즈 추가 기능은 구현 예정입니다.")

            elif number == 3:
                print("퀴즈 목록 기능은 구현 예정입니다.")

            elif number == 4:
                print("점수 확인 기능은 구현 예정입니다.")

            elif number == 5:
                print("게임을 종료합니다.")
                break

            else:
                print("1부터 5까지의 숫자를 입력하세요.")

        except ValueError:
            print("숫자만 입력할 수 있습니다.")

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 안전하게 종료합니다.")
            break


if __name__ == "__main__":
    main()
