# Kosha MS SQL Server Connector


MS SQL (Microsoft SQL Server) is a relational database that offers excellent performance, high availability, and advanced security features. It integrates well with the Microsoft technology stack, providing seamless integration with tools like Visual Studio and Azure. 


The Kosha MS SQL Server connector enables you to perform REST API operations from the MS SQL Server in your Kosha workflow or custom application. Using the Kosha MS SQL Server connector, you can directly access MS SQL Server to:

* Get database schemas
* Create, read, and delete table records
* Create functions

## Useful Actions

You can use the Kosha MS SQL Server connector to perform a variety of functions related to managing database tables.

Refer to the Kosha MS SQL Server connector [API specification](openapi.json) for details.

### Table records

A table record is a single row of data within a table. Use the PostgreSQL connector to:

* Create, delete, and read records
* Read records by query params

### Table metadata

Table metadata describes tables in the database and includes details such as the table name, column names, and data types of the columns. Use the Kosha PostgreSQL connector to retrieve metadata for tables and table columns.

### Database schemas

A database schema organizes database objects such as tables, views, indexes, procedures, and other related entities. Use the PostgreSQL connector to get schemas for a database.

### Stored procedures

Stored procedures enable you to group related database operations, improve performance, ensure data consistency, and promote code reusability and security in your applications. Use the PostgreSQL connector to:

* Create, get, and delete user-defined functions
* Execute RPC functions

## Authentication

To authenticate when provisioning the Kosha MS SQL Server connector, you need your:

* MS SQL Server database username and password
* MS SQL Server database host
* MS SQL Server database name
* MS SQL Server port number

## Kosha Connector Open Source Development

All connectors Kosha shares on the marketplace are open source. We believe in fostering collaboration and open development. Everyone is welcome to contribute their ideas, improvements, and feedback for any Kosha connector. We encourage community engagement and appreciate any contributions that align with our goals of an open and collaborative API management platform.
