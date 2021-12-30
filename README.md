This is a little documentation on the test-APP.

I have created and hosted the app at the end point:https://sodiq-umba-test.herokuapp.com/users/  on   heroku machine. It can as well be run locally. And the app is committed to the repo  at 
https://github.com/mallamsiddiq/sodiq-umba-test.git 

A.Running locally: 

	Move into the root directory of the project and:
	1.Dockerizing : if you have docker installed on your machine, just run the following commands:

	docker-compose  build
	docker-compose  up
	
	All  necessary dependencies will be installed and you’ll have your app 	running on 	port :80000                         localhost:8000   
	
	2.And if you don’t have docker installed don’t worry I’ve got you covered, with python and pip installed you just run the following lines [inside app root directory]:

	 pip install --upgrade pip
	 pip install -r requirements.txt  
	 python manage.py makemigrations
	 python manage.py migrate
	 python manage.py loaddata dump.json 
	 python manage.py runserver

	These will install necessary dependencies and again BOOM!! your app is running on port: 8000                localhost:8000



B.Setting up the app:
	I started by getting the github users from the api specified cleaned using python pandas and save it into mysql database, all these rough work I did in /scripts/seed.py file. I created a django app using 
	M-V-T Achitecture , see this documentation for details on how to set-up a djang appo          

	https://docs.djangoproject.com/en/4.0/intro/tutorial01/  

	I populated the django database from the data I stored in mysql, I later disconnected the mysql database from django and used sqlite3 instead for ease of deployment and third party interaction and configuration as I purposefully hosted the app and built it mainly using docker image. I dockerize the app running on sqlite3 database and tested it on port 8000 locally then populate the database by dumping the .json file I created when connected with mysql.
	And boom my app is up and running.


C.TESTING THE APP:

	All end-pionts are as specified in the test document and could be tested as instructed. But for ease of navigation I added few redirecting icon buttons that points to the api’s and also return you back to the home age. 
	At the /users/ endpoit clicking the profile picture redirects you  to user profile on git. Just to observe culture of design, I created a user profile detail page at the endpoint 'users/details/<int:user_pk>/’  you’ll notice a small profile icon when hover on a specific user clicking on this icon redirect you to the user details.

	While the raw json API response is at 'api/users/profiles/' as instructed, I creted a custom api documentaion using swagger doc to easily play around with the API’s and query it how you like. This end point is at 'costum-api/'. and the raw json response is well reported at the instructed end point. 





D. Deployment :

	I deployed this app on heroku as a docker image then connect to a pstgreSQL on heroku, I used django memcachier both locally and deployed but the functionality on server might fall sort of full functionality as I’m currently having little issue with my debit card verification - this obviously will soon be rectified.  Visit the app with full functionality on  
	https://sodiq-umba-test.herokuapp.com/users/ 


Thanks

Akinyemi Sodiq
mallamsiddiq@gmail.com 




	

	






