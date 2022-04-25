USE online_banking_system;

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
SELECT Card_Number, Linked_Mobile_Number
FROM Card
WHERE EXISTS (SELECT * FROM Debit_Card WHERE Debit_Card.Card_Number =
Card.Card_Number);

-- Query 8 [like]
SELECT * FROM Customer
WHERE City_Village_Town LIKE '%_pur';

-- Query 9 [between, and]
SELECT * FROM Transaction_Details
WHERE Transaction_Status = 'success' AND Transaction_Date_Time BETWEEN
'2022-01-01 00:00:00' AND '2022-02-01 00:00:00';

-- Query 10 [count, group by, having]
SELECT COUNT(Account_Number) , Min_Balance_Required
FROM Bank_Account
GROUP BY Min_Balance_Required
Having COUNT(Account_Number)>100;

-- Query 11 [inner join all]
SELECT Account_Number, Card_Number, Cash_Withdrawl_Limit
FROM Bank_Account INNER JOIN ATM_Card ON Account_Number = Linked_Account;

-- Query 12 [left join]
SELECT Account_Number, Card_Number, Cash_Withdrawl_Limit
FROM Bank_Account LEFT JOIN ATM_Card ON Account_Number = Linked_Account;

-- Query 13 [inner join some]
SELECT Account_Number, Card_Number, Cash_Withdrawl_Limit
FROM Bank_Account INNER JOIN ATM_Card ON Account_Number = Linked_Account
WHERE Account_Number = '11000000120';

-- Query 14 [union names]
SELECT first_name FROM Customer
UNION
SELECT first_name FROM Employee
ORDER BY first_name;

-- Query 15 [alter table]
ALTER TABLE Employee
ADD CONSTRAINT chk_age CHECK (Age>=18);
-- ALTER TABLE Employee
-- DROP CONSTRAINT chk_age;
SELECT * FROM Employee;

-- Query 16 [create view]
CREATE VIEW JalandharCustomer AS
SELECT *
FROM Customer
WHERE City_Village_Town = 'Jalandhar';
SELECT * FROM JalandharCustomer;

-- Query 17 [authorization]
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

-- [View 1]
CREATE VIEW JalandharCustomer AS SELECT * FROM Customer WHERE City_Village_Town = 'Jalandhar';
-- [View 2]
CREATE VIEW HighDefaultCustomer AS SELECT * FROM Loan WHERE loan_amount >= 200000;
-- [View 3]
CREATE VIEW HighUpiTransactions AS SELECT * FROM upi_transactions WHERE transaction_amount >= 40000;
-- [View 4]
CREATE VIEW MedicalInsuranceID AS SELECT medical_insurance.policy_id, insurance.nominee_id, insurance.policy_start_date, insurance.policy_duration_years, insurance.premium_amount FROM medical_insurance inner join insurance on medical_insurance.policy_id = insurance.policy_id;

-- [Grant 1]
CREATE USER IF NOT EXISTS 'advt_board'@'localhost'
IDENTIFIED BY 'advt_board';
GRANT SELECT, INSERT, UPDATE, DELETE
ON advertisement
TO 'advt_board'@'localhost';
SHOW GRANTS FOR 'advt_board'@'localhost';
-- REVOKE INSERT
-- ON advertisement
-- FROM 'advt_board'@'localhost';
-- DROP USER IF EXISTS 'advt_board'@'localhost';

-- [Grant 2]
CREATE USER IF NOT EXISTS 'collateral_dept'@'localhost'
IDENTIFIED BY 'collateral_dept';
GRANT SELECT, INSERT, UPDATE, DELETE
ON collateral
TO 'collateral_dept'@'localhost';
SHOW GRANTS FOR 'collateral_dept'@'localhost';
-- REVOKE INSERT
-- ON collateral
-- FROM 'collateral_dept'@'localhost';
-- DROP USER IF EXISTS 'collateral_dept'@'localhost';

-- [Index 1]
-- customer->pincode
CREATE INDEX `idx_customer_pincode`  ON `online_banking_system`.`customer` (pincode) COMMENT '' ALGORITHM DEFAULT LOCK DEFAULT;
-- [Index 2]
-- employee->department
CREATE INDEX `idx_employee_department`  ON `online_banking_system`.`employee` (department) COMMENT '' ALGORITHM DEFAULT LOCK DEFAULT;
-- [Index 3]
-- bank_account->account_balance
CREATE INDEX `idx_bank_account_account_balance`  ON `online_banking_system`.`bank_account` (account_balance) COMMENT '' ALGORITHM DEFAULT LOCK DEFAULT;
-- [Index 4]
-- loan->loan_end_date
CREATE INDEX `idx_loan_loan_end_date`  ON `online_banking_system`.`loan` (loan_end_date) COMMENT '' ALGORITHM DEFAULT LOCK DEFAULT;
-- [Index 5]
-- upi->upi_id
CREATE INDEX `idx_upi_upi_id`  ON `online_banking_system`.`upi` (upi_id) COMMENT '' ALGORITHM DEFAULT LOCK DEFAULT;
-- [Index 6]
-- insurance->nominee_id
CREATE INDEX `idx_insurance_nominee_id`  ON `online_banking_system`.`insurance` (nominee_id) COMMENT '' ALGORITHM DEFAULT LOCK DEFAULT;

-- [Trigger 1]
DROP TRIGGER IF EXISTS `online_banking_system`.`bank_account_BEFORE_INSERT`;
DELIMITER $$
USE `online_banking_system`$$
CREATE DEFINER = CURRENT_USER TRIGGER `online_banking_system`.`bank_account_BEFORE_INSERT` BEFORE INSERT ON `bank_account` FOR EACH ROW
BEGIN
	IF NEW.account_balance < NEW.min_balance_required THEN SET NEW.account_balance = NEW.min_balance_required;
END IF;  
END$$
DELIMITER ;

-- [Trigger 2]
DROP TRIGGER IF EXISTS `online_banking_system`.`card_BEFORE_INSERT`;
DELIMITER $$
USE `online_banking_system`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `card_BEFORE_INSERT` BEFORE INSERT ON `card` FOR EACH ROW BEGIN
	IF NEW.expiry_date < NEW.issued_date THEN SET NEW.expiry_date = NEW.issued_date+1;
END IF; 
END$$
DELIMITER ;

-- [Trigger 3]
DROP TRIGGER IF EXISTS `online_banking_system`.`fixed_deposit_BEFORE_INSERT`;
DELIMITER $$
USE `online_banking_system`$$
CREATE DEFINER = CURRENT_USER TRIGGER `online_banking_system`.`fixed_deposit_BEFORE_INSERT` BEFORE INSERT ON `fixed_deposit` FOR EACH ROW
BEGIN
	IF NEW.duration_years = 0 THEN SET NEW.duration_years = 1;
end if;
END$$
DELIMITER ;


-- [Trigger 4]
DROP TRIGGER IF EXISTS `online_banking_system`.`recurring_deposit_BEFORE_INSERT`;
DELIMITER $$
USE `online_banking_system`$$
CREATE DEFINER = CURRENT_USER TRIGGER `online_banking_system`.`recurring_deposit_BEFORE_INSERT` BEFORE INSERT ON `recurring_deposit` FOR EACH ROW
BEGIN
	IF NEW.duration_years = 0 THEN SET NEW.duration_years = 1;
end if;
END$$
DELIMITER ;

SHOW TRIGGERS;
