
import xlrd
import csv
import sys
import display
import tools
import parsing_functions
import check_path

def write_row(fd, row):
    a=0

def parsing(row, fd_good_set, fd_to_review):
    row_array = row.split(',')
    is_clean = False

    if len(row_array[5]) > 0 and row_array[5] == "1":
        return 0
    if (parsing_functions.is_digit(2)) == False:
        write_row(fd_to_review, row)
        return 0
    if (check_path.check_path(row_array[1], row_array[2], row_array[4]) == False):
        write_row(fd_to_review, row)
        return 0
    print(row_array)


def reader(dataset_path, fd_good_set, fd_to_review):
    wb = xlrd.open_workbook(dataset_path)
    sh = wb.sheet_by_name('Sheet1')
    nb_rows = sh.nrows
    nb_columns = sh.ncols
    cur_row = ""

    for i in range(2):#nb_rows):
        for n in range(nb_columns):
            cur_row = cur_row + str(sh.row_values(i)[n]) + ','
        parsing(cur_row, fd_good_set, fd_to_review)
        cur_row = ""

def buff_file(dataset_path):
    wb = xlrd.open_workbook(dataset_path)
    sh = wb.sheet_by_name('Sheet1')
    file = ""
    cur_row = ""
    rows = sh.nrows
    columns = sh.ncols

    for i in range(rows):
        for n in range(columns):
            cur_row = cur_row + str(sh.row_values(i)[n]) + ','
        file = file + cur_row + '\n'
        cur_row = ""
    return file

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
            # buff_file(dataset_path)
            reader(dataset_path, fd_good_set, fd_to_review)
            fd_good_set.close()
            fd_to_review.close()
            return 0
    else:
        display.help()

main()