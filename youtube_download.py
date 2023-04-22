import pafy
url = "https://www.youtube.com/watch?v=Ej1XtVQn5Ws"
result = pafy.new(url)
best_quality_video = result.getbest()
print(best_quality_video)
best_quality_video.download()
