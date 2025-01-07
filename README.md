# E-commerce Management API

This is a Django-based API for managing e-commerce platforms, including features for managing products, categories, orders, and order items.

## Features
- Manage **Products** (Create, Read, Update, Delete)
- Manage **Categories** (Create, Read)
- Manage **Orders** with detailed **Order Items**
- Calculate and display total order prices dynamically

---

## Getting Started

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <project_directory>
```

---

### 2. Create and Activate a Virtual Environment

#### On Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies
Install all required dependencies using the following command:
```bash
pip install -r requirements.txt
```

---

### 4. Run Database Migrations
Set up the database by running migrations:
```bash
python3 manage.py migrate
```

---

### 5. Start the Development Server
Run the Django development server:
```bash
python3 manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Products
- **GET** `/products/` - List all products
- **POST** `/products/` - Create a new product
- **GET** `/products/{id}/` - Retrieve a product by ID
- **PUT** `/products/{id}/` - Update a product by ID
- **DELETE** `/products/{id}/` - Delete a product by ID

### Categories
- **GET** `/categories/` - List all categories
- **POST** `/categories/` - Create a new category

### Orders
- **GET** `/orders/` - List all orders
- **POST** `/orders/` - Create a new order
- **GET** `/orders/{id}/` - Retrieve an order by ID

### Order Items
- **GET** `/order-items/` - List all order items
- **POST** `/order-items/` - Create a new order item
- **GET** `/order-items/{id}/` - Retrieve an order item by ID
- **PUT** `/order-items/{id}/` - Update an order item by ID
- **DELETE** `/order-items/{id}/` - Delete an order item by ID

---

## Example Requests

### Get All Products
```bash
curl -X GET http://127.0.0.1:8000/products/ -H "accept: application/json"
```

### Create a New Product
```bash
curl -X POST http://127.0.0.1:8000/products/ \
-H "Content-Type: application/json" \
-d '{
    "name": "Sample Product",
    "description": "This is a sample product.",
    "price": 100.50,
    "category": 1
}'
```

---

## Additional Notes
- **Python Version**: Ensure you are using Python 3.7+.
- **Database Configuration**: By default, the project uses SQLite. Update `settings.py` to configure your database as needed.
- **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/`.

---

## Contributing
Feel free to open issues or submit pull requests to enhance the project.

---

## License
This project is licensed under the MIT License.
