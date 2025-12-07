-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 13, 2025 lúc 05:26 AM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `banhkeo`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(55) NOT NULL,
  `email` varchar(55) NOT NULL,
  `password` varchar(50) NOT NULL,
  `sdt` varchar(11) NOT NULL,
  `address` varchar(99) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `admin`
--

INSERT INTO `admin` (`id`, `username`, `email`, `password`, `sdt`, `address`, `created_at`) VALUES
(1, 'huyhuy15', 'huy1505@gmail.com', '12345', '123456789', 'Ba Vì , Hà Nội', '2025-03-13 05:58:14'),
(3, 'huy1505', 'huyhuy@gmail.com', '12345', '123456789', 'Nam Từ Liêm, Hà Nội', '2025-04-02 17:07:00'),
(4, 'hai', 'hai34@gmai.com', '12345', '0912345678', 'Ngã 3 Ba Trại, Vĩnh Phúc', '2025-04-16 16:46:33'),
(5, 'Anh14', 'Anh1414@gmail.com', '12345', '0123456789', 'Ba Vì ,Hà Nội', '2025-04-16 16:50:11'),
(6, 'Tubeo', 'Tu2@gmail.com', '12345', '0912345678', 'Số 5, Vĩnh Tường , Vĩnh Phúc', '2025-04-16 16:52:20'),
(7, 'dung23', 'dung23@gmail.com', '12345', '0998765431', 'Ba Vì ,Hà Nội', '2025-04-18 08:30:58'),
(8, 'Vyvy', 'Vy123@gmail.com', '12345', '0912345678', 'Ba Vì ,Hà Nội', '2025-04-18 08:37:40'),
(9, 'huyhuy1505', 'Huy@gmail.com', '12345', '0375891580', 'Ba Vì ,Hà Nội', '2025-04-18 08:38:44');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietdonhang`
--

CREATE TABLE `chitietdonhang` (
  `id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chitietdonhang`
--

INSERT INTO `chitietdonhang` (`id`, `order_id`, `product_id`, `quantity`, `price`) VALUES
(16, 11, 9, 3, 0),
(17, 11, 11, 1, 0),
(18, 12, 17, 2, 0),
(19, 12, 16, 2, 0),
(20, 12, 15, 1, 0),
(21, 12, 14, 1, 0),
(22, 13, 4, 4, 0),
(23, 13, 10, 3, 0),
(24, 13, 12, 2, 0),
(25, 14, 1, 2, 0),
(26, 14, 11, 1, 0),
(27, 15, 13, 2, 0),
(28, 15, 8, 5, 0),
(29, 15, 10, 2, 0),
(30, 15, 7, 2, 0),
(31, 16, 12, 1, 0),
(32, 16, 9, 1, 0),
(33, 16, 11, 1, 0),
(34, 17, 18, 1, 0),
(35, 18, 5, 1, 0),
(36, 18, 6, 3, 0),
(37, 18, 2, 1, 0),
(38, 19, 14, 2, 0),
(39, 20, 10, 2, 0),
(40, 20, 8, 3, 0),
(41, 21, 12, 1, 0),
(42, 22, 5, 2, 0),
(43, 23, 16, 1, 0),
(44, 24, 14, 1, 0),
(45, 25, 18, 1, 0),
(46, 26, 10, 3, 0),
(47, 26, 8, 2, 0),
(48, 27, 14, 1, 0),
(49, 28, 10, 2, 0),
(50, 28, 2, 2, 0),
(51, 28, 11, 3, 0),
(52, 29, 16, 1, 0),
(53, 30, 9, 1, 0),
(54, 31, 6, 2, 0),
(55, 32, 4, 2, 0),
(56, 33, 15, 1, 0),
(57, 34, 13, 1, 0),
(58, 35, 8, 1, 0),
(59, 35, 7, 1, 0),
(60, 36, 18, 1, 0),
(61, 37, 18, 4, 0),
(62, 38, 13, 2, 0),
(63, 39, 17, 1, 0),
(64, 40, 14, 1, 0),
(65, 41, 10, 1, 0),
(66, 42, 17, 2, 0),
(67, 43, 12, 1, 0),
(68, 44, 11, 1, 0),
(69, 45, 9, 1, 0),
(70, 46, 13, 1, 0),
(71, 47, 16, 1, 0),
(72, 48, 18, 1, 0),
(73, 49, 17, 1, 0),
(74, 50, 12, 1, 0),
(75, 51, 8, 1, 0),
(76, 51, 10, 3, 0),
(77, 52, 5, 1, 0),
(78, 53, 16, 1, 0),
(79, 54, 12, 1, 0),
(80, 55, 7, 1, 0),
(81, 56, 11, 1, 0),
(82, 57, 12, 1, 0),
(83, 58, 10, 1, 0),
(84, 59, 13, 1, 0),
(85, 60, 13, 1, 0),
(86, 61, 17, 3, 0),
(87, 62, 10, 1, 0),
(88, 63, 12, 1, 0),
(89, 64, 17, 1, 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `admin_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`id`, `name`, `admin_id`) VALUES
(1, 'Chocolate', NULL),
(2, 'Keo deo', NULL),
(3, 'Banh quy', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `donhang`
--

CREATE TABLE `donhang` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `status` enum('pending','completed','shipped') DEFAULT 'pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `admin_id` int(11) DEFAULT NULL,
  `address` varchar(99) NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `donhang`
--

INSERT INTO `donhang` (`id`, `user_id`, `total_price`, `status`, `created_at`, `admin_id`, `address`, `updated_at`) VALUES
(11, 5, 97000.00, 'completed', '2025-04-01 16:26:38', NULL, 'Ngõ1 nhà 2 Hà Nội', '2025-04-03 15:28:06'),
(12, 5, 391000.00, 'completed', '2025-04-02 16:11:33', NULL, 'Đối diện 12 , ngã 3 Hà Nội', '2025-04-03 15:41:56'),
(13, 5, 370000.00, 'completed', '2025-04-02 16:15:49', NULL, 'Đối diện 12 , ngã 3 Hà Nội', '2025-04-03 15:42:41'),
(14, 5, 122000.00, 'completed', '2025-04-02 16:18:21', NULL, 'Ngã 3 Ba Trại, Vĩnh Phúc', '2025-04-08 15:31:42'),
(15, 6, 582000.00, 'completed', '2025-04-03 15:24:43', 1, 'Đầu ngõ 23, Ba VÌ, Hà Nội', '2025-04-08 15:31:37'),
(16, 6, 77000.00, 'completed', '2025-04-03 15:25:37', NULL, 'Đầu ngõ 23, Ba VÌ, Hà Nội', '2025-04-03 15:44:14'),
(17, 6, 42000.00, 'shipped', '2025-04-03 15:26:09', 1, 'Đầu ngõ 23, Ba VÌ, Hà Nội', '2025-04-08 15:31:33'),
(18, 11, 230000.00, 'shipped', '2025-04-08 17:01:52', 1, 'Ba Vì ,Hà Nội', '2025-04-22 06:17:52'),
(19, 11, 300000.00, 'completed', '2025-04-08 17:02:47', 3, 'Ba Vì ,Hà Nội', '2025-04-09 15:47:07'),
(20, 8, 270000.00, 'completed', '2025-04-09 15:05:37', 3, 'Số 5, Vĩnh Tường , Vĩnh Phúc', '2025-04-09 15:47:00'),
(21, 8, 30000.00, 'completed', '2025-04-09 15:06:08', 3, 'Số 5, Vĩnh Tường , Vĩnh Phúc', '2025-04-09 15:47:04'),
(22, 11, 120000.00, 'shipped', '2025-04-09 15:19:51', 3, 'Số 5, Vĩnh Tường , Vĩnh Phúc', '2025-04-09 15:46:53'),
(23, 11, 50000.00, 'pending', '2025-04-09 15:28:20', NULL, 'Số 5, Vĩnh Tường , Vĩnh Phúc', '2025-04-09 15:28:20'),
(24, 11, 150000.00, 'shipped', '2025-04-09 15:35:50', 3, 'Ngã 3 Ba Trại, Vĩnh Phúc', '2025-04-09 15:47:01'),
(25, 11, 42000.00, 'pending', '2025-04-09 15:42:38', NULL, 'Số 5, Vĩnh Tường , Vĩnh Phúc', '2025-04-09 15:42:38'),
(26, 5, 230000.00, 'completed', '2025-04-18 08:55:36', 1, 'Đầu ngõ 23, Ba VÌ, Hà Nội', '2025-04-19 10:55:58'),
(27, 5, 150000.00, 'pending', '2025-04-18 09:32:05', NULL, 'Ngõ1 nhà 2 Hà Nội', '2025-04-18 09:32:05'),
(28, 11, 166000.00, 'completed', '2025-04-18 14:52:39', 1, 'Khánh Thượng,Ba Vì ,Hà Nội', '2025-04-18 15:45:58'),
(29, 11, 50000.00, 'shipped', '2025-04-18 14:59:45', 3, 'Ba Vì ,Hà Nội', '2025-11-10 16:32:25'),
(30, 11, 25000.00, 'pending', '2025-04-18 15:12:04', NULL, 'Ba Vì ,Hà Nội', '2025-04-18 15:12:04'),
(31, 11, 100000.00, 'shipped', '2025-04-18 15:13:45', 1, 'Ba Vì ,Hà Nội', '2025-04-22 06:18:14'),
(32, 11, 110000.00, 'pending', '2025-04-18 15:21:52', NULL, 'Ba Vì ,Hà Nội', '2025-04-18 15:21:52'),
(33, 11, 45000.00, 'shipped', '2025-04-18 15:22:29', 1, 'Số 5, Vĩnh Tường , Vĩnh Phúc', '2025-04-22 06:17:54'),
(34, 11, 28000.00, 'pending', '2025-04-18 15:23:11', NULL, 'Ba Vì ,Hà Nội', '2025-04-18 15:23:11'),
(35, 11, 128000.00, 'pending', '2025-04-18 15:32:08', NULL, 'Ba Vì ,Hà Nội', '2025-04-18 15:32:08'),
(36, 11, 42000.00, 'pending', '2025-04-18 15:35:03', NULL, 'Ba Vì ,Hà Nội', '2025-04-18 15:35:03'),
(37, 5, 168000.00, 'shipped', '2025-04-19 10:54:28', 1, 'Ngõ1 nhà 2 Hà Nội', '2025-04-19 10:55:28'),
(38, 5, 56000.00, 'shipped', '2025-04-21 17:26:20', 3, 'Số 5, Vĩnh Tường , Vĩnh Phúc', '2025-11-10 16:37:05'),
(39, 5, 48000.00, 'pending', '2025-04-21 17:29:55', NULL, 'Ba Vì ,Hà Nội', '2025-04-21 17:29:55'),
(40, 5, 150000.00, 'completed', '2025-04-22 03:28:41', 1, 'Ngõ1 nhà 2 Hà Nội', '2025-11-10 16:35:59'),
(41, 5, 30000.00, 'pending', '2025-04-22 03:36:35', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 03:36:35'),
(42, 5, 96000.00, 'pending', '2025-04-22 03:42:17', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 03:42:17'),
(43, 5, 30000.00, 'pending', '2025-04-22 03:44:45', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 03:44:45'),
(44, 5, 22000.00, 'pending', '2025-04-22 03:47:32', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 03:47:32'),
(45, 5, 25000.00, 'pending', '2025-04-22 03:57:52', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 03:57:52'),
(46, 5, 28000.00, 'shipped', '2025-04-22 04:00:53', 3, 'Ba Vì ,Hà Nội', '2025-11-10 16:32:36'),
(47, 5, 50000.00, 'pending', '2025-04-22 04:10:18', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 04:10:18'),
(48, 5, 42000.00, 'pending', '2025-04-22 04:52:33', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 04:52:33'),
(49, 5, 48000.00, 'pending', '2025-04-22 04:53:45', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 04:53:45'),
(50, 5, 30000.00, 'pending', '2025-04-22 04:59:12', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 04:59:12'),
(51, 5, 160000.00, 'pending', '2025-04-22 05:18:59', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 05:18:59'),
(52, 5, 60000.00, 'pending', '2025-04-22 05:20:38', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 05:20:38'),
(53, 5, 50000.00, 'completed', '2025-04-22 05:24:56', 1, 'Ba Vì ,Hà Nội', '2025-11-10 16:35:53'),
(54, 5, 30000.00, 'pending', '2025-04-22 05:27:24', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 05:27:24'),
(55, 5, 58000.00, 'pending', '2025-04-22 05:31:51', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 05:31:51'),
(56, 5, 22000.00, 'pending', '2025-04-22 05:36:29', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 05:36:29'),
(57, 5, 30000.00, 'pending', '2025-04-22 05:39:25', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 05:39:25'),
(58, 5, 30000.00, 'pending', '2025-04-22 05:52:05', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 05:52:05'),
(59, 5, 28000.00, 'pending', '2025-04-22 06:07:11', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 06:07:11'),
(60, 5, 28000.00, 'pending', '2025-04-22 06:13:24', NULL, 'Ba Vì ,Hà Nội', '2025-04-22 06:13:24'),
(61, 7, 144000.00, 'pending', '2025-04-22 06:17:09', NULL, 'Hà Nội', '2025-04-22 06:17:09'),
(62, 5, 30000.00, 'pending', '2025-04-25 02:52:53', NULL, 'Ba Vì ,Hà Nội', '2025-04-25 02:52:53'),
(63, 5, 30000.00, 'completed', '2025-04-25 02:55:53', 3, 'Ba Vì ,Hà Nội', '2025-11-10 16:41:19'),
(64, 5, 48000.00, 'pending', '2025-11-11 10:31:52', NULL, 'ba vi, ha noi', '2025-11-11 10:31:52');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `giohang`
--

CREATE TABLE `giohang` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) DEFAULT 1,
  `price` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `giohang`
--

INSERT INTO `giohang` (`id`, `user_id`, `product_id`, `quantity`, `price`) VALUES
(70, 11, 17, 1, 48000),
(98, 5, 14, 1, 150000),
(99, 5, 13, 1, 28000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nhaphang`
--

CREATE TABLE `nhaphang` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_import_price` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `admin_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nhaphang`
--

INSERT INTO `nhaphang` (`id`, `product_id`, `name`, `quantity`, `unit_import_price`, `created_at`, `admin_id`) VALUES
(1, 6, '', 10, 40000, '2025-04-21 09:04:44', 1),
(2, 7, '', 12, 45000, '2025-04-21 09:04:44', 1),
(3, 15, '', 20, 30000, '2025-04-21 09:04:44', 1),
(5, 8, '', 20, 50000, '2025-04-21 09:08:24', 1),
(6, 18, 'Bánh Quy Dừa', 2, 60000, '2025-04-21 10:03:40', 1),
(7, 3, 'Banh quy bo', 4, 120000, '2025-04-21 10:03:40', 1),
(8, 1, 'Socola den', 1, 42000, '2025-04-21 10:04:45', 1),
(9, 5, 'Socola Hạnh Nhân', 20, 1000000, '2025-11-10 17:06:13', 1),
(10, 17, 'Bánh Quy Yến Mạch', 30, 1050000, '2025-11-10 17:06:13', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `price` int(10) NOT NULL,
  `import_price` int(10) NOT NULL,
  `stock` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `url_img` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `admin_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`id`, `name`, `description`, `price`, `import_price`, `stock`, `category_id`, `url_img`, `created_at`, `admin_id`) VALUES
(1, 'Socola den', 'Socola đen là loại sô cô la có hàm lượng ca cao cao (thường từ 50% trở lên), ít hoặc không có sữa. Nó có vị đắng đặc trưng, giàu chất chống oxy hóa và mang lại nhiều lợi ích cho sức khỏe, như hỗ trợ tim mạch và cải thiện tâm trạng.', 50000, 42000, 101, 1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrTkKEq2N1IUUqfAHqBf_V9HHMENsNTI9a0Q&s', '2025-03-13 05:58:14', NULL),
(2, 'Kẹo dẻo trái cây Lot', 'Kẹo dẻo trái cây LOT là loại kẹo mềm, dẻo dai với hương vị trái cây tự nhiên, thường có lớp đường phủ bên ngoài. Chúng có nhiều hình dạng và màu sắc bắt mắt, mang đến cảm giác ngon miệng và vui vẻ khi thưởng thức.', 20000, 15000, 197, 2, 'https://www.lottemart.vn/media/catalog/product/cache/0x0/9/5/9556296311777.jpg.webp', '2025-03-13 05:58:14', NULL),
(3, 'Banh quy bo', 'Bánh quy bơ là loại bánh quy giòn, xốp, có hương vị béo ngậy nhờ lượng bơ cao trong thành phần. Chúng thường có hình tròn hoặc vuông, thích hợp để thưởng thức cùng trà hoặc cà phê.', 35000, 30000, 154, 3, 'https://product.hstatic.net/200000459373/product/osifood__4__86ec385e42744770ae33a56186458a61_master.png', '2025-03-13 05:58:14', NULL),
(4, 'Socola Đen Nguyên Chất', 'Hương vị đắng nhẹ, nguyên chất 100%', 55000, 45000, 100, 1, 'https://bizweb.dktcdn.net/thumb/large/100/004/714/products/socola-nguyen-chat-75-percentage-2-f1f7aaf4-95da-4943-870a-086104bc6945.png?v=1635299044940', '2025-03-13 06:05:26', NULL),
(5, 'Socola Hạnh Nhân', 'Socola hạnh nhân là sự kết hợp giữa sô cô la và hạnh nhân, tạo nên hương vị bùi béo, giòn tan. Loại socola này có thể ở dạng thanh, viên hoặc phủ socola lên hạnh nhân nguyên hạt. Nó không chỉ thơm ngon mà còn giàu dinh dưỡng, tốt cho sức khỏe.', 60000, 50000, 140, 1, 'https://yeuhangngoai.net/wp-content/uploads/2022/02/keo-socola-sua-boc-hanh-nhan-kirkland-almonds-136kg.jpeg', '2025-03-13 06:05:26', NULL),
(6, 'Socola Sữa', 'Socola sữa là loại sô cô la chứa bơ ca cao, đường và sữa, có hương vị ngọt ngào và mềm mịn. Nhờ hàm lượng sữa cao, nó có kết cấu mịn, tan chảy nhanh trong miệng, được nhiều người yêu thích, đặc biệt là trẻ em.', 50000, 40000, 100, 1, 'https://vinacacao.com.vn/wp-content/uploads/2020/06/Capture.png', '2025-03-13 06:05:26', NULL),
(7, 'Socola Trắng', 'Hương vị socola trắng béo nhẹ, ngọt dịu', 58000, 45000, 93, 1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsjk662e7KCqISSNmCCBGko0wtF-rHFqM8cg&s', '2025-03-13 06:05:26', NULL),
(8, 'Thanh Socola Mix', 'Thanh socola mix là sự kết hợp của socola đen, socola sữa và socola trắng, tạo nên hương vị đa dạng và hài hòa. Mỗi lớp socola mang đặc trưng riêng: đắng nhẹ từ socola đen, béo ngậy từ socola sữa và ngọt thanh từ socola trắng. Sự pha trộn này mang đến trải nghiệm thưởng thức phong phú và hấp dẫn.', 70000, 50000, 130, 1, 'https://cf.shopee.vn/file/d1bfb3de3c78716f536651338edf345c', '2025-03-13 06:05:26', NULL),
(9, 'Kẹo Dẻo Hương Trái Cây', 'Kẹo dẻo hương trái cây là loại kẹo mềm, dẻo dai với nhiều hương vị trái cây như dâu, cam, nho, chanh. Chúng có màu sắc bắt mắt, thường được phủ lớp đường hoặc chua nhẹ, mang đến cảm giác ngon miệng và vui vẻ khi thưởng thức.', 25000, 15000, 200, 2, 'https://cdn.tgdd.vn/Products/Images/7199/305480/bhx/keo-deo-huong-trai-cay-hon-hop-alpenliebe-jelly-bien-xanh-long-lanh-goi-90g-202304081533455295.jpg', '2025-03-13 06:05:26', NULL),
(10, 'Kẹo Dẻo Dâu', 'Kẹo dẻo dâu là loại kẹo mềm, dai với hương vị dâu tây ngọt ngào và thơm mát. Chúng thường có màu đỏ hấp dẫn, có thể phủ đường hoặc chua nhẹ, mang lại cảm giác ngon miệng và thích hợp cho mọi lứa tuổi.', 30000, 20000, 180, 2, 'https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lz7izl2rf0dd6a', '2025-03-13 06:05:26', NULL),
(11, 'Kẹo Dẻo Hương Xoài', 'Kẹo dẻo hương xoài là loại kẹo mềm, dẻo với hương vị xoài chín thơm ngọt, mang đến cảm giác tươi mát và hấp dẫn. Chúng thường có màu vàng bắt mắt, có thể phủ lớp đường hoặc chua nhẹ, phù hợp để thưởng thức mọi lúc.', 22000, 15000, 160, 2, 'https://haiha-kotobuki.com.vn/wp-content/uploads/2024/03/k%E1%BA%B9o-xo%C3%A0i.jpg', '2025-03-13 06:05:26', NULL),
(12, 'Kẹo Dẻo Viên Mix Vị', 'Kẹo dẻo viên mix vị là loại kẹo mềm, dẻo dai với nhiều hương vị trái cây khác nhau như dâu, cam, nho, táo,... Mỗi viên kẹo có màu sắc rực rỡ, tạo cảm giác ngon miệng và thú vị khi thưởng thức. Đây là lựa chọn hoàn hảo cho những ai thích sự đa dạng trong hương vị.', 30000, 20000, 250, 2, 'https://www.lottemart.vn/media/catalog/product/cache/0x0/8/9/8936036028034.jpg.webp', '2025-03-13 06:05:26', NULL),
(13, 'Kẹo Dẻo Gấu', 'Kẹo dẻo gấu là loại kẹo mềm, dẻo dai có hình gấu nhỏ đáng yêu, nhiều màu sắc và hương vị trái cây như dâu, cam, nho, táo. Chúng có vị ngọt dịu, đôi khi hơi chua nhẹ, mang đến trải nghiệm vui nhộn và thú vị khi thưởng thức.', 28000, 15000, 220, 2, 'https://bizweb.dktcdn.net/thumb/grande/100/383/667/products/deo-3.jpg?v=1589796765580', '2025-03-13 06:05:26', NULL),
(14, 'Bánh Quy Bơ Pháp', 'Bánh quy bơ Pháp là loại bánh quy giòn xốp, được làm từ bơ nguyên chất, bột mì và đường, mang hương vị béo ngậy đặc trưng. Chúng thường có kết cấu mềm mịn, tan nhẹ trong miệng, thích hợp để thưởng thức cùng trà hoặc cà phê.', 150000, 110000, 150, 3, 'https://tuoimart.vn/wp-content/uploads/2024/10/BANH-LU-310G.jpg', '2025-03-13 06:05:26', NULL),
(15, 'Bánh Quy Hạnh Nhân', 'Bánh quy hạnh nhân là loại bánh giòn xốp, kết hợp giữa bơ thơm béo và hạnh nhân bùi giòn. Chúng có hương vị thơm ngon đặc trưng, thường được dùng kèm trà hoặc cà phê, thích hợp cho những ai yêu thích đồ ngọt tinh tế.', 45000, 30000, 150, 3, 'https://www.fujimarket.vn/images_upload/san-pham/4902888218859-banh-quy-hanh-nhan-morinaga-almond-cookies.png', '2025-03-13 06:05:26', NULL),
(16, 'Bánh Quy Chocolate Chip', 'Bánh quy chocolate chip là loại bánh quy giòn hoặc mềm, được trộn cùng những mẩu chocolate chip tan chảy, tạo nên hương vị thơm ngon, béo ngậy. Đây là món bánh ngọt phổ biến, thích hợp để thưởng thức cùng sữa, trà hoặc cà phê.', 50000, 40000, 140, 3, 'https://cf.shopee.vn/file/3a88dc28288423948467dbdd0ecbfb24', '2025-03-13 06:05:26', NULL),
(17, 'Bánh Quy Yến Mạch', 'Bánh quy yến mạch là loại bánh giòn xốp, làm từ yến mạch, bơ và đường, mang hương vị thơm ngon, béo nhẹ. Nhờ thành phần giàu chất xơ, bánh không chỉ ngon mà còn tốt cho sức khỏe, thích hợp cho bữa ăn nhẹ hoặc ăn vặt lành mạnh.', 48000, 35000, 150, 3, 'https://cdn.tgdd.vn/Files/2022/12/25/1498683/gioi-thieu-banh-quy-yen-mach-oat-krunch-moi-gion-ngon-tot-cho-suc-khoe-202212252327172797.jpg', '2025-03-13 06:05:26', NULL),
(18, 'Bánh Quy Dừa', 'Bánh quy dừa là loại bánh giòn xốp, có hương vị béo thơm đặc trưng từ dừa sấy. Bánh thường được làm từ bột mì, bơ, đường và dừa nạo, tạo nên độ giòn rụm và mùi thơm hấp dẫn. Đây là món ăn vặt ngon miệng, thích hợp để thưởng thức cùng trà hoặc cà phê.', 42000, 30000, 127, 3, 'https://vietnamlibra.com/images/products/2022/09/05/large/banh_quy_dua-removebg-preview_1662345082.png', '2025-03-13 06:05:26', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `sdt` varchar(10) NOT NULL,
  `diachi` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `sdt`, `diachi`, `created_at`) VALUES
(1, 'nguyenhoang', 'nguyenhoang@gmail.com', 'd123', '0', '', '2025-03-13 06:03:20'),
(2, 'tranminh', 'tranminh@gmail.com', 'minh', '0', 'qư', '2025-03-13 06:03:20'),
(3, 'lethu', 'lethu@gmail.com', 'thu12345', '0', '', '2025-03-13 06:03:20'),
(5, 'huyhuy15', 'huy@gmail.com', '123', '0', '', '2025-03-18 15:20:34'),
(6, 'hai', 'hai13@gmai.com', '123', '123456789', 'Cà Mau', '2025-03-18 16:00:10'),
(7, 'huyhuy1505', 'huyhuy@gmail.com', '123', '912345678', 'Thanh Xuân, Hà Nội', '2025-03-18 16:09:18'),
(8, 'giang', 'giang2002@gmai.com', '123', '0998765431', 'Ba Vì, Hải Dương', '2025-03-18 16:19:51'),
(9, 'huyhuy150503', 'buihuy150503@gmail.com', '123', '0375891580', 'Vân Hòa , Ba Vì, Hà Nội', '2025-03-18 16:25:00'),
(11, 'Anh14', 'Anh14@gmail.com', '123', '098652132', 'Ba Vì, ở', '2025-03-20 16:43:35');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Chỉ mục cho bảng `chitietdonhang`
--
ALTER TABLE `chitietdonhang`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `fk_danhmuc_admin` (`admin_id`);

--
-- Chỉ mục cho bảng `donhang`
--
ALTER TABLE `donhang`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `fk_donhang_admin` (`admin_id`);

--
-- Chỉ mục cho bảng `giohang`
--
ALTER TABLE `giohang`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Chỉ mục cho bảng `nhaphang`
--
ALTER TABLE `nhaphang`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `admin_id` (`admin_id`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`),
  ADD KEY `fk_sanpham_admin` (`admin_id`);

--
-- Chỉ mục cho bảng `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `chitietdonhang`
--
ALTER TABLE `chitietdonhang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=90;

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT cho bảng `donhang`
--
ALTER TABLE `donhang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT cho bảng `giohang`
--
ALTER TABLE `giohang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT cho bảng `nhaphang`
--
ALTER TABLE `nhaphang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT cho bảng `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `chitietdonhang`
--
ALTER TABLE `chitietdonhang`
  ADD CONSTRAINT `chitietdonhang_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `donhang` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `chitietdonhang_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `sanpham` (`id`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD CONSTRAINT `fk_danhmuc_admin` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE SET NULL;

--
-- Các ràng buộc cho bảng `donhang`
--
ALTER TABLE `donhang`
  ADD CONSTRAINT `donhang_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_donhang_admin` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE SET NULL;

--
-- Các ràng buộc cho bảng `giohang`
--
ALTER TABLE `giohang`
  ADD CONSTRAINT `giohang_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `giohang_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `sanpham` (`id`);

--
-- Các ràng buộc cho bảng `nhaphang`
--
ALTER TABLE `nhaphang`
  ADD CONSTRAINT `nhaphang_ibfk_2` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`);

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `fk_sanpham_admin` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `danhmuc` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
