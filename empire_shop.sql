
CREATE USER empire_user WITH PASSWORD 'empire_password';
GRANT ALL PRIVILEGES ON DATABASE empire_shop TO empire_user;

    GRANT ALL ON SCHEMA public TO empire_user;
    ALTER SCHEMA public OWNER TO empire_user;
CREATE TABLE shop_product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price NUMERIC(8,2) NOT NULL,
    product_type VARCHAR(10) NOT NULL CHECK (product_type IN ('tie', 'bowtie')),
    image VARCHAR(1000)
);

INSERT INTO shop_product (name, description, price, product_type, image) VALUES
('Классический галстук', 'Элегантный галстук для деловых встреч.', 1990.00, 'tie', NULL),
('Бабочка с узором', 'Яркая бабочка для особых случаев.', 1490.00, 'bowtie', NULL);

select * from shop_product