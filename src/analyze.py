import parsing_functions
import parsing_disease
import display

def known_disease_analyze(entry, fd_to_review, row):
    if parsing_disease.verify_main_class(entry) == False:
        print("Analyzing : " + entry)
        print("Problem found : [main disease not in known disease]")
        display.write_row(fd_to_review, row)
        return 1
    return 0

def doctor_analyze(entry, fd_to_review, row):
    if parsing_functions.is_empty(entry) == True:
        print("Analyzing : " + entry)
        print("Problem found : [Doctor name not found]")
        display.write_row(fd_to_review, row)
        return 1
    return 0

def confident_rate_analyze(entry, fd_to_review, row):
    if parsing_functions.is_contain_between(entry, 0, 100) == False:
        print("Analyzing : " + entry)
        print("Problem found : [Confident Rate Error]")
        display.write_row(fd_to_review, row)
        return 1
    return 0

def macroscopic_analyze(entry, fd_to_review, row):
    if parsing_functions.is_macro(entry) == False:
        print("Analyzing : " + entry)
        print("Problem found : [Is Macro entry Error]")
        display.write_row(fd_to_review, row)
        return 1
    return 0