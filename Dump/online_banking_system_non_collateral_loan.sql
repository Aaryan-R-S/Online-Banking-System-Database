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
-- Table structure for table `non_collateral_loan`
--

DROP TABLE IF EXISTS `non_collateral_loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `non_collateral_loan` (
  `loan_id` mediumint unsigned NOT NULL,
  `loan_type` enum('Personal','Educational','Business','Rural Development') NOT NULL,
  PRIMARY KEY (`loan_id`),
  CONSTRAINT `non_collateral_loan_ibfk_1` FOREIGN KEY (`loan_id`) REFERENCES `loan` (`loan_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `non_collateral_loan`
--

LOCK TABLES `non_collateral_loan` WRITE;
/*!40000 ALTER TABLE `non_collateral_loan` DISABLE KEYS */;
INSERT INTO `non_collateral_loan` VALUES (10051,'Personal'),(10052,'Personal'),(10053,'Personal'),(10054,'Personal'),(10055,'Personal'),(10056,'Personal'),(10057,'Business'),(10058,'Business'),(10059,'Business'),(10060,'Business'),(10061,'Business'),(10062,'Business'),(10063,'Business'),(10064,'Business'),(10065,'Business'),(10066,'Business'),(10067,'Educational'),(10068,'Educational'),(10069,'Educational'),(10070,'Educational'),(10071,'Rural Development'),(10072,'Rural Development'),(10073,'Rural Development'),(10074,'Rural Development'),(10075,'Rural Development');
/*!40000 ALTER TABLE `non_collateral_loan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:11:54
