Designing Data Intensive Applications
https://public.nikhil.io/Designing%20Data%20Intensive%20Applications.pdf

1 - Reliable, Scalable, and Maintainable Applications

- Components of a data intensive application:
  - Storing data to be retrieved later (databases)
  - Remembering the results of expensive computations (Caching)
  - Allowing users to search or filter for data (search indexes)
  - Sending messages to other processes (Stream processing)
  - Periodically crunching a large amount of data (batch processing)
- These concepts may seem obvious, but that's because they're the basic blocks of all larger systems
- As time goes on, tools emerge that fit many of these different qualifications
- Three important metrics:
  - **Reliability**: resistance to software/hardware/user failures
    - Things that can go wrong are called **faults**, which are different from **failures**: a fault is one part of the system deviating from spec, while failure means the system as a whole stops working
    - Manually triggering faults can be a good way to find and test ones which may suprise you
    - Hardware faults: are becoming a larger issue as systems expand to use more seperate hardware systems. 
    - Software errors: leaks, bugs, system rot
    - Human error: if tools are too restrictive, people will not use them
  - **Scalability**: growth due to data volume, traffic volume, or additional complexity
    - Let's talk about Load
      - Twitter example: two ways to design the timeline system; 
        - 1 - add new tweets to a database, and run a query every time a user requests their timeline
        - 2 - when a user tweets, add it to the timeline cache for each of their followers
    - **Performance**: (compute * load)
    - **Throughput**: requests per second, or time to run a job on a dataset of certain size
    - **Response time**: more important for online systems, time between request and response 
      - Latency and response time are not the same - latency is the measure of time between when a requesst reaches the backend and when it gets processed. 
      - Response time is a distribution, not a constant number. Often measured in p50, p99, p999
    - **SLOs and SLAs**: Service Level Objectives and Agreements
    - **Head of Line blocking**: an early thing slowing down downstream things
  - **Maintaiability**: system should not become harder to work with as it ages
    - Three principles:
      - **Operatability**: make it easy for ops teams to keep a system running
        - Monitoring health, locating problems, updates, predictability, Observability platforms help this, Documentation
      - **Simplicity**: remove complexity in the architecture
        - Abstraactions, APIs
      - **Evolvability**: also known as extensability, easy to change
        - AGILE baby
        
- 2 - Data Models and Query Languages

  - Relational Model
    - **RDBMS** , or Relational DataBase Management System: maianly **SQL** 
    - Alternatives have come and gone, but SQL is suprisingly sticky
    - **NoSQL**: more scalable, specialized queries
    - **Query Optimizers**: the magic part of a RDBMS, which makes it work so well 
  - Document Model
    - **JSON**, sometimes XML
    - Advantage is that all data is in one place: as opposed to you may have to run multiple SQL queries to get everything, as some entries cana reference other tables (resume example)
    - However, RDBMS can be easier to update and modify
    - "Shredding": the process of breaking a document model into a relational model
  - Query Languages
    - **Declarative** QLs: SQL
      - Select * from Animals where Type = Shark
      - Abstracts functionality and implementation 
      - Database is free to be refactored or optimized
      - Doesn't care about order, better parallel execution
      - CSS works like this, and thank god - see examples of alterntaives
    - **Imperative** QLs: IMS, CODASYL
      - Sharks = []; For x in animals: if x == shark {sharks.append(x)}; return Sharks
      - Harder to parallelize
  - Graph Data Models
    - Nodes and Edges, classic algos 
    - Some graphs have mixed data types as nodes and edges - IE not all nodes are people and all edges are friendships
    - Triple-store model: subject, predicate, object model
    
- 3 - Storage and Retrieval

  - Hash tables - you love to see them
    - Not great on disks, better in memory - requires lots of random read/writes
    - Range queries also don't work well - each hash is a separate read/write
  - B-trees
    - Similar to a red/black tree, but better for reading from disks - deal in 4kb pages, less node traversals	
    - log(n) for search, insert, delete


- 4 - Encoding and Evolution

  - Most common problem to work around is changing the in-memory representation of data into a network-friendly format
  - Language-specific formats: 
    - python pickle, java serializable. Problem is that this is brittle - language specific, often language version specific. Also introduces parsing risk when passing these around and reading shit directly into memory 
  - JSON, XML, CSV
    - highly compatible, human-readable
    - some disagreement on the margins about things like handling numbers, binary
  - 
    
   