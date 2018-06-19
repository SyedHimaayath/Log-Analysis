# Log-Analysis

### Overview
> A reporting tool that prints out reports based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

### How to Run?

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory inside the fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log-in using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant.
  
#### Setting up the database:

  1. Load the data from the file into local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * Articles table
  * Authors table and
  * Log table
  
  2. Use `psql -d news` to connect to database.

#### views used:

  downnload the views.sql file from the repository to look into the views created.

  1. Popular articles view

  ```
  create view pop_articles as
  select title, author, count(*) as views from articles
  join log on log.path = ('/article/'||articles.slug)
  group by articles.title, articles.author
  order by views desc;

  ```
  2. Error Log View

  ```
  create view log_err_view as 
  select date(time), round(100.0*sum(case log.status
  when '200 OK' then 0 else 1 end)/count(log.status),2)
  as percent_error from log
  group by date(time) order by percent_error desc;

  ```

#### Loading the views
  views can be loaded using the following command in the terminal
  ```
    $ psql -d news -f views.sql
  ```
  
#### Running the queries:
  ```
    $ python3 query.py
  ```