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
-- Table structure for table `documents_link`
--

DROP TABLE IF EXISTS `documents_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documents_link` (
  `document_id` int unsigned NOT NULL AUTO_INCREMENT,
  `collateral_id` int unsigned NOT NULL,
  `document_link` varchar(100) NOT NULL,
  PRIMARY KEY (`document_id`,`collateral_id`),
  KEY `documents_link_ibfk_1` (`collateral_id`),
  CONSTRAINT `documents_link_ibfk_1` FOREIGN KEY (`collateral_id`) REFERENCES `collateral` (`collateral_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10052 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documents_link`
--

LOCK TABLES `documents_link` WRITE;
/*!40000 ALTER TABLE `documents_link` DISABLE KEYS */;
INSERT INTO `documents_link` VALUES (10001,10001,'https:\\\\drive.google.com\\SWAACZQEWVOXLKIT'),(10002,10002,'https:\\\\drive.google.com\\TEJMOCPPBXXZCHZJ'),(10003,10003,'https:\\\\drive.google.com\\TYZCSUVOUKBLCPOZ'),(10004,10004,'https:\\\\drive.google.com\\SCJOLWDRINCJNFRX'),(10005,10005,'https:\\\\drive.google.com\\BKHUVFZNUWMKTYKM'),(10006,10006,'https:\\\\drive.google.com\\PBDUSRTQEGDXIKPW'),(10007,10007,'https:\\\\drive.google.com\\ALIYFWJGCWSYLKFA'),(10008,10008,'https:\\\\drive.google.com\\CQTLOBYTIOUXTHKE'),(10009,10009,'https:\\\\drive.google.com\\VZDUHXQLWOWWBPTI'),(10010,10010,'https:\\\\drive.google.com\\XMKLXJAPCCZWYAZS'),(10011,10011,'https:\\\\drive.google.com\\QONNEBKKIAYBVNJZ'),(10012,10012,'https:\\\\drive.google.com\\WXDILSRSBGSRHKEX'),(10013,10013,'https:\\\\drive.google.com\\FTUXFPVNBWOLRBDQ'),(10014,10014,'https:\\\\drive.google.com\\BCFTAZIEDROSYLNO'),(10015,10015,'https:\\\\drive.google.com\\OOHYUPYUHRAKTRGP'),(10016,10016,'https:\\\\drive.google.com\\EMTRFSNPULCVWNTP'),(10017,10017,'https:\\\\drive.google.com\\HNYGRRPUMHWDEYAE'),(10018,10018,'https:\\\\drive.google.com\\PIOQZBKGFZTTZNDO'),(10019,10019,'https:\\\\drive.google.com\\QVEQRAFISEECPSNA'),(10020,10020,'https:\\\\drive.google.com\\TVDNPQNEFLTGQFMV'),(10021,10021,'https:\\\\drive.google.com\\ARCWAFKOMZOFINFF'),(10022,10022,'https:\\\\drive.google.com\\ZSKJTSISWOSOEUHH'),(10023,10023,'https:\\\\drive.google.com\\ZMURTPAXSTWGLBNZ'),(10024,10024,'https:\\\\drive.google.com\\YHNGZPDCEZZXKGZH'),(10025,10025,'https:\\\\drive.google.com\\JTUFVUPMDFSLTKXQ'),(10026,10026,'https:\\\\drive.google.com\\EMYILBWIUDNBTNVZ'),(10027,10027,'https:\\\\drive.google.com\\YRFMUQRGZDBMCJVH'),(10028,10028,'https:\\\\drive.google.com\\VKCDUAKWQWTSUGEY'),(10029,10029,'https:\\\\drive.google.com\\SINLPKSLPOYFGQOO'),(10030,10030,'https:\\\\drive.google.com\\WHTYUVDHLFYSGYPT'),(10031,10031,'https:\\\\drive.google.com\\JKMIHOFLSYYNKNZO'),(10032,10032,'https:\\\\drive.google.com\\ZGXFKLLVUSAKDEVI'),(10033,10033,'https:\\\\drive.google.com\\GGTFKLVWKETIRJDW'),(10034,10034,'https:\\\\drive.google.com\\JKMWDGAZJWIMGGPG'),(10035,10035,'https:\\\\drive.google.com\\NIHDKOIBGKXBLNLH'),(10036,10036,'https:\\\\drive.google.com\\CWWRLURHQZGLFCKP'),(10037,10037,'https:\\\\drive.google.com\\MYRCKZJKXTTTCYHE'),(10038,10038,'https:\\\\drive.google.com\\MXRRSUEITVUBWGKH'),(10039,10039,'https:\\\\drive.google.com\\ENWHGSLTYLJOLELR'),(10040,10040,'https:\\\\drive.google.com\\PZOOSVCESUQXWVOX'),(10041,10041,'https:\\\\drive.google.com\\KMDWTSRMBSPDMKMZ'),(10042,10042,'https:\\\\drive.google.com\\DIFJYBSXFEPHAGHJ'),(10043,10043,'https:\\\\drive.google.com\\QWYTDTJLYJRDFDMM'),(10044,10044,'https:\\\\drive.google.com\\IOCCTGJIPYVHASWZ'),(10045,10045,'https:\\\\drive.google.com\\CTYQPYMKSYTIJESH'),(10046,10046,'https:\\\\drive.google.com\\IPHWAKQKQDFMGGZL'),(10047,10047,'https:\\\\drive.google.com\\AGBVMYEUIHASPHGC'),(10048,10048,'https:\\\\drive.google.com\\KSFFHJDRUYDKIIFA'),(10049,10049,'https:\\\\drive.google.com\\EKPXMWFTDWMHCQXV'),(10050,10050,'https:\\\\drive.google.com\\RXRWEITPMZEINHBO');
/*!40000 ALTER TABLE `documents_link` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:12:04
