
def help():
    print("\n\n\t\tUSAGE : python3 src/main.py --path [path_file_to_parse.xlsx]")
    print("\n\n\t\tFLAGS : -p [path_file.xlsx], --path [path_file.xlsx] : Specify the path to the dataset to analyze.\n\n\t\t\t-h, --help : Print the help message.")
    print("\n\n\t\tProject Architecture Need: \n\n\t\t\t\t.\n\t\t\t\t|\n\t\t\t\tsrc/\n\t\t\t\t    |\n\t\t\t\t    main.py\n\t\t\t\t|\n\t\t\t\tresult/\n\t\t\t\t|\n\t\t\t\tdataset/\n\t\t\t\t        |\n\t\t\t\t        [dataset_file.xlsx]")
    print("\n\n\t\tINSTALL NEED : pip3 install xlrd")
    print("\n\n\t\tCREDIT : This program is made by Sofian Belahouel to analyze input data files, for any question ask : sofian.belahouel@gmail.com\n\n")

def result(file, nb_rows, error):
    print("\n\n\n\tRESULT : \n\n\t\tFILE : " + file + "\n\n\t\t\tNUMBER LINE IN FILE : " + str(nb_rows) + "\n\n\t\t\t\tNUMBER OF CORRUPTED LINES : " + str(error) + "\n\n\t\t\t\tNUMBER OF VALID LINES : " + str(nb_rows - error) + "\n\n\t\t\t\tRATIO : " + str(((nb_rows - error) / nb_rows) * 100) + " %\n\n")