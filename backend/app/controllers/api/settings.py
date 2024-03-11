'''
This module defines the controller methods for user setting on the Trendit³ Flask application.

@author: Emmanuel Olowu
@link: https://github.com/zeddyemy
@package: Trendit³
'''

import logging, hashlib, pyotp
from flask import request
from sqlalchemy.exc import ( DataError, DatabaseError )
from flask_jwt_extended import get_jwt_identity
from werkzeug.exceptions import UnsupportedMediaType

from ...extensions import db
from ...models import Trendit3User, UserSettings, NotificationPreference, UserPreference, SecuritySetting
from ...exceptions import InvalidTwoFactorMethod
from ...utils.helpers.basic_helpers import console_log, log_exception
from ...utils.helpers.settings_helpers import set_2fa_method, generate_google_authenticator_secret_key, generate_google_authenticator_qr_code
from ...utils.helpers.response_helpers import error_response, success_response
from ...utils.helpers.settings_helpers import update_notification_preferences, update_user_preferences, update_security_settings


class ManageSettingsController:
    @staticmethod
    def get_notification_settings():
        try:
            current_user_id = get_jwt_identity()
            current_user = Trendit3User.query.get(current_user_id)
            if not current_user:
                return error_response(f"user not found", 404)
            
            user_settings = UserSettings.query.filter_by(trendit3_user_id=current_user_id).first()
            if not user_settings:
                user_settings = UserSettings(trendit3_user_id=current_user_id)
                db.session.add(user_settings)
            
            
            if not user_settings.notification_preference:
                user_settings.notification_preference = NotificationPreference()
            
            db.session.commit()
            
            notification_preference = user_settings.notification_preference
            
            extra_data = {"notification_preference": notification_preference.to_dict()}
            
            api_response = success_response('Notification preferences fetched successfully', 200, extra_data)
        except (DataError, DatabaseError) as e:
            db.session.rollback()
            log_exception('Database error occurred fetching preference', e)
            return error_response('Error interacting with the database.', 500)
        except Exception as e:
            db.session.rollback()
            msg = f'An unexpected error occurred fetching notification preference: {e}'
            logging.exception(f"An exception occurred fetching notification preference. {str(e)}")
            api_response = error_response(msg, 500)
        finally:
            db.session.close()
        
        return api_response


    @staticmethod
    def get_preference_settings():
        try:
            current_user_id = get_jwt_identity()
            current_user = Trendit3User.query.get(current_user_id)
            if not current_user:
                return error_response(f"user not found", 404)
            
            
            user_settings = UserSettings.query.filter_by(trendit3_user_id=current_user_id).first()
            if not user_settings:
                user_settings = UserSettings(trendit3_user_id=current_user_id)
                db.session.add(user_settings)
            
            if not user_settings.user_preference:
                user_settings.user_preference = UserPreference()
            
            user_preference = user_settings.user_preference
            
            db.session.commit()
            
            extra_data = {"user_preferences": user_preference.to_dict()}
            
            api_response = success_response('preferences fetched successfully', 200, extra_data)
            
        except (DataError, DatabaseError) as e:
            db.session.rollback()
            log_exception('Database error occurred fetching preference', e)
            api_response = error_response('Error interacting with the database.', 500)
        except Exception as e:
            db.session.rollback()
            msg = f'An unexpected error occurred fetching user preference: {e}'
            logging.exception(f"An exception occurred fetching user preference. {str(e)}")
            api_response = error_response(msg, 500)
        finally:
            db.session.close()
        
        return api_response


    @staticmethod
    def get_security_settings():
        try:
            current_user_id = get_jwt_identity()
            current_user = Trendit3User.query.get(current_user_id)
            if not current_user:
                return error_response(f"user not found", 404)
            
            
            user_settings = UserSettings.query.filter_by(trendit3_user_id=current_user_id).first()
            if not user_settings:
                user_settings = UserSettings(trendit3_user_id=current_user_id)
                db.session.add(user_settings)
            
            if not user_settings.security_setting:
                user_settings.security_setting = SecuritySetting()
            
            db.session.commit()
            
            security_setting = user_settings.security_setting
            
            extra_data = {"security_settings": security_setting.to_dict()}
            
            api_response = success_response('Security settings fetched successfully', 200, extra_data)
            
        except (DataError, DatabaseError) as e:
            db.session.rollback()
            log_exception('Database error occurred fetching security settings', e)
            api_response = error_response('Error interacting with the database.', 500)
        except Exception as e:
            db.session.rollback()
            msg = f'An unexpected error occurred fetching security settings: {e}'
            log_exception(f"An exception occurred fetching security settings.", str(e))
            api_response = error_response(msg, 500)
        finally:
            db.session.close()
        
        return api_response


    @staticmethod
    def update_notification_settings():
        try:
            current_user_id = get_jwt_identity()
            current_user = Trendit3User.query.get(current_user_id)
            if not current_user:
                return error_response(f"user not found", 404)
            
            data = request.get_json()
            
            user_settings = UserSettings.query.filter_by(trendit3_user_id=current_user_id).first()
            if not user_settings:
                user_settings = UserSettings(trendit3_user_id=current_user_id)
                db.session.add(user_settings)
            
            
            if not user_settings.notification_preference:
                user_settings.notification_preference = NotificationPreference()
            
            notification_preference = user_settings.notification_preference
            
            # Update notification preferences
            notification_preferences = update_notification_preferences(notification_preference, data)
            
            extra_data = {"notification_preference": notification_preferences.to_dict()}
            
            db.session.commit()
            api_response = success_response('Notification preferences updated successfully', 200, extra_data)
        except (DataError, DatabaseError) as e:
            db.session.rollback()
            log_exception('Database error occurred saving preference', e)
            return error_response('Error interacting with the database.', 500)
        except Exception as e:
            db.session.rollback()
            msg = f'An unexpected error occurred saving notification preference: {e}'
            logging.exception(f"An exception occurred saving notification preference. {str(e)}")
            api_response = error_response(msg, 500)
        finally:
            db.session.close()
        
        return api_response


    @staticmethod
    def update_preference_settings():
        try:
            current_user_id = get_jwt_identity()
            current_user = Trendit3User.query.get(current_user_id)
            if not current_user:
                return error_response(f"user not found", 404)
            
            data = request.get_json()
            
            user_settings = UserSettings.query.filter_by(trendit3_user_id=current_user_id).first()
            if not user_settings:
                user_settings = UserSettings(trendit3_user_id=current_user_id)
                db.session.add(user_settings)
            
            if not user_settings.user_preference:
                user_settings.user_preference = UserPreference()
            
            user_preference = user_settings.user_preference
            
            # Update user preferences
            user_preferences = update_user_preferences(user_preference, data)
            
            extra_data = {"user_preferences": user_preferences.to_dict()}
            
            db.session.commit()
            api_response = success_response('preferences updated successfully', 200, extra_data)
            
        except (DataError, DatabaseError) as e:
            db.session.rollback()
            log_exception('Database error occurred saving preference', e)
            api_response = error_response('Error interacting with the database.', 500)
        except Exception as e:
            db.session.rollback()
            msg = f'An unexpected error occurred saving user preference: {e}'
            logging.exception(f"An exception occurred saving user preference. {str(e)}")
            api_response = error_response(msg, 500)
        finally:
            db.session.close()
        
        return api_response


    @staticmethod
    def update_security_settings():
        try:
            current_user_id = get_jwt_identity()
            current_user = Trendit3User.query.get(current_user_id)
            if not current_user:
                return error_response(f"user not found", 404)
            
            data = request.get_json()
            
            user_settings = UserSettings.query.filter_by(trendit3_user_id=current_user_id).first()
            if not user_settings:
                user_settings = UserSettings(trendit3_user_id=current_user_id)
                db.session.add(user_settings)
            
            if not user_settings.security_setting:
                user_settings.security_setting = SecuritySetting()
            
            security_setting = user_settings.security_setting
            
            # Update user preferences
            security_settings = update_security_settings(security_setting, data)
            
            extra_data = {"security_settings": security_settings.to_dict()}
            
            api_response = success_response('Security settings updated successfully', 200, extra_data)
        except InvalidTwoFactorMethod as e:
            db.session.rollback()
            api_response = error_response(f'{e}', 400)
        except (DataError, DatabaseError) as e:
            db.session.rollback()
            log_exception('Database error occurred saving security settings', e)
            api_response = error_response('Error interacting with the database.', 500)
        except Exception as e:
            db.session.rollback()
            msg = f'An unexpected error occurred saving security settings: {e}'
            logging.exception(f"An exception occurred saving security settings. {str(e)}")
            api_response = error_response(msg, 500)
        finally:
            db.session.close()
        
        return api_response


    @staticmethod
    def activate_google_2fa():
        try:
            current_user_id = get_jwt_identity()
            user = Trendit3User.query.get(current_user_id)
            
            # Generate a secret key
            secret_key = user.two_fa_secret
            if not secret_key:
                secret_key = generate_google_authenticator_secret_key()
                
                # TODO: Encrypt Secrete key for secure storage
                # Update user object with secret key
                user.update(two_fa_secret=secret_key)

            # Generate QR code data URI 
            qr_code_data = generate_google_authenticator_qr_code(secret_key, user.email)

            api_response = success_response('Download the Google Authentication app on your new device. Within the app, scan this QR code.', 200, {'qr_code_data': qr_code_data})

        except Exception as e:
            logging.exception(f"An error occurred enabling 2FA: {e}")
            api_response = error_response('Failed to activate 2-factor authentication with Google Auth App.', 500)
        finally:
            db.session.close()
        
        return api_response
    
    
    @staticmethod
    def complete_google_2fa_activation():
        try:
            current_user_id = get_jwt_identity()
            user = Trendit3User.query.get(current_user_id)
            
            if not user:
                return error_response('user not found', 404)
            
            data = request.get_json()
            entered_code = data.get('entered_code')
            
            secret_key = user.two_fa_secret
            
            # Verify the OTP
            totp = pyotp.TOTP(secret_key)
            if not totp.verify(entered_code):
                return error_response('Wrong 2-factor authentication Code: Please provide a correct code to complete activation.', 400)
            
            # If the OTP is correct, enable 2FA for the user
            two_fa_method = set_2fa_method(method="google_auth_app", user_id=current_user_id)
            
            api_response = success_response('2-factor authentication enabled successfully.', 200)
        except UnsupportedMediaType as e:
            api_response = error_response(f'{e}', 500)
        except Exception as e:
            logging.exception(f"An exception occurred trying to login: {e}") # Log the error details for debugging
            api_response = error_response('An Unexpected error occurred processing the request.', 500)
        
        return api_response
    
    
    @staticmethod
    def deactivate_google_2fa():
        try:
            current_user_id = get_jwt_identity()
            user = Trendit3User.query.get(current_user_id)
            
            user.two_fa_secret = None
            two_fa_method = set_2fa_method(method=None, user_id=current_user_id)

            api_response = success_response('2 Factor Authentication with Google Auth App deactivated successfully.', 200)

        except Exception as e:
            logging.exception(f"An error occurred enabling 2FA: {e}")
            api_response = error_response('Failed to activate 2FA with Google Auth App.', 500)
        finally:
            db.session.close()
        
        return api_response
    