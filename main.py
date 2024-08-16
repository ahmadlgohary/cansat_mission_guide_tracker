import requests as r

from program_info_manager import personal_access_token, channel_url
from check_competition_page_for_updates import get_mission_guide_page


def main():
    """main function that handles the logic and ties all functions together"""
    has_file_changed, mission_guide_pdf_url = get_mission_guide_page().values()
    if has_file_changed:
        message_to_send = f"Hello @everyone The Mission Guide has been updated today\n the updated mission guide is:\n {mission_guide_pdf_url}"

        # send a post request to the discord server to send a notification message
        r.post(channel_url, {"content": message_to_send}, headers={"authorization": personal_access_token})


if __name__ == "__main__":
    main()
