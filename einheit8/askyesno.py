def ask_yes_or_no_question(question_text):
    # stelle dem Benutzer eine Frage
    # rueckgabewert: True / False

    while True:
        answer = raw_input(question_text)
        answer = answer.lower()

        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print 'invalid answer. Enter yes or no'