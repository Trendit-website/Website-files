'''
This module defines the controller methods for pricing in the Trendit³ Flask application.

It includes methods for getting prices, adding pricing, updating pricing and deleting pricing.

@author: Chris
@link: https://github.com/al-chris
@package: Trendit³
'''

from flask import request

from ...extensions import db
from ...models import Pricing
from ...utils.helpers.basic_helpers import console_log
from ...utils.helpers.response_helpers import error_response, success_response


class PricingController:
    @staticmethod
    def get_all_pricing():
        try:
            pricings = {item.item_name: item.price for item in Pricing.query.all()}

            db.session.close()

            return success_response('Pricing retrieved successfully', 200, extra_data=pricings)
        
        except Exception as e:
            console_log("An error occurred while retrieving pricing", e)
            return error_response('An error occurred while retrieving pricing', 500)
        
    @staticmethod
    def add_pricing():
        try:
            data = request.get_json()
            item_name = data.get('item_name')
            price = data.get('price')

            if not item_name or not price:
                return error_response('Item name and price are required', 400)

            pricing = Pricing(item_name=item_name, price=price)
            db.session.add(pricing)
            db.session.commit()
            db.session.close()

            return success_response('Pricing added successfully', 201)
        
        except Exception as e:
            console_log("An error occurred while adding pricing", e)
            return error_response('An error occurred while adding pricing', 500)
        
    @staticmethod
    def update_pricing():
        try:
            data = request.get_json()
            item_name = data.get('item_name')
            price = data.get('price')

            if not item_name or not price:
                return error_response('Item name and price are required', 400)

            pricing = Pricing.query.filter_by(item_name=item_name).first()

            if not pricing:
                return error_response('Pricing not found', 404)

            pricing.price = price
            db.session.commit()
            db.session.close()

            return success_response('Pricing updated successfully', 200)
        
        except Exception as e:
            console_log("An error occurred while updating pricing", e)
            return error_response('An error occurred while updating pricing', 500)
        
    @staticmethod
    def delete_pricing():
        try:
            data = request.get_json()
            item_name = data.get('item_name')

            if not item_name:
                return error_response('Item name is required', 400)

            pricing = Pricing.query.filter_by(item_name=item_name).first()

            if not pricing:
                return error_response('Pricing not found', 404)

            db.session.delete(pricing)
            db.session.commit()
            db.session.close()

            return success_response('Pricing deleted successfully', 200)
        
        except Exception as e:
            console_log("An error occurred while deleting pricing", e)
            return error_response('An error occurred while deleting pricing', 500)