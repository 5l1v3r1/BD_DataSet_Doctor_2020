import parsing_functions
import display

def folder_analyze(entry, fd_to_review, row):
    if (parsing_functions.is_digit(entry)) == False:
        print("Analyzing : " + entry)
        print("Problem found : [Folder not digit]")
        display.write_row(fd_to_review, row)
        return 1
    return 0

def rm_line_analyze(entry):
    if len(entry) > 0 and entry == "1":
        print("Analyzing : " + entry)
        print("Problem found : [Delete]")
        return 1
    return 0