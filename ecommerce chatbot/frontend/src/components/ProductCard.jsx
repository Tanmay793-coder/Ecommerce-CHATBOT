import React from 'react';

export default function ProductCard({ product }) {
  return (
    <div className="max-w-xs rounded overflow-hidden shadow-lg m-2">
      <img className="w-full h-48 object-cover" src={product.image} alt={product.name} />
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{product.name}</div>
        <p className="text-gray-700 text-base">
          ${product.price.toFixed(2)}
        </p>
        <p className="text-gray-700 text-base">
          {product.category}
        </p>
        <button className="mt-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded text-sm">
          Add to Cart
        </button>
      </div>
    </div>
  );
}