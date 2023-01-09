import json

def categorize_entities(text, labeled_entities):
    #if nothing is in the labeled entites
    if labeled_entities == "!":
        return [(0, 0, "")]

    # Split the labeled entities string by the '@@' symbol
    categories = labeled_entities.split('@@')
    # Initialize an empty list to store the tuples
    tuples = []
    # Iterate over the categories
    for category in categories:
        # Split the category string by the '&&' symbol to get the category label and the list of entities
        try:
            label, entity_string = category.split('&&')
        except:
            raise Exception(f"This doesn't split into label and entity: {category}")

        # Strip any leading or trailing whitespace from the label and entity string
        label = label.strip()
        entity_string = entity_string.strip()
        # Split the entity string by the '%%' symbol to get a list of entities
        entities = entity_string.split('%%')
        # Strip any leading or trailing whitespace from each entity
        entities = [entity.strip() for entity in entities]
        # Add a tuple for each entity in the list, with the start and end character spans,
        # the category label, and the entity as elements
        for entity in entities:
            start = text.find(entity)
            end = start + len(entity)
            if start != -1:
                tuples.append((start, end, label))
            else:
                tuples.append((0,0,""))
    combined_tuple = {"content":text,"entities":tuples}
    # Return the list of tuples
    return combined_tuple

import os

def make_train_data(text_file_path, labeled_entities_file_path,output_file_path):
    # Initialize an empty list to store the train data
    train_data = []
    # Open the text file and labeled entities file for reading
    with open(text_file_path, 'r', encoding='utf-8') as text_file, \
            open(labeled_entities_file_path, 'r', encoding='utf-8') as labeled_entities_file:
        # Iterate over the lines in the text file and labeled entities file
        text_list = text_file.read().split('\n\n')
        labeled_entities_list = labeled_entities_file.read().split('\n\n')

        if len(text_list) != len(labeled_entities_list):
            print(len(text_list),"text len \t", len(labeled_entities_list), "label len \t")
            raise ValueError("The two are not matching in length")

        for text, labeled_entities in zip(text_list,labeled_entities_list):
            # Strip any leading or trailing whitespace from the text and labeled entities strings
            text = text.strip()
            labeled_entities = labeled_entities.strip()
            # Call the categorize_entities function on the text and labeled entities strings
            data = categorize_entities(text, labeled_entities)
            # Append the returned data to the train_data list
            train_data.append(data)
    with open(output_file_path, 'w') as output_file:
        # Write the train data as a JSON object to the output file
        json.dump(train_data, output_file)