from flask_jwt_extended import jwt_required

from . import api
from ...controllers.api import TransactionController

@api.route('/transactions', methods=['GET'])
@jwt_required()
def transaction_history():
    """
    Fetches the transaction history for a user.

    Returns:
        json: A JSON object containing the status of the request, a status code, and the transaction history.
    """
    return TransactionController.get_transaction_history()


@api.route('/transactions/metrics', methods=['GET'])
@jwt_required()
def transaction_metrics():
    """
    Fetches the transaction metrics for the current user.

    Returns:
        json: A JSON object containing the status of the request, a status code, and the metrics.
    """
    return TransactionController.get_transaction_stats()