#sql self join
#(1)
SELECT DISTINCT a.company, a.num
FROM route a JOIN route b ON (a.company=b.company AND a.num=b.num)
             JOIN stops stopa ON (a.stop=stopa.id)
             JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart' 
  AND stopb.name = 'Tollcross';
#self join route表格on 公司和num得到一个笛卡尔组合，表示了从每个站，通过同一route
#可以到达的另外的站（因为每一行公司和route num都是相同的）。再额外join两个stop
#表格分配给出发站和到达站的站名。之后就可以用where来查询不同的站。

#(2)
找到乘坐两趟公共汽车从Craiglockhart到Lochend的路线

SELECT DISTINCT bus1.num, bus1.company, name, bus2.num, bus2.company 
FROM (SELECT start1.num, start1.company, stop1.stop 
        FROM route AS start1 JOIN route AS stop1 #这里self join得到起始站和中转站，join时公司和num要相等，但是两个站要不同
                             ON start1.num = stop1.num AND start1.company = stop1.company AND start1.stop != stop1.stop 
         WHERE start1.stop = (SELECT id FROM stops WHERE name = 'Craiglockhart')) AS bus1 #再用subquery找到C站的编号，在新表中查询
-- 找出从Craiglockhart出发坐一辆巴士可以到达的线路和站台
JOIN (SELECT start2.num, start2.company, start2.stop #与前面相似，不同的是，前面select的是终点站，这里select起始站，这样当join这两个表时才能使得中转站相同
        FROM route AS start2 JOIN route AS stop2 
                               ON start2.num = stop2.num AND start2.company = stop2.company AND start2.stop != stop2.stop 
         WHERE stop2.stop = (SELECT id FROM stops WHERE name = 'Lochend')) AS bus2 #注意这里要让终点站等于L站的编号
-- 找出坐一辆巴士可以到达Lochend的线路及站台
   ON bus1.stop = bus2.stop
-- 找出bus1的到达站和bus2的出发站相同的路线 
JOIN stops ON bus1.stop = stops.id;
#这题明白了逻辑就不是很难，注意细节即可
#题目意思为从C出发，转一次车到达L，可以理解为寻找C站出发能到达的全部站，再找
#全部能到达L站的车站，join这两个表格，使得第一个表格的到达站和第二个表格的出发
#站相等即可(中转站),需要站名的话，最后再join stops表格获取站名

#sql网站题刷完了，明天去全面回顾一下sql知识点，再后面就刷一下leetcode上的sql
