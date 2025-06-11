import requests
import html
parameters = {"amount": 10, "type": 'boolean'}
response = requests.get("https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
content = response.json()
i = 0
question_data = []
for q in content['results']:
    data = content['results'][i]
    question_data.append({'question': html.unescape(data['question']), 'correct_answer': data['correct_answer'], 'incorrect_answers' : data['incorrect_answers'], 'difficulty': data['difficulty'], 'category': data['category']})
    i+=1
