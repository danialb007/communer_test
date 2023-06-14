# Bounded Context for each microservice 🚀

### 1. Health Data Service: process the health data collected from the IoT devices and provide insights and analytics on the patient's health.
## |
>## Interactions:
>* Patient Service to store and manage patient health data
>* Recommendation Service to run ML operations and analysis.
>* Notification Service to provide notifications base on health data if necessary.


### 2. Patient Service: manage patient information, including health data, medical history, and personal information.
## |
>## Interactions:
>* Health Data Service to provide access to health data.
>* Doctor Service to provide access to patient information.
>* User Service to manage authentication, patient profiles and credentials.
>* Messaging Service to enable secure messaging between patients and doctors.
>* ML and Recommendation Service to provide recommendations and new trends base on health data.
>* Gateway Service to process data collected from patient app or IoT devices.

#
### 3. Doctor Service: manage doctor information, including medical credentials, specialties, and contact information.
## |
>## Interactions:
>* Patient Service to provide access to patient information.
>* User Service to manage authentication, doctor profiles and credentials
>* Messaging Service to enable secure messaging between doctors and patients.
>* Gateway Service to process data collected from doctor app.

#
### 4. User Service: handle user authentication, authorization, and user profiles.
## |
>## Interactions:
>* Patient Service and Doctor Service to manage patient and doctor information.

#
### 5. Notification Service: send real-time notificatio to patients and doctors, including new health data, appointment reminders, and urgent alerts.
## |
>## Interactions:
>* Messaging Service to enable real-time messaging.
>* Recommendation Service to send notifications base on health data and urgent alerts.

#
### 6. Messaging Service: provide a secure messaging platform for patients and doctors to communicate with each other.
## |
>## Interactions:
>* Patient Service and Doctor Service to provide communications between them.
>* Notification Service to enable real-time messaging 

#
### 7. Gateway Service: provide a secure entry point for the IoT devices to connect to the platform.
## |
>## Interactions:
>* IoT devices to receive and process health data.
>* Patient and Doctor app to provide a secure connection.

#
### 8. Recommendation and ML Service: provide recommendations and analytics base on patient health data.
## |
>## Interactions:
>* Health Data Service to access and analyze patient health data, run ML algorithems on them and provide health care recommendations base on patterns and trends.
>* Notification Service to provide notifications base on health data if necessary.

#
### 9. Integration Service: integrate with third-party healthcare systems and applications.
## |
>## Interactions:
>* Patient Service and Doctor Service to access and manage patient and doctor information form third-party platforms.