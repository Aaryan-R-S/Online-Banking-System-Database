-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: online_banking_system
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `highupitransactions`
--

DROP TABLE IF EXISTS `highupitransactions`;
/*!50001 DROP VIEW IF EXISTS `highupitransactions`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `highupitransactions` AS SELECT 
 1 AS `upi_transaction_id`,
 1 AS `from_upi_id`,
 1 AS `to_upi_id`,
 1 AS `transaction_date_time`,
 1 AS `transaction_status`,
 1 AS `transaction_amount`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `highdefaultcustomer`
--

DROP TABLE IF EXISTS `highdefaultcustomer`;
/*!50001 DROP VIEW IF EXISTS `highdefaultcustomer`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `highdefaultcustomer` AS SELECT 
 1 AS `loan_id`,
 1 AS `loan_amount`,
 1 AS `interest_rate`,
 1 AS `tenure_months`,
 1 AS `loan_issued_date`,
 1 AS `loan_end_date`,
 1 AS `loan_given_to`,
 1 AS `emi_amount`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `medicalinsuranceid`
--

DROP TABLE IF EXISTS `medicalinsuranceid`;
/*!50001 DROP VIEW IF EXISTS `medicalinsuranceid`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `medicalinsuranceid` AS SELECT 
 1 AS `policy_id`,
 1 AS `nominee_id`,
 1 AS `policy_start_date`,
 1 AS `policy_duration_years`,
 1 AS `premium_amount`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `jalandharcustomer`
--

DROP TABLE IF EXISTS `jalandharcustomer`;
/*!50001 DROP VIEW IF EXISTS `jalandharcustomer`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `jalandharcustomer` AS SELECT 
 1 AS `cin`,
 1 AS `pan_number`,
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `building`,
 1 AS `street`,
 1 AS `city_village_town`,
 1 AS `district`,
 1 AS `state`,
 1 AS `pincode`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `highupitransactions`
--

/*!50001 DROP VIEW IF EXISTS `highupitransactions`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `highupitransactions` AS select `upi_transactions`.`upi_transaction_id` AS `upi_transaction_id`,`upi_transactions`.`from_upi_id` AS `from_upi_id`,`upi_transactions`.`to_upi_id` AS `to_upi_id`,`upi_transactions`.`transaction_date_time` AS `transaction_date_time`,`upi_transactions`.`transaction_status` AS `transaction_status`,`upi_transactions`.`transaction_amount` AS `transaction_amount` from `upi_transactions` where (`upi_transactions`.`transaction_amount` >= 40000) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `highdefaultcustomer`
--

/*!50001 DROP VIEW IF EXISTS `highdefaultcustomer`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `highdefaultcustomer` AS select `loan`.`loan_id` AS `loan_id`,`loan`.`loan_amount` AS `loan_amount`,`loan`.`interest_rate` AS `interest_rate`,`loan`.`tenure_months` AS `tenure_months`,`loan`.`loan_issued_date` AS `loan_issued_date`,`loan`.`loan_end_date` AS `loan_end_date`,`loan`.`loan_given_to` AS `loan_given_to`,`loan`.`emi_amount` AS `emi_amount` from `loan` where (`loan`.`loan_amount` >= 200000) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `medicalinsuranceid`
--

/*!50001 DROP VIEW IF EXISTS `medicalinsuranceid`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `medicalinsuranceid` AS select `medical_insurance`.`policy_id` AS `policy_id`,`insurance`.`nominee_id` AS `nominee_id`,`insurance`.`policy_start_date` AS `policy_start_date`,`insurance`.`policy_duration_years` AS `policy_duration_years`,`insurance`.`premium_amount` AS `premium_amount` from (`medical_insurance` join `insurance` on((`medical_insurance`.`policy_id` = `insurance`.`policy_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `jalandharcustomer`
--

/*!50001 DROP VIEW IF EXISTS `jalandharcustomer`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `jalandharcustomer` AS select `customer`.`cin` AS `cin`,`customer`.`pan_number` AS `pan_number`,`customer`.`first_name` AS `first_name`,`customer`.`last_name` AS `last_name`,`customer`.`building` AS `building`,`customer`.`street` AS `street`,`customer`.`city_village_town` AS `city_village_town`,`customer`.`district` AS `district`,`customer`.`state` AS `state`,`customer`.`pincode` AS `pincode` from `customer` where (`customer`.`city_village_town` = 'Jalandhar') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:12:06
