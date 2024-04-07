# WebApp-MBTA - Jaiveer Nalwa & Aryan Subramanian

## 1. Project Overview
The web application designed in this project helps users in Boston find the closest MBTA stop that they can use to their current location. The code utilizes APIs fetched from Mapbox and the MBTA to obtain geographic data and relevant information about nearby stations. It converts the inputted user location into latitude and longitude coordinates, which is used to query the MBTA API for information about its train stations. It finds the station with the closest latitude and longitude coordinates and displays its name, wheelchair accessibility, and the time of the next arriving train, all sourced from the MBTA API. It also uses the Pytz and DateTime libraries to calculate and convert relevant times into a legible format. The front-end design uses Flask servers to render an HTML template with CSS that displays the information for the user in a concise and legible format. 

## 2. Reflection
The process point of view started with both of us feeling that the project would be straightforward, as we are combining things we have already learned and all it took was sourcing data from relevant APIs. However, as the project commenced, the scope got wider as we wanted to add additional features and make it more visually appealing. We also underestimated the difficulty of the implementation and took assistance from both Gemini as well as Professor Li to solve issues, such as the misrepresentation of latitude and longitude (we got it backward at first). Additionally, working as a team was a new challenge, as previously both team members had only worked on projects individually. We took advantage of GitHub and the Live Share extension on VSCode to collaborate asynchronously and together, respectively. The extended scope and difficulty led to the project taking more time to complete, as well as many iterations of functions being written and testing being done to successfully debug the project. In the future, creating a plan or agenda of steps needed to be taken could make the project more efficient and less complicated to complete.

The work division between the two team members was planned and accomplished effectively. We decided to split the work by front-end and back-end, with one member handling the functions on the backend that dealt with the API calls and data comprehension and the other handling the Flask and HTML/CSS code. This division was successful as it prevented either team member from getting in the way of the other while allowing both of us to work simultaneously. Even though we worked on separate sections of the project, we worked together in the same room synchronously to assist each other with issues and brainstorm solutions together. We decided to use the Live Share extension for real-time editing and collaboration. Although we initially encountered some minor difficulties such as only one person being able to test the code, we resolved them promptly through constant communication. We decided to distribute the work according to our strengths, as Jaiveer worked primarily on the main Python file and Aryan worked on the Flask server and HTML file, whilst providing input to enhance one another's work. We believe our team was able to efficiently complete the project because we entered with a clear plan of collaborating together in person to ensure strong communication and teamwork. Next time, we wouldn't change too much about our process besides creating a concrete plan/agenda of tasks to make both team members work more efficiently.

The two main pieces of learning gained through this project were the backend development of an application that relies on real-time API calls to provide a service to the user and the frontend development of the application to create a simple user interface. Within these aspects, we learned the specific implementations of API calls and turning illegible computer data into a legible, user-friendly package. Converting data required the use of libraries we were unfamiliar with such as DateTime and Geopy. However, the implementation of these libraries made the overall project less complex for us to develop and saved a lot of time. We learned how to implement these libraries through the documentation that is provided with each one. Furthermore, any time we ran into an issue regarding the API or library implementation, we used Google Gemini or ChatGPT to help clarify solutions to our issues. We also used it to help us understand errors and efficiently debug the program. Our lack of knowledge regarding the functions in the APIs and libraries made it so we took longer to complete the project, and would have been helpful to know beforehand. However, the use of generative AI shortened the timeline and without it, we would not have been able to debug and move forward efficiently. Below are screenshots of how we leveraged Gemini to help us build the program.

<img width="501" alt="ss3" src="https://github.com/aryansubramanian4/Assignment_3/assets/156847974/9de071d6-d5b5-4b38-a6c0-cd08a77c7e18">
<img width="551" alt="ss2" src="https://github.com/aryansubramanian4/Assignment_3/assets/156847974/b6d4ea2e-2ed3-4e8d-abb7-b6212ac37096">
<img width="548" alt="ss1" src="https://github.com/aryansubramanian4/Assignment_3/assets/156847974/1b8554c3-30a8-4080-9f6a-ae2b6c67a8f8">
