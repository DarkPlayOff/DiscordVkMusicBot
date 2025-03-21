def format_error_message(error):
    return f"Error: {str(error)}"

def format_track_info(track_info):
    return f"Track: {track_info['title']} by {track_info['artist']}"

def validate_vk_link(link):
    if "vk.com" in link and "audio" in link:
        return True
    return False

def extract_track_id(link):
    # This function should extract the track ID from a VK music link
    # Implementation will depend on the specific format of the VK music link
    pass