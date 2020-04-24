#继续sql
#COUNT(*)可以用来数行数
#几个比较难的

##13. 列出演员’Julie Andrews’曾参与的电影名称及其第一主角
##
##SELECT title, name
##  FROM movie JOIN casting ON movie.id = movieid
##             JOIN actor ON actor.id = actorid
##WHERE movie.id IN (SELECT movieid FROM casting   
##                    WHERE actorid = (SELECT id FROM actor   
##                                      WHERE name = 'Julie Andrews'))  
##  AND ord = 1;

##12. ‘John Travolta’最忙是哪一年？显示年份和该年的电影数目
##SELECT yr,COUNT(title) FROM
##  movie JOIN casting ON movie.id=movieid
##        JOIN actor   ON actorid=actor.id
##WHERE name='Rock Hudson'
##GROUP BY yr
##HAVING COUNT(title)=(SELECT MAX(c) 
##                         FROM (SELECT yr,COUNT(title) AS c 
##                                 FROM movie JOIN casting ON movie.id=movieid
##                                            JOIN actor   ON actorid=actor.id
##                                WHERE name='John Travolta'
##                                GROUP BY yr) AS t);

##13. 列出每场比赛中的比赛日期、队伍1、队伍1进球数、队伍2、队伍2进球数，并按照比赛日期、队伍1、队伍2排序
##难点为如果不group by team1, team2得话，同一天的不同比赛进球数会叠加到一个
##SELECT mdate,
##       team1,
##       SUM(CASE WHEN teamid=team1 
##                THEN 1 ELSE 0 END) score1,
##       team2,
##       SUM(CASE WHEN teamid=team2 
##                THEN 1 ELSE 0 END) score2
##  FROM game JOIN goal ON matchid = id
##GROUP BY mdate, team1, team2
##ORDER BY mdate, team1, team2;

##8. 列出全部赛事中射入德国球门的球员名字
##
##SELECT DISTINCT goal.player
##  FROM goal JOIN game ON goal.matchid = game.id
##WHERE (teamid <> 'GER' AND team1 = 'GER')
##   OR (teamid <> 'GER' AND team2 = 'GER');
