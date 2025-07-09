-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 09, 2025 at 10:44 AM
-- Server version: 8.0.42
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trud`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Форма обратной связи', 6, 'add_feedbackform'),
(22, 'Can change Форма обратной связи', 6, 'change_feedbackform'),
(23, 'Can delete Форма обратной связи', 6, 'delete_feedbackform'),
(24, 'Can view Форма обратной связи', 6, 'view_feedbackform'),
(25, 'Can add Пользователь', 7, 'add_user'),
(26, 'Can change Пользователь', 7, 'change_user'),
(27, 'Can delete Пользователь', 7, 'delete_user'),
(28, 'Can view Пользователь', 7, 'view_user'),
(29, 'Can add Научная работа', 8, 'add_work'),
(30, 'Can change Научная работа', 8, 'change_work'),
(31, 'Can delete Научная работа', 8, 'delete_work'),
(32, 'Can view Научная работа', 8, 'view_work'),
(33, 'Can add Работа в коллекции', 9, 'add_collectionwork'),
(34, 'Can change Работа в коллекции', 9, 'change_collectionwork'),
(35, 'Can delete Работа в коллекции', 9, 'delete_collectionwork'),
(36, 'Can view Работа в коллекции', 9, 'view_collectionwork'),
(37, 'Can add Коллекция', 10, 'add_collection'),
(38, 'Can change Коллекция', 10, 'change_collection'),
(39, 'Can delete Коллекция', 10, 'delete_collection'),
(40, 'Can view Коллекция', 10, 'view_collection');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-07-05 13:32:02.421310', '2', 'Макаров Василий (vasiliy@gmail.com)', 2, '[{\"changed\": {\"fields\": [\"\\u0420\\u043e\\u043b\\u044c\"]}}]', 7, 3);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(10, 'main', 'collection'),
(9, 'main', 'collectionwork'),
(6, 'main', 'feedbackform'),
(7, 'main', 'user'),
(8, 'main', 'work'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-07-04 12:31:17.314149'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-07-04 12:31:17.429679'),
(3, 'auth', '0001_initial', '2025-07-04 12:31:17.798226'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-07-04 12:31:17.874805'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-07-04 12:31:17.881724'),
(6, 'auth', '0004_alter_user_username_opts', '2025-07-04 12:31:17.887932'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-07-04 12:31:17.893896'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-07-04 12:31:17.896844'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-07-04 12:31:17.903173'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-07-04 12:31:17.910159'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-07-04 12:31:17.916170'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-07-04 12:31:17.997620'),
(13, 'auth', '0011_update_proxy_permissions', '2025-07-04 12:31:18.006822'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-07-04 12:31:18.015139'),
(15, 'main', '0001_initial', '2025-07-04 12:31:18.589426'),
(16, 'admin', '0001_initial', '2025-07-04 12:31:18.784214'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-07-04 12:31:18.794674'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-07-04 12:31:18.804436'),
(19, 'sessions', '0001_initial', '2025-07-04 12:31:18.849161'),
(20, 'main', '0002_collection_collectionwork', '2025-07-05 10:52:52.008959'),
(21, 'main', '0003_work_pdf_file', '2025-07-05 11:34:40.088618'),
(22, 'main', '0004_work_cover_image', '2025-07-05 11:39:59.838835'),
(23, 'main', '0005_work_tags', '2025-07-05 12:05:26.377761'),
(24, 'main', '0006_work_views', '2025-07-05 12:10:27.388876'),
(25, 'main', '0007_user_date_joined', '2025-07-05 13:11:09.225709'),
(26, 'main', '0008_alter_user_role', '2025-07-05 13:31:39.517935'),
(27, 'main', '0009_collection_tags', '2025-07-05 13:38:45.572158'),
(28, 'main', '0010_collection_cover_image', '2025-07-05 14:05:55.935884'),
(29, 'main', '0011_feedbackform_processing_by_and_more', '2025-07-08 14:11:13.886684');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('d4wpfawkmgo4hwgeav0jtzu082p9j49u', '.eJxVjEEOwiAQRe_C2hAcBhCX7nsGMsBUqgaS0q6Md7dNutDtf-_9twi0LiWsnecwZXEVKE6_W6T05LqD_KB6bzK1usxTlLsiD9rl0DK_bof7d1Col612iRWjBn1Gn7wGzkgKeCRAYJsAiWFMxoO3zhjOpJzb4MUqNDZqJz5f3XI3cg:1uZS6U:igSc6ebkmuKpp-xXdlmr-BGMXddNtK1B9dfR-I9Ze8o', '2025-07-23 10:32:42.541912');

-- --------------------------------------------------------

--
-- Table structure for table `main_collection`
--

CREATE TABLE `main_collection` (
  `id` bigint NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` bigint NOT NULL,
  `tags` varchar(500) DEFAULT NULL,
  `cover_image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `main_collection`
--

INSERT INTO `main_collection` (`id`, `name`, `description`, `created_at`, `updated_at`, `created_by_id`, `tags`, `cover_image`) VALUES
(7, 'Искуственный интеллект', 'Данная коллекция объединяет современные научные исследования, посвящённые теоретическим основам и практическим применениям машинного обучения (ML) и искусственного интеллекта (AI). В сборник вошли статьи, рассматривающие широкий спектр тем — от базовых алгоритмов и нейронных сетей до новейших достижений в области глубокого обучения, обработки естественного языка, обучения с подкреплением и генеративных моделей.', '2025-07-09 10:24:40.595546', '2025-07-09 10:24:40.595546', 2, 'машинное обучение, искуственный интеллект', 'collections/covers/ml.jpg'),
(8, 'Биология', 'Данная коллекция представляет собой обширный сборник научных работ, посвящённых ключевым направлениям современной биологии и анатомии человека. В нее включены исследования, охватывающие как молекулярный и клеточный уровень организации живых систем, так и структурно-функциональные особенности органов и систем организма человека.', '2025-07-09 10:27:33.309814', '2025-07-09 10:27:33.309814', 2, 'биология, анатомия', 'collections/covers/биологя.jpg'),
(9, 'Физика', 'Данная коллекция объединяет широкий спектр научных исследований, посвящённых фундаментальным и прикладным аспектам физики — науки, лежащей в основе понимания природы материи, энергии и взаимодействий. В сборнике представлены труды по таким ключевым направлениям, как классическая механика, электродинамика, термодинамика, квантовая физика, физика твёрдого тела, астрофизика, оптика и ядерная физика.', '2025-07-09 10:28:45.806343', '2025-07-09 10:28:45.806343', 2, 'физика, наука, мир', 'collections/covers/физика.png');

-- --------------------------------------------------------

--
-- Table structure for table `main_collectionwork`
--

CREATE TABLE `main_collectionwork` (
  `id` bigint NOT NULL,
  `added_at` datetime(6) NOT NULL,
  `added_by_id` bigint NOT NULL,
  `collection_id` bigint NOT NULL,
  `work_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `main_collectionwork`
--

INSERT INTO `main_collectionwork` (`id`, `added_at`, `added_by_id`, `collection_id`, `work_id`) VALUES
(8, '2025-07-09 10:24:40.601654', 2, 7, 8),
(9, '2025-07-09 10:24:40.606783', 2, 7, 2),
(10, '2025-07-09 10:27:33.316134', 2, 8, 5),
(11, '2025-07-09 10:27:33.322151', 2, 8, 4),
(12, '2025-07-09 10:28:45.812693', 2, 9, 7),
(13, '2025-07-09 10:28:45.819097', 2, 9, 6),
(14, '2025-07-09 10:28:45.823898', 2, 9, 3);

-- --------------------------------------------------------

--
-- Table structure for table `main_feedbackform`
--

CREATE TABLE `main_feedbackform` (
  `id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `student_number` varchar(30) DEFAULT NULL,
  `description` longtext NOT NULL,
  `date_submitted` datetime(6) NOT NULL,
  `processing_by_id` bigint DEFAULT NULL,
  `processing_ended_at` datetime(6) DEFAULT NULL,
  `processing_started_at` datetime(6) DEFAULT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `main_feedbackform`
--

INSERT INTO `main_feedbackform` (`id`, `name`, `email`, `phone`, `student_number`, `description`, `date_submitted`, `processing_by_id`, `processing_ended_at`, `processing_started_at`, `status`) VALUES
(1, 'Руслан', 'ruslan@gmail.com', '1231231123', '109172401', 'Не могу зарегистрироватся', '2025-07-05 11:11:40.844410', 2, '2025-07-08 14:46:33.914723', '2025-07-08 14:15:28.987083', 'resolved');

-- --------------------------------------------------------

--
-- Table structure for table `main_user`
--

CREATE TABLE `main_user` (
  `id` bigint NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `student_number` varchar(30) DEFAULT NULL,
  `role` varchar(20) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_joined` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `main_user`
--

INSERT INTO `main_user` (`id`, `password`, `last_login`, `is_superuser`, `name`, `surname`, `email`, `student_number`, `role`, `is_active`, `is_staff`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$5jeo2HKPAphMUSokDRPTGn$2eYIuwNfkelEs18hi7/aHdRcCF0rzsQWFZU9P0ErpSs=', '2025-07-09 10:21:26.316827', 0, 'Дмитрий', 'Щербаков', 'dima@gmail.com', '991023713', 'user', 1, 0, '2025-07-05 16:11:27.000000'),
(2, 'pbkdf2_sha256$1000000$jR6hhAaGMH3mdipINgqQPe$IdZzKN8DoUERlME9GhCTEwu0X4Ulqmx9Hzu7X+7T+fw=', '2025-07-09 10:22:42.506886', 0, 'Василий', 'Макаров', 'vasiliy@gmail.com', '0912049102', 'manager', 1, 0, '2025-07-05 13:13:35.000000'),
(3, 'pbkdf2_sha256$1000000$HNWpqF9ed0Kz4Ot4Iqbg7T$JQSWlTUHvaxmod1yRFGS3kR9Onx04XyErqGeKdok2UU=', '2025-07-09 10:32:19.142591', 1, 'Admin', 'Adminov', 'admin@gmail.com', NULL, 'administrator', 1, 1, '2025-07-05 13:23:29.758957'),
(4, 'pbkdf2_sha256$1000000$86mLAY7xueB5CPNHl5rljY$tCkWiu7KwOw4sMsU/Bzrcsmc/owLDlt/8c25FuXxV1s=', '2025-07-09 10:32:42.536768', 0, 'Илья', 'Шугаев', 'ilya@gmail.com', '18712921', 'user', 1, 0, '2025-07-08 15:39:01.061550'),
(5, 'pbkdf2_sha256$1000000$sK08FjNCgJyB7fb8i887aF$jyroOEPEZ0VeAddwMeZ37LSO0jXcL4fHqH6Xfa+20iw=', '2025-07-09 10:19:39.799497', 0, 'Анастасия', 'Сабурова', 'nastya@gmail.com', '9908120948', 'user', 1, 0, '2025-07-09 09:57:55.763144'),
(6, 'pbkdf2_sha256$1000000$5aJS2xZoaO2ZYh4kpn8AeH$bZuwzdXgMQP92/qABQDVXLLMc0A3mT+MdmA6gKgVO4c=', '2025-07-09 10:13:13.530977', 0, 'Михаил', 'Валиев', 'misha@gmail.com', '79871283', 'user', 1, 0, '2025-07-09 10:13:13.524900');

-- --------------------------------------------------------

--
-- Table structure for table `main_user_groups`
--

CREATE TABLE `main_user_groups` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `main_user_user_permissions`
--

CREATE TABLE `main_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `main_work`
--

CREATE TABLE `main_work` (
  `id` bigint NOT NULL,
  `name` varchar(200) NOT NULL,
  `date_published` datetime(6) NOT NULL,
  `short_description` varchar(300) NOT NULL,
  `long_description` longtext NOT NULL,
  `likes` int UNSIGNED NOT NULL,
  `author_id` bigint NOT NULL,
  `pdf_file` varchar(100) DEFAULT NULL,
  `cover_image` varchar(100) DEFAULT NULL,
  `tags` varchar(500) DEFAULT NULL,
  `views` int UNSIGNED NOT NULL
) ;

--
-- Dumping data for table `main_work`
--

INSERT INTO `main_work` (`id`, `name`, `date_published`, `short_description`, `long_description`, `likes`, `author_id`, `pdf_file`, `cover_image`, `tags`, `views`) VALUES
(2, 'Сила подделки: влияние алгоритма ранжирования, расширенного дизайна и симметричной статистики', '2025-07-05 11:53:22.961818', 'Фильтр подделки — это недавний метод контроля частоты ложных срабатываний (FDR) для линейных моделей высокой размерности.', 'Фильтр подделки — это недавний метод контроля частоты ложных срабатываний (FDR) для линейных\r\nмоделей высокой размерности. Мы отмечаем, что у подделки есть три ключевых компонента: алгоритм ранжирования,\r\nрасширенный дизайн и симметричная статистика, и каждый компонент допускает множественный выбор.\r\nРассматривая различные комбинации трех компонентов, мы получаем набор\r\nвариантов подделки. Все эти варианты гарантируют контроль FDR с конечной выборкой, и наша цель — сравнить их мощность. Мы предполагаем модель редких и слабых сигналов на коэффициентах регрессии и сравниваем мощность различных вариантов подделки, выводя явные формулы\r\nложноположительного и ложноотрицательного коэффициентов. Наши результаты дают новое представление о том, как\r\nповысить мощность при контроле FDR на целевом уровне. Мы также сравниваем мощность\r\nподделки с ее прототипом — методом, который использует тот же алгоритм ранжирования, но имеет доступ\r\nк идеальному порогу. Сравнение показывает дополнительную цену, которую платят, находя\r\nуправляемый данными порог для контроля FDR. Ключевые слова: CI-knockoff, ошибка Хэмминга, фазовая диаграмма, модель Rare/Weak Signal, SDPknockoff, ранжирование переменных, выбор переменных', 2, 1, 'works/pdfs/sciwork.pdf', 'works/covers/статистика.jpg', 'машинное обучение', 16),
(3, 'Туннелирующие фотоны бросают вызов интерпретации квантовой механики', '2025-07-05 13:20:11.481427', 'Измерения с ограниченными фотонами ставят под сомнение прогноз о том, что частицы, которые «квантовым образом туннелируют» в бесконечно длинные барьеры, застревают там.', 'В этом году отмечается Международный год квантовой науки и технологий, отмечающий столетие развития квантовой механики. Квантовая механика делает точные предсказания на атомном и субатомном уровнях, но физики все еще спорят о том, как следует интерпретировать уравнения квантовой теории. Шароглазова и др. в своей статье в журнале Nature1 протестировали альтернативу стандартной интерпретации квантовой теории, измерив, сколько времени требуется фотонам для выполнения квантового явления, называемого туннелированием. Эта альтернативная интерпретация, называемая бомовской механикой, предсказывает, что туннелирование заставляет квантовые частицы оставаться неподвижными внутри бесконечно длинных барьеров, но выводы исследователей ставят под сомнение эту теорию', 0, 1, 'works/pdfs/d41586-025-01765-x.pdf', 'works/covers/physics.jpg', 'физика, математика, квантовая физика', 6),
(4, 'Мировой опыт регистрации и применения препаратов для генной терапии в клинической практике', '2025-07-09 09:51:34.766961', 'Внедрение инновационных препаратов в клиническую практику', 'На современном этапе развитии биомедицины происходит активное внедрение в клиническую практику достижения молекулярной биологии и генетической инженерии для создания инновационных препаратов с целью лечения тяжелых заболеваний или состояний, одним из направлений которой является генная терапия.', 0, 4, 'works/pdfs/mirovoy-opyt-registratsii-i-primeneniya-preparatov-dlya-gennoy-terapii-v-klin_YTSlyCI.pdf', 'works/covers/gen_therapy.jpg', 'биология, анатомия, генная терапия', 0),
(5, 'Микробиом человека', '2025-07-09 09:54:58.935160', 'Симбиотическая микрофлора играет огромную роль в обеспечении здорового состояния нашего организма. Она защищает от патогенов, поддерживает иммунитет, обеспечивает производство важных компонентов питания.', 'Симбиотическая микрофлора играет огромную роль в обеспечении здорового состояния нашего организма. Она\r\nзащищает от патогенов, поддерживает иммунитет, обеспечивает производство важных компонентов питания. Микробиота человека включает, по всей видимости, несколько тысяч видов грибов, эубактерий, архей и вирусов. Суммарное количество клеток только эубактерий в составе микробиоты превышает десять триллионов, что в сто раз больше числа собственных клеток организма человека. С появлением методов высокопроизводительного секвенирования исследователи получили возможность очень точной и комплексной оценки всего микробного сообщества с глубиной до тысячных долей процента (по содержанию микроба). Это позволило выйти на новый уровень понимания взаимосвязи здоровья человека и состояния его микробиома. В данном обзоре представлено современное состояние исследований ключевых микробных биоценозов человека — пищеварительного и урогенитального трактов. Менее изученные биоценозы носа и носоглотки, слухового канала, глаз, кожи и ряд других в обзор не вошли.\r\n\r\nКлючевые слова: микробный биоценоз, микрофлора кишечника, урогенитальный, пародонтальный, метагеном, высокопроизводительное секвенирование', 0, 4, 'works/pdfs/mikrobiom-cheloveka.pdf', 'works/covers/микробиом.jpg', 'микро биология, биология, метагеном, биоценоз', 0),
(6, 'Тёмная материя в галактиках', '2025-07-09 10:10:11.079900', 'Вопрос о тёмной материи в галактиках, её количестве и распределении', 'Вопрос о тёмной материи в галактиках, её количестве и распределении долгие годы остаётся дискуссионным, особенно если учесть, что тела или частицы, образующие тёмную материю, до сих пор не обнаружены. Мнения специалистов варьируются от утверждения о существовании очень большого количества абсолютно \"тёмных\" галактик до отрицания сколь-либо значимого количества небарионной тёмной материи. Проведено обсуждение астрономических свидетельств наличия тёмной материи внутри галактик, её связи с видимой материей, а также попыток оценить её массу и характер распределения в галактиках по данным наблюдений (фотометрия, динамика, гравитационное линзирование и др.), не вдаваясь в подробное рассмотрение космологических аспектов существования тёмной материи. Авторы считают наличие тёмной материи в галактиках и вокруг них хорошо аргументированным фактом. В заключении рассмотрены возможные механизмы влияния тёмного гало на процессы внутри галактик.', 0, 5, 'works/pdfs/темная_материя.pdf', 'works/covers/universe0.jpg', 'физика, космос, материя, темная материя', 0),
(7, 'Квантовые компьютеры и квантовые вычисления', '2025-07-09 10:15:37.740594', 'Принцип работы квантовых компьютеров', 'Обзор посвящен изложению принципов работы квантовых компьютеров и их элементов. Представлена теория идеальных компьютеров, не взаимодействующих с окружением и не подверженных процессам квантовой декогерентизации. Исследованы процессы декогерентизации в квантовых компьютерах. Рассмотрены методы коррекции ошибок в квантовых вычислениях, обусловленных декогерентизацией состояния квантового компьютера, а также возможные методы подавления процессов декогерентизации. Обзор завершается кратким перечислением предложений по реализации квантовых компьютеров.', 0, 6, 'works/pdfs/квант.pdf', 'works/covers/квантовый.jpg', 'физика, математика, квантовая физика, компьютеры, квантовые компьютеры, вычисления', 0),
(8, 'Применение методов глубокого обучения в задаче распознавания изображений', '2025-07-09 10:18:40.351926', 'Данная работа посвящена распознаванию (классификации) изображений коллекции, собранной Alex Krizhevsky, Vinod Nair и Geoffrey Hinton', 'Компьютерное зрение – одна из главных областей теории искусственных интеллектов, активно\r\nразвивающейся последние 50 лет с наибольшим пиком активности последние 10 лет.\r\nГлубинное (глубокое) обучение – раздел теории нейронных сетей, разрабатывающий и исследующий\r\nмодели нейронных сетей с большим количеством слоев.\r\nФормально, нейросети решают задачу аппроксимации неизвестной функции. На сегодняшний день все\r\nобъяснения эффективности методов обучения нейросетей являются гипотетическими. Часть гипотез\r\nподтверждается многочисленными экспериментами, часть гипотез опровергается, что приводит к\r\nвозникновению новых гипотез. Каждый год публикуются десятки работ, в частности, [3,6], пытающиеся\r\nобобщить и формализовать результаты экспериментов.', 0, 6, 'works/pdfs/primenenie-metodov-glubokogo-obucheniya-v-zadache-raspoznavaniya-izobrazheniy.pdf', 'works/covers/dl.png', 'машинное обучение, распозвнование изображений, глубокое обучение, искуственный интеллект', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_main_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `main_collection`
--
ALTER TABLE `main_collection`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_collection_created_by_id_65f66ffb_fk_main_user_id` (`created_by_id`);

--
-- Indexes for table `main_collectionwork`
--
ALTER TABLE `main_collectionwork`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `main_collectionwork_collection_id_work_id_eec86132_uniq` (`collection_id`,`work_id`),
  ADD KEY `main_collectionwork_added_by_id_f1f560dd_fk_main_user_id` (`added_by_id`),
  ADD KEY `main_collectionwork_work_id_13c087a6_fk_main_work_id` (`work_id`);

--
-- Indexes for table `main_feedbackform`
--
ALTER TABLE `main_feedbackform`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_feedbackform_processing_by_id_ec90a936_fk_main_user_id` (`processing_by_id`);

--
-- Indexes for table `main_user`
--
ALTER TABLE `main_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `main_user_groups`
--
ALTER TABLE `main_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `main_user_groups_user_id_group_id_ae195797_uniq` (`user_id`,`group_id`),
  ADD KEY `main_user_groups_group_id_a337ba62_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `main_user_user_permissions`
--
ALTER TABLE `main_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `main_user_user_permissions_user_id_permission_id_96b9fadf_uniq` (`user_id`,`permission_id`),
  ADD KEY `main_user_user_permi_permission_id_cd2b56a3_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `main_work`
--
ALTER TABLE `main_work`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_work_author_id_551e0238_fk_main_user_id` (`author_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `main_collection`
--
ALTER TABLE `main_collection`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `main_collectionwork`
--
ALTER TABLE `main_collectionwork`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `main_feedbackform`
--
ALTER TABLE `main_feedbackform`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `main_user`
--
ALTER TABLE `main_user`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `main_user_groups`
--
ALTER TABLE `main_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_user_user_permissions`
--
ALTER TABLE `main_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_work`
--
ALTER TABLE `main_work`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`);

--
-- Constraints for table `main_collection`
--
ALTER TABLE `main_collection`
  ADD CONSTRAINT `main_collection_created_by_id_65f66ffb_fk_main_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `main_user` (`id`);

--
-- Constraints for table `main_collectionwork`
--
ALTER TABLE `main_collectionwork`
  ADD CONSTRAINT `main_collectionwork_added_by_id_f1f560dd_fk_main_user_id` FOREIGN KEY (`added_by_id`) REFERENCES `main_user` (`id`),
  ADD CONSTRAINT `main_collectionwork_collection_id_3ad600fd_fk_main_collection_id` FOREIGN KEY (`collection_id`) REFERENCES `main_collection` (`id`),
  ADD CONSTRAINT `main_collectionwork_work_id_13c087a6_fk_main_work_id` FOREIGN KEY (`work_id`) REFERENCES `main_work` (`id`);

--
-- Constraints for table `main_feedbackform`
--
ALTER TABLE `main_feedbackform`
  ADD CONSTRAINT `main_feedbackform_processing_by_id_ec90a936_fk_main_user_id` FOREIGN KEY (`processing_by_id`) REFERENCES `main_user` (`id`);

--
-- Constraints for table `main_user_groups`
--
ALTER TABLE `main_user_groups`
  ADD CONSTRAINT `main_user_groups_group_id_a337ba62_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `main_user_groups_user_id_df502602_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`);

--
-- Constraints for table `main_user_user_permissions`
--
ALTER TABLE `main_user_user_permissions`
  ADD CONSTRAINT `main_user_user_permi_permission_id_cd2b56a3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `main_user_user_permissions_user_id_451ce57f_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`);

--
-- Constraints for table `main_work`
--
ALTER TABLE `main_work`
  ADD CONSTRAINT `main_work_author_id_551e0238_fk_main_user_id` FOREIGN KEY (`author_id`) REFERENCES `main_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
