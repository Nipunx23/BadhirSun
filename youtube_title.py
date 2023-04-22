import pafy
url = "https://www.youtube.com/watch?v=dBxOYE2j55U"
result = pafy.new(url)
print(f"{result.title}")
