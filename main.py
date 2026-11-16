"""기계설계 기초 퀴즈 게임."""

import json
import os
from pathlib import Path


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






def play_quiz(quizzes):
    """등록된 퀴즈를 출제하고 최종 점수를 반환합니다."""
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return 0

    total = len(quizzes)
    correct = 0

    print(f"\n퀴즈를 시작합니다! 총 {total}문제")

    for number, quiz in enumerate(quizzes, start=1):
        print("\n" + "-" * 40)
        print(f"[문제 {number}/{total}]")

        quiz.display()

        answer = get_number_input("정답 입력 (1-4): ", 1, 4)

        if quiz.check_answer(answer):
            print("정답입니다!")
            correct += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

    score = round(correct / total * 100)

    print("\n" + "=" * 40)
    print(f"결과: {total}문제 중 {correct}문제 정답!")
    print(f"최종 점수: {score}점")
    print("=" * 40)

    return score




def get_text_input(prompt):
    """빈 문자열을 허용하지 않는 텍스트 입력 함수입니다."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("입력값이 비어 있습니다. 다시 입력하세요.")


def add_quiz(quizzes):
    """새로운 퀴즈를 입력받아 목록에 추가합니다."""
    print("\n새로운 퀴즈를 등록합니다.")

    question = get_text_input("문제 입력: ")

    choices = []

    for number in range(1, 5):
        choice = get_text_input(f"선택지 {number}: ")
        choices.append(choice)

    answer = get_number_input("정답 번호 (1-4): ", 1, 4)

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)

    print("새로운 퀴즈가 등록되었습니다!")
    print(f"현재 등록된 퀴즈: {len(quizzes)}개")

    return new_quiz




def list_quizzes(quizzes):
    """등록된 퀴즈 목록을 출력합니다."""
    print()
    print("=" * 40)
    print(f"등록된 퀴즈 목록 (총 {len(quizzes)}개)")
    print("=" * 40)

    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    for number, quiz in enumerate(quizzes, start=1):
        print(f"[{number}] {quiz.question}")

    print("=" * 40)




def update_best_score(score, best_score):
    """새로운 점수와 기존 최고 점수를 비교합니다."""
    if best_score is None or score > best_score:
        print("새로운 최고 점수입니다!")
        return score

    return best_score


def show_score(best_score):
    """현재 최고 점수를 출력합니다."""
    print()
    print("=" * 40)

    if best_score is None:
        print("아직 퀴즈를 푼 기록이 없습니다.")
    else:
        print(f"최고 점수: {best_score}점")

    print("=" * 40)


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self):
        self.state_path = Path(__file__).resolve().parent / "state.json"
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.load_state()


    def _read_state(self, path):
        """JSON 구조를 검증하고 퀴즈 객체로 변환합니다."""
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("저장 데이터는 객체여야 합니다.")

        quiz_data = data["quizzes"]
        best_score = data["best_score"]

        if not isinstance(quiz_data, list):
            raise ValueError("퀴즈 목록 형식 오류")

        if best_score is not None and (
            type(best_score) is not int
            or not 0 <= best_score <= 100
        ):
            raise ValueError("최고 점수 형식 오류")

        quizzes = []
        for item in quiz_data:
            if not isinstance(item, dict):
                raise ValueError("문제 데이터 형식 오류")
            quizzes.append(
                Quiz(item["question"], item["choices"], item["answer"])
            )

        return quizzes, best_score

    def save_state(self):
        """원자적으로 저장하고 최신 정상 데이터를 백업합니다."""
        if getattr(self, "_state_load_blocked", False):
            print("손상된 저장 파일 보호: 자동 저장을 중단합니다.")
            return False

        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }

        temp_path = self.state_path.with_suffix(".json.tmp")
        backup_path = self.state_path.with_suffix(".json.bak")
        backup_temp = self.state_path.with_suffix(".json.bak.tmp")

        try:
            with temp_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.write("\n")

            os.replace(temp_path, self.state_path)

            # 정상 저장된 데이터의 백업을 원자적으로 갱신
            backup_temp.write_bytes(self.state_path.read_bytes())
            os.replace(backup_temp, backup_path)
            return True

        except OSError as error:
            print(f"데이터 저장 또는 백업 실패: {error}")
            return False

    def load_state(self):
        """주 파일을 우선 읽고 손상되면 백업을 복원합니다."""
        self._state_load_blocked = False

        backup_path = self.state_path.with_suffix(".json.bak")

        if not self.state_path.exists() and not backup_path.exists():
            print("저장된 데이터가 없어 기본 퀴즈를 사용합니다.")
            return

        for candidate in (self.state_path, backup_path):
            if not candidate.exists():
                continue

            try:
                quizzes, best_score = self._read_state(candidate)

                if candidate == backup_path:
                    restore_temp = self.state_path.with_suffix(
                        ".json.restore.tmp"
                    )
                    try:
                        restore_temp.write_bytes(backup_path.read_bytes())
                        os.replace(restore_temp, self.state_path)
                        print("백업 파일에서 저장 데이터를 복구했습니다.")
                    except OSError as error:
                        self._state_load_blocked = True
                        print(f"백업 복원 실패: {error}")
                        print("자동 저장을 차단합니다.")

                self.quizzes = quizzes
                self.best_score = best_score
                print(
                    f"저장된 데이터를 불러왔습니다. "
                    f"(퀴즈 {len(quizzes)}개)"
                )
                return

            except (
                OSError, UnicodeError, json.JSONDecodeError,
                ValueError, TypeError, KeyError
            ) as error:
                print(f"데이터 불러오기 실패 ({candidate.name}): {error}")

        self._state_load_blocked = True
        print("정상적인 저장 파일이 없습니다.")
        print("원본 보호를 위해 자동 저장을 차단합니다.")
        print("기본 퀴즈는 임시로 사용할 수 있습니다.")

    def play(self):
        """퀴즈를 진행하고 최고 점수를 갱신합니다."""
        if not self.quizzes:
            play_quiz(self.quizzes)
            return

        score = play_quiz(self.quizzes)
        self.best_score = update_best_score(
            score, self.best_score
        )
        self.save_state()

    def add(self):
        """새로운 퀴즈를 등록하고 저장합니다."""
        add_quiz(self.quizzes)
        self.save_state()

    def list_all(self):
        """등록된 퀴즈 목록을 출력합니다."""
        list_quizzes(self.quizzes)

    def show_best_score(self):
        """최고 점수를 출력합니다."""
        show_score(self.best_score)


    def run(self):
        """메뉴를 반복 실행하고 안전하게 종료합니다."""
        try:
            while True:
                show_menu()

                number = get_number_input(
                    "메뉴 선택 (1-5): ", 1, 5
                )

                if number == 1:
                    self.play()
                elif number == 2:
                    self.add()
                elif number == 3:
                    self.list_all()
                elif number == 4:
                    self.show_best_score()
                elif number == 5:
                    print("게임을 종료합니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 안전하게 종료합니다.")

        finally:
            self.save_state()


def main():
    """QuizGame 객체를 생성하고 실행합니다."""
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()
