

CREATE TABLE IF NOT EXISTS Units (
    unit_id SMALLSERIAL PRIMARY KEY,
    unit_name VARCHAR (50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS FoodNames (
    food_id SERIAL PRIMARY KEY,
    food_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS NutritionData (
    food_id INT PRIMARY KEY,
    serving_size INT NOT NULL,
    calories INT NOT NULL,
    total_fat INT NOT NUll,
    saturated_fat INT NOT NUll,
    trans_fat INT NOT NUll,
    polyunsaturated_fat INT NOT NUll,
    monounsaturated_fat INT NOT NUll,
    cholesterol INT NOT NUll,
    sodium INT NOT NUll,
    potassium INT NOT NUll,
    total_carbohydrates INT NOT NUll,
    dietary_fiber INT NOT NUll,
    soluble_fiber INT NOT NUll,
    dietary_sugars INT NOT NUll,
    total_sugars INT NOT NUll,
    added_sugars INT NOT NUll,
    erythritol INT NOT NUll,
    protein INT NOT NUll,
    FOREIGN KEY (food_id) REFERENCES FoodNames(food_id) ON DELETE CASCADE
);
