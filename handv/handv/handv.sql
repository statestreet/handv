/*
Navicat MySQL Data Transfer

Source Server         : handv
Source Server Version : 50156
Source Host           : localhost:3306
Source Database       : handv

Target Server Type    : MYSQL
Target Server Version : 50156
File Encoding         : 65001

Date: 2012-04-09 16:44:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_message`
-- ----------------------------
DROP TABLE IF EXISTS `auth_message`;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_403f60f` (`user_id`),
  CONSTRAINT `user_id_refs_id_650f49a6` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_message
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add permission', '1', 'add_permission');
INSERT INTO `auth_permission` VALUES ('2', 'Can change permission', '1', 'change_permission');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete permission', '1', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add user', '3', 'add_user');
INSERT INTO `auth_permission` VALUES ('8', 'Can change user', '3', 'change_user');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete user', '3', 'delete_user');
INSERT INTO `auth_permission` VALUES ('10', 'Can add message', '4', 'add_message');
INSERT INTO `auth_permission` VALUES ('11', 'Can change message', '4', 'change_message');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete message', '4', 'delete_message');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add site', '7', 'add_site');
INSERT INTO `auth_permission` VALUES ('20', 'Can change site', '7', 'change_site');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete site', '7', 'delete_site');
INSERT INTO `auth_permission` VALUES ('22', 'Can add user', '8', 'add_user');
INSERT INTO `auth_permission` VALUES ('23', 'Can change user', '8', 'change_user');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete user', '8', 'delete_user');
INSERT INTO `auth_permission` VALUES ('25', 'Can add tag', '9', 'add_tag');
INSERT INTO `auth_permission` VALUES ('26', 'Can change tag', '9', 'change_tag');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete tag', '9', 'delete_tag');
INSERT INTO `auth_permission` VALUES ('28', 'Can add article', '10', 'add_article');
INSERT INTO `auth_permission` VALUES ('29', 'Can change article', '10', 'change_article');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete article', '10', 'delete_article');
INSERT INTO `auth_permission` VALUES ('31', 'Can add comment', '11', 'add_comment');
INSERT INTO `auth_permission` VALUES ('32', 'Can change comment', '11', 'change_comment');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete comment', '11', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('34', 'Can add attachment', '12', 'add_attachment');
INSERT INTO `auth_permission` VALUES ('35', 'Can change attachment', '12', 'change_attachment');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete attachment', '12', 'delete_attachment');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`),
  CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'permission', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('2', 'group', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'user', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('4', 'message', 'auth', 'message');
INSERT INTO `django_content_type` VALUES ('5', 'content type', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'session', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'site', 'sites', 'site');
INSERT INTO `django_content_type` VALUES ('8', 'user', 'home', 'user');
INSERT INTO `django_content_type` VALUES ('9', 'tag', 'home', 'tag');
INSERT INTO `django_content_type` VALUES ('10', 'article', 'home', 'article');
INSERT INTO `django_content_type` VALUES ('11', 'comment', 'home', 'comment');
INSERT INTO `django_content_type` VALUES ('12', 'attachment', 'home', 'attachment');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('7040d5a508d9231a58882c2d954e4d05', 'gAJ9cQFVBHVzZXJjZGphbmdvLmRiLm1vZGVscy5iYXNlCm1vZGVsX3VucGlja2xlCnECY2hhbmR2\nLmhvbWUubW9kZWxzClVzZXIKcQNdY2RqYW5nby5kYi5tb2RlbHMuYmFzZQpzaW1wbGVfY2xhc3Nf\nZmFjdG9yeQpxBIdScQV9cQYoVQh1c2VybmFtZXEHWAcAAAB5aXhpdWdnVQV3ZWlib3EIWAAAAABV\nBGNvZGVxCVgkAAAAMWI0ZWI2MmUtODFlNi0xMWUxLWJhMDAtMDAxZTM3NGY0MTIwVQRuYW1lcQpY\nCQAAAOS4gOS8keWTpVUGX3N0YXRlcQtjZGphbmdvLmRiLm1vZGVscy5iYXNlCk1vZGVsU3RhdGUK\ncQwpgXENfXEOKFUGYWRkaW5ncQ+JVQJkYnEQVQdkZWZhdWx0cRF1YlUHcmVndGltZXESY2RhdGV0\naW1lCmRhdGV0aW1lCnETVQoH3AQJCTAdAAAAhVJxFFUFZW1haWxxFVgPAAAAeWl4aXVnZ0AxMjYu\nY29tVQVzdGF0ZXEWWAEAAAAxVQhpbnRlcm5hbHEXigBVCndlaWJvX25pY2txGFgAAAAAVQhwYXNz\nd29yZHEZWCAAAAA1NjVlODVmZDhiNTMyOGY1OTlhNDdjYzRiNDgyNWYwM1UCaWRxGooBAXVicy43\nOTMwNTQ0MjcyMzhmNjExMjEyYjNiNjliOTA3NjBlNA==\n', '2012-04-23 09:53:15');

-- ----------------------------
-- Table structure for `django_site`
-- ----------------------------
DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_site
-- ----------------------------
INSERT INTO `django_site` VALUES ('1', 'example.com', 'example.com');

-- ----------------------------
-- Table structure for `home_article`
-- ----------------------------
DROP TABLE IF EXISTS `home_article`;
CREATE TABLE `home_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `tag` varchar(200) DEFAULT NULL,
  `addtime` datetime NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `state` varchar(2) NOT NULL,
  `type` varchar(2) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `home_article_403f60f` (`user_id`),
  CONSTRAINT `user_id_refs_id_7aad2b9` FOREIGN KEY (`user_id`) REFERENCES `home_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of home_article
-- ----------------------------
INSERT INTO `home_article` VALUES ('1', '1', '飞机 坦克', '2012-04-09 11:29:57', 'Project Manager', '<p style=\"line-height:100%;\">写点什么吧</p>', '00', '00', null);
INSERT INTO `home_article` VALUES ('2', '1', '飞机 坦克', '2012-04-09 13:15:32', 'Project Manager', '<h1 id=\"artibodyTitle\" style=\"color:#03005c;\"><span style=\";color:#ff0000;\">苏克附体！劳尔4场5球谁不服&nbsp;球迷为他起立鼓掌一分钟</span></h1><div class=\"artInfo\"><span id=\"art_source\"><a href=\"http://sports.sina.com.cn/\">http://sports.sina.com.cn</a></span>&nbsp;&nbsp;<span id=\"pub_date\">2012年04月09日10:00</span>&nbsp;&nbsp;<span id=\"media_name\"><span class=\"linkRed02\"><a href=\"http://sports.sina.com.cn/\" target=\"_blank\">新浪体育</a></span></span><a id=\"media_weibo\" class=\"weibo-card-dropdown\" href=\"http://weibo.com/sportschannel?zwm=sports\">微博</a></div><div class=\"img_wrapper\"><img alt=\"劳尔进球后，亲吻自己右手上的戒指\" src=\"http://i0.sinaimg.cn/ty/g/2012-04-09/U7880P6T12D6015349F44DT20120409094904.jpg\" /><span class=\"img_descr\">劳尔进球后，亲吻自己右手上的戒指</span></div><p>　　新浪体育讯　劳尔又进球了！德甲<a href=\"http://weibo.com/fussballnews?zw=sports\" target=\"_blank\">(微博)</a>第29轮，劳尔梅开二度，帮助沙尔克3比0战胜汉诺威96，现场球迷起立给劳尔送上长达1分钟的掌声，其中劳尔的第二球尤为精彩。</p><p>　　比赛进行到第47分钟，沙尔克04右路发动攻势，劳尔在汉诺威左侧禁区外得球后拨<span class=\"contentPlayer\"><span class=\"cp_tit\" style=\"font-weight:normal;\"><a target=\"_blank\" href=\"http://video.sina.com.cn/p/sports/g/v/2012-04-08/232061715609.html\">进球视频-劳尔潇洒拉球过门将&nbsp;精准推射梅开二度</a></span><span class=\"cp_from\" style=\"font-weight:normal;\">媒体来源：新浪体育</span></span>给了附近的队友法尔范，法尔范顺势停球时，劳尔趁势跑动至禁区，法尔范轻挑皮球越过防守后卫的头顶，与劳尔打出精妙的二过一撞墙式配合。劳尔在小禁区左侧接法尔范的传球后，挤开防守球员，直面门将时，左脚拉球晃过门将齐勒，将球轻松打入空门。主持人惊呼：“这球太妙了！又是劳尔！闲情信步一般！”</p><p>　　打进第二球后，劳尔神情自若，面对球迷双手举天表示庆贺，而情绪高涨的沙尔克球迷则起立为沙尔克04的7号鼓掌长达一分钟，表达对他们王子的崇高敬意！不经意间，劳尔已经打进德甲14粒入球，个人赛季入球已达20粒！而此球四两拨千斤，不仅把沙尔克前场进攻配合体现得如火纯青，也把劳尔个人作为前锋的灵巧与冷静的特点一展无遗，而劳尔左脚拉球的动作宛如小提琴琴弓在琴弦上缓缓拉过，让人不禁想起克罗地亚传奇前锋“金左脚”达沃-苏克原地拉球的动作。</p><p>　　沙尔克在上周过得并不愉快，欧联杯八强与西甲<a href=\"http://weibo.com/ligabbva?zw=sports\" target=\"_blank\">(微博)</a>劲旅毕尔巴鄂竞技火拼180分钟，最后被淘汰出局，幸好他们收获了劳尔。首回合时，劳尔就曾梅开二度，让沙尔克重塑获胜希望，只可惜伤员太多，人员不整，球队主场遭致沦陷，被打进4粒入球。而来到毕尔巴鄂竞技主场，劳尔又打响反击的号角，打进自己欧战第77粒进球，无奈首场交锋客场失球过多。沙尔克04与劳尔遗憾被挡在了欧联杯四强的门外。</p><p>　　加盟沙尔克04后，劳尔不仅虏获了沙尔克04球迷的心，同时也让西班牙球迷牵动着。在面对汉诺威梅开二度后，马德里地区报纸《阿斯报》直接用数据体现在标题上，“劳尔，进球本赛季第20球！”这不禁让人想起前不久媒体热炒的劳尔重回国家队的传闻。2012年欧洲杯日益临近，西班牙虽然身为卫冕冠军，却没有得以仰仗的当家前锋。遥想08年夺冠功臣的比利亚因一场世俱杯让自己挂靴半个赛季之久。而另一金童托雷斯在高价转会斯坦福桥后，迟迟没有打出自己应有的水准，而当年另一锋煞古伊萨早在夺冠之后，迷失在土耳其联赛中。翻过国内，略伦特虽然状态火热，但是资质尚且，不能委以重任。而瓦伦前锋索尔达多，状态时好时坏，一遇球荒并是一个月之久。。。此时，最近4场比赛打进5球的劳尔，状态喜人，又有着大量的国家队经验。前锋紧缺的西班牙，何不考虑重新招劳尔入队呢？</p><p>　　(北江户川)</p><p><br /></p>', '01', '00', 'P_M');
INSERT INTO `home_article` VALUES ('3', '1', '飞机 坦克', '2012-04-09 13:16:29', 'Project Manager', '<p>写点什么吧</p>', '01', '00', 'TEK');
INSERT INTO `home_article` VALUES ('4', '1', '飞机 坦克', '2012-04-09 13:16:34', 'Project Manager', '<p>写点什么吧</p>', '01', '00', 'TANK_PLAN');
INSERT INTO `home_article` VALUES ('5', '1', '飞机 坦克', '2012-04-09 13:16:38', 'Project Manager', '<p>写点什么吧</p>', '01', '00', '__TT');

-- ----------------------------
-- Table structure for `home_attachment`
-- ----------------------------
DROP TABLE IF EXISTS `home_attachment`;
CREATE TABLE `home_attachment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `addtime` datetime NOT NULL,
  `filepath` varchar(500) NOT NULL,
  `type` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_attachment_403f60f` (`user_id`),
  KEY `home_attachment_30525a19` (`article_id`),
  CONSTRAINT `article_id_refs_id_4aa5e6ed` FOREIGN KEY (`article_id`) REFERENCES `home_article` (`id`),
  CONSTRAINT `user_id_refs_id_6b3e9deb` FOREIGN KEY (`user_id`) REFERENCES `home_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of home_attachment
-- ----------------------------

-- ----------------------------
-- Table structure for `home_comment`
-- ----------------------------
DROP TABLE IF EXISTS `home_comment`;
CREATE TABLE `home_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `addtime` datetime NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `state` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_comment_403f60f` (`user_id`),
  KEY `home_comment_30525a19` (`article_id`),
  CONSTRAINT `article_id_refs_id_33010b4a` FOREIGN KEY (`article_id`) REFERENCES `home_article` (`id`),
  CONSTRAINT `user_id_refs_id_55f066b8` FOREIGN KEY (`user_id`) REFERENCES `home_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of home_comment
-- ----------------------------

-- ----------------------------
-- Table structure for `home_tag`
-- ----------------------------
DROP TABLE IF EXISTS `home_tag`;
CREATE TABLE `home_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `type` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_tag_403f60f` (`user_id`),
  CONSTRAINT `user_id_refs_id_3eb543ad` FOREIGN KEY (`user_id`) REFERENCES `home_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of home_tag
-- ----------------------------
INSERT INTO `home_tag` VALUES ('1', '1', '飞机', '', '00');
INSERT INTO `home_tag` VALUES ('2', '1', '坦克', '', '00');

-- ----------------------------
-- Table structure for `home_user`
-- ----------------------------
DROP TABLE IF EXISTS `home_user`;
CREATE TABLE `home_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `state` varchar(2) NOT NULL,
  `code` varchar(50) NOT NULL,
  `regtime` datetime NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(32) NOT NULL,
  `weibo` varchar(32) NOT NULL,
  `weibo_nick` varchar(50) NOT NULL,
  `internal` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of home_user
-- ----------------------------
INSERT INTO `home_user` VALUES ('1', 'yixiugg', '一休哥', '1', '1b4eb62e-81e6-11e1-ba00-001e374f4120', '2012-04-09 09:48:29', 'yixiugg@126.com', '565e85fd8b5328f599a47cc4b4825f03', '', '', '0');
