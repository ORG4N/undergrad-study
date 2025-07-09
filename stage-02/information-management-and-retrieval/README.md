![title image](https://github.com/ORG4N/undergrad-study/blob/main/stage-02/information-management-and-retrieval/docs/images/2001.png)

<p align="center"><strong>Module Overview</strong>
<br>
"To introduce students to fundamental principles around graphical representation along with information management, database systems and modelling. <br> To consider issues around image compression techniques, how humans can access information and data to support their needs, learn declarative queries and considercommon designs for database systems. <br> To understand the differences between relational and semi-structured data models anduse appropriate data modelling techniques."
</p>
<br/>

<h2>Learning Outcomes</h2>

- Demonstrate explicit uses of modelling techniques to gain access to information and data to support a given need.
- Illustrate an appropriate technical solution to the problems of information privacy, integrity, security and preservation.
- Illustrate the design of an application of moderate complexity to elicit and visualise information from a data store.

<br>

<h2>Assessments</h2>
The module is assessed via 100% coursework, across two elements:

<br>
<br>

<b> Set Exercises (30%) </b>
<br>
Assessment consists of: carry out an analysis of a chosen scenario, identify the appropriate data items, design and then create an appropriate database layer that will store the data appropriately and preserve the integrity of the data. Then implement the design on a Microsoft SQL Server database.

<b> Report (70%) </b>
<br>
Assessment consists of two parts: 1. create a web service that provides access through a RESTful API interface, and 2. develop a prototype linked data application providing the visualisation of a chosen
dataset.

<br>

<h2>Futher Information on Assignment 2: Report</h2>

### Part 1
This part of the coursework included making the following deliverables:
<ul>
  <li>A Microsoft SQL database</li>
  <li>An API to interact with the database</li>
</ul>

The database contains several tables that represent the three following entities: Students, their Projects, and the Programmes that they are enrolled within. The database also contains Stored Procedures and Triggers to provide speciifc behaviours. The following were created to meet the Assessment criteria:

The following tables were created:
<ul>
  <li>Students</li>
  <li>Programmes</li>
  <li>Projects</li>
  <li>StudentProgrammes</li>
  <li>StudentProjects</li>
  <li>Audit</li>
</ul>

Three stored procedures were then created to represent the following actions: Create, Update, Delete.
A student and their programme information can be found within a the StudentDetails view.
Finally, upon updating a Programme, a trigger would be called to store the old data in the Audit table, before it is overwritten by the new changes.

#### API
An API was written in ASP.NET to interact with this database, by using the following HTTP methods: POST, GET, PUT, DELETE.

---

### Part 2
Part 2 of the assignment involved making a Linked Data Application. 

The dataset chosen to theme the project around was: Active Library User age statistics: 
https://plymouth.thedata.place/dataset/active-library-users-by-age

This part of the assignment involved reading data from a file and displaying it on a webpage. Reading the data involved writing a filereader in C#, using ASP.NET .
The data is written to the DATA webpage after being fetched via javascript scripts, and then dynamically written to a table, again using javascript.

The LDA includes three total webpages:
<ul>
  <li>Index - introduces application</li>
  <li>Data  - displays dataset information</li>
  <li>Borrowers - displays dataset information in JSON-LD format</li>
</ul>


Bootstrap has been used to style the webpages: https://getbootstrap.com/
