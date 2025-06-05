from flask import Blueprint, request, jsonify
from app.models import Product
from app.utils.query_parser import parse_query
from flask_jwt_extended import jwt_required

product_bp = Blueprint('products', __name__)

@product_bp.route('/search', methods=['POST'])
@jwt_required()
def search_products():
    try:
        data = request.json
        query = data.get('query', '')
        
        # Parse query into filters
        filters = parse_query(query)
        
        # Build DB query
        results = Product.query
        if filters.get('category'):
            results = results.filter_by(category=filters['category'])
        if filters.get('max_price'):
            results = results.filter(Product.price <= filters['max_price'])
        if filters.get('min_price'):
            results = results.filter(Product.price >= filters['min_price'])
        if filters.get('keyword'):
            # Simple keyword search in name and description
            keyword = f'%{filters["keyword"]}%'
            results = results.filter(Product.name.ilike(keyword) | Product.description.ilike(keyword))
        
        products = [p.to_dict() for p in results.limit(10).all()]
        return jsonify({'products': products})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500