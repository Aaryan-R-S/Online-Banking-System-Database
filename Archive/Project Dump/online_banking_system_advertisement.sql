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
-- Table structure for table `advertisement`
--

DROP TABLE IF EXISTS `advertisement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `advertisement` (
  `advertisemnt_id` int unsigned NOT NULL AUTO_INCREMENT,
  `total_cost` mediumint unsigned NOT NULL,
  `ad_type` enum('social-media','offline','on-site','other-online') NOT NULL,
  `channel_id` mediumint unsigned NOT NULL,
  `authorized_by` smallint unsigned NOT NULL,
  PRIMARY KEY (`advertisemnt_id`),
  KEY `channel_id` (`channel_id`),
  KEY `authorized_by` (`authorized_by`),
  CONSTRAINT `advertisement_ibfk_1` FOREIGN KEY (`channel_id`) REFERENCES `ad_channel` (`channel_id`),
  CONSTRAINT `advertisement_ibfk_2` FOREIGN KEY (`authorized_by`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9010 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `advertisement`
--

LOCK TABLES `advertisement` WRITE;
/*!40000 ALTER TABLE `advertisement` DISABLE KEYS */;
INSERT INTO `advertisement` VALUES (1109,150000,'other-online',909,10014),(1526,250000,'on-site',934,10013),(1617,175000,'offline',345,10004),(1781,100000,'offline',387,10008),(1890,50000,'other-online',491,10012),(3006,150000,'offline',411,10000),(3123,25000,'other-online',866,10007),(3148,225000,'other-online',161,10006),(4079,25000,'on-site',548,10003),(4616,225000,'social-media',493,10015),(4658,25000,'on-site',717,10001),(4853,225000,'offline',187,10011),(6410,50000,'social-media',900,10005),(6873,50000,'social-media',690,10002),(7101,150000,'other-online',937,10010),(9009,200000,'on-site',507,10009);
/*!40000 ALTER TABLE `advertisement` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-02 16:05:07
