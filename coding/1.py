while True:
    print("\n--- 성별 확인 프로그램 (종료하려면 'exit' 입력) ---")
    a = input("성별을 입력해주세요 (male 혹은 female): ").strip().lower()

    if a == "male":
        print("\n결과: 남자입니다.")
    elif a == "female":
        print("\n결과: 여자입니다.")
    elif a == "exit" or a == "종료":
        print("프로그램을 종료합니다.")
        break  
    else:
        print("\n결과: 알 수 없는 성별입니다. 다시 입력해주세요.")
