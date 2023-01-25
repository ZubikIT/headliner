Start project:  
$ python3 manage.py makemigrations        
$ python3 manage.py migrate                 
$ python3 manage.py createsuperuser             
$ python3 manage.py runserver                         

Later:              
127.0.0.1:8000/admin (data superuser) =====>> append in table (Promos, Budgets) data                      
127.0.0.1:8000/drf-auth/login ============> authenticate                                
127.0.0.1:8000/headliner ======> see all data in db and create new data       
127.0.0.1:8000/headliner/<int:pk> ======> see <int:pk> data and put and delete this 
