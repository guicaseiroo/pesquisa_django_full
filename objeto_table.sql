
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `u417647346_pesquisasams` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `u417647346_pesquisasams`;

CREATE TABLE `campanhas_campanha` (
  `id` bigint(20) NOT NULL,
  `campanha_nome` varchar(100) NOT NULL,
  `campanha_descricao` longtext NOT NULL,
  `campanha_data_hora_validade` datetime(6) NOT NULL,
  `campanha_imagem` varchar(100) NOT NULL,
  `campanha_fundo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `perguntas_respostas_pergunta` (
  `id` bigint(20) NOT NULL,
  `pergunta_texto` varchar(100) NOT NULL,
  `pergunta_campanha_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `perguntas_respostas_resposta` (
  `id` bigint(20) NOT NULL,
  `resposta_texto` varchar(100) NOT NULL,
  `resposta_pergunta_id` bigint(20) NOT NULL,
  `proxima_campanha_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `respostas_clientes_respostausuario` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `resposta_texto` longtext NOT NULL,
  `data_resposta` datetime(6) NOT NULL,
  `campanha_id` bigint(20) NOT NULL,
  `pergunta_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


ALTER TABLE `campanhas_campanha`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `perguntas_respostas_pergunta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `perguntas_respostas__pergunta_campanha_id_625c1b64_fk_campanhas` (`pergunta_campanha_id`);


ALTER TABLE `perguntas_respostas_resposta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `perguntas_respostas__resposta_pergunta_id_a19cd5a9_fk_perguntas` (`resposta_pergunta_id`),
  ADD KEY `perguntas_respostas__proxima_campanha_id_8a7b5d39_fk_campanhas` (`proxima_campanha_id`);

ALTER TABLE `respostas_clientes_respostausuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `respostas_clientes_r_campanha_id_f9f9c39a_fk_campanhas` (`campanha_id`),
  ADD KEY `respostas_clientes_r_pergunta_id_b22d402d_fk_perguntas` (`pergunta_id`);

ALTER TABLE `campanhas_campanha`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;


ALTER TABLE `perguntas_respostas_pergunta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `perguntas_respostas_resposta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;


ALTER TABLE `respostas_clientes_respostausuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;


ALTER TABLE `perguntas_respostas_pergunta`
  ADD CONSTRAINT `perguntas_respostas__pergunta_campanha_id_625c1b64_fk_campanhas` FOREIGN KEY (`pergunta_campanha_id`) REFERENCES `campanhas_campanha` (`id`);


ALTER TABLE `perguntas_respostas_resposta`
  ADD CONSTRAINT `perguntas_respostas__proxima_campanha_id_8a7b5d39_fk_campanhas` FOREIGN KEY (`proxima_campanha_id`) REFERENCES `campanhas_campanha` (`id`),
  ADD CONSTRAINT `perguntas_respostas__resposta_pergunta_id_a19cd5a9_fk_perguntas` FOREIGN KEY (`resposta_pergunta_id`) REFERENCES `perguntas_respostas_pergunta` (`id`);


ALTER TABLE `respostas_clientes_respostausuario`
  ADD CONSTRAINT `respostas_clientes_r_campanha_id_f9f9c39a_fk_campanhas` FOREIGN KEY (`campanha_id`) REFERENCES `campanhas_campanha` (`id`),
  ADD CONSTRAINT `respostas_clientes_r_pergunta_id_b22d402d_fk_perguntas` FOREIGN KEY (`pergunta_id`) REFERENCES `perguntas_respostas_pergunta` (`id`);
COMMIT;

