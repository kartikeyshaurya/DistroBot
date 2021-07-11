# RealTime Maps using Apache Kafka and leftlet


The aim of this project was to generate live location of object in real time on the  opensource map . along with using free APIS and Apache Kafka For mhandling requests.

Content 
1. Setups 
2. 
3. Tools Used 
4. Final Result 




## Setup 


* First we need to start the  `apache zookeeper` by using this command(make sure your terminal to kafka location )

```
$ bin/kafka-server-start.sh config/zookeeper.properties 
```

* simarly we need to start the  `kafka environemt ` by using 

```
bin/kafka-server-start.sh config/server.properties 
```

once we ae done with the server part run the app.py and also one busdata.py 
the commnand is :- 
```
python3 app.py 
```  

and open another terminal and run
```
python3 busdata1.py
```
and the result should be similar to this one 

<br>

![final Photo](data/final.gif)