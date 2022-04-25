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
-- Table structure for table `asset_insurance`
--

DROP TABLE IF EXISTS `asset_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asset_insurance` (
  `policy_id` int unsigned NOT NULL,
  `asset_document` blob NOT NULL,
  `asset_value` mediumint unsigned NOT NULL,
  PRIMARY KEY (`policy_id`),
  CONSTRAINT `asset_insurance_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `insurance` (`policy_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset_insurance`
--

LOCK TABLES `asset_insurance` WRITE;
/*!40000 ALTER TABLE `asset_insurance` DISABLE KEYS */;
INSERT INTO `asset_insurance` VALUES (100001,_binary 'efcnlkj45r',500000),(100002,_binary 'f96riehipm',4500000),(100003,_binary 'q66jecnrt2',1000000),(100004,_binary 'lhsfezmfme',500000),(100005,_binary 'zqth9r0axd',5000000),(100006,_binary '2juh07hcvz',3500000),(100007,_binary '1ie4jvysum',500000),(100008,_binary 'lphv32itvg',2000000),(100009,_binary 'jljujt02yo',1500000),(100010,_binary 't7mh9heq0k',5000000),(100011,_binary '1q0p88byei',2000000),(100012,_binary 'mbe4dew7d1',500000),(100013,_binary '0pqhl22tbd',500000),(100014,_binary '7yekaf6wu8',4000000),(100015,_binary 'fp23z1ka2a',500000),(100016,_binary 'r8tyk8tm4v',2500000),(100017,_binary '1fwptkrtns',5000000),(100018,_binary 'pdf5hoot4t',3500000),(100019,_binary 'xo88d017l2',4500000),(100020,_binary '57248bzt26',1500000),(100021,_binary 'pdx5nd3w1w',1500000),(100022,_binary '58xhcgyou7',3000000),(100023,_binary 'mqecrjuazp',500000),(100024,_binary 'j0zph8fdkl',2000000),(100025,_binary 'ne2ar9u3q6',2000000);
/*!40000 ALTER TABLE `asset_insurance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:12:06
