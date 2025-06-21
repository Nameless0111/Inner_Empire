
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
-- Категории
-- Категории
INSERT INTO store_категория (название) VALUES
('Галстуки'),
('Бабочки'),
('Аксессуары');

-- Производители
INSERT INTO store_производитель (название, страна, сайт) VALUES
('TieMaster', 'Россия', 'https://tiemaster.ru'),
('BowStyle', 'Италия', 'https://bowstyle.it');

-- Материалы
INSERT INTO store_материал (название, описание, экологичный) VALUES
('Шелк', 'Натуральный шелк', TRUE),
('Хлопок', 'Высококачественный хлопок', TRUE),
('Полиэстер', 'Синтетический материал', FALSE);

-- Товары
INSERT INTO store_товар (название, описание, цена, тип, производитель_id, категория_id)
VALUES
('Классический галстук', 'Элегантный галстук для деловых встреч.', 1990.00, 'галстук', 1, 1),
('Бабочка с узором', 'Яркая бабочка для особых случаев.', 1490.00, 'бабочка', 2, 2);

-- Материалы товаров (связь многие-ко-многим)
INSERT INTO store_материалтовара (товар_id, материал_id) VALUES
(1, 1), -- Классический галстук - Шелк
(2, 2); -- Бабочка с узором - Хлопок