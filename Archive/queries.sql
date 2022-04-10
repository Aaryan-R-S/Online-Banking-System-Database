-- Query 1 [select, order by asc/desc]
SELECT IFSC_Code, Branch_Name, District, State
FROM Branch
ORDER BY State ASC, Branch_Name DESC;

-- Query 2 [insert]
INSERT INTO Branch_Managed_By
VALUES (100014, 10026, '2027-11-12', '2030-11-12');
SELECT * FROM Branch_Managed_By;
-- DELETE FROM Branch_managed_By WHERE Employee_Id = 10026;

-- Query 3 [update]
UPDATE Employee
SET Department = 1
WHERE Employee_ID = 10026;
SELECT * FROM Employee;

-- Query 4 [delete]
DELETE FROM Customer_Phone_Number
WHERE CIN = 100000400;
-- INSERT INTO Customer_Phone_Number
-- VALUES (100000400, 6679930452);
SELECT * FROM Customer_Phone_Number;

-- Query 5 [sum, if_null]
SELECT COALESCE(SUM(Collateral_Value), 0) 
AS Total_Collateral_Value
FROM Collateral;

-- Query 6 [case when then else]
SELECT Account_Number,
CASE
    WHEN Account_Balance > 500000 THEN 'The balance is greater than 5 lakhs'
    WHEN Account_Balance > 100000 THEN 'The balance is between 1 to 5 lakhs'
    ELSE 'The balance is under 1 lakh'
END AS Balance
FROM Bank_Account;

-- Query 7 [exists]
SELECT Card_Number,  Linked_Mobile_Number
FROM Card
WHERE EXISTS (SELECT * FROM Debit_Card WHERE Debit_Card.Card_Number = Card.Card_Number);

-- Query 8 [like]
SELECT * FROM Customer
WHERE City_Village_Town LIKE '%_pur';

-- Query 9 [between, and]
SELECT * FROM Transaction_Details
WHERE Transaction_Status = 'success' AND Transaction_Date_Time BETWEEN '2022-01-01 00:00:00' AND '2022-02-01 00:00:00';

-- Query 10 [count, group by, having]
SELECT COUNT(Account_Number) , Min_Balance_Required
FROM Bank_Account 
GROUP BY Min_Balance_Required
Having COUNT(Account_Number)>100;

-- Query 11 [join]
SELECT Account_Number, Card_Number, Cash_Withdrawl_Limit
FROM Bank_Account INNER JOIN ATM_Card ON Account_Number = Linked_Account
WHERE Account_Number = '11000000120';

-- Query 12 [alter table]
ALTER TABLE Employee
ADD CONSTRAINT chk_age CHECK (Age>=18);
-- ALTER TABLE Employee
-- DROP CONSTRAINT chk_age;
SELECT * FROM Employee;

-- Query 13 [create view]
CREATE VIEW JalandharCustomer AS
SELECT *
FROM Customer
WHERE City_Village_Town = 'Jalandhar';
SELECT * FROM JalandharCustomer;

-- Query 14 [authorization]
CREATE USER IF NOT EXISTS 'ars'@'localhost'
IDENTIFIED BY 'ars';

GRANT INSERT
ON online_banking_system.advertisement
TO 'ars'@'localhost';

SHOW GRANTS FOR 'ars'@'localhost';

REVOKE INSERT
ON online_banking_system.advertisement
FROM 'ars'@'localhost';

DROP USER IF EXISTS 'ars'@'localhost';