# README for Grazioso Salvare Dashboard Project

## Module Eight Journal Entry
### How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
Writing maintainable, readable, and adaptable code involves several best practices:

- Modular Design: Breaking down the code into smaller, self-contained modules makes it easier to understand and maintain. For instance, the CRUD Python module from Project One was designed to handle all database operations, making it reusable across different projects without the need for modifications.

- Clear Documentation: Adding comments and docstrings helps others (and future me) understand the purpose and functionality of the code. This practice was particularly useful in the CRUD module where each function was well-documented to explain its purpose and usage.

- Consistent Naming Conventions: Using descriptive and consistent naming for variables, functions, and classes enhances code readability. This was applied in both the CRUD module and the dashboard code to ensure clarity.

- Error Handling: Implementing robust error handling ensures that the code can gracefully handle unexpected situations, which enhances reliability and maintainability.

The advantages of working in this modular and well-documented way include:

- Reusability: The CRUD module can be reused in future projects that require database operations, saving time and effort.
- Ease of Maintenance: With clear documentation and modular design, updating or fixing issues in the code becomes straightforward.
- Scalability: The code can be easily extended to add new features without disrupting the existing functionality.
In the future, the CRUD Python module could be used in various applications that require database interactions, such as web applications, data analysis scripts, or even machine learning pipelines.

### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
As a computer scientist, my approach to problem-solving involves the following steps:

- Requirements Analysis: Understanding the client's needs and defining the scope of the project. For Grazioso Salvare, this involved identifying the key functionalities of the dashboard and the types of data to be handled.

- Design: Planning the architecture of the solution, including database schema design and the layout of the dashboard.

- Implementation: Writing the code in a modular and organized manner. This involved developing the CRUD module first and then integrating it with the dashboard application.

- Testing: Thoroughly testing the application to ensure it functions as expected. This included testing each CRUD operation, the interactive filtering options, and the dynamic updates of the charts.

- Iteration and Refinement: Continuously improving the code based on feedback and testing results. This step ensures that any issues are addressed promptly and the application meets the client's expectations.

In the future, I would use the following strategies to create databases and meet client requests:

- Agile Development: Adopting an agile methodology to allow for iterative development and continuous feedback.
- Prototyping: Creating prototypes to quickly demonstrate functionality to the client and gather feedback.
- Scalability Considerations: Designing databases with scalability in mind to handle future growth and data volume increases.
- Security Best Practices: Ensuring that the database and application follow security best practices to protect sensitive data.
   
### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
Computer scientists design and develop software solutions to solve real-world problems. They work on a wide range of tasks, including algorithm development, data analysis, software engineering, and system design. Their work is essential for advancing technology and improving efficiency in various industries.

In this project, my work involved creating a dashboard that allows Grazioso Salvare to efficiently filter and analyze data on animal outcomes. This tool helps the company:

- Streamline Operations: By quickly identifying suitable dogs for training, the company can focus its resources more effectively.
- Data-Driven Decisions: The interactive charts and data tables provide valuable insights that support informed decision-making.
- Improved Accuracy: Automating the data filtering process reduces the risk of human error and ensures accurate results.

Overall, the dashboard enhances Grazioso Salvare's ability to manage and utilize their data, ultimately supporting their mission to train rescue animals and save lives.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<p align="center">
  
![Grazioso Salvare Logo](https://github.com/JPDengler/Client-Server-Development-CS-340-/assets/130941901/8a505730-3fad-4d7a-ba25-195e84106fc2)

</p>

## Project Description
The Grazioso Salvare Dashboard is an interactive web application designed to filter and display data on animal outcomes from the Austin Animal Center. The dashboard includes interactive filtering options, an interactive data table, a geolocation chart, and a pie chart.

## Tools Used
- **Python**: Used for scripting and data manipulation.
- **Dash**: Framework for building web applications.
- **MongoDB**: Database used for storing and retrieving animal data.
- **Plotly**: Used for creating interactive charts and graphs.

## MongoDB Explanation
MongoDB was chosen for its flexibility in handling large volumes of unstructured data and its ability to easily interface with Python through the pymongo library.

## Dash Framework Explanation
Dash provides a simple yet powerful framework for building web applications with Python. It supports interactive, real-time data visualization and integrates seamlessly with Plotly for creating charts and maps.

## Steps Taken
1. **Setup MongoDB and Python Environment**.
2. **Develop CRUD Operations**: Implemented in `ModuleJosephDengler.py`.
3. **Build Dashboard Layout**: Created interactive filters, data table, and charts in `ProjectTwoDashboard.ipynb`.
4. **Implement Callbacks**: Added interactivity to update charts and data table based on filter selections.
5. **Testing and Debugging**: Ensured all components work as expected.

## Challenges and Solutions
- **Authentication Errors**: Adjusted the initialization parameters in the CRUD module to resolve authentication issues.
- **Interactive Filtering**: Debugged issues with filter options not updating correctly by refining the MongoDB queries.

## Screenshots
### Starting State
![Startup](https://github.com/JPDengler/Client-Server-Development-CS-340-/assets/130941901/5d12f7ff-a5b3-4930-bc84-234f5aa3c498)


### Water Rescue Filter
![Water](https://github.com/JPDengler/Client-Server-Development-CS-340-/assets/130941901/3febf4d2-3053-421d-b667-862e9778347d)


### Mountain or Wilderness Rescue Filter
![Mountain](https://github.com/JPDengler/Client-Server-Development-CS-340-/assets/130941901/3e706371-4ab2-49ea-9a95-78a41fec5a79)


### Disaster or Individual Tracking Filter
![Disaster](https://github.com/JPDengler/Client-Server-Development-CS-340-/assets/130941901/e0e02431-61a3-4ffe-b403-caeb6e86969e)


### Reset Filter
![Reset](https://github.com/JPDengler/Client-Server-Development-CS-340-/assets/130941901/057a4856-8af0-47af-81a9-69e0367f1832)


## Resources
- [Dash Documentation](https://dash.plotly.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)

## Contact
Joseph Dengler
- [GitHub](https://github.com/JPDengler/)
- [Email](mailto:jp.dengler@gmail.com)
