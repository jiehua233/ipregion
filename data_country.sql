-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2015-08-12 14:35:03
-- 服务器版本: 5.5.44-0ubuntu0.14.04.1
-- PHP 版本: 5.5.9-1ubuntu4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `ip2loc`
--

-- --------------------------------------------------------

--
-- 表的结构 `data_country`
--

CREATE TABLE IF NOT EXISTS `data_country` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `c2` varchar(2) NOT NULL COMMENT '两位字母',
  `c3` varchar(3) NOT NULL COMMENT '三位字母',
  `code` smallint(6) NOT NULL COMMENT '数字',
  `phone_code` smallint(6) NOT NULL DEFAULT '0' COMMENT '国家电话区域码',
  `name` varchar(32) NOT NULL COMMENT '名字',
  PRIMARY KEY (`id`),
  UNIQUE KEY `c2` (`c2`,`c3`,`code`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=249 ;

--
-- 转存表中的数据 `data_country`
--

INSERT INTO `data_country` (`id`, `c2`, `c3`, `code`, `phone_code`, `name`) VALUES
(1, 'AD', 'AND', 20, 376, '安道尔'),
(2, 'AE', 'ARE', 784, 971, '阿联酋'),
(3, 'AF', 'AFG', 4, 93, '阿富汗'),
(4, 'AG', 'ATG', 28, 1268, '安提瓜和巴布达'),
(5, 'AI', 'AIA', 660, 1264, '安圭拉'),
(6, 'AL', 'ALB', 8, 355, '阿尔巴尼亚'),
(7, 'AM', 'ARM', 51, 374, '亚美尼亚'),
(8, 'AO', 'AGO', 24, 244, '安哥拉'),
(9, 'AQ', 'ATA', 10, 0, '南极洲'),
(10, 'AR', 'ARG', 32, 54, '阿根廷'),
(11, 'AS', 'ASM', 16, 0, '美属萨摩亚'),
(12, 'AT', 'AUT', 40, 43, '奥地利'),
(13, 'AU', 'AUS', 36, 61, '澳大利亚'),
(14, 'AW', 'ABW', 533, 0, '阿鲁巴'),
(15, 'AX', 'ALA', 248, 0, '奥兰群岛'),
(16, 'AZ', 'AZE', 31, 994, '阿塞拜疆'),
(17, 'BA', 'BIH', 70, 0, '波黑'),
(18, 'BB', 'BRB', 52, 1246, '巴巴多斯'),
(19, 'BD', 'BGD', 50, 880, '孟加拉'),
(20, 'BE', 'BEL', 56, 32, '比利时'),
(21, 'BF', 'BFA', 854, 226, '布基纳法索'),
(22, 'BG', 'BGR', 100, 359, '保加利亚'),
(23, 'BH', 'BHR', 48, 973, '巴林'),
(24, 'BI', 'BDI', 108, 257, '布隆迪'),
(25, 'BJ', 'BEN', 204, 229, '贝宁'),
(26, 'BL', 'BLM', 652, 970, '圣巴泰勒米岛'),
(27, 'BM', 'BMU', 60, 1441, '百慕大'),
(28, 'BN', 'BRN', 96, 673, '文莱'),
(29, 'BO', 'BOL', 68, 591, '玻利维亚'),
(30, 'BQ', 'BES', 535, 0, '荷兰加勒比区'),
(31, 'BR', 'BRA', 76, 55, '巴西'),
(32, 'BS', 'BHS', 44, 1242, '巴哈马'),
(33, 'BT', 'BTN', 64, 0, '不丹'),
(34, 'BV', 'BVT', 74, 0, '布韦岛'),
(35, 'BW', 'BWA', 72, 267, '博茨瓦纳'),
(36, 'BY', 'BLR', 112, 375, '白俄罗斯'),
(37, 'BZ', 'BLZ', 84, 501, '伯利兹'),
(38, 'CA', 'CAN', 124, 1, '加拿大'),
(39, 'CC', 'CCK', 166, 0, '科科斯群岛'),
(40, 'CD', 'COD', 180, 0, '刚果（金）'),
(41, 'CF', 'CAF', 140, 236, '中非'),
(42, 'CG', 'COG', 178, 242, '刚果（布）'),
(43, 'CH', 'CHE', 756, 41, '瑞士'),
(44, 'CI', 'CIV', 384, 0, '科特迪瓦'),
(45, 'CK', 'COK', 184, 682, '库克群岛'),
(46, 'CL', 'CHL', 152, 56, '智利'),
(47, 'CM', 'CMR', 120, 237, '喀麦隆'),
(48, 'CN', 'CHN', 156, 86, '中国'),
(49, 'CO', 'COL', 170, 57, '哥伦比亚'),
(50, 'CR', 'CRI', 188, 506, '哥斯达黎加'),
(51, 'CU', 'CUB', 192, 53, '古巴'),
(52, 'CV', 'CPV', 132, 0, '佛得角'),
(53, 'CW', 'CUW', 531, 0, '库拉索'),
(54, 'CX', 'CXR', 162, 0, '圣诞岛'),
(55, 'CY', 'CYP', 196, 357, '塞浦路斯'),
(56, 'CZ', 'CZE', 203, 420, '捷克'),
(57, 'DE', 'DEU', 276, 49, '德国'),
(58, 'DJ', 'DJI', 262, 253, '吉布提'),
(59, 'DK', 'DNK', 208, 45, '丹麦'),
(60, 'DM', 'DMA', 212, 0, '多米尼克'),
(61, 'DO', 'DOM', 214, 1890, '多米尼加'),
(62, 'DZ', 'DZA', 12, 213, '阿尔及利亚'),
(63, 'EC', 'ECU', 218, 593, '厄瓜多尔'),
(64, 'EE', 'EST', 233, 372, '爱沙尼亚'),
(65, 'EG', 'EGY', 818, 20, '埃及'),
(66, 'EH', 'ESH', 732, 0, '西撒哈拉'),
(67, 'ER', 'ERI', 232, 0, '厄立特里亚'),
(68, 'ES', 'ESP', 724, 34, '西班牙'),
(69, 'ET', 'ETH', 231, 251, '埃塞俄比亚'),
(70, 'FI', 'FIN', 246, 358, '芬兰'),
(71, 'FJ', 'FJI', 242, 679, '斐济群岛'),
(72, 'FK', 'FLK', 238, 0, '马尔维纳斯群岛（福克兰）'),
(73, 'FM', 'FSM', 583, 0, '密克罗尼西亚联邦'),
(74, 'FO', 'FRO', 234, 0, '法罗群岛'),
(75, 'FR', 'FRA', 250, 33, '法国'),
(76, 'GA', 'GAB', 266, 241, '加蓬'),
(77, 'GB', 'GBR', 826, 44, '英国'),
(78, 'GD', 'GRD', 308, 1809, '格林纳达'),
(79, 'GE', 'GEO', 268, 995, '格鲁吉亚'),
(80, 'GF', 'GUF', 254, 594, '法属圭亚那'),
(81, 'GG', 'GGY', 831, 0, '根西岛'),
(82, 'GH', 'GHA', 288, 233, '加纳'),
(83, 'GI', 'GIB', 292, 350, '直布罗陀'),
(84, 'GL', 'GRL', 304, 0, '格陵兰'),
(85, 'GM', 'GMB', 270, 220, '冈比亚'),
(86, 'GN', 'GIN', 324, 224, '几内亚'),
(87, 'GP', 'GLP', 312, 0, '瓜德罗普'),
(88, 'GQ', 'GNQ', 226, 0, '赤道几内亚'),
(89, 'GR', 'GRC', 300, 30, '希腊'),
(90, 'GS', 'SGS', 239, 0, '南乔治亚岛和南桑威奇群岛'),
(91, 'GT', 'GTM', 320, 502, '危地马拉'),
(92, 'GU', 'GUM', 316, 1671, '关岛'),
(93, 'GW', 'GNB', 624, 0, '几内亚比绍'),
(94, 'GY', 'GUY', 328, 592, '圭亚那'),
(95, 'HK', 'HKG', 344, 852, '香港'),
(96, 'HM', 'HMD', 334, 0, '赫德岛和麦克唐纳群岛'),
(97, 'HN', 'HND', 340, 504, '洪都拉斯'),
(98, 'HR', 'HRV', 191, 0, '克罗地亚'),
(99, 'HT', 'HTI', 332, 509, '海地'),
(100, 'HU', 'HUN', 348, 36, '匈牙利'),
(101, 'ID', 'IDN', 360, 62, '印尼'),
(102, 'IE', 'IRL', 372, 353, '爱尔兰'),
(103, 'IL', 'ISR', 376, 972, '以色列'),
(104, 'IM', 'IMN', 833, 0, '马恩岛'),
(105, 'IN', 'IND', 356, 91, '印度'),
(106, 'IO', 'IOT', 86, 0, '英属印度洋领地'),
(107, 'IQ', 'IRQ', 368, 964, '伊拉克'),
(108, 'IR', 'IRN', 364, 98, '伊朗'),
(109, 'IS', 'ISL', 352, 354, '冰岛'),
(110, 'IT', 'ITA', 380, 39, '意大利'),
(111, 'JE', 'JEY', 832, 0, '泽西岛'),
(112, 'JM', 'JAM', 388, 1876, '牙买加'),
(113, 'JO', 'JOR', 400, 962, '约旦'),
(114, 'JP', 'JPN', 392, 81, '日本'),
(115, 'KE', 'KEN', 404, 254, '肯尼亚'),
(116, 'KG', 'KGZ', 417, 331, '吉尔吉斯斯坦'),
(117, 'KH', 'KHM', 116, 855, '柬埔寨'),
(118, 'KI', 'KIR', 296, 0, '基里巴斯'),
(119, 'KM', 'COM', 174, 0, '科摩罗'),
(120, 'KP', 'PRK', 408, 850, '朝鲜'),
(121, 'KR', 'KOR', 410, 82, '韩国'),
(122, 'KW', 'KWT', 414, 965, '科威特'),
(123, 'KY', 'CYM', 136, 0, '开曼群岛'),
(124, 'KZ', 'KAZ', 398, 327, '哈萨克斯坦'),
(125, 'LA', 'LAO', 418, 856, '老挝'),
(126, 'LB', 'LBN', 422, 961, '黎巴嫩'),
(127, 'LC', 'LCA', 662, 1758, '圣卢西亚'),
(128, 'LI', 'LIE', 438, 423, '列支敦士登'),
(129, 'LK', 'LKA', 144, 94, '斯里兰卡'),
(130, 'LR', 'LBR', 430, 231, '利比里亚'),
(131, 'LS', 'LSO', 426, 266, '莱索托'),
(132, 'LT', 'LTU', 440, 370, '立陶宛'),
(133, 'LU', 'LUX', 442, 352, '卢森堡'),
(134, 'LV', 'LVA', 428, 371, '拉脱维亚'),
(135, 'LY', 'LBY', 434, 218, '利比亚'),
(136, 'MA', 'MAR', 504, 212, '摩洛哥'),
(137, 'MC', 'MCO', 492, 377, '摩纳哥'),
(138, 'MD', 'MDA', 498, 373, '摩尔多瓦'),
(139, 'ME', 'MNE', 499, 0, '黑山'),
(140, 'MF', 'MAF', 663, 0, '法属圣马丁'),
(141, 'MG', 'MDG', 450, 261, '马达加斯加'),
(142, 'MH', 'MHL', 584, 0, '马绍尔群岛'),
(143, 'MK', 'MKD', 807, 0, '马其顿'),
(144, 'ML', 'MLI', 466, 223, '马里'),
(145, 'MM', 'MMR', 104, 95, '缅甸'),
(146, 'MN', 'MNG', 496, 976, '蒙古国'),
(147, 'MO', 'MAC', 446, 853, '澳门'),
(148, 'MP', 'MNP', 580, 0, '北马里亚纳群岛'),
(149, 'MQ', 'MTQ', 474, 0, '马提尼克'),
(150, 'MR', 'MRT', 478, 0, '毛里塔尼亚'),
(151, 'MS', 'MSR', 500, 1664, '蒙塞拉特岛'),
(152, 'MT', 'MLT', 470, 356, '马耳他'),
(153, 'MU', 'MUS', 480, 230, '毛里求斯'),
(154, 'MV', 'MDV', 462, 960, '马尔代夫'),
(155, 'MW', 'MWI', 454, 265, '马拉维'),
(156, 'MX', 'MEX', 484, 52, '墨西哥'),
(157, 'MY', 'MYS', 458, 60, '马来西亚'),
(158, 'MZ', 'MOZ', 508, 258, '莫桑比克'),
(159, 'NA', 'NAM', 516, 264, '纳米比亚'),
(160, 'NC', 'NCL', 540, 0, '新喀里多尼亚'),
(161, 'NE', 'NER', 562, 977, '尼日尔'),
(162, 'NF', 'NFK', 574, 0, '诺福克岛'),
(163, 'NG', 'NGA', 566, 234, '尼日利亚'),
(164, 'NI', 'NIC', 558, 505, '尼加拉瓜'),
(165, 'NL', 'NLD', 528, 31, '荷兰'),
(166, 'NO', 'NOR', 578, 47, '挪威'),
(167, 'NP', 'NPL', 524, 977, '尼泊尔'),
(168, 'NR', 'NRU', 520, 674, '瑙鲁'),
(169, 'NU', 'NIU', 570, 0, '纽埃'),
(170, 'NZ', 'NZL', 554, 64, '新西兰'),
(171, 'OM', 'OMN', 512, 968, '阿曼'),
(172, 'PA', 'PAN', 591, 507, '巴拿马'),
(173, 'PE', 'PER', 604, 51, '秘鲁'),
(174, 'PF', 'PYF', 258, 689, '法属波利尼西亚'),
(175, 'PG', 'PNG', 598, 675, '巴布亚新几内亚'),
(176, 'PH', 'PHL', 608, 63, '菲律宾'),
(177, 'PK', 'PAK', 586, 92, '巴基斯坦'),
(178, 'PL', 'POL', 616, 48, '波兰'),
(179, 'PM', 'SPM', 666, 0, '圣皮埃尔和密克隆'),
(180, 'PN', 'PCN', 612, 0, '皮特凯恩群岛'),
(181, 'PR', 'PRI', 630, 1787, '波多黎各'),
(182, 'PS', 'PSE', 275, 0, '巴勒斯坦'),
(183, 'PT', 'PRT', 620, 351, '葡萄牙'),
(184, 'PW', 'PLW', 585, 0, '帕劳'),
(185, 'PY', 'PRY', 600, 595, '巴拉圭'),
(186, 'QA', 'QAT', 634, 974, '卡塔尔'),
(187, 'RE', 'REU', 638, 0, '留尼汪'),
(188, 'RO', 'ROU', 642, 40, '罗马尼亚'),
(189, 'RS', 'SRB', 688, 0, '塞尔维亚'),
(190, 'RU', 'RUS', 643, 7, '俄罗斯'),
(191, 'RW', 'RWA', 646, 0, '卢旺达'),
(192, 'SA', 'SAU', 682, 966, '沙特阿拉伯'),
(193, 'SB', 'SLB', 90, 677, '所罗门群岛'),
(194, 'SC', 'SYC', 690, 248, '塞舌尔'),
(195, 'SD', 'SDN', 729, 249, '苏丹'),
(196, 'SE', 'SWE', 752, 46, '瑞典'),
(197, 'SG', 'SGP', 702, 65, '新加坡'),
(198, 'SH', 'SHN', 654, 0, '圣赫勒拿'),
(199, 'SI', 'SVN', 705, 386, '斯洛文尼亚'),
(200, 'SJ', 'SJM', 744, 0, '斯瓦尔巴群岛和扬马延岛'),
(201, 'SK', 'SVK', 703, 421, '斯洛伐克'),
(202, 'SL', 'SLE', 694, 232, '塞拉利昂'),
(203, 'SM', 'SMR', 674, 378, '圣马力诺'),
(204, 'SN', 'SEN', 686, 221, '塞内加尔'),
(205, 'SO', 'SOM', 706, 252, '索马里'),
(206, 'SR', 'SUR', 740, 597, '苏里南'),
(207, 'SS', 'SSD', 728, 0, '南苏丹'),
(208, 'ST', 'STP', 678, 239, '圣多美和普林西比'),
(209, 'SV', 'SLV', 222, 503, '萨尔瓦多'),
(210, 'SX', 'SXM', 534, 0, '荷属圣马丁'),
(211, 'SY', 'SYR', 760, 963, '叙利亚'),
(212, 'SZ', 'SWZ', 748, 268, '斯威士兰'),
(213, 'TC', 'TCA', 796, 0, '特克斯和凯科斯群岛'),
(214, 'TD', 'TCD', 148, 235, '乍得'),
(215, 'TF', 'ATF', 260, 0, '法属南部领地'),
(216, 'TG', 'TGO', 768, 228, '多哥'),
(217, 'TH', 'THA', 764, 66, '泰国'),
(218, 'TJ', 'TJK', 762, 992, '塔吉克斯坦'),
(219, 'TK', 'TKL', 772, 0, '托克劳'),
(220, 'TL', 'TLS', 626, 0, '东帝汶'),
(221, 'TM', 'TKM', 795, 993, '土库曼斯坦'),
(222, 'TN', 'TUN', 788, 216, '突尼斯'),
(223, 'TO', 'TON', 776, 676, '汤加'),
(224, 'TR', 'TUR', 792, 90, '土耳其'),
(225, 'TT', 'TTO', 780, 1809, '特立尼达和多巴哥'),
(226, 'TV', 'TUV', 798, 0, '图瓦卢'),
(227, 'TW', 'TWN', 158, 886, '台湾'),
(228, 'TZ', 'TZA', 834, 255, '坦桑尼亚'),
(229, 'UA', 'UKR', 804, 380, '乌克兰'),
(230, 'UG', 'UGA', 800, 256, '乌干达'),
(231, 'UM', 'UMI', 581, 0, '美国本土外小岛屿'),
(232, 'US', 'USA', 840, 1, '美国'),
(233, 'UY', 'URY', 858, 598, '乌拉圭'),
(234, 'UZ', 'UZB', 860, 233, '乌兹别克斯坦'),
(235, 'VA', 'VAT', 336, 0, '梵蒂冈'),
(236, 'VC', 'VCT', 670, 1784, '圣文森特和格林纳丁斯'),
(237, 'VE', 'VEN', 862, 58, '委内瑞拉'),
(238, 'VG', 'VGB', 92, 0, '英属维尔京群岛'),
(239, 'VI', 'VIR', 850, 0, '美属维尔京群岛'),
(240, 'VN', 'VNM', 704, 84, '越南'),
(241, 'VU', 'VUT', 548, 0, '瓦努阿图'),
(242, 'WF', 'WLF', 876, 0, '瓦利斯和富图纳'),
(243, 'WS', 'WSM', 882, 0, '萨摩亚'),
(244, 'YE', 'YEM', 887, 967, '也门'),
(245, 'YT', 'MYT', 175, 0, '马约特'),
(246, 'ZA', 'ZAF', 710, 27, '南非'),
(247, 'ZM', 'ZMB', 894, 260, '赞比亚'),
(248, 'ZW', 'ZWE', 716, 263, '津巴布韦');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;