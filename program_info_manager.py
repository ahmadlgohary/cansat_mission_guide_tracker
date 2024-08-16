import os
import json

# current directory the program is running in
current_directory = os.path.dirname(os.path.realpath(__file__))

# load the json file
with open(os.path.join(current_directory, 'program_info.json'), 'r') as f:
    program_data = json.load(f)

# load the json file items into variables
old_file_hash = program_data['old_file_hash']
channel_url = program_data['channel_url']
mission_guide_url = program_data['mission_guide_url']
competition_website = program_data['competition_website']

# load the personal access token from the environment secretes
personal_access_token = os.environ['personal_access_token']


def set_new_file_hash(new_file_hash):
    """
    updates the file hash in the program_info.json file

    Args:
        new_file_hash (int): the new file hash
    """
    program_data['old_file_hash'] = new_file_hash
    with open(os.path.join(current_directory, 'program_info.json'), 'w') as f:
        f.write(json.dumps(program_data, indent=4))
