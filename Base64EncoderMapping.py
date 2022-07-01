base64_mapping='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def get_mapping(decimal) -> str:
    return str(base64_mapping[decimal])