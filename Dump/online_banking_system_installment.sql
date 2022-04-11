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
-- Table structure for table `installment`
--

DROP TABLE IF EXISTS `installment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `installment` (
  `loan_id` mediumint unsigned NOT NULL,
  `transaction_date_time` datetime NOT NULL DEFAULT (now()),
  `transaction_status` enum('success','failed') NOT NULL DEFAULT (_utf8mb4'failed'),
  `transaction_amount` mediumint unsigned NOT NULL,
  `transaction_type` enum('NEFT','RTGS','IMPS') DEFAULT NULL,
  PRIMARY KEY (`loan_id`,`transaction_date_time`),
  CONSTRAINT `installment_ibfk_1` FOREIGN KEY (`loan_id`) REFERENCES `loan` (`loan_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `installment`
--

LOCK TABLES `installment` WRITE;
/*!40000 ALTER TABLE `installment` DISABLE KEYS */;
INSERT INTO `installment` VALUES (10003,'2022-01-04 11:07:55','success',1412788,'IMPS'),(10004,'2022-01-17 02:31:15','success',707333,'IMPS'),(10005,'2022-01-04 01:55:07','failed',1876154,'RTGS'),(10006,'2022-02-02 14:11:18','success',1618014,'RTGS'),(10007,'2022-01-10 15:41:22','success',90490,'NEFT'),(10008,'2022-02-23 06:12:24','success',2808450,'RTGS'),(10009,'2022-02-21 01:19:37','failed',2154596,'RTGS'),(10011,'2022-01-15 17:35:27','success',624453,'IMPS'),(10012,'2022-01-23 06:56:58','success',1181712,'IMPS'),(10014,'2022-01-04 05:10:36','success',683240,'IMPS'),(10015,'2022-01-05 17:10:24','failed',2816326,'RTGS'),(10015,'2022-01-27 11:31:42','success',1441305,'IMPS'),(10019,'2022-02-24 04:56:44','failed',1408054,'IMPS'),(10019,'2022-02-25 15:06:59','success',1926468,'RTGS'),(10022,'2022-01-04 07:01:06','success',42472,'NEFT'),(10023,'2022-02-25 15:08:02','success',1617876,'RTGS'),(10028,'2022-02-17 15:48:27','success',1183883,'IMPS'),(10028,'2022-02-27 14:43:12','success',938157,'IMPS'),(10030,'2022-01-31 18:36:00','failed',718586,'IMPS'),(10036,'2022-01-11 09:23:43','success',2574502,'RTGS'),(10037,'2022-01-16 03:03:06','success',2080578,'RTGS'),(10039,'2022-02-24 22:02:18','success',2733692,'RTGS'),(10045,'2022-01-16 01:41:21','success',871567,'IMPS'),(10048,'2022-01-29 06:51:06','failed',135749,'NEFT'),(10055,'2022-02-20 02:24:46','success',266474,'NEFT'),(10057,'2022-01-10 10:33:55','failed',2600760,'RTGS'),(10062,'2022-01-05 01:58:12','failed',2613889,'RTGS'),(10064,'2022-03-01 07:32:06','success',1286971,'IMPS'),(10067,'2022-02-11 15:43:30','success',649452,'IMPS'),(10070,'2022-01-17 22:09:11','success',911192,'IMPS');
/*!40000 ALTER TABLE `installment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-10 21:09:50
