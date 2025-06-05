from flask import Blueprint, request, jsonify
from app.models import Product
from app.utils.query_parser import parse_query
from flask_jwt_extended import jwt_required

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
@jwt_required()
def handle_chat():
    data = request.json
    message = data.get('message', '').lower()
    
    # Simple response logic
    if any(greeting in message for greeting in ['hello', 'hi', 'hey']):
        return jsonify({
            'message': 'Hello! How can I assist you with your shopping today?'
        })
    elif any(bye in message for bye in ['bye', 'goodbye', 'exit']):
        return jsonify({
            'message': 'Goodbye! Thank you for shopping with us.'
        })
    else:
        # Attempt to parse product search
        filters = parse_query(message)
        if filters:
            results = Product.query
            if filters.get('category'):
                results = results.filter_by(category=filters['category'])
            if filters.get('max_price'):
                results = results.filter(Product.price <= filters['max_price'])
            if filters.get('min_price'):
                results = results.filter(Product.price >= filters['min_price'])
            if filters.get('keyword'):
                keyword = f'%{filters["keyword"]}%'
                results = results.filter(Product.name.ilike(keyword))
                
            products = [p.to_dict() for p in results.limit(3).all()]
            if products:
                return jsonify({
                    'message': 'Here are some products that match your request:',
                    'products': products
                })
        
        # Default response
        return jsonify({
            'message': "I can help you find products. Try asking something like: 'Show me electronics under $100'"
        })