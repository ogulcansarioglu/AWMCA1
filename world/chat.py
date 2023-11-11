from pathlib import Path

import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["POST"])
def get_hotel_information(hotel_name):
    openai.api_key = ""
    BASE_DIR = Path(__file__).resolve().parent.parent
    with open(f'{BASE_DIR}/openAI.txt') as f:
        openai.api_key = f.read().strip()


    try:
        response = openai.ChatCompletion.create(
            model="gpt-4.0-turbo",  # or another version of the model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Tell me more about the history of {hotel_name}."}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        # Handle exceptions
        return JsonResponse({'error': 'An error occurred: ' + str(e)}, status=500)
