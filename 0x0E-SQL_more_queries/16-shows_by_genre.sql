-- A script that lists all shows contained in hbtn_0d_tvshows and
--  their corresponding genres if any
SELECT `tv_shows`.`title`, `tv_genres`.`name`
    FROM tv_show_genres
    INNER JOIN tv_genres ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
    RIGHT JOIN tv_shows ON `tv_show_genres`.`show_id` = `tv_shows`.`id`
    ORDER BY `tv_shows`.`title` ASC, `tv_genres`.`name` ASC;
