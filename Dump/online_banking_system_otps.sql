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
-- Table structure for table `otps`
--

DROP TABLE IF EXISTS `otps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `otps` (
  `cin` int unsigned NOT NULL,
  `valid_from` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `account_number` bigint unsigned NOT NULL,
  `valid_till` timestamp NULL DEFAULT ((`valid_from` + interval 5 minute)),
  `otp` mediumint unsigned NOT NULL,
  PRIMARY KEY (`cin`,`valid_from`),
  KEY `otps_ibfk_1` (`account_number`),
  CONSTRAINT `otps_ibfk_1` FOREIGN KEY (`account_number`) REFERENCES `bank_account` (`account_number`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `otps_ibfk_2` FOREIGN KEY (`cin`) REFERENCES `customer` (`cin`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `otps`
--

LOCK TABLES `otps` WRITE;
/*!40000 ALTER TABLE `otps` DISABLE KEYS */;
INSERT INTO `otps` VALUES (100000001,'2022-03-02 07:01:02',11000000026,'2022-03-02 07:07:02',570811),(100000002,'2022-03-01 20:22:48',11000000027,'2022-03-01 20:24:48',794055),(100000003,'2022-03-02 03:55:48',11000000028,'2022-03-02 03:57:48',711772),(100000004,'2022-03-02 09:38:24',11000000029,'2022-03-02 09:46:24',679934),(100000005,'2022-03-02 03:25:48',11000000030,'2022-03-02 03:34:48',849599),(100000006,'2022-03-01 19:33:00',11000000031,'2022-03-01 19:39:00',962432),(100000007,'2022-03-02 12:25:12',11000000032,'2022-03-02 12:32:12',494942),(100000008,'2022-03-02 13:34:48',11000000033,'2022-03-02 13:44:48',546647),(100000009,'2022-03-02 10:34:12',11000000034,'2022-03-02 10:44:12',349020),(100000010,'2022-03-02 02:33:36',11000000035,'2022-03-02 02:37:36',419628),(100000011,'2022-03-02 06:10:12',11000000036,'2022-03-02 06:20:12',804137),(100000012,'2022-03-02 01:25:48',11000000037,'2022-03-02 01:26:48',544572),(100000013,'2022-03-02 10:57:36',11000000038,'2022-03-02 11:06:36',949471),(100000014,'2022-03-02 00:31:48',11000000039,'2022-03-02 00:35:48',556034),(100000015,'2022-03-01 23:11:24',11000000040,'2022-03-01 23:17:24',341641),(100000016,'2022-03-02 01:14:24',11000000041,'2022-03-02 01:15:24',846735),(100000017,'2022-03-02 07:08:24',11000000042,'2022-03-02 07:17:24',677666),(100000018,'2022-03-01 21:02:24',11000000043,'2022-03-01 21:04:24',986150),(100000019,'2022-03-02 06:23:24',11000000044,'2022-03-02 06:32:24',234157);
/*!40000 ALTER TABLE `otps` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:11:48
