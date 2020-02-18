from utils import expand_contractions


def main():
    user_text = input("Type a sentence:")
    expanded_text = expand_contractions(user_text)
    print(f"The expanded form of << {user_text} >> is:")
    print(expanded_text)


if __name__ == "__main__":
    main()
