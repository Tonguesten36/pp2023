import os
import pickle
import threading

import tarfile as tar
import os.path as path

def __init__():
    pass

# Step1: Check if the save files (students, courses, marks) exist yet
#   If not then create these files, unless students.tar.gz already exists
# Step2: Extrall all data from students.tar.gz (if it exist)
# Step3: Once the program ends, do the following:
#   3.1: serialize all 3 lists of objects with pickles into binary files
#   3.2: combine all those files into a tar.gz file
# Step4: Exit
# Step5: When started again, repeat Step1


def serialize_objects(database, save_file):
    """
    Convert a list into a binary file

    Parameters
    -----------
    database: data you want to save to save_file
    save_file: file you want to save your data into

    Return None
    """
    with open(save_file, "wb") as sf:
        pickle.dump(database, sf)

def load_data(save_file, list_to_append_to):
    """
    Load data from a file and append them to a list

    Parameters
    -----------
    save_file: file that contain data you wish to extract
    list_to_append_to: list that you want to append the data (as objects) into
    
    Return None
    """
    # Open the save_file
    with open(save_file, 'rb') as f:
        # Read all data in the binary files
        unpickled_data = pickle.load(f)     

        # Append obj to the list_to_append_to
        try:
            for obj in unpickled_data:
                list_to_append_to.append(obj)
        except:
            return

def check_if_savefiles_not_exists(file_names):
    """
    Create new savefiles if student.tar.gz does not exist

    Parameter
    ----------
    file_names: list of file names (in strings)

    Return None
    """
    if path.exists("students.tar.gz") == False:
        for i in range(0, 3, 1):
            # Create a new file with specific name if it does not exist yet
            if path.exists(file_names[i]) == False:
                new_file = open(file_names[i], 'x')
                new_file.close()

def combine_all_to_tarfile(file_names):
    """
    Combine all data into a tar.gz file  

    Parameter
    ----------
    file_names: list of files that you want to combine into a tar.gz file

    Return None
    """
    # Create a new student.tar.gz file if it does not exist yet
    if path.exists("students.tar.gz") == False:
        new_tar_file = tar.open("students.tar.gz", "x:gz")
        new_tar_file.close()

    # Combine all three .txt files into a single tar.gz file
    with tar.open("students.tar.gz", "w:gz") as students_tar:
        for name in file_names:
            students_tar.add(name) 
            os.remove(name) # I should probably uses another module instead of os

def extract_tarfile(tar_file, file_names, students_list, courses_list, marks_list):
    """
    Extract all data from students.tar.gz  

    Parameters
    ----------
    students
    tar_file: the .tar.gz file that you want to extract data from
    file_names: list of files that you want to extract from tar_file
    students_list: list of student objects
    courses_list: list of course objects
    marks_list: list of mark objects

    Return None
    """
    # Check if the .tar.gz file exist
    if path.exists("students.tar.gz"):
        try:
            # Open the .tar.gz file and extract all data inside it
            # Once finished, the program will delete the .tar.gz file
            student_tar = tar.open(tar_file, "r:gz")
            for name in file_names:
                student_tar.extract(name)
            student_tar.close()
            os.remove("students.tar.gz")

            # Load all data from students.tar.gz into students_list, courses_list and marks_list
            load_data(file_names[0], students_list)
            load_data(file_names[1], courses_list)
            load_data(file_names[2], marks_list)
            return True
        except tar.ExtractError:
            return False