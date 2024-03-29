#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Varun Keerthy
# DATE CREATED: 19/08/2019
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}
    filename_list = listdir(image_dir)

    # Fix filename_list to pop out config files that has file names starts with dot
    filename_list = list(filter(lambda name: not(name.startswith('.')), filename_list))


    def filename_with_underscore(filename, labels_list):
        """
        Method to process filenames containing underscores
        Parameters:
            filename - From the list of filenames
            labels_list - List under construction for labels
        Returns:
            labels_list
        """
        if "_" in filename:
            pet_full_name = filename.lower().split("_")
            pet_name = ""
            for word in pet_full_name:
                # Now call to check if the word contains str with dot extension
                word = filename_with_extension(word)
                if word.isalpha():
                    pet_name += word + " "
            pet_name = pet_name.strip()
            labels_list.append(pet_name)
        return labels_list

    def filename_with_extension(filename):
        """
        Method to process filenames containing extensions
        Parameters:
            filename - From the list of filenames
        Returns:
            filename - Processed filename without extension
        """
        pet_full_name = ""
        if "." in filename:
            pet_full_name = filename.lower().split(".")[0]
        else:
            pet_full_name = filename
        return pet_full_name

    def get_labels(filename_list):
        labels_list = []
        for filename in filename_list:
            if "_" in filename:
                # Now call utility to process str with underscores
                filename_with_underscore(filename,labels_list)
            else:
                pet_full_name =filename_with_extension(filename)
                labels_list.append(pet_full_name)
        return labels_list

    # get_labels method assembles list of label names based on file names list
    def pet_dict_assembler(filename_list,label_list):
        for idx in range(0, len(filename_list),1):
            if filename_list[idx] not in results_dic:
                results_dic[filename_list[idx]] = [label_list[idx]]
            else:
                print("** Warning: Key=", filename_list[idx], "already exists in temp_dic with value =", results_dic[filename_list[idx]])
        return results_dic

    results_dic = pet_dict_assembler(filename_list,get_labels(filename_list))

    #print("Value of results_dic in get_pet_labels module is : {}".format(results_dic))
    return results_dic
