- get minecraft server running in a docker container?
- use aws sdk to start and stop ec2 instance

- host simple site in an s3 bucket. site has buttons that make calls 



this is hard. start with something simpler and scale up.

- [done] minimum viable aws amplify site 
    - created mc-holder repo in aws-codecommit to store codebase
    - hello world html file in the repo
    - create new amplify site tied to repo 
- [here] create the world's simplest api 
    - take a number, square it, return it
    - create a lambda function that squares a number
    - add a form to html page, and get form to send request to api
    - need to configure API gateway now
        - create new REST API 
        - actions, create method, post, point it to the squarer lambda function
        - add mapping 
    - test the POST method in API gateway: feed it {"input":6} and get a response body 36
- [here] get the site to call and respond to the API 
    - surf stackoverflow to find some code 
    - getting blocked by CORS protections
        - maybe running the page on amplify instead of off my desktop will let me not fully deal with this right now
        - nope, that doesn't do it
        - turns out it's easy: there's an option to enable CORS on the API gateway
    - need to get the response from the API to show up on the HTML page
    - found an issue: I think my API request is wrong. It might show the response how I want it to, but there's currently no parameters passed to the request in the first place

- [todo] replace squarer api with ec2 launcher api 
- [todo] create minecraft server on ec2
- [todo] move logs from ec2 to webpage
