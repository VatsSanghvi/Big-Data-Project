DBCC CHECKIDENT ('stores', RESEED, 0);

INSERT INTO stores (store_name, location, fk_owner_id, fk_manager_id)
VALUES
    ('Walmart', 'Location 1', 
        (SELECT user_id FROM users WHERE email = 'vats_admin@gmail.com'),
        (SELECT user_id FROM users WHERE email = 'vats_manager@gmail.com')),
    ('Zehrs', 'Location 2', 
        (SELECT user_id FROM users WHERE email = 'dev_admin@gmail.com'),
        (SELECT user_id FROM users WHERE email = 'dev_manager@gmail.com')),
    ('FreshCo', 'Location 3', 
        (SELECT user_id FROM users WHERE email = 'zeel_admin@gmail.com'),
        (SELECT user_id FROM users WHERE email = 'zeel_manager@gmail.com')),
    ('No Frills', 'Location 4', 
        (SELECT user_id FROM users WHERE email = 'andre_admin@gmail.com'),
        (SELECT user_id FROM users WHERE email = 'andre_manager@gmail.com')),
    ('Costco', 'Location 5', 
        (SELECT user_id FROM users WHERE email = 'diego_admin@gmail.com'),
        (SELECT user_id FROM users WHERE email = 'diego_manager@gmail.com'));
