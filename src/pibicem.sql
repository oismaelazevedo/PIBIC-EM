-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 14, 2021 at 03:26 AM
-- Server version: 5.7.17
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pibicem`
--

-- --------------------------------------------------------

--
-- Table structure for table `resposta`
--

CREATE TABLE `resposta` (
  `id_resp` int(10) UNSIGNED NOT NULL,
  `rodada` int(10) UNSIGNED NOT NULL,
  `id_user` int(10) UNSIGNED NOT NULL,
  `questao` varchar(50) NOT NULL,
  `resposta` varchar(50) NOT NULL,
  `correta` varchar(50) NOT NULL,
  `selecionada` varchar(50) DEFAULT NULL,
  `tipoerro` varchar(50) NOT NULL,
  `obs` text NOT NULL,
  `tempo_gasto` varchar(10) NOT NULL,
  `ip` varchar(30) NOT NULL,
  `data_hora` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `qtdaleatoriapositiva` tinyint(3) UNSIGNED NOT NULL,
  `qtdaleatorianegativa` tinyint(3) UNSIGNED NOT NULL,
  `qtdinvertidapositiva` tinyint(3) UNSIGNED NOT NULL,
  `qtdinvertidanegativa` tinyint(3) UNSIGNED NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `resposta`
--

INSERT INTO `resposta` (`id_resp`, `rodada`, `id_user`, `questao`, `resposta`, `correta`, `selecionada`, `tipoerro`, `obs`, `tempo_gasto`, `ip`, `data_hora`, `qtdaleatoriapositiva`, `qtdaleatorianegativa`, `qtdinvertidapositiva`, `qtdinvertidanegativa`) VALUES
(155, 1, 1, 'json/Gerador1/questao132.json', 'E', 'Não', 'D', 'gerada aleatoriamente e positiva', '', '0:00:06', '127.0.0.1', '2021-04-10 18:50:12', 3, 0, 1, 0),
(156, 1, 1, 'json/Gerador2/questao27.json', 'C', 'Sim', 'C', 'nenhum', '', '0:04:31', '127.0.0.1', '2021-04-10 18:54:45', 2, 2, 0, 0),
(157, 1, 1, 'json/Gerador3/questao112.json', 'C', 'Não', 'D', 'gerada aleatoriamente e positiva', '', '0:00:18', '127.0.0.1', '2021-04-10 18:55:05', 2, 2, 0, 0),
(158, 1, 1, 'json/Gerador4/questao174.json', 'B', 'Sim', 'B', 'nenhum', '', '0:01:20', '127.0.0.1', '2021-04-10 18:56:27', 1, 2, 0, 1),
(159, 1, 1, 'json/Gerador5/questao27.json', 'A', 'Sim', 'A', 'nenhum', '', '0:02:11', '127.0.0.1', '2021-04-10 18:58:40', 3, 1, 0, 0),
(160, 1, 1, 'json/Gerador6/questao50.json', 'D', 'Não', 'B', 'invertida e positiva', '', '0:00:19', '127.0.0.1', '2021-04-10 18:59:01', 1, 2, 1, 0),
(161, 1, 1, 'json/Gerador7/questao104.json', 'C', 'Sim', 'C', 'nenhum', '', '0:00:10', '127.0.0.1', '2021-04-10 18:59:13', 2, 1, 0, 1),
(162, 1, 1, 'json/Gerador8/questao35.json', 'C', 'Sim', 'C', 'nenhum', '', '0:00:03', '127.0.0.1', '2021-04-10 18:59:18', 1, 2, 0, 1),
(163, 1, 1, 'json/Gerador9/questao143.json', 'D', 'Sim', 'D', 'nenhum', '', '0:00:03', '127.0.0.1', '2021-04-10 18:59:23', 1, 2, 1, 0),
(164, 1, 1, 'json/Gerador10/questao45.json', 'D', 'Não', 'B', 'gerada aleatoriamente e negativa', '', '0:00:03', '127.0.0.1', '2021-04-10 18:59:28', 2, 2, 0, 0),
(165, 2, 1, 'json/Gerador1/questao69.json', 'D', 'Sim', 'D', 'nenhum', '', '0:00:08', '127.0.0.1', '2021-04-11 16:04:35', 3, 0, 1, 0),
(166, 2, 1, 'json/Gerador2/questao82.json', 'B', 'Sim', 'B', 'nenhum', '', '0:03:17', '127.0.0.1', '2021-04-11 16:07:54', 2, 1, 0, 1),
(167, 2, 1, 'json/Gerador3/questao131.json', 'E', 'Sim', 'E', 'nenhum', '', '0:00:15', '127.0.0.1', '2021-04-11 16:08:11', 3, 1, 0, 0),
(168, 2, 1, 'json/Gerador4/questao46.json', 'E', 'Sim', 'E', 'nenhum', '', '0:00:53', '127.0.0.1', '2021-04-11 16:09:06', 3, 1, 0, 0),
(169, 2, 1, 'json/Gerador5/questao110.json', 'B', 'Sim', 'B', 'nenhum', '', '0:00:51', '127.0.0.1', '2021-04-11 16:09:59', 3, 1, 0, 0),
(170, 3, 1, 'json/Gerador1/questao171.json', 'B', 'Sim', 'B', 'nenhum', '', '0:00:06', '127.0.0.1', '2021-04-14 01:20:58', 3, 0, 1, 0),
(171, 3, 1, 'json/Gerador2/questao162.json', 'D', 'Não', 'E', 'gerada aleatoriamente e negativa', '', '0:00:03', '127.0.0.1', '2021-04-14 01:21:03', 2, 2, 0, 0),
(172, 3, 1, 'json/Gerador3/questao160.json', 'A', 'Não', 'B', 'gerada aleatoriamente e positiva', '', '0:00:02', '127.0.0.1', '2021-04-14 01:21:07', 3, 1, 0, 0),
(173, 3, 1, 'json/Gerador4/questao184.json', 'A', 'Não', 'D', 'gerada aleatoriamente e negativa', '', '0:00:04', '127.0.0.1', '2021-04-14 01:21:13', 0, 4, 0, 0),
(174, 3, 1, 'json/Gerador5/questao138.json', 'A', 'Não', 'C', 'gerada aleatoriamente e positiva', '', '0:00:04', '127.0.0.1', '2021-04-14 01:21:19', 3, 1, 0, 0),
(175, 3, 1, 'json/Gerador6/questao138.json', 'C', 'Não', 'B', 'gerada aleatoriamente e positiva', '', '0:00:03', '127.0.0.1', '2021-04-14 01:21:24', 3, 1, 0, 0),
(176, 3, 1, 'json/Gerador7/questao190.json', 'B', 'Sim', 'B', 'nenhum', '', '0:00:06', '127.0.0.1', '2021-04-14 01:21:32', 1, 2, 0, 1),
(177, 3, 1, 'json/Gerador8/questao136.json', 'C', 'Sim', 'C', 'nenhum', '', '0:00:03', '127.0.0.1', '2021-04-14 01:21:37', 0, 3, 1, 0),
(178, 3, 1, 'json/Gerador9/questao93.json', 'B', 'Sim', 'B', 'nenhum', '', '0:00:03', '127.0.0.1', '2021-04-14 01:21:43', 2, 1, 1, 0),
(179, 3, 1, 'json/Gerador10/questao109.json', 'C', 'Sim', 'C', 'nenhum', '', '0:00:07', '127.0.0.1', '2021-04-14 01:21:52', 0, 3, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `email`) VALUES
(1, 'Estevão Naval', 'navalestevao@gmail.com'),
(2, 'Alexandre Paiva de Mello', 'alexandrepaiva@gmail.com'),
(3, 'Felipe Cruz e Souza de Lima', 'felipecruzsouza@oi.com.br');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `resposta`
--
ALTER TABLE `resposta`
  ADD PRIMARY KEY (`id_resp`) USING BTREE;

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `resposta`
--
ALTER TABLE `resposta`
  MODIFY `id_resp` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=180;
--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
