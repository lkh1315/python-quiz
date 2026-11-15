"""기계설계 기초 퀴즈 게임."""




class Quiz:
    """하나의 퀴즈 문제를 표현하는 클래스."""

    def __init__(self, question, choices, answer):
        """문제, 선택지, 정답을 초기화합니다."""
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 비어 있을 수 없습니다.")

        if (
            not isinstance(choices, list)
            or len(choices) != 4
            or any(not isinstance(choice, str) or not choice.strip()
                   for choice in choices)
        ):
            raise ValueError("선택지는 비어 있지 않은 문자열 4개여야 합니다.")

        if type(answer) is not int or not 1 <= answer <= 4:
            raise ValueError("정답 번호는 1부터 4까지여야 합니다.")

        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        """퀴즈 문제와 선택지를 출력합니다."""
        print(f"\n문제: {self.question}")

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        """입력한 번호가 정답인지 확인합니다."""
        return self.answer == user_answer

    def to_dict(self):
        """JSON 저장을 위한 딕셔너리로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }




def create_default_quizzes():
    """기계설계 기초 퀴즈 5개를 생성합니다."""
    return [
        Quiz(
            "베어링의 주요 역할은 무엇인가?",
            [
                "회전축 지지 및 마찰 감소",
                "절삭 공구 냉각",
                "전압 제어",
                "공압 생성",
            ],
            1,
        ),
        Quiz(
            "볼트의 주요 기능은 무엇인가?",
            [
                "유체 압력 측정",
                "기계 부품 체결",
                "회전 속도 검출",
                "열에너지 전달",
            ],
            2,
        ),
        Quiz(
            "기계제도에서 치수공차란 무엇인가?",
            [
                "부품의 표면 거칠기",
                "도면의 축척 비율",
                "허용되는 치수의 변동 범위",
                "재료의 인장강도",
            ],
            3,
        ),
        Quiz(
            "CNC는 무엇을 의미하는가?",
            [
                "Computer Network Control",
                "Central Numeric Calculation",
                "Computer Normal Cutting",
                "Computer Numerical Control",
            ],
            4,
        ),
        Quiz(
            "일반적인 공압 실린더의 구동 에너지는 무엇인가?",
            [
                "압축공기",
                "작동유",
                "전기 자기장",
                "증기",
            ],
            1,
        ),
    ]




def get_number_input(prompt, min_value, max_value):
    """지정한 범위의 정수를 입력받습니다."""
    while True:
        value = input(prompt).strip()

        if not value:
            print("입력값이 비어 있습니다.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("숫자만 입력할 수 있습니다.")
            continue

        if min_value <= number <= max_value:
            return number

        print(f"{min_value}부터 {max_value}까지의 숫자를 입력하세요.")


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
            number = get_number_input("메뉴 선택 (1-5): ", 1, 5)

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

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 안전하게 종료합니다.")
            break


if __name__ == "__main__":
    main()
