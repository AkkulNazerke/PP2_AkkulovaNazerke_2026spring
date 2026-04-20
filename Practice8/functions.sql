-- 1. Поиск по паттерну (имя, фамилия или телефон)
CREATE OR REPLACE FUNCTION search_pattern(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
       OR surname ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- 2. Пагинация (LIMIT + OFFSET)
CREATE OR REPLACE FUNCTION get_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;