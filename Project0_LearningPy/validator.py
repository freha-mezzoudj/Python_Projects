
# costum module to be imported
import re

def validate_email(email):
    if len(email) >7:
        #regular expression
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))


