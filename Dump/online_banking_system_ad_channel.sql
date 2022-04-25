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
-- Table structure for table `ad_channel`
--

DROP TABLE IF EXISTS `ad_channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ad_channel` (
  `channel_id` mediumint unsigned NOT NULL AUTO_INCREMENT,
  `channel_name` varchar(15) NOT NULL,
  `channel_link` varchar(100) NOT NULL,
  PRIMARY KEY (`channel_id`),
  UNIQUE KEY `channel_link` (`channel_link`)
) ENGINE=InnoDB AUTO_INCREMENT=938 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ad_channel`
--

LOCK TABLES `ad_channel` WRITE;
/*!40000 ALTER TABLE `ad_channel` DISABLE KEYS */;
INSERT INTO `ad_channel` VALUES (161,'channel7','https:\\\\drive.google.com\\ALIYFWJGCWSYLKFA'),(187,'channel12','https:\\\\drive.google.com\\WXDILSRSBGSRHKEX'),(345,'channel5','https:\\\\drive.google.com\\BKHUVFZNUWMKTYKM'),(387,'channel9','https:\\\\drive.google.com\\VZDUHXQLWOWWBPTI'),(411,'channel1','https:\\\\drive.google.com\\SWAACZQEWVOXLKIT'),(491,'channel13','https:\\\\drive.google.com\\FTUXFPVNBWOLRBDQ'),(493,'channel16','https:\\\\drive.google.com\\EMTRFSNPULCVWNTP'),(507,'channel10','https:\\\\drive.google.com\\XMKLXJAPCCZWYAZS'),(548,'channel4','https:\\\\drive.google.com\\SCJOLWDRINCJNFRX'),(690,'channel3','https:\\\\drive.google.com\\TYZCSUVOUKBLCPOZ'),(717,'channel2','https:\\\\drive.google.com\\TEJMOCPPBXXZCHZJ'),(866,'channel8','https:\\\\drive.google.com\\CQTLOBYTIOUXTHKE'),(900,'channel6','https:\\\\drive.google.com\\PBDUSRTQEGDXIKPW'),(909,'channel15','https:\\\\drive.google.com\\OOHYUPYUHRAKTRGP'),(934,'channel14','https:\\\\drive.google.com\\BCFTAZIEDROSYLNO'),(937,'channel11','https:\\\\drive.google.com\\QONNEBKKIAYBVNJZ');
/*!40000 ALTER TABLE `ad_channel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:11:50
