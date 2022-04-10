-- for testing and recreation
-- DROP DATABASE online_banking_system;

-- created the database => online_banking
CREATE DATABASE online_banking_system;
USE online_banking_system;

-- super-table for general account 
create table bank_account(
	account_number bigint unsigned not null,
    date_of_opening date not null default (curdate()),
    min_balance_required mediumint unsigned not null default(0),
    account_balance int default (0),
    ifsc_code mediumint unsigned NOT NULL,
    interest_rate tinyint unsigned default (0),
    withdrawal_limit int unsigned default (10000),
    
    primary key (account_number)
);
alter table bank_account auto_increment=10000000000; -- 11 digit account number 

-- table Branch
create table branch(
	ifsc_code mediumint unsigned NOT NULL auto_increment,
    branch_name varchar(25) NOT NULL, 
    branch_account_number bigint unsigned not null,
    -- address components
    street varchar(50) NOT NULL,    
    city_village_town varchar(25) NOT NULL,
    district varchar(25) NOT NULL,
    state varchar(25) NOT NULL,
    pincode mediumint NOT NULL,
    check (pincode>=100000 and pincode<=999999),
    
    opening_date DATE NOT NULL,
    -- all the constraint
    UNIQUE (branch_name),
    PRIMARY KEY (ifsc_code)
    -- foreign key (branch_account_number) references bank_account(account_number)
);
alter table branch auto_increment=10000;
alter table bank_account add foreign key (ifsc_code) references branch(ifsc_code);
alter table branch add foreign key (branch_account_number) references bank_account(account_number);

-- table department
create table department(
	department_id smallint unsigned not null,
    department_name varchar(25),
    
    unique(department_name),
    primary key (department_id)
);

-- table Employee
create table employee(
	employee_id SMALLINT UNSIGNED NOT NULL auto_increment,
    pan_number char(10) NOT NULL,
    aadhaar_number char(12) NOT NULL,
    first_name varchar(15) NOT NULL,
    last_name varchar(15) NOT NULL,
    employee_account_number bigint unsigned not null,
    department smallint unsigned not null,
    -- address components
    apartment varchar(25) NOT NULL,
    street varchar(50) NOT NULL,
    city_village_town varchar(25) NOT NULL,
	district varchar(25) NOT NULL,
    state varchar(25) NOT NULL,
    pincode mediumint NOT NULL,
    check (pincode>=100000 and pincode <=999999),
    dob DATE NOT NULL,
    age SMALLINT UNSIGNED NOT NULL,
    employee_phone_number bigint unsigned NOT NULL, -- only one phone number for employee
    ifsc_code mediumint unsigned NOT NULL,
    photo blob NOT NULL,
    
    foreign key (ifsc_code) references branch(ifsc_code),
    foreign key (employee_account_number) references bank_account(account_number),
    foreign key (department) references department(department_id),
    check(employee_phone_number >= 1000000000 and employee_phone_number <= 9999999999),
    CHECK(age>=18),
    PRIMARY KEY (employee_id),
    UNIQUE (pan_number, aadhaar_number)
);

-- relation table manages
create table branch_managed_by(
	ifsc_code mediumint unsigned NOT NULL,
    employee_id SMALLINT UNSIGNED NOT NULL,
    manages_from date NOT NULL,
    manages_till date,
    
    primary key(ifsc_code,employee_id, manages_from),
    foreign key (ifsc_code) references branch(ifsc_code),
    foreign key (employee_id) references employee(employee_id)
);

-- super-table customer
create table customer(
	cin int unsigned not null auto_increment, -- should be of length 9
    pan_number char(10) NOT NULL,
    first_name varchar(15) NOT NULL,
    last_name varchar(15) NOT NULL,
    -- address components
	building varchar(50) NOT NULL,
    street varchar(50) NOT NULL,
    city_village_town varchar(50) NOT NULL,
	district varchar(50) NOT NULL,
    state varchar(50) NOT NULL,
    pincode mediumint NOT NULL,
    check (pincode>=100000 and pincode <=999999),
    
    UNIQUE (pan_number),
    primary key (cin)
);
alter table customer auto_increment=100000000;

-- table for customer phone number
create table customer_phone_number(
    cin int unsigned not null,
	phone_number bigint unsigned not null,
    
    primary key (cin,phone_number),
    check(phone_number >= 1000000000 and phone_number <= 9999999999),
    foreign key (cin) references customer(cin)
);

-- table for collateral
create table collateral(
	collateral_id int unsigned not null auto_increment,
    collateral_name varchar(25) not null,
    collateral_value int unsigned not null default(0),
    collateral_owner int unsigned not null,
    
    foreign key (collateral_owner) references customer(cin),
    primary key (collateral_id)
);
alter table collateral auto_increment=1;

-- table for documents link
create table documents_link(
	document_id int unsigned not null auto_increment,
    collateral_id int unsigned not null,
    document_link varchar(100) not null,
    
    foreign key (collateral_id) references collateral(collateral_id),
    primary key (document_id, collateral_id)
);
alter table documents_link auto_increment=1;

-- sub-table personal_customer
create table personal_customer(
	cin int unsigned not null,
    aadhaar_number char(12) NOT NULL,
    dob DATE NOT NULL,
    age SMALLINT UNSIGNED NOT NULL,
    photo blob NOT NULL,
    
    check(age>=18),
    UNIQUE (aadhaar_number),
    primary key (cin),
    foreign key (cin) references customer(cin)
);

-- sub-table business_customer
create table business_customer(
	gst varchar(20) not null, -- also contains pan number
	cin int unsigned not null,
    business_name varchar(40) NOT NULL,
    business_logo blob NOT NULL,
    
    UNIQUE (gst),
    primary key (cin),
    foreign key (cin) references customer(cin)
);

-- sub-table for Savings account
create table savings_account(
	account_number bigint unsigned not null,
    cin int unsigned not null,
    
    primary key (account_number),
    unique(cin),
    foreign key (account_number) references bank_account(account_number),
    foreign key (cin) references personal_customer(cin)
);

-- sub-table for current account
create table current_account(
	account_number bigint unsigned not null,
    cin int unsigned not null,
    maintance_charges smallint unsigned default (0), 
    
    primary key (account_number),
    unique(cin),
    foreign key (account_number) references bank_account(account_number),
    foreign key (cin) references business_customer(cin)
);

-- sub-table for minor_account
create table minor_account(
	minor_first_name varchar(15) NOT NULL,
    minor_last_name varchar(15) NOT NULL,
	account_number bigint unsigned not null, -- minor's account# (put pan_number='XXXXXXXXXX')
    parent_cin int unsigned not null,
    parent_account_number bigint unsigned not null,
    
    primary key (account_number),
    unique(parent_cin),
    foreign key (parent_account_number) references savings_account(account_number),
    foreign key (account_number) references bank_account(account_number),
    foreign key (parent_cin) references personal_customer(cin)
);

-- sub-table for zero balance account
create table zero_balance_account(
	-- interest rate=0 ; min_balance_required=0 ; withdrawal_limit=10000
	account_number bigint unsigned not null,
    cin int unsigned not null,
    
    primary key (account_number),
    unique(cin),
    foreign key (account_number) references bank_account(account_number),
    foreign key (cin) references personal_customer(cin)
);

-- super-table for card 
create table card(
	card_number bigint unsigned NOT NULL auto_increment,
    linked_mobile_number bigint unsigned NOT NULL,
    card_pin smallint unsigned NOT NULL,
    issued_date date not null default(curdate()),
    expiry_date date not null,
    cvv smallint unsigned not null,
    daily_limit int unsigned default(2000),
    monthly_limit int unsigned default(10000),
    
    check(linked_mobile_number >= 1000000000 and linked_mobile_number <= 9999999999),
    check(monthly_limit > daily_limit),
    primary key (card_number)
);
alter table card auto_increment=1000000000000000; -- 16 digit card number

-- sub-table for debit card
create table debit_card(
	card_number bigint unsigned NOT NULL,
	linked_account bigint unsigned not null,
    
    primary key (card_number),
    foreign key (card_number) references card(card_number),
    foreign key (linked_account) references bank_account(account_number)
);

-- sub-table for PREPAID CARD
create table prepaid_card(
	card_number bigint unsigned NOT NULL,
	cin int unsigned not null, -- prepaid_card only allowed to personal customer
    prepaid_balance mediumint unsigned default(0),
    
    primary key (card_number),
    foreign key (card_number) references card(card_number),
    foreign key (cin) references personal_customer(cin)
);

-- sub-table for ATM CARD
create table atm_card(
	card_number bigint unsigned NOT NULL,
	linked_account bigint unsigned not null,
    cash_withdrawl_limit smallint unsigned default (2000), 
    
    primary key (card_number),
    foreign key (card_number) references card(card_number),
    foreign key (linked_account) references bank_account(account_number)
);

-- sub-table for CREDIT CARD
create table credit_card(
	card_number bigint unsigned NOT NULL,
	cin int unsigned not null,
    billing_date date default(curdate()),
    due_date date default(curdate()+20),
    credit_limit mediumint not null default(0),
    total_amount_due mediumint not null default (0),
    rewards_point smallint unsigned default(0),
    minimum_amount_due mediumint default(total_amount_due*0.05),
    
    primary key (card_number),
    foreign key (cin) references customer(cin),
    foreign key (card_number) references card(card_number)
);

-- account link credit card table relation many to many
create table account_linked_creditcard(
	card_number bigint unsigned NOT NULL,
    linked_account bigint unsigned not null,
    
    primary key (card_number, linked_account),
    foreign key (card_number) references credit_card(card_number),
    foreign key (linked_account) references bank_account(account_number)
);

-- super- table for loan
create table loan(
	loan_id mediumint unsigned not null auto_increment,
    loan_amount int unsigned not null,
    interest_rate tinyint unsigned not null,
    tenure_months smallint unsigned not null default(0),
    loan_issued_date date default(curdate()),
    loan_end_date date default(loan_issued_date+(tenure_months*30)),
    loan_given_to int unsigned not null,
    emi_amount int unsigned default(loan_amount/tenure_months),
    
    primary key(loan_id),
    foreign key (loan_given_to) references customer(cin)
); 
alter table loan auto_increment=1;

-- sub-table for collateral_loan
create table collateral_loan(
	loan_id mediumint unsigned not null,
    collateral_id int unsigned not null,
    loan_type ENUM('Vehicle', 'Home', 'Mortgage') not null,
    
    primary key(loan_id),
    unique(collateral_id), -- only one loan per collateral is allowed
    foreign key (loan_id) references loan(loan_id),
    foreign key (collateral_id) references collateral(collateral_id)
);

-- sub-table for non_collateral_loan
create table non_collateral_loan(
	loan_id mediumint unsigned not null,
    loan_type ENUM('Personal', 'Educational', 'Business', 'Rural Development') not null,
    
    primary key(loan_id),
    foreign key (loan_id) references loan(loan_id)
);

-- table for documents
create table documents_pdf(
	document_id int unsigned not null auto_increment,
    loan_id mediumint unsigned not null,
    document_pdf mediumblob not null,
    
    foreign key (loan_id) references non_collateral_loan(loan_id),
    primary key (document_id, loan_id)
);
alter table documents_pdf auto_increment=1;

-- sub-table for loan-account
create table loan_account(
	account_number bigint unsigned not null,
    loan_id mediumint unsigned not null,
    
    primary key (loan_id),
    foreign key (account_number) references bank_account(account_number),
    foreign key (loan_id) references loan(loan_id)
);

-- table for insurance
create table insurance(
	policy_id int unsigned not null auto_increment,
    policy_start_date date default(curdate()),
    policy_duration_years tinyint unsigned default(1),
    policy_expiry_date date default (policy_start_date+365),
    premium_amount mediumint unsigned not null,
    sum_insured mediumint unsigned not null,
    unclaimed_amount mediumint unsigned default(sum_insured),
    nominee_id int unsigned not null,
    
    primary key(policy_id),
    foreign key (nominee_id) references customer(cin)
);
alter table insurance auto_increment=1;

-- table for asset insurance
create table asset_insurance(
	policy_id int unsigned not null,
    asset_document blob not null,
    asset_value mediumint unsigned not null,
    
    primary key(policy_id),
    foreign key (policy_id) references insurance(policy_id)
);

-- table for loan protection insurance
create table loan_protection_insurance(
	policy_id int unsigned not null,
    loan_id mediumint unsigned not null,
    
    primary key(policy_id),
    foreign key (policy_id) references insurance(policy_id),
    foreign key (loan_id) references loan(loan_id)
);

-- table for term life insurance
create table term_life_insurance(
	policy_id int unsigned not null,
    insured_person int unsigned not null,
    
    primary key(policy_id),
    foreign key (policy_id) references insurance(policy_id),
    foreign key (insured_person) references personal_customer(cin)
);

-- table for medical insurance
create table medical_insurance(
	policy_id int unsigned not null,
    insured_person int unsigned not null,
    
    primary key(policy_id, insured_person),
    foreign key (policy_id) references insurance(policy_id),
    foreign key (insured_person) references personal_customer(cin)
);

-- table for transaction_details
create table transaction_details(
	transaction_id int unsigned not null auto_increment,
    from_account_number bigint unsigned not null,
    to_account_number bigint unsigned not null,
    transaction_date_time datetime default(CURRENT_TIMESTAMP()),
    transaction_status enum('success', 'failed') not null default('failed'),
    transaction_amount mediumint unsigned not null,
    transaction_type enum('NEFT', 'RTGS', 'IMPS'),
    
    primary key (transaction_id),
    foreign key (from_account_number) references bank_account(account_number),
    foreign key (to_account_number) references bank_account(account_number)
);
alter table transaction_details auto_increment=1;

-- table for passbook
create table passbook(
	barcode mediumint unsigned not null auto_increment,
    passbook_account_number bigint unsigned not null,
    date_issued date default(curdate()),
    date_last_printed date default (curdate()),
    
    primary key (barcode), -- 6 digit barcode
    foreign key (passbook_account_number) references bank_account(account_number)
);
alter table passbook auto_increment=100000;

-- table for UPI accounts
create table upi(
	upi_id varchar(15) not null,
    account_number_linked bigint unsigned not null,
    active_status bool not null default(false),
    last_used date not null,
    transaction_limit_remaining mediumint unsigned not null default(0),
    
    check(locate('@bank',upi_id)>0), -- upi_id should contain @bank at last
    primary key (upi_id),
    foreign key (account_number_linked) references bank_account(account_number)
);

-- table for upi transactions
create table upi_transactions(
	upi_transaction_id int unsigned not null auto_increment,
    from_upi_id varchar(15) not null,
    to_upi_id varchar(15) not null,
    transaction_date_time datetime default(CURRENT_TIMESTAMP()),
    transaction_status enum('success', 'failed') not null default('failed'),
    transaction_amount mediumint unsigned not null,
    
    primary key(upi_transaction_id),
    foreign key (from_upi_id) references upi(upi_id),
    foreign key (to_upi_id) references upi(upi_id)
);
alter table upi_transactions auto_increment=1;

-- table for bill payment 
create table bill_payment(
	bill_id bigint unsigned not null,
    transaction_id int unsigned not null,
    
    primary key (bill_id),
    unique(transaction_id),
    foreign key (transaction_id) references transaction_details(transaction_id)
);

-- table for card transactions
create table card_transactions(
	transaction_id int unsigned not null,
    from_card_number bigint unsigned NOT NULL,
    to_card_number bigint unsigned NOT NULL,
	transaction_date_time datetime default(CURRENT_TIMESTAMP()),
    transaction_status enum('success', 'failed') not null default('failed'),
    transaction_amount mediumint unsigned not null,
    
    primary key (transaction_id),
    foreign key (transaction_id) references transaction_details(transaction_id),
    foreign key (from_card_number) references card(card_number),
	foreign key (to_card_number) references card(card_number)
);

-- table for auto payment 
create table auto_payment(
	auto_payment_id mediumint unsigned not null auto_increment,
    payment_date date not null,
    payment_frequency smallint unsigned not null default(1),
    autodebit_account_number bigint unsigned not null,
    
    primary key(auto_payment_id),
    foreign key (autodebit_account_number) references bank_account(account_number)
);
alter table auto_payment auto_increment=1;


-- table for auto payment loan
create table auto_payment_loan(
	auto_payment_id mediumint unsigned not null,
    linked_loan_account bigint unsigned not null,
    
    primary key (auto_payment_id),
    foreign key (auto_payment_id) references auto_payment(auto_payment_id),
    foreign key (linked_loan_account) references loan_account(account_number)
);

-- table for auto bill payment 
create table auto_bill_payment(
	auto_payment_id mediumint unsigned not null,
    bill_id bigint unsigned not null,
    
    primary key (auto_payment_id),
    foreign key (auto_payment_id) references auto_payment(auto_payment_id),
    foreign key (bill_id) references bill_payment(bill_id)
);

-- table for transaction log
create table transaction_log(
	log_id mediumint unsigned not null auto_increment,
    log_date_time datetime default (CURRENT_TIMESTAMP()),
    transaction_id int unsigned not null,
    log_file blob not null,
    
    primary key (log_id),
    foreign key (transaction_id) references transaction_details(transaction_id)
);
alter table transaction_log auto_increment=1;

-- table for advertisement 


-- table for channel
create table ad_channel(
	channel_id mediumint unsigned not null auto_increment,
    channel_name varchar(15) not null,
    channel_link varchar(100) not null,
    
    primary key (channel_id),
    unique(channel_link)
);
alter table ad_channel auto_increment=1;

-- table for advertisement 
create table advertisement(
	advertisemnt_id int unsigned not null auto_increment,
    total_cost mediumint unsigned not null,
    ad_type enum('social-media', 'offline', 'on-site', 'other-online') not null,
    channel_id mediumint unsigned not null,
    authorized_by SMALLINT UNSIGNED NOT NULL,
    
    primary key (advertisemnt_id),
    foreign key (channel_id) references ad_channel(channel_id),
    foreign key (authorized_by) references employee(employee_id)
);
alter table advertisement auto_increment=1;

-- table for user credentials
create table user_credential(
	user_login_id varchar(25) not null,
	user_login_password varchar(25) not null,
    user_id int unsigned not null,
    
    primary key (user_login_id),
    unique(user_login_id),
    foreign key (user_id) references customer(cin)
);

-- table for employee credentials
create table employee_credential(
	employee_login_id varchar(25) not null,
	employee_login_password varchar(25) not null,
    employee_id SMALLINT UNSIGNED NOT NULL,
    
    primary key (employee_login_id),
    unique(employee_login_id),
    foreign key (employee_id) references employee(employee_id)
);

-- table for fixed deposit
create table fixed_deposit(
	account_number bigint unsigned not null,
	cin int unsigned not null,
    start_date date default(curdate()),
    duration_years tinyint unsigned default(1),
    maturity_date date default (start_date+365),
    fixed_amount mediumint unsigned not null,
    interest_rate mediumint unsigned default (0),
    
    primary key (account_number),
	foreign key (account_number) references bank_account(account_number),
	foreign key (cin) references customer(cin)
);

-- table for recurring deposit
create table recurring_deposit(
	account_number bigint unsigned not null,
	cin int unsigned not null,
    start_date date default(curdate()),
    duration_years mediumint unsigned default(1),
    maturity_date date default (start_date+365),
    monthly_deposit_amount mediumint unsigned not null,
    interest_rate mediumint unsigned default (0),
    
    primary key (account_number),
	foreign key (account_number) references bank_account(account_number),
	foreign key (cin) references customer(cin)
);

-- table for chequebook
create table chequebook(
    account_number bigint unsigned not null,
	micr_code bigint unsigned NOT NULL,	-- 9 digit code
    date_issued date default(curdate()),
    starting_cheque_number bigint unsigned NOT NULL,
    pages int unsigned NOT NULL,
    
    primary key (account_number),
    foreign key (account_number) references bank_account(account_number)
);

-- table for bank statements
create table bank_statement(
    account_number bigint unsigned not null,
	date_issued date default(curdate()),
    info_from_date date default(curdate()),
	info_till_date date default(curdate()+30),
    
    primary key (account_number),
    foreign key (account_number) references bank_account(account_number)
);

-- table for OTPs
SET time_zone='+05:30';
create table otps(
	account_number bigint unsigned not null,
	cin int unsigned not null,
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valid_till TIMESTAMP default (valid_from + INTERVAL 5 MINUTE),
    otp mediumint unsigned NOT null,
    
    primary key (cin, valid_from),
	foreign key (account_number) references bank_account(account_number),
	foreign key (cin) references customer(cin)
);

-- table for installments
create table installment(
	loan_id mediumint unsigned not null,
    transaction_date_time datetime default(CURRENT_TIMESTAMP()),
    transaction_status enum('success', 'failed') not null default('failed'),
    transaction_amount mediumint unsigned not null,
    transaction_type enum('NEFT', 'RTGS', 'IMPS'),
    
    primary key (loan_id, transaction_date_time),
    foreign key (loan_id) references loan(loan_id)
);

-- end of online-banking_ayatem --