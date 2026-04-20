-- 1. INSERT или UPDATE (UPSERT)
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- 2. Массовая вставка с проверкой телефона
CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        -- проверка: только цифры и длина >= 10
        IF phones[i] ~ '^[0-9]{10,}$' THEN
            CALL insert_or_update_user(names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: %', phones[i];
        END IF;
    END LOOP;
END;
$$;


-- 3. Удаление по имени или телефону
CREATE OR REPLACE PROCEDURE delete_user(value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = value OR phone = value;
END;
$$;