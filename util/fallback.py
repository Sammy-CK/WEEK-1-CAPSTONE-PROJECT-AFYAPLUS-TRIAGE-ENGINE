# Define fallback responses
FALLBACK_RESPONSE = (
    "I am currently unable to process your request. "
    "For immediate assistance, please contact our helpline at +254-XXX-XXXX "
    "or visit your nearest healthcare facility."
)
FALLBACK_TIMEOUT = (
    "Our system is responding slowly right now. Please try again in a moment. "
    "If urgent, call our helpline at +254-XXX-XXXX."
)
FALLBACK_RATE_LIMIT = (
    "Our service is busy at the moment. Please wait one minute and try again."
)
FALLBACK_API_ERROR = (
    "We could not process your request. Please contact our helpline at "
    "+254-XXX-XXXX or visit your nearest healthcare facility."
)
FALLBACK_HTTP_ERROR = ( 
    "An HTTP error occurred. Please check your network connection and try again."
)
FALLBACKS = {
    "timeout":    FALLBACK_TIMEOUT,
    "rate_limit": FALLBACK_RATE_LIMIT,
    "api_error":  FALLBACK_API_ERROR,
    "fallback": FALLBACK_RESPONSE,
    "http_error": FALLBACK_HTTP_ERROR,
}