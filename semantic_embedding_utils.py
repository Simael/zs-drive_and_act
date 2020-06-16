import os
import numpy as np


def create_dawa(class_names_to_load, path_to_dawa):
    # Set the paths to the attribute information
    path_to_attribute_names = os.path.join(path_to_dawa, 'attributes.txt')
    path_to_class_names = os.path.join(path_to_dawa, 'classes.txt')
    path_to_attribute_matrix = os.path.join(path_to_dawa, 'attribute_matrix.csv')

    # Load the attributes into a numpy matrix
    attribute_matrix = np.loadtxt(open(path_to_attribute_matrix, "rb"), delimiter=",")

    # Load the attribute names into a list
    with open(path_to_attribute_names) as f:
        attribute_names = f.readlines()
    attribute_names = [x.strip() for x in attribute_names]

    # Load the class names into a list
    with open(path_to_class_names) as f:
        class_names = f.readlines()
    class_names = [x.strip() for x in class_names]

    # Make sure the matrix dimensions match the list
    assert len(attribute_names) == attribute_matrix.shape[1] and len(class_names) == \
           attribute_matrix.shape[0]

    # Gather the embeddings specified in the class_names_to_load
    semantic_attributes = []
    for current_class in class_names_to_load:
        current_class_index = class_names.index(current_class)
        current_semantic_attribute = attribute_matrix[current_class_index]
        semantic_attributes.append(current_semantic_attribute)

    return semantic_attributes


if __name__ == '__main__':
    # Example code for loading the attributes.

    # Create list of activity names for that embeddings should be loaded.
    # In this case, we load all activities.
    with open('./attributes/classes.txt') as f:
        class_names_to_load = f.readlines()
    class_names_to_load = [x.strip() for x in class_names_to_load]

    # Set up the semantic space: Driver activities with Attribtutes
    dawa = create_dawa(class_names_to_load=class_names_to_load, path_to_dawa='./attributes/')

    # You are ready to go, the ordering of the attributes corresponds to the ordering
    # in the supplied class_names_to_load
    print("There are {} classes with {} attributes respectively.\n".format(len(class_names_to_load),
                                                                         dawa[0].shape[0]))

    print("The activity \"{}\" has the following attribute representation:".format(
        class_names_to_load[0]))
    print(dawa[0])
