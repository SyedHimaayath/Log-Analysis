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
    print("Q01. What are the most popular three articles of all time?")
    for name, num in results:
        print("sol: " + name + " - " + str(num) + " views")
        print("\n")


def popular_authors():
    query_02 = '''select authors.name as author, sum(pop_articles.views) as
    views from pop_articles, authors where pop_articles.author = authors.id
    group by authors.name order by views desc;'''
    results = take_query(query_02)
    print("Q02. Who are the most popular article author of all time?")
    for name, num in results:
        print("sol: " + name + " - " + str(num) + " views")
    print("\n")


def error_log():
    query_03 = '''select to_char(date,'Mon DD,YYYY') as date, percent_error
    from log_err_view where percent_error > 1;'''
    results = take_query(query_03)
    print("Q03. On which days did more than '1%' of requests lead to errors?")
    for date, value in results:
        print("sol: " + date + " - " + str(value) + "%"+" errors")
    print("\n")


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    error_log()
