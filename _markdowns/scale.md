# Thoughts on scale and performance

	Since the project is set to aim for microservice architecture
	we have advantage of scaling up the systems per microservice which
	means the scaling process would be more efficient.

`Note: This means scaling is done vertically. this method of
scaling has it's own pros and cons.`

# Key ideas to improve overall performance

1. Load Testing: The platform should be thoroughly load tested to ensure that it can handle high loads. This involves simulating high traffic and user loads to identify any performance bottlenecks and optimize the system accordingly.

2. Caching: To reduce the load on the database, caching can be used to store frequently accessed data in memory. This can improve performance and reduce the load on the database.

		Also caching can be done on other parts of the platform rather than just the database.

3. Content Delivery Network (CDN): A CDN can be used to distribute static content, such as images and videos, to servers located closer to the end-users. This can reduce the load on the platform's servers and improve performance for users in different geographic locations.

4. Message Queues: Message queues can be used to manage the flow of data between microservices and prevent overload. By using a message queue, requests can be processed in a queue and prioritized based on their importance.

5. Message Broker: Message Broker which is similiar to Message queues
can be used to manage notifications and messages since these are one of the most important aspects of the platform and the both need to be handled asyncronously.