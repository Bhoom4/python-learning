def http_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "not found"
        case 500:
            return "internal server error"
        case _:
            return "unknown status"
        
#usage
print(http_status (200))
print(http_status (400))
print(http_status (500))
print(http_status (403))