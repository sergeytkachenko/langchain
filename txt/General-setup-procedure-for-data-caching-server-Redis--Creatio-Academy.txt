


 Use Redis caching server to optimize execution of heavy database queries. Caching improves Creatio performance and reduces the resource usage.
 



 The Redis server package is available in the standard Debian repositories. This article covers installing Redis on Debian and Debian derivatives (such as Ubuntu and Linux Mint). To install Redis:
 


1. Log in as root:
 






```

sudo su
```
2. Update the package lists:
 






```

apt-get update
```
3. Install Redis:
 






```

apt-get install redis-server
```
4. Enable Redis to run as a
 **systemd** 
 service. To do this:
 


	1. Open
	 **redis.conf** 
	 in a text editor as root. For example, use the Nano text editor:
	 
	
	
	
	
	
	
	```
	
	nano /etc/redis/redis.conf
	```
	2. Locate the “
	 **supervised no** 
	 ” entry. Replace the entry with “
	 **supervised systemd** 
	 .”
	3. Save changes and exit the editor.
	4. Restart the Redis server.
	 
	
	
	
	
	
	
	```
	
	systemctl restart redis-server
	```
	5. Log out from your root session:
	 
	
	
	
	
	
	
	```
	
	exit
	```




