create view pop_articles as
select title, author, count(*) as views from articles
join log on log.path = ('/article/'||articles.slug)
group by articles.title, articles.author
order by views desc;

create view log_err_view as 
select date(time), round(100.0*sum(case log.status
when '200 OK' then 0 else 1 end)/count(log.status),2)
as percent_error from log
group by date(time) order by percent_error desc;