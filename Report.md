# Sprint 03 - Jhoeel Luna
**STRUCTURE**
### Tested on 16.0 GiB RAM, Intel® Core™ i3-8100 CPU @ 3.60GHz × 4 and NVIDIA GeForce GTX 1050 Ti/PCIe/SSE2
---
**LOCUST TEST**
---
For the initial test with locust, the setup parameters I used were:
- Number of users = 200
- Spawn rate = 10 /second
- Host = Localhost

Ratio per users
- Index 20%
- Predict 80%

With the test running for 10 seconds, the first error was enconter

The average requests per second before the error occured was 6-RPS for 200-users
![total_requests_per_second](https://user-images.githubusercontent.com/116731540/199787940-52cfefa1-34e9-4380-9463-b997f7d6483f.png)

The median response time before the error was 23000 ms and analizing it is a valid number 
because the wait time in the script was between 1-5 sec for each request 
![response_times_(ms)](https://user-images.githubusercontent.com/116731540/199787917-325cd194-60da-4a41-beaa-2c7b6194a257.png)

The number of users was at its peak before the error happend 
![number_of_users](https://user-images.githubusercontent.com/116731540/199787909-a78aacfa-cb9d-437d-adbe-536eef86cff0.png)

---
The stress test log shows that the model can't handle to many requests and for that reason
the service get a close connection

So I can say that the bottleneck is in the ml_container that get saturated with many requests
| **Type** | **Name**   | **#Reqs** | **#Fails** | **AVG** | **Min** | **Max** | **Med** | **Req/s** | **Failures/s** |
|---------:|-----------:|----------:|-----------:|--------:|--------:|--------:|--------:|----------:|---------------:|
| **GET**  | /          | 47        | 0(0.00%)   | 12372   | 18      | 52284   | 11000   | 0.70      | 0.00           |
| **POST** | /predict   | 175       | 8(4.57%)   | 12813   | 229     | 52776   | 12000   | 2.60      | 0.12           |
|          | Aggredated | 222       | 8(3.60%)   | 12720   | 18      | 52776   | 12000   | 3.30      | 0.12 


Type     Name                               # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s


![Locust Test Report](https://user-images.githubusercontent.com/116731540/199789936-bc3f3e9f-ba6e-4472-9e2a-346f7e8d98b6.PNG)

**LOCUST TEST WITH SCALED SERVICE MODEL**
---
the setup parameters I used were:
- Number of users = 200
- Spawn rate = 10 /second
- Host = Localhost

Ratio per users
- Index 20%
- Predict 80%

With the test running for 1 minute and having 3 containers for the ml_model there is an improvement
the requests per second get to 6.2 before the first failure occurs, but in this case the closed connection error dind stop the
procces because the other 2 containers were doing the job.
the median response time stays in 30000 ms and its still ok because the waiting time is between 1-5 sec set up in the stress script
As we can see in the chard the response time was not stable when the failure occured and that because the job is separated in 3 containers so the response time when the error occurs is around 1/3 of the median response time

![total_requests_per_second_1667497988](https://user-images.githubusercontent.com/116731540/199799311-4f5777fe-a083-4e7e-9078-d42e3b8d17fa.png)

With scaled service model the performance improved but not drasticly.
I can say that now the Api is more stable because it will not get a closed connection when it handles a lot of requests.

![report scaled service](https://user-images.githubusercontent.com/116731540/199800179-e1a8103d-bc7d-439b-b6bd-fc3f19874a42.PNG)

|**Type**|**Name**                                                    |**# reqs** |**# fails**  |**Avg**|**Min**|**Max**|**Med**|**req/s**|**failures/s**|
|--------|------------------------------------------------------------|-----------|-------------|-------|-------|-------|-------|---------|--------------|
|**GET** |/                                                           |        100|     0(0.00%)|  18259|     17|  29160| 22000 |     1.30|          0.00|
|**POST**|/predict                                                    |        379|     2(0.53%)|  20218|    220|  31093| 23000 |     4.92|          0.03|
|        |Aggregated                                                  |        479|     2(0.42%)|  19809|     17|  31093| 23000 |     6.21|          0.03


**Conclusion**
The API can run up to 6 requests per second before it fails 