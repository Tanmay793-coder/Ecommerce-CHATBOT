import re

def parse_query(query):
    """Convert natural language to search filters"""
    filters = {}
    query = query.lower()
    
    # Price extraction
    price_matches = re.findall(r'under (\$\d+)', query)
    if price_matches:
        filters['max_price'] = float(price_matches[0].replace('$', ''))
    
    price_matches = re.findall(r'below (\$\d+)', query)
    if price_matches:
        filters['max_price'] = float(price_matches[0].replace('$', ''))
    
    price_matches = re.findall(r'over (\$\d+)', query)
    if price_matches:
        filters['min_price'] = float(price_matches[0].replace('$', ''))
    
    price_matches = re.findall(r'above (\$\d+)', query)
    if price_matches:
        filters['min_price'] = float(price_matches[0].replace('$', ''))
    
    # Category detection
    categories = ['electronics', 'books', 'clothing', 'fashion', 'textiles', 'home']
    for cat in categories:
        if cat in query:
            filters['category'] = cat
            break
    
    # Keyword extraction (if no specific filters, use the whole query as keyword)
    if not filters and query:
        filters['keyword'] = query.split()[0]  # Use first word as keyword
    
    return filters