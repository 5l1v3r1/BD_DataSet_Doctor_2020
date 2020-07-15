import parsing_functions
import display

def age_analyze(entry, fd_to_review, row):
    if parsing_functions.is_digit(entry) == False and entry != "":
        print("Analyzing : " + entry)
        print("Problem found : [Age Error]")
        display.write_row(fd_to_review, row)
        return 1
    return 0

def gender_analyze(entry, fd_to_review, row):
    if parsing_functions.is_gender(entry) == False:
        print("Analyzing : " + entry)
        print("Problem found : [Gender Error]")
        display.write_row(fd_to_review, row)
        return 1
    return 0