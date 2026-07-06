import os, json, asyncio, time
from dotenv import load_dotenv
from openai import AsyncOpenAI, APITimeoutError, RateLimitError, APIError
from httpx import HTTPStatusError
from util.fallback import FALLBACKS, FALLBACK_TIMEOUT, FALLBACK_RATE_LIMIT, FALLBACK_API_ERROR, FALLBACK_HTTP_ERROR
from util.prompt import PROMPT_V1, PROMPT_V2, PROMPT_V3
from util.messages import define_messages
from util.get_ai_response import get_ai_response

# Load environment variables
load_dotenv()

# Define model and API keys
cloud_model, cloud_api_key, cloud_base_url = os.getenv('CLOUD_AI_MODEL') or 'gpt-4o-mini', os.getenv('CLOUD_API_KEY'), os.getenv('CLOUD_BASE_URL') or 'https://api.openai.com/v1'
local_model, local_api_key, local_base_url = os.getenv('LOCAL_AI_MODEL') or 'llama3.2', os.getenv('LOCAL_API_KEY') or 'ollama', os.getenv('LOCAL_BASE_URL') or 'http://localhost:11434/v1'

# Define clients
cloud_async_client = AsyncOpenAI(api_key=cloud_api_key, base_url=cloud_base_url)
local_async_client = AsyncOpenAI(api_key=local_api_key, base_url=local_base_url)

# Define user request
user_request = input("Enter your Symptoms: ")

# Define messages
messages = define_messages(user_request) 

# Define function to generate the response
async def generate_response(messages):
    try:
        return await get_ai_response(messages, cloud_model, cloud_async_client, "cloud", timeout=4.0)
    except APITimeoutError:
        # Fallback to local client
        print(f"LOCAL FALLBACK DUE TO CLOUD ERROR. PLEASE WAIT......")
        try:
            return await get_ai_response(messages, local_model, local_async_client, "local")
        except Exception:
            print(FALLBACK_TIMEOUT)
            return FALLBACKS["timeout"]
    except RateLimitError as e:
        print(f"LOCAL FALLBACK DUE TO CLOUD ERROR. PLEASE WAIT......")
        # Fallback to local client
        try:
            return await get_ai_response(messages, local_model, local_async_client, "local")
        except Exception as e:      
            print(FALLBACK_RATE_LIMIT)
            return FALLBACKS["rate_limit"]
    except APIError:
        print(f"LOCAL FALLBACK DUE TO CLOUD ERROR. PLEASE WAIT......")
        # Fallback to local client
        try:
            return await get_ai_response(messages, local_model, local_async_client, "local")
        except Exception:
            print(FALLBACK_API_ERROR)
            return FALLBACKS["api_error"]
    except HTTPStatusError:
        print(f"LOCAL FALLBACK DUE TO CLOUD ERROR. PLEASE WAIT......")
        # Fallback to local client
        try:
            return await get_ai_response(messages, local_model, local_async_client, "local")
        except Exception:
            print(FALLBACK_HTTP_ERROR)
            return FALLBACKS["http_error"]
    except Exception as e:
        print(FALLBACKS["fallback"])
        return FALLBACKS["fallback"]

# Generate the response
result = asyncio.run(generate_response(messages))

# Print the response json
print(json.dumps(result, indent=4))

# Print the routing destination
print(
    f"\nROUTING DECISION: "
    f"{result['routing_destination']}"
)
