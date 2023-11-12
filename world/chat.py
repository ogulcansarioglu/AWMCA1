import logging
from pathlib import Path
import openai
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["POST"])
def get_hotel_information(request):
    logger.debug("Received request for hotel information")

    try:
        # Extract hotel name from request body

        # Set up OpenAI API key
        openai.api_key = ""
        BASE_DIR = Path(__file__).resolve().parent.parent
        with open(f'{BASE_DIR}/openAI.txt') as f:
            openai.api_key = f.read().strip()
        logger.debug("OpenAI API key set")

        # Making OpenAI API call

        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key="API_KEY",
        )

        GPT_MODEL = "gpt-4-1106-preview"  # "gpt-3.5-turbo-1106"
        messages = [
            {"role": "system", "content": 'You answer question about attractions in Ireland'
             },
            {"role": "user", "content": 'provide more information about parks'},
        ]
        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=0
        )
        response_message = response.choices[0].message.content
        print(response_message)

        return {"response": response_message}
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return JsonResponse({'error': 'An error occurred: ' + str(e)}, status=500)
