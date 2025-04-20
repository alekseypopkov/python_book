import requests
import pandas as pd
import plotly.express as px

from pprint import pprint

# Создание вызова API и сохранение ответа.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Преобразование объекта ответа в словарь.
response_dict = r.json()

# Обработка результатов.
print(response_dict.keys())

# Работа со словарем
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    stars.append(repo_dict['stargazers_count'])
    
    # Создание всплывающих текстов.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Создание визуализации.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
#fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, 
             hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()

# # Анализ первого репозитория.
# repo_dict = repo_dicts[0]

# # Прочитаем значения некоторых ключей repo_dict:

# print("\nSelected information about first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")
# pprint(f"\nKeys: {len(repo_dict)}")

# for key in sorted(repo_dict.keys()):
#     print(key)