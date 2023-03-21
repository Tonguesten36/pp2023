import domains

def __init__():
    pass

# Load data from a .txt file and append them to a list
# - save_file: the .txt file that contain data you wish to extract
# - list_to_append_to: the list that you want to append the data (as objects) into
# - object_type: what kind of object do you want to create?
def load_data(save_file, list_to_append_to, object_type):
    # Open the save_file
    with open(save_file, 'r') as f:
        # Read all data in the .txt files
        content = f.readlines()     

        try:
            for row in content:
                # Split the data at the current row into individual elements
                sliced_data = row.split(',')

                # Create an object from domains package depend on the value of object_type
                if object_type == 's':
                    new_student = domains.Student(sliced_data[0], sliced_data[1], sliced_data[2])
                    list_to_append_to.append(new_student)
                elif object_type == 'c':
                    new_course = domains.Course(sliced_data[0], sliced_data[1])
                    list_to_append_to.append(new_course)
                elif object_type == 'm':
                    new_marks = domains.StudentMark(sliced_data[0], sliced_data[1], float(sliced_data[2]))
                    list_to_append_to.append(new_marks)
                else:
                    print("Wrong object_type!!!!!!!!!")
                    return
        except TypeError:
            #print(f"Shape of opened_file: {opened_file.shape}")
            return
