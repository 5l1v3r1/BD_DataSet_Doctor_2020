from sys import argv

def get_args():
    result = ""

    for i in range(len(argv)):
        if (argv[i] == "-p" or argv[i] == "--path") and i < len(argv) - 1:
            result = argv[i + 1]
        elif argv[i] == "-h" or argv[i] == "--help":
            return ""
    return result

def clean_entry(entry):
    entry = entry.split(',')
    entry = str("|".join(entry))
    return entry
