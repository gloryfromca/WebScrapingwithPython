
from twitter import Twitter,OAuth
t=Twitter (auth=OAuth("2875649376-YWYc87J6iw7zd3KLqinfeyjtr0XpwDMOANR3VTh","sFepdYSVgg3MUhUV0W2WzKIGiTbbvDV7aSxslSvRbuHkR","xZV0qZNKdgrWQnZTw6KWbKEYm","9fQsWNwDBF3YROF8NljKPdHJnrt7gQUCxR0uy92q6efhRZjAQ0"))
# pythontweets=t.search.tweets(q='#python')
# print(pythontweets)
# statusupdate=t.statuses.update(status='hello,world')
# print(statusupdate)
pythonstatuses=t.statuses.user_timeline(screen_name="montypython",count=5)
print(pythonstatuses)
