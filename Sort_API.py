import psycopg2
from django.http import Http404

'''this function accepts two parameters:
    a request and key for the query in order to provide 
    list of sorted elements.
    '''
def get_sorted(request, query):
    #establish connection
    try:
        conn = psycopg2.connect(

                    host = "",     #host name of the server
                    database = "", #database name that you want to querry from
                    port = "",     #port number 
                    user = "",     #username to access databae
                    password = ""  #password for the database
        )
    except:
        raise HTTp404("incorrect request")


    #generate cursor
    cur = conn.cursor()

    # execute the query
    '''You can select to retrieve every column in the database or
        you can choose particular columns you want. If you want all columns
        use:  cur.execute("select * From tablename")
    '''

    cur.execute("select username, firstname, lastname, phone, action FROM tablename")

    #retrieves all rows from the table in form of a list of tuples
    ''' the data is retrieved in the following form
        [(username, firstname, lastname, phone, action)]
        
        each tuple in the list represent a row in the database
    '''
    rows = cur.fetchall()


    #options: username, firstname,or lastname
    if query == "username": #first column
        index = 0
    if query == "firstname": #second column
        index = 1
    if query == "lastname":  #third column
        index = 2
    else:
        raise  HTTP404("incorrect query")

    #sorts the list of tuples depending on the query passed it
    rows.sort(key=lambda tup: tup[index])

    #close cursor
    cur.close()
    #close the connection
    conn.close()

    #you should put your html file in charge of this web view instead of sorted.html
    #if it's not a webview, you can print the results. It will depend on your usage
    return render(request,'sorted.html', context=rows)
