import { useEffect, useState } from "react";

import { getProducts } from "../services/productService";

function Products() {

    const [products, setProducts] = useState([]);

    useEffect(() => {

        const fetchProducts = async () => {

            const data = await getProducts();

            setProducts(data);

        };

        fetchProducts();

    }, []);

    return (

        <div>

            <h1 className="text-3xl font-bold mb-5">
                Products
            </h1>

            <pre>
                {JSON.stringify(products, null, 2)}
            </pre>

        </div>

    );

}

export default Products;