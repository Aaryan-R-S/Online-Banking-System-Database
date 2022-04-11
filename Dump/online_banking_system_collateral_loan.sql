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
-- Table structure for table `collateral_loan`
--

DROP TABLE IF EXISTS `collateral_loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collateral_loan` (
  `loan_id` mediumint unsigned NOT NULL,
  `collateral_id` int unsigned NOT NULL,
  `loan_type` enum('Vehicle','Home','Mortgage') NOT NULL,
  PRIMARY KEY (`loan_id`),
  UNIQUE KEY `collateral_id` (`collateral_id`),
  CONSTRAINT `collateral_loan_ibfk_1` FOREIGN KEY (`loan_id`) REFERENCES `loan` (`loan_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `collateral_loan_ibfk_2` FOREIGN KEY (`collateral_id`) REFERENCES `collateral` (`collateral_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collateral_loan`
--

LOCK TABLES `collateral_loan` WRITE;
/*!40000 ALTER TABLE `collateral_loan` DISABLE KEYS */;
INSERT INTO `collateral_loan` VALUES (10001,10001,'Home'),(10002,10002,'Home'),(10003,10003,'Home'),(10004,10004,'Home'),(10005,10005,'Home'),(10006,10006,'Home'),(10007,10007,'Home'),(10008,10008,'Home'),(10009,10009,'Home'),(10010,10010,'Home'),(10011,10011,'Home'),(10012,10012,'Home'),(10013,10013,'Home'),(10014,10014,'Home'),(10015,10015,'Home'),(10016,10016,'Home'),(10017,10017,'Home'),(10018,10018,'Vehicle'),(10019,10019,'Vehicle'),(10020,10020,'Vehicle'),(10021,10021,'Vehicle'),(10022,10022,'Vehicle'),(10023,10023,'Vehicle'),(10024,10024,'Vehicle'),(10025,10025,'Vehicle'),(10026,10026,'Vehicle'),(10027,10027,'Vehicle'),(10028,10028,'Vehicle'),(10029,10029,'Vehicle'),(10030,10030,'Vehicle'),(10031,10031,'Vehicle'),(10032,10032,'Vehicle'),(10033,10033,'Vehicle'),(10034,10034,'Vehicle'),(10035,10035,'Vehicle'),(10036,10036,'Vehicle'),(10037,10037,'Vehicle'),(10038,10038,'Vehicle');
/*!40000 ALTER TABLE `collateral_loan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-10 21:10:00
