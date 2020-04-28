# The marketing team is spending way too much time typing in hashtags.

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(tag):
    if not tag or len(tag) > 140:
        return False
    else:
        tag = tag.title()
        tag = tag.replace(" ", "")
        return f'#{tag}'
    
