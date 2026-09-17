import requests
from decouple import config


from django.shortcuts import render

# Create your views here.

##Home view is the main page of the website, it will render the home.html template when accessed.
def home(request):
    return render(request, 'core/home.html')

def ai_tab(request):
    answer = None
    question = None
    error = None

    if request.method == 'POST':
        question = request.POST.get('question', '').strip()

        if not question:
            error = 'Please ask a question first.'
        else:
            try:
                response = requests.post(
                    'https://api.openai.com/v1/chat/completions',
                    headers={
                        'Authorization': f'Bearer {config("OPENAI_API_KEY")}',
                        'Content-Type': 'application/json',
                    },
                    json={
                        'model': 'gpt-4o-mini',
                        'messages': [
                            {
                                'role': 'user',
                                'content': question
                            }
                        ],
                    },
                    timeout=30,
                )

                data = response.json()

                if response.status_code == 200:
                    answer = data['choices'][0]['message']['content']
                else:
                    error = data.get('error', {}).get(
                        'message',
                        'Something went wrong with the AI.'
                    )

            except requests.exceptions.RequestException as e:
                error = f'Could not connect to the AI: {e}'

            except (KeyError, IndexError, TypeError):
                error = 'The AI returned an unexpected response.'

    return render(
        request,
        'core/ai.html',
        {
            'answer': answer,
            'question': question,
            'error': error,
        }
    )