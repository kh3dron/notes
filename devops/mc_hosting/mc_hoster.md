- get minecraft server running in a docker container?
- use aws sdk to start and stop ec2 instance

- host simple site in an s3 bucket. site has buttons that make calls 



this is hard. start with something simpler and scale up.

- [done] minimum viable aws amplify site 
    - created mc-holder repo to store codebase
    - hello world html file in the repo
    - create new amplify site tied to repo 
- [here] create the world's simplest api 
    - take a number, square it, return it
    - create a lambda function that squares a number
    - add a form to html page, and get form to send request to api
    - need to configure API gateway now
        - create new REST API 
        - actions, create method, post, point it to the squarer lambda function
        
- [todo] replace squarer api with ec2 launcher api 
- [todo] create minecraft server on ec2
- [todo] move logs from ec2 to webpage
