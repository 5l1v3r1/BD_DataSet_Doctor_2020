import xlrd
import csv
import sys
import display
import tools
import parsing_functions
import parsing_disease



def parsing(row, fd_good_set, fd_to_review):
    row_array = row.split(',')
    is_clean = False

    if len(row_array[5]) > 0 and row_array[5] == "1":
        print("Analyzing : " + row_array[5])
        print("Problem found : [Delete]")
        return 1
    if (parsing_functions.is_digit(row_array[2])) == False:
        print("Analyzing : " + row_array[2])
        print("Problem found : [Folder not digit]")
        display.write_row(fd_to_review, row)
        return 1
    if parsing_disease.verify_main_class(row_array[6]) == False:
        print("Analyzing : " + row_array[6])
        print("Problem found : [main disease not in known disease]")
        display.write_row(fd_to_review, row)
        return 1
    if parsing_functions.is_empty(row_array[8]) == True:
        print("Analyzing : " + row_array[8])
        print("Problem found : [Doctor name not found]")
        display.write_row(fd_to_review, row)
        return 1
    if parsing_functions.is_digit(row_array[10]) == False and row_array[10] != "":
        print("Analyzing : " + row_array[10])
        print("Problem found : [Age Error]")
        display.write_row(fd_to_review, row)
        return 1
    if parsing_functions.is_gender(row_array[11]) == False:
        print("Analyzing : " + row_array[11])
        print("Problem found : [Gender Error]")
        display.write_row(fd_to_review, row)
        return 1
    if parsing_functions.is_contain_between(row_array[15], 0, 100) == False:
        print("Analyzing : " + row_array[15])
        print("Problem found : [Confident Rate Error]")
        display.write_row(fd_to_review, row)
        return 1
    if parsing_functions.is_macro(row_array[16]) == False:
        print("Analyzing : " + row_array[16])
        print("Problem found : [Is Macro entry Error]")
        display.write_row(fd_to_review, row)
        return 1
    display.write_row(fd_good_set, row)
    print("Analyzing :\nProblem found : Notting")
    return 0

def reader(dataset_path, fd_good_set, fd_to_review):
    wb = xlrd.open_workbook(dataset_path)
    sh = wb.sheet_by_name('Sheet1')
    cur_row = ""
    error = 0;

    for i in range(sh.nrows):
        for n in range(sh.ncols):
            cur_row = cur_row + tools.clean_entry(str(sh.row_values(i)[n])) + ','
        if i == 0:
            display.write_row(fd_good_set, cur_row)
            display.write_row(fd_to_review, cur_row)
        else:
            print("\n\n\nSend row " + str(i))
            error = error + parsing(cur_row, fd_good_set, fd_to_review)
        cur_row = ""
    del wb
    display.result(dataset_path, sh.nrows, error)


def main():
    dataset_path = "dataset/Khoi-task-6-7-20.xlsx"

    if len(sys.argv) > 1:
        dataset_path = tools.get_args()
        if dataset_path == "":
            display.help()
            return 1
        else:
            fd_good_set = open("result/good_set.csv", "w")
            fd_to_review = open("result/to_review.csv", "w")
            reader(dataset_path, fd_good_set, fd_to_review)
            fd_good_set.close()
            fd_to_review.close()
            return 0
    else:
        display.help()

main()