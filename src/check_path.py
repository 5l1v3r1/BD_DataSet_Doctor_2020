def check_path(id_img, folder_name, img_name):
    if (str(id_img) == str(folder_name) + '/' + str(img_name)):
        return True;
    return False;

print(check_path("0826/diwtMZnTzfrpIakV.jpg", "0826", "diwtMZnTzfrpIakV.jpg"))