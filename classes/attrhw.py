class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


firstpost = BlogPost("John Smith", "Hello!", 45)
secondpost = BlogPost("Jane Smith", "This is my second post", 61)

print(firstpost.number_of_likes)
print(secondpost.number_of_likes)
