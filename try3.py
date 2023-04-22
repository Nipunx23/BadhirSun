import pafy

url = 'https://www.youtube.com/watch?v=dBxOYE2j55U'
result = pafy.new(url)

title = result.title
title = title.replace(" ","_")

best = result.getbest()

best.download(filepath=title + '.' + best.extension)
