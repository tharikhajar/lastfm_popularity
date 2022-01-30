from IPython.display import clear_output
def tag_flagger_machine(tags: list, start_index=0, write_csv=False):
    '''
    This function will iterate through a list of tags
    from LastFM and prompt the user to categorize it or dump it
    input: list of tags
    output: dict of tags broken down by category
    '''

    import copy
    import csv
    import os
    from IPython.display import clear_output

    instructions_message = (
        f'{"-" * 20}\
        \n 1 = genre\
        \n 2 = mood\
        \n 3 = decade\
        \n r = tag name did not display. reload\
        \n x = exit program\
        \n anything else = dump\
        \n {"-" * 20}'
        )

    input_to_category_map = dict([
        (1, 'genre'),
        (2, 'mood'),
        (3, 'decade')
    ])

    tag = tags[0]
    message = ''
    tag_index = copy.copy(start_index)

    tags_package = dict(
        genre=dict(values=[], message=' -> genre'),
        mood=dict(values=[], message=' -> mood'),
        decade=dict(values=[], message=' -> decade')
    )
    temp_csv_name = create_tags_csv()
    with open(temp_csv_name, 'w', newline='') as tags_csv:

        tags_writer = csv.writer(
             tags_csv, delimiter=';',
             quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for tag in tags:

            print(f'{message} \n', instructions_message, f'\n Tag: {tag}')

            user_input = input()

            while user_input == 'r':
                print(f'\n Tag: {tag}')
                user_input = input()

            if user_input == 'x':
                break

            else:
                try:
                    user_input = int(user_input)
                    tag_category = input_to_category_map[user_input]

                    tags_package[tag_category]['values'].append(tag)
                    message = tag + tags_package[tag_category]['message']
                    tags_writer.writerow([tag_index, tag_category, tag])

                    tag_index += 1
                    clear_output(wait=True)

                except (ValueError, KeyError):
                    message = f'The tag {tag} was dumped'

                    tag_index += 1
                    clear_output(wait=True)
        

    print(f'Tags {start_index} to {tag_index} have been successfully classified!')
    csv_name = str(start_index) + '_to_' + str(tag_index) + temp_csv_name[4:]
    os.rename(temp_csv_name, csv_name)

    return tags_package


def create_tags_csv():
    # Creates the csv file that will keep the tags classification

    from datetime import datetime

    # Using datetime to make sure this name is unique
    now = datetime.now()
    now = now.strftime('%Y-%m-%d_%H-%M-%S')
    temp_file_name = 'temp_tags_csv_' + now +'.csv'

    open(temp_file_name, 'x').close()

    return temp_file_name
