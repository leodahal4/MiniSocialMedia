-- MariaDB dump 10.17  Distrib 10.5.5-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: minisocialmedia
-- ------------------------------------------------------
-- Server version	10.5.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `friends`
--

DROP TABLE IF EXISTS `friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friends` (
  `origin_user` int(11) NOT NULL,
  `destination_user` int(11) NOT NULL,
  `request` int(11) NOT NULL,
  KEY `origin_user` (`origin_user`),
  KEY `destination_user` (`destination_user`),
  CONSTRAINT `friends_ibfk_1` FOREIGN KEY (`origin_user`) REFERENCES `user` (`id`),
  CONSTRAINT `friends_ibfk_2` FOREIGN KEY (`destination_user`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friends`
--

LOCK TABLES `friends` WRITE;
/*!40000 ALTER TABLE `friends` DISABLE KEYS */;
INSERT INTO `friends` VALUES (2,3,1),(4,2,1),(2,4,0),(2,6,1),(2,8,1),(8,2,1),(2,1,0),(2,7,0),(2,5,1),(2,2,0),(5,1,0),(5,1,0),(5,4,1),(4,1,0),(4,3,0),(4,7,0),(4,8,1),(4,6,0),(4,4,0),(5,6,0),(6,1,0),(6,3,0),(8,5,0),(8,5,0),(8,5,0),(8,5,0),(8,5,0),(8,5,0),(8,5,0),(8,5,0),(8,5,0),(8,7,0),(8,8,0),(8,6,0),(8,1,0),(5,5,0),(5,7,1),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0),(2,8,0);
/*!40000 ALTER TABLE `friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `likes` (
  `user_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  KEY `post_id` (`post_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `likes_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`),
  CONSTRAINT `likes_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (2,31),(2,32),(2,33),(2,34),(2,35),(1,36),(2,36),(2,37),(2,38),(2,39),(2,40),(3,33),(3,35),(3,31),(2,41),(1,41);
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `messageContent` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fromUser` int(11) NOT NULL,
  `toUser` int(11) NOT NULL,
  `seen` int(11) DEFAULT NULL,
  PRIMARY KEY (`message_id`),
  KEY `fromUser` (`fromUser`),
  KEY `toUser` (`toUser`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`fromUser`) REFERENCES `user` (`id`),
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`toUser`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,'fadsfadsfad',2,2,1),(2,'fadsfadsfad',2,3,1),(3,'this is a try message from mausam1',4,2,1),(4,'this is a try message from mausam1',4,2,1),(5,'Hi. Its me again :-) ',2,4,1),(6,'Hi. Its me again :-) ',2,4,1),(7,'This is my message babe',2,3,1),(8,'this is my message babe',2,5,1),(9,'Ok this is also my new message to you.',3,2,1),(10,'Aw! Thanks. My name leo and urs?',2,3,1),(11,'where are you from?',2,3,1),(12,'Hey are you there?',3,4,1),(13,'I ammfine thank you',2,3,0),(14,'This i smy random message to you.',2,8,1),(15,'Hi again',2,8,1),(16,'Hello man?',2,8,1),(17,'yeah?',8,2,1),(18,'hello',8,2,1),(19,'see you man',2,8,1),(20,'ok. Bye',2,8,1),(21,'Thanks man',8,3,0),(22,'Ok bye by etake care',8,2,1),(23,'Ok bye bye',5,2,1),(24,'Bye bye',5,2,1),(25,'fadsfad',1,2,1);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_associated` int(11) DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_associated` (`user_associated`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`user_associated`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (31,'How to generate a random string?','Put a first year Computer Science student on VIM and ask them to save and exit.',2,201),(32,'Breaking News','Hackers managed to exit Vim\nAsked How they did it, they said, \'Its because, we all use Arch.\'\n	BTW I use Arch',2,200),(33,'just one for try','This is just for try',2,6),(34,'hfajdskhfjk','just another random post with description',1,0),(35,'fasjdkhfkajhdsjfhajkdsh','just a random  text for the description of the post.',2,1),(36,'hfasdjfhajkhd','fadsfadsfadsfadsfadfadsfasdfadsfasdfadsf',2,0),(37,'fasdfasdfasdf','asdfadsfadsfasdfadsfadsf',2,0),(38,'mausamfjadshkjfahkdsjhfajkdshfka','thank you dfkjhakdsfhakjdshfjkajdfhkajds',2,0),(39,'fasdfadsfadsfadsfa','dsfadsfadsfadsfadsfasd',2,0),(40,'hfakjsdhfjkahdskjfhakdshfakdhjk','fkdasjlkfajdsklfjakldsjfklajdklfajkldjfkladffdsfadsfadsfadsfadfadfadsfadsfadfadfadfadfadsfa',2,1),(41,'This is the last post for try','some random description.',2,2);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fname` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lname` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'mausam','4b17751b60942d13404229d384d66347','mausam','dahal'),(2,'leo','4b17751b60942d13404229d384d66347','mausam','dahal'),(3,'leodahal','4b17751b60942d13404229d384d66347','mausam','dahal'),(4,'mausam1','4b17751b60942d13404229d384d66347','mausam','dhaal'),(5,'mausam2','4b17751b60942d13404229d384d66347','mausam','dhaal'),(6,'leodahal2312','4b17751b60942d13404229d384d66347','Leo','Dahal'),(7,'isaidleo','4b17751b60942d13404229d384d66347','Leo','Dahal'),(8,'random','4b17751b60942d13404229d384d66347','Random','Guy'),(9,'test','098f6bcd4621d373cade4e832627b4f6','Test First Name','Test Last Name');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-04 16:56:25
