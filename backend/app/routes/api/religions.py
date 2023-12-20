import logging
from flask import request

from app.routes.api import bp
from app.utils.helpers.response_helpers import error_response, success_response

# list of all practiced religions
religions = [
    "Christianity",
    "Islam",
    "Hinduism",
    "Buddhism",
    "Sikhism",
    "Judaism",
    "Traditional African Religions",
    "Bahai Faith",
    "Jainism",
    "Shintoism",
]

# RELIGIONS ENDPOINTS
@bp.route("/religions", methods=['GET'])
def get_all_religion():
    """
    Get a list of all practiced religions.

    Returns:
        JSON response with a list of religions.
    """
    try:
        extra_data = {
            "religions": religions,
        }
        return success_response('Successfully retrieved practiced religions.', 200, extra_data)
    except Exception as e:
        return error_response('Error occurred retrieving practiced religions.', 500)


@bp.route("/religions/search", methods=["GET"])
def search_religions():
    """
    Search for religions containing a specific keyword in their name.

    Args:
        keyword (query parameter): The keyword to search for.

    Returns:
        JSON response with a list of matching religions or an empty list if not found.
    """
    
    try:
        keyword = request.args.get("keyword")
        if not keyword:
            return error_response('Keyword parameter is required.', 400)
        
        # Implement logic to search for religions based on the keyword

        matched_religions = []
        for religion in religions:
            if keyword.lower() in religion.lower():
                matched_religions.append(religion)
        
        return success_response('Found matching religions.', 200, {"religions": matched_religions})
    except Exception as e:
        logging.exception(f"An exception occurred searching religions. {e}")
        return error_response('An error occurred while processing the request.', 500)
