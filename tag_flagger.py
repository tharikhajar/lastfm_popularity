from IPython.display import clear_output
def tag_flagger_machine(tags: list):
    '''
    This function will iterate through a list of tags
    from LastFM and prompt the user to categorize it or dump it
    input: list of tags
    output: lists of tags broken down by category
    '''
    from IPython.display import clear_output

    tag = tags[0]
    message = ''

    tags_package = dict([
        (1, dict(values=[], message=' -> genre')), # genres
        (2, dict(values=[], message=' -> mood')), # moods
        (3, dict(values=[], message=' -> decade'))  # decade
    ])
    
    for tag in tags:

        print(
        f'{message} \n',
        '-' * 20, '\n',
        '1 = genre \
        \n 2 = mood \
        \n 3 = decade \
        \n x = exit program \
        \n anything else = dump \n',
        '-' * 20
        )

        print(f'Tag: {tag}')
        user_input = input()

        if user_input == 'x':
            print('Program terminated.')
            return

        else:
            try:
                user_input = int(user_input)
                tags_package[user_input]['values'].append(tag)
                message = tag + tags_package[user_input]['message']
                clear_output(wait=True)

            except (ValueError, KeyError):
                message = f'The tag {tag} was dumped'
                clear_output(wait=True)
                continue
        
    tag_count = len(tags)
    print(f'All {tag_count} tags have been successfully classified!')

    return tags_package

#%%
