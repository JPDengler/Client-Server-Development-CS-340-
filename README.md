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
