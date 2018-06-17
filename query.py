import psycopg2


def take_query(query):
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def popular_articles():
    query_01 = '''select title, views from pop_articles limit 3;'''
    results = take_query(query_01)
    print("01. What are the most popular three articles of all time?")
    for name, num in results:
        print("sol: " + name + " - " + str(num) + " views")
        print("\n\n")


def popular_authors():
    query_02 = '''select authors.name as author, sum(pop_articles.views) as
    views from pop_articles, authors where pop_articles.author = author.id
    group by authors.name order by views desc;'''
    results = take_query(query_02)
    print("01. Who are the most popular article author of all time?")
    for name, num in results:
        print("sol: " + name + " - " + str(num) + " views")
    print("\n\n")


def error_log():
    query_03 = '''select to_char(date,'MON DD YYYY') as date, percent_error
    from log_err_view where percent_error > 1;'''
    results = take_query(query_03)
    print("01. What are the most popular three articles of all time?")
    for date, value in results:
        print("sol: " + date + " - " + str(value) + " %"+" errors")
    print("\n\n")


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    error_log()