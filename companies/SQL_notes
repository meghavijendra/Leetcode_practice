INTRODUCTION TO DATABASES

-> The relational model means that the logical data structures—the data tables, views, 
and indexes—are separate from the physical storage structures, and this separation provides flexibility in how data is stored and managed.

-> Structured query language helps data move between databases and apps, playing a key role in today's software setup.

-> Importance of Databases:
1. Efficient Data Storage and Retrieval
2. Data Security and Integrity
3. Support for Multiple Users
4. Flexibility in Data Management
5. Driving Decision-Making



CORE COMPONENTS OF DATABASES

-> Core Functional Components
1. Query Processor :  query processor is responsible for interpreting and executing user queries, translating them into operations the database can perform
2. Storage Engine : storage engine is responsible for managing how data is physically stored, retrieved, and maintained
3. Transaction Manager : transaction manager ensures that database transactions adhere to ACID properties
4. Lock Manager : lock manager handles concurrency by ensuring multiple users can access the database simultaneously without conflicts
5. Cache Manager : cache manager speeds up query execution by storing frequently accessed data in memory.
6. Recovery Manager : recovery manager ensures the database can be restored to a consistent state after failures, such as crashes or hardware issues
7. Catalog : catalog, also known as the data dictionary, is a metadata repository that stores information about the database like schema definitions, user roles & permissions and storage details.

-> In query processor we have:
1. parser/translater
2. Optimizer (containing different execution plans)
3. Execution engine

-> What is an SQL Query Execution Plan?
An SQL query execution plan is a roadmap that the database engine uses to execute a query efficiently. It’s a step-by-step strategy that outlines how the database will process the query, including which indexes or table scans will be used, the order of operations, and how data will be joined and filtered.

-> When "estimated execution plans" are generated, the T-SQL queries or batches do not execute. Because of this, an estimated execution plan does not contain any runtime information, such as actual resource usage metrics or runtime warnings. Instead, the execution plan that is generated displays the query execution plan that SQL Server Database Engine would most probably use if the queries were actually executed, and displays the estimated rows flowing through the several operators in the plan

-> "Actual execution plans" are generated after the T-SQL queries or batches execute. Because of this, an actual execution plan contains runtime information, such as actual resource usage metrics and runtime warnings (if any). The execution plan that is generated displays the actual query execution plan that the SQL Server Database Engine used to execute the queries.

-> Important Parts of an Execution Plan
Understanding the components of an execution plan is vital for identifying performance bottlenecks:
1. Table Scans vs. Index Seeks: Execution plans reveal whether tables are being fully scanned or if indexes are being utilized for efficient data retrieval.
2. Join Algorithms: Different join algorithms (e.g., nested loop, hash join) impact how data from multiple tables is combined.
3. Filtering and Sorting: The plan highlights where data filtering and sorting occur, indicating potential performance hotspots.

-> How to Optimize SQL Queries
Execution plans and statistics play a crucial role in optimizing query performance
Optimizing SQL queries involves enhancing execution plans to achieve better performance:
1. Indexing: Properly designed indexes can significantly speed up data retrieval.
2. Query Rewriting: Restructure queries to be more efficient without changing their logical output.
3. Data Denormalization: In some cases, de-normalizing data can reduce the need for complex joins and improve query speed.
4. Using Joins Wisely: Choosing the right type of join and optimizing join conditions can impact query efficiency.

-> Statistics:
Definition: Statistics are metadata that SQL Server uses to estimate the distribution of data in a table or index. They help SQL Server generate optimal execution plans.



DATABASE ARCHITECTURE

1. Client-Server Architecture : The client-server architecture is a two-tier model where clients (applications or users) directly interact with a database server.

2. Three-Tier Architecture : The three-tier architecture builds on the client-server model by introducing an intermediate application layer. This layer handles business logic, creating a clear separation between the user interface (client) and the database (server). The three layers are:
~ Presentation Layer (Client): Provides the user interface and interacts with the user.
~ Application Layer (Middleware): Processes business logic, validates data, and coordinates between the client and database.
~ Data Layer (Database): Stores and manages the application’s data.
This separation enhances scalability and flexibility, making it easier to update individual layers without affecting the entire system.

3. N-Tier Architecture : N-tier architecture extends the three-tier model by introducing additional layers, such as service layers, integration layers, or caching layers. This approach provides even more modularity, allowing each layer to specialize in specific tasks.
This is used in complex systems with high performance requirements, such as multi-service enterprise applications or microservices architectures

4. Cloud-Based Database Architectures : Cloud-based architectures host databases on cloud platforms, such as Amazon Web Services (AWS), Google Cloud Platform (GCP), or Microsoft Azure. These architectures offer flexibility, scalability, and managed services, allowing businesses to focus on application development rather than infrastructure.
Cloud databases can be deployed in various models:
~ Infrastructure as a Service (IaaS): Provides virtual machines for hosting traditional databases.
~ Platform as a Service (PaaS): Offers managed database services, such as AWS RDS or Google Cloud SQL.
~ Software as a Service (SaaS): Provides fully managed applications that abstract database interactions, like Salesforce or Google Workspace.

5. Distributed Database Architectures : Distributed database architectures store data across multiple physical locations, often in different regions. These systems are designed for scalability, fault tolerance, and low-latency access. Data can be partitioned (sharded) across nodes or replicated for redundancy.



RELATIONAL VS NON-RELATIONAL DATABASES

-> The relational model organizes data into tables (also known as relations) consisting of rows and columns. EX: Oracle Database
Microsoft SQL Server, MySQL and PostgreSQL
Characteristics
~ Structured Schema: Enforces a predefined schema, ensuring data consistency and integrity.
~ ACID Compliance: Guarantees Atomicity, Consistency, Isolation, and Durability for transactions.
~ SQL Support: Utilizes Structured Query Language (SQL) for data manipulation and querying.
Advantages
~ Data Integrity: Strong enforcement of data constraints ensures accuracy and reliability.
~ Flexibility in Querying: Powerful SQL capabilities allow complex queries and data manipulations.
~ Standardization: Widely adopted standards facilitate interoperability between different DBMSs.
Disadvantages
~ Scalability Limitations: Vertical scaling (enhancing a single server) can be costly and has physical limits.
~ Rigid Schema: Adapting to changing data requirements may require significant schema modifications. Strong consistency
~ Performance Overheads: Complex joins and transactions can lead to performance bottlenecks in large-scale applications.

-> Non-relational databases, often referred to as NoSQL (Not Only SQL) databases, provide flexible data models designed to handle unstructured or semi-structured data, high scalability, and distributed data storage.
Types:
~ Document stores : Store data in documents. Examples: MongoDB, CouchDB
~ Key-Value Stores : Store data as simple key-value pairs. Examples: Redis, Riak, Amazon DynamoDB
~ Column-Family Stores : Organize data into columns grouped into families, allowing storage of large volumes of data. Examples: Apache Cassandra, HBase
~ Graph Databases : Use graph structures with nodes, edges, and properties to represent and store data. Examples: Neo4j, Amazon Neptune
Characteristics
~ Flexible Schema: Allows dynamic data models that can evolve with application requirements.
~ Horizontal Scalability: Easily scales out across multiple servers or clusters.
~ Eventual Consistency: Many NoSQL systems prioritize availability and partition tolerance, offering eventual consistency over strict ACID compliance.
Advantages
~ Scalability: Optimized for distributed environments, handling large-scale data efficiently.
~ Performance: Tailored for specific use cases, offering high performance for targeted operations.
~ Flexibility: Accommodates diverse and evolving data structures without significant schema changes.
Disadvantages
~ Limited Standardization: Lack of universal query languages can lead to complexity in querying and integration.
~ Eventual Consistency: May not be suitable for applications requiring immediate consistency.
~ Complexity in Transactions: Handling complex transactions and ensuring data integrity can be challenging.



DATA STORAGE FUNDAMENTALS

-> The memory hierarchy is a layered structure of storage technologies, organized by speed, cost, and capacity.
1. RAM (Random Access Memory): Storing frequently accessed data and intermediate results during query execution.
2. SSD (Solid-State Drives): Ideal for index storage and transaction logs due to fast read/write speeds.
3. HDD (Hard Disk Drives):  Storing archival data and infrequently accessed information.

-> Serialization is the process of converting in-memory data structures into a format that can be stored or transmitted (e.g., JSON, BSON, or binary formats). 
-> Deserialization is the reverse process, reconstructing data into its original structure.

-> Endianness refers to the order in which bytes are stored or transmitted:
1. Big Endian: Stores the most significant byte first.
2. Little Endian: Stores the least significant byte first.
A database system storing binary data must account for the endianness of the underlying hardware to avoid errors when reading or writing data.

-> Data alignment ensures that data is stored in memory at addresses that are multiples of its size. Misaligned data can cause performance penalties on some architectures.
-> Index structures like B-trees are aligned to ensure efficient traversal and minimal access times.



FILE ORGANIZATION IN DBMS

-> File organization defines how data records are stored in a database file, impacting how data is retrieved, inserted, updated, or deleted. Proper file organization is essential for optimizing database performance.
-> Types of file organizations:
1. Sequential File Organization : In sequential file organization, records are stored in a sequential order based on a specific key field (e.g., primary key). When new records are added, they are placed in the correct order, maintaining the sequence.
2. Heap File Organization : Heap files are unordered, meaning new records are inserted wherever space is available. No sorting or indexing is applied, making this the simplest form of file organization.
3. Hash File Organization : In hash file organization, a hash function is used to calculate the address of a record based on a key field. Records are stored in buckets corresponding to hash values.
4. Clustered File Organization : In clustered file organization, records with similar values are stored together physically. This organization is often based on clustering indexes.
5. B+ Tree File Organization
6. ISAM (Indexed Sequential Access Method)

-> With a clustered index the rows are stored physically on the disk in the same order as the index. Therefore, there can be only one clustered index.

-> With a non clustered index there is a second list that has pointers to the physical rows. You can have many non clustered indices, although each new index will increase the time it takes to write new records.


DATA COMPRESSION AND ENCODING

-> Data compression and encoding techniques help reduce storage space and improve query performance.
1. Lossless Compression Algorithms
Lossless compression reduces the size of data without any loss of information, ensuring the original data can be perfectly reconstructed after decompression (common algos used : Huffman Encoding, Run-Length Encoding)
2. Columnar Storage Benefits
Columnar storage organizes data by columns instead of rows. Each column is stored sequentially on disk, enabling efficient compression and fast access for analytical queries.
3. Encoding Techniques
~ Dictionary Encoding
Dictionary encoding replaces repetitive values in a dataset with unique identifiers stored in a dictionary. The actual data references these identifiers instead of storing the original values repeatedly.
~ Run-Length Encoding (RLE)
RLE compresses consecutive repeating values by storing the value and its count instead of storing each occurrence.



DATABASE INDEXES

-> Indexing is a technique used in databases to enhance the speed of data retrieval operations. An index acts as a reference point, allowing the database to quickly locate and access the desired data without scanning the entire table
-> Indexes can be broadly classified into two categories: 
1. single-level indexing : index directly maps to the data records (primary index, secondary index and clustering index)
2. multi-level indexing : Instead of directly pointing to data records, higher-level indexes point to lower-level indexes, which then lead to the data. (Two widely used tree-based structures in database indexing are B-trees and B+ trees)
3. Hash-Based Indexing : Hash-based indexing employs a hash function to compute a hash value for each key, determining the bucket or slot where the corresponding record will be stored. (Static and dynamic hashing)

-> A Bloom filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. Unlike traditional data structures like hash tables, it does not store the actual data but instead uses a bit array and multiple hash functions
For example, a social media platform uses Bloom filters to quickly check if a username is already taken. Instead of scanning through millions of records, Bloom filters provide a quick probabilistic answer.
-> Limitations of Bloom Filters
~ False Positives: The filter may claim an element is present when it is not.
~ No Deletion Support: Removing an element is not possible without affecting other elements in the filter.
~ Increased Latency with Size: As the size of the bit array increases, hashing operations take more time.



TRANSACTION MANAGEMENT

-> A transaction in a database represents a single, logical unit of work. It ensures that a series of operations either completes successfully as a whole or fails entirely, leaving the database unchanged.
-> A transaction can either be:
1. Committed: All operations within the transaction are successfully executed and changes are permanently saved.
2. Aborted: If any operation fails, all changes made by the transaction are undone, leaving the database in its original state.

-> ACID Properties of Transactions
1. Atomicity: Transactions are "all-or-nothing" operations. If one part fails, the entire transaction fails, ensuring no partial changes occur.( Can be achieved using write ahead logging and two phase commit )
2. Consistency: Transactions move the database from one valid state to another, maintaining all defined rules, constraints, and relationships. ( Can be achieved by Validation Rules, Pre-Transaction Checks, Post-Transaction Verification and Atomic Execution)
3. Isolation: Multiple transactions occurring simultaneously do not interfere with each other, preserving the correctness of operations.
(Isolation levels -  Read Uncommitted,  Read committed , Repetable read and Serializable)
4. Durability: Once a transaction is committed, its changes are permanent, even in the case of system failures. ( Can be achieved by  Write-Ahead Logging (WAL), Checkpointing, Synchronous Disk Writes and Replication)

-> The Lost Update Problem occurs when two or more transactions modify the same data concurrently, and the updates of one transaction are overwritten by another, leading to data loss.
-> CAS (Compare-And-Swap) is an atomic operation used to address the Lost Update Problem by ensuring that updates are applied only if the original value matches the expected value.



CONCURRENCY CONTROL

-> Concurrency control is a mechanism used in databases to ensure the correct execution of transactions when multiple users or processes are accessing and modifying the database simultaneously.
-> Databases use various techniques to manage concurrency and prevent the issues mentioned above:
1. Optimistic Concurrency Control
Assumes conflicts are rare and allows transactions to execute without locks.
Example: Two users edit the same document. If no overlapping changes are found, both edits are saved.
2. Locking Mechanisms
Locks restrict access to data during a transaction, ensuring data consistency. (Two-Phase Locking, Predicate Locking, Index-Range Locking)
Example: Transaction A locks a row to update it. Transaction B must wait until Transaction A releases the lock.
3. Timestamp Ordering
Transactions are executed in the order of their timestamps to avoid conflicts.
Example: If Transaction A starts at 10:00 AM and Transaction B starts at 10:01 AM, A will execute first.
4. Multiversion Concurrency Control (MVCC)
Maintains multiple versions of data for concurrent transactions. Each transaction works on its own version, ensuring isolation.
Example: Transaction A reads the old version of a row while Transaction B updates it. A will see the old value until B commits.



DATABASE SHARDING AND PARTIONING

-> A distributed database is a collection of multiple interconnected databases spread across different physical locations but appearing as a single database to users.
-> Scalability is one of the most significant advantages of distributed databases, allowing systems to grow seamlessly as demand increases. There are two primary types of scalability:
1. Horizontal Scalability:
Adding more servers or nodes to distribute the workload.
Example: A database cluster for an online retailer grows as the number of users and orders increases.
2. Vertical Scalability:
Upgrading the hardware of existing nodes (e.g., adding more memory or processing power).
Example: Enhancing a single database server to handle temporary spikes in traffic.

-> Partitioning is the process of dividing a single database table or data set into smaller subsets, each stored and managed independently. While users interact with the database as a whole, the underlying system accesses only the relevant partition(s), significantly improving query performance.
1. Horizontal Partitioning
Horizontal partitioning involves splitting rows of a table into smaller partitions based on a specific criterion. Each partition contains a subset of rows, but all partitions have the same columns.
2. Vertical Partitioning
Vertical partitioning splits a table into smaller tables based on columns rather than rows. Each partition contains a subset of the columns, typically grouping them based on their usage patterns.

-> Sharding is a database architecture pattern that splits a single, large database into smaller, more manageable pieces called shards. Each shard is a subset of the database and operates as an independent database. Sharding helps improve performance, scalability, and availability in systems with large amounts of data or high transaction volumes.
-> Sharding Key Selection
The choice of a sharding key is critical for the effectiveness of sharding. A good sharding key should:
1. Distribute Data Evenly: The key should ensure that data is evenly distributed across shards to avoid hotspots or overloaded shards.
2. Support Query Patterns: The key should align with common query filters, ensuring queries can be routed to specific shards without scanning unnecessary data.
3. Minimize Rebalancing: The sharding key should reduce the need to move data between shards when scaling or redistributing the database.



DATA REPLICATION AND CONSISTENCY MODELS

-> Replication is the process of copying and maintaining data across multiple servers or nodes in a database system.
A global retail system uses replication to handle customer data: (Types of replication)
1. Full Replication: A complete copy of the database is maintained in each region for disaster recovery.
2. Transactional Replication: Real-time synchronization of order and inventory updates ensures accurate stock levels across warehouses.
3. Snapshot Replication: Periodic snapshots of product catalogs are shared with regional stores to update their systems.

-> Consistency models define the rules for the visibility and ordering of updates. They determine how and when changes made by one node become visible to others, affecting the behavior of reads and writes across the system.
Types of consistency models:
1. Strong Consistency
2. Sequential Consistency
3. Causal Consistency
4. Weak Consistency
5. Session Consistency
6. Monotonic Reads and Writes

-> The CAP theorem states that a distributed data store cannot simultaneously provide more than two out of the following three guarantees:
Consistency (C)
Availability (A)
Partition Tolerance (P)

-> Consensus is a critical concept in distributed systems, ensuring that multiple nodes in a system agree on a single source of truth or a shared state. It enables reliable coordination and consistency among nodes, even in the face of failures or network issues. 

-> Fault Tolerance is the capability of a system to continue its operations without interruption even when some of its components fail. In essence, a fault-tolerant system anticipates potential failures and incorporates mechanisms to handle them gracefully, ensuring uninterrupted service and data consistency.



DATA MODELING

-> Levels of Data Modeling
        Model                       Level	                                     Description Detail Level	        Example
1. Conceptual Model	High-level overview focusing on entities and relationships	            Low	    Entities: Customer, Order, Product
2. Logical Model	Detailed structure with entities, attributes, and relationships	        Medium	Attributes: CustomerID, Name, Email
3. Physical Model	Database-specific implementation with data types and storage details	High	SQL Table: Customer with VARCHAR fields

-> The Entity-Relationship (ER) model is a conceptual framework used to visually represent the data structure and relationships within a database. ER models define entities, attributes, and relationships, helping database designers translate complex, real-world scenarios into a clear, structured format that forms the basis for the database schema.



STORED PROCEDURES, VIEWS, TRIGGERS AND CURSORS IN SQL

-> Stored procedures in SQL Server are precompiled collections of SQL statements and optional control-of-flow statements such as IF statements and loops, stored under a name and processed as a unit.
Execution: Stored procedures must be explicitly called or executed by the user or application.
Parameters: They can accept input parameters and return output parameters.
CREATE PROCEDURE GetEmployeeDetails
    @EmployeeID INT
AS
BEGIN
    SELECT FirstName, LastName, Title, Department
    FROM Employees
    WHERE EmployeeID = @EmployeeID;
END;

-> A view in SQL is a virtual table that is based on the result set of a SQL SELECT query. It does not store the data itself but rather provides a way to access and manipulate the data stored in one or more tables.
Execution: Views are used in queries like regular tables but do not contain data themselves; they fetch data from the underlying tables.
Parameters: Views do not accept parameters.
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

-> A trigger in SQL is a special type of stored procedure that automatically runs when certain events occur in the database. These events can be insertions, updates, or deletions on a table or view. Triggers can be used to enforce business rules, validate input data, maintain audit trails, and more.
Execution: Triggers are implicitly executed when the specified event occurs.
Parameters: They do not accept parameters.
1. Types of Triggers
DML Triggers (Data Manipulation Language): These triggers fire in response to data manipulation events (INSERT, UPDATE, DELETE).
DDL Triggers (Data Definition Language): These triggers fire in response to changes in the database schema (CREATE, ALTER, DROP).
Logon Triggers: These triggers fire in response to logon events to the SQL Server.
2. Timing of Triggers
BEFORE Triggers: These triggers execute before the triggering action is performed.
AFTER Triggers: These triggers execute after the triggering action is performed.
INSTEAD OF Triggers: These triggers replace the triggering action.

-> In SQL, a cursor is a database object used to retrieve, manipulate, and navigate through a result set row-by-row. Cursors are particularly useful when you need to perform operations on each row individually rather than operating on the entire result set at once
