from flask import jsonify
from werkzeug.exceptions import HTTPException
from app import app

class APIError(Exception):
    """Base error class for API exceptions"""
    def __init__(self, message, status_code=400, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv

@app.errorhandler(APIError)
def handle_api_error(error):
    """Handle custom API errors"""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(404)
def handle_not_found(error):
    """Handle 404 Not Found errors"""
    if isinstance(error, HTTPException):
        response = jsonify({
            'message': error.description,
            'status_code': 404
        })
        return response, 404
    return jsonify({
        'message': 'Resource not found',
        'status_code': 404
    }), 404

@app.errorhandler(405)
def handle_method_not_allowed(error):
    """Handle 405 Method Not Allowed errors"""
    return jsonify({
        'message': 'Method not allowed',
        'status_code': 405
    }), 405

@app.errorhandler(500)
def handle_internal_error(error):
    """Handle 500 Internal Server errors"""
    app.logger.error(f'Server error: {str(error)}')
    return jsonify({
        'message': 'Internal server error',
        'status_code': 500
    }), 500

@app.errorhandler(Exception)
def handle_unexpected_error(error):
    """Catch-all for unexpected errors"""
    app.logger.error(f'Unexpected error: {str(error)}')
    return jsonify({
        'message': 'An unexpected error occurred',
        'status_code': 500
    }), 500

def register_error_handlers(app):
    """Register all error handlers with the Flask app"""
    app.register_error_handler(APIError, handle_api_error)
   