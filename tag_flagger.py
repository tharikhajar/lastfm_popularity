from IPython.display import clear_output
def tag_flagger_machine(tags: list, start_index=0, write_csv=False):
    '''
    This function will iterate through a list of tags
    from LastFM and prompt the user to categorize it or dump it
    input: list of tags
    output: dict of tags broken down by category
    '''
    from IPython.display import clear_output

    instructions_message = (
        f'{"-" * 20}\
        \n 1 = genre\
        \n 2 = mood\
        \n 3 = decade\
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

    tags_package = dict(
        genre=dict(values=[], message=' -> genre'),
        mood=dict(values=[], message=' -> mood'),
        decade=dict(values=[], message=' -> decade')
    )
    
    #csv_temp_name = create_tags_csv()

    #with open(csv_temp_name, 'w', newline=''):

        # tags_writer = csv.writer(
        #     csv_temp_name, delimiter=';',
        #     quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for tag in tags:

        print(
            f'{message} \n',
            instructions_message,
            f'\n Tag: {tag}'
            )

        user_input = input()

        if user_input == 'x':
            print('Program terminated.')
            return

        else:
            try:
                user_input = int(user_input)
                tag_category = input_to_category_map[user_input]

                tags_package[tag_category]['values'].append(tag)
                message = tag + tags_package[tag_category]['message']
                #tags_writer.writerow()

                clear_output(wait=True)

            except (ValueError, KeyError):
                message = f'The tag {tag} was dumped'
                clear_output(wait=True)
        
    tag_count = len(tags) - start_index
    print(f'All {tag_count} tags have been successfully classified!')

    return tags_package

#%%

def create_tags_csv():
    # Creates the csv file that will keep the tags classification

    from datetime import datetime

    # Using datetime to make sure this name is unique
    now = datetime.now()
    now = now.strftime('%Y-%m-%d_%H-%M-%S')
    temp_file_name = 'temp_tags_csv_' + now +'.csv'

    open(temp_file_name, 'x').close()

    return temp_file_name

#%%

#%%
import csv

with open('test.csv', 'w', newline='') as tags_csv:
    tag_writer = csv.writer(tags_csv, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    tag_writer.writerow(['rock', 'genre'])

# %%
