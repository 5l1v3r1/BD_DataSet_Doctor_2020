import xlrd
import csv
import sys
import display
import tools
import parsing_functions
import parsing_disease
import analyze
import analyze_patient
import analyze_tech

def patient_analyze(age_entry, gender_entry, fd_to_review, row):
    if analyze_patient.age_analyze(age_entry, fd_to_review, row):
        return 1
    elif analyze_patient.gender_analyze(gender_entry, fd_to_review, row):
        return 1
    else:
        return 0

def doctor_disease_analyze(entries, fd_to_review, row):
    if analyze.known_disease_analyze(entries[0], fd_to_review, row):
        return 1
    if analyze.confident_rate_analyze(entries[1], fd_to_review, row):
        return 1
    if analyze.doctor_analyze(entries[2], fd_to_review, row):
        return 1
    if analyze.macroscopic_analyze(entries[3], fd_to_review, row):
        return 1
    return 0

def parsing(row, fd_good_set, fd_to_review):
    row_array = row.split(',')
    disease_doctor_analyze = [row_array[6], row_array[15], row_array[8], row_array[16]]

    if analyze_tech.rm_line_analyze(row_array[5]):
        return 0
    elif analyze_tech.folder_analyze(row_array[2], fd_to_review, row):
        return 1
    elif patient_analyze(row_array[10], row_array[11], fd_to_review, row):
        return 1
    else:
        if doctor_disease_analyze(disease_doctor_analyze, fd_to_review, row):
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