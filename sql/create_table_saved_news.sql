-- Медиум текст, т.к. не знаем максимальной длинны новости
-- хранение версий анализатора новости
-- Создаем таблицу для хранения новостей и оценки
CREATE TABLE saved_news (
id integer,
date_input_post timestamp,
resource varchar(255),
str_news MEDIUMTEXT,
final_review int,
text_analyze_version varchar(16)
);