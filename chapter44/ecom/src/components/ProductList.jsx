import React, { useEffect, useState } from 'react';
import ProductForm from './ProductForm';

const ProductList = () => {
  const [products, setProducts] = useState([]);

  const fetchProduct = async () => {
    const res = await fetch('http://localhost:8000/products');
    const data = await res.json();
    setProducts(data);
  };

  useEffect(() => {
    fetchProduct();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-start py-10">
      <div className="bg-white w-full max-w-3xl p-8 rounded-2xl shadow-md">

        <h1 className="text-3xl font-bold text-center mb-8 text-gray-800">
          Product List
        </h1>

        {/* Product Form */}
        <h2 className="text-xl font-semibold text-center text-gray-700 mb-4">
          Add Product
        </h2>

        <ProductForm
          onProductAdded={(product) =>
            setProducts((prev) => [...prev, product])
          }
        />

        <hr className="my-6" />

        <div className="space-y-4">
          {products.map((p) => (
            <div
              key={p.id}
              className="p-5 bg-blue-50 rounded-xl shadow-sm border border-blue-100 hover:bg-blue-100 transition"
            >
              <h3 className="text-lg font-bold text-blue-600 text-center">
                {p.title}
              </h3>
              <p className="text-gray-700 text-center mt-1">
                : {p.description}
              </p>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
};

export default ProductList;
