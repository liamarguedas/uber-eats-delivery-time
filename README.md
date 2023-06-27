# Uber Eats Delivery Time Prediction

## Business Case
Uber Eats is an online food ordering and delivery platform. It is a subsidiary of Uber Technologies, the same company known for its ride-hailing service. Uber Eats allows users to browse menus, place orders, and have food delivered from a wide range of restaurants and food establishments in their area. The Uber Eats platform operates through a mobile application and a website. Users can download the app on their smartphones or access the service through the website. Once logged in, users can enter their delivery address to view a list of participating restaurants nearby.

Users can browse through various menus, select items they want to order, customize their meals if applicable, and add them to their virtual cart. The app also provides total cost of the order, including taxes, fees, and delivery charges. When the order is placed, it is transmitted to the restaurant. The restaurant then prepares the food and hands it over to an Uber Eats driver for delivery. Uber Eats drivers, often referred to as "delivery partners," use their own vehicles to pick up the food and deliver it to the customer's location.

Throughout the process, users can track the progress of their order within the app, including when it's being prepared, when the driver is en route, and when it's delivered. Payment for the order is typically done through the app, using a credit card or other payment methods available in the user's account.

## Uber Eats system drawbacks
 Food Delivery services like Uber need to show the time it will take to deliver the order to keep transparency with their customers. Showing accurate delivery times is crucial for Uber Eats because:

- **Customer Expectations:** In today's fast-paced world, customers have come to expect convenience and efficiency when it comes to food delivery. Providing accurate delivery time estimates helps manage customer expectations and ensures they are aware of when their order will arrive. It enhances transparency and helps build trust between the platform and the customer.

- **Customer Satisfaction:** Delivery time accuracy directly impacts customer satisfaction. If a delivery is consistently delayed or arrives much later than anticipated, it can lead to frustration and dissatisfaction. On the other hand, if the estimated delivery time is reliable and the order arrives promptly, it enhances the overall customer experience and increases the likelihood of repeat business.

- **Time Management:** Accurate delivery time predictions enable customers to plan their day effectively. By knowing when their order will arrive, they can schedule their activities accordingly, whether it's waiting at home or stepping out briefly. This feature is particularly important for busy individuals who have limited time and need to manage their daily routines efficiently.

- **Operational Efficiency:** Reliable delivery time predictions allow delivery platforms to optimize their operations. By accurately estimating delivery times, they can manage their fleet of delivery partners more effectively, assign orders based on distance and estimated delivery time, and streamline the entire delivery process. This can lead to improved efficiency, reduced idle time, and better resource allocation.

- **Reputation and Competition:** Delivery platforms operate in a highly competitive market, and accurate delivery time predictions contribute to their overall reputation. When customers consistently receive their orders within the estimated time frame, it enhances the platform's reliability and positive word-of-mouth, which can attract new customers and retain existing ones.

- **Customer Retention:** Timely delivery is crucial for customer retention. When customers have a positive experience with on-time deliveries, they are more likely to continue using the service and recommend it to others. On the other hand, frequent delays or unreliable delivery times can drive customers away, leading to a loss of business.

Accurate delivery time predictions are vital for services like Uber Eats to manage customer expectations, enhance customer satisfaction, optimize operations, build a positive reputation, and ultimately retain and attract customers. By leveraging data science and advanced analytics, these platforms can improve their prediction capabilities, leading to a more reliable and enjoyable food delivery experience for customers.

## Project Objective
To accurately predict food delivery times in real-time, several factors need to be taken into account. One crucial aspect is calculating the distance between the food preparation point (usually a restaurant) and the point of food consumption (the delivery location). By determining the geographical separation, we gain a fundamental parameter for estimating the delivery duration.

In addition to distance, it is essential to consider historical data on delivery times for similar distances. This information allows us to identify and establish relationships between the time taken by delivery partners in the past and the corresponding delivery distances. Analyzing this data enables us to uncover patterns, trends, and dependencies that can help us make accurate predictions about future delivery durations.

By leveraging machine learning algorithms and statistical techniques, we can build a predictive model that takes into account not only the distance but also various other factors that can impact delivery times. These factors may include traffic conditions, time of day, day of the week, weather conditions, and even the current workload of delivery partners. By incorporating these variables into our model, we can create a more comprehensive and accurate estimation of the food delivery time.

Moreover, the model can be continuously improved and updated as new data becomes available. By regularly updating the model with the latest delivery data, we can ensure that it remains relevant and reflective of changing conditions and trends in the delivery process.

It is worth noting that real-time delivery time prediction requires a dynamic and responsive system. As new orders come in and delivery partners are assigned, the model needs to recalculate and adjust the estimated delivery times based on the current circumstances. This ensures that customers receive up-to-date and reliable information about when they can expect their food to arrive.

## Data Description

|Column|Description|Dtype|
| :------------ |:---------------:|:---------------:|
|**ID**|order ID number| object |
|**Delivery_person_ID**|ID number of the delivery partner| object |
|**Delivery_person_Age**|Age of the delivery partner|object|
|**Delivery_person_Ratings**|Ratings of the delivery partner based on past deliveries|object
|**Restaurant_latitude**|The latitude of the restaurant|float64
|**Restaurant_longitude**|The longitude of the restaurant|float64
|**Delivery_location_latitude**|The latitude of the delivery location|float64
|**Delivery_location_longitude**|The longitude of the delivery location|float64
|**Order_Date**|Date of the order|object
|**Time_Orderd**|Time the order was placed|object
|**Time_Order_picked**|Time the order was picked|object
|**Weatherconditions**|Weather conditions of the day|object
|**Road_traffic_density**|Density of the traffic|object
|**Vehicle_condition**|Condition of the vehicle|int64
|**Type_of_order**|The type of meal ordered by the customer|object
|**Type_of_vehicle**|The type of vehicle delivery partner rides|object
|**multiple_deliveries**|Amount of deliveries driver picked|object
|**Festival**|If there was a Festival or no.|object
|**City**|Type of city|object
|**Time_taken(min)**| The time taken by the delivery partner to complete the order|object

## Decision-making process.