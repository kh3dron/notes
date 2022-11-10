# Clean Code (8/13/2022 - 9/15/2022)

### 1 - Clean Code

- We will never be rid of code, because code represents the details of the requirements.
- We will never eliminate necesarry precision - so there will always be code.

### 2 - Meaningful Names

- Use intention revealing numbers
- Avoid:
    - magic numbers: hold in named variables
    - “data”, “info”, “count”
- Use:
    - Units (elapsedTimeInDays instead of Time)
    - Pronouncable, readable names
    - Searchable names
- Grammar:
    - Classes / vars: nouns, functions: verbs
- One word per concept: don’t mix “fetch” and “retrieve”

### 3 - Functions

- Should be SMALL
- should do ONE THING
- Break into multiple functions if:
    - more than 1 or 2 levels of nested logic
- Pass in as few arguments as possible
- Passing in booleans is especially ugly
- If many arguments are better described as a single object, package them as such! (X, Y) → (Point)
- Command-Query seperation
    - Do something or answer something, not both
    - not great to return false if an operation failed, or error codes
- Master programmers think of systems as stories to be told rather than programs to be run.

### 4 - Comments

- A necesarry evil!
- Wrapping logic in a nicely named function
- Good comments:
    - explain intent, clarify dense logic (regex)
    - warning of consequences
    - TODOs
- Bad comments
    - Clutter (javadocs)
    - provide no new information
    - closing braces
    - code. Version control is fine

### 5 - Formatting

- “Code formatting is abotu communication, and communicstion is a professional developer’s first order of business.”
- Make spacing, new line decisions deliberately
- declare variables near their use
- Agree on rules as a team and follow them.

### 6 - Objects and Data Structures

- Objects have no functions and expose data. Structures have functions and no data.
    - square data in a Shape structure. Where to add a perimeter?

### 7 - Error Handling

- failures should attempt to be atomic - you don’t want to change state if something fails. Check for failures before making changes if possible
- Don’t pass nulls in and out of functions
- Error handling should not be relied on as a part of logic flow!

### 8 - Boundaries

- Wrap external libraries in your own classes if you want to be lean
- If you’re blocked, write yourself custom objects and interact with mocks

### 9 - Unit Tests

- The three laws of Test Driven Development:
    - No writing code until you’ve written a failing unit test
    - Don’t write more test than is required to fail, and not compiling is failing
    - Write as little code as possible to pass the currently failing test
- Test code should be maintained as well as production code, not as an afterthought
- Some like “one assert per test” for maximum readability, but this can be extra
- “One concept per test” is a little more flexible
- FIRST rules: tests should be:
    - Fast to run
    - Independent of eachother
    - Repeatable
    - Self-validating, outputting booleans
    - Timely, not written adfter deployment

### 10 - Classes

- Classes should have managable, limited responsibilities
    - If it’s too hard to name, it’s too big
- Cohesion: class methods should manipulate most of the variables in that class. Make classes out of these bound circles, and split off what you can into smaller subclasses

### 11 - Systems

- Seperate Conustruction logic from Usage logic
- All constructions should happen in the main method. all other methods should assume that main has been constructed.
- Abstract Factory pattern: bundle several factories together without specifying classes
- Dependency Injection
- Use the simplest thing that can possibly work

### 12 - Emergence

- Kent Beck’s 4 rules of simple design:
    - runs all the tests
    - containes no suplication
    - expresses the intent of the programmer
    - minimizes the number of classes and methods

### 13 - Concurrency

- concurrency is decoupling from time (cool)
- keep concurrency-related code seperate from other code
    - use synchronous blocks when you can
- race conditions, all that good stuff - see Designing Data Intensive Applications

### 14 - Successive Refinement

- To write clean code, you can write dirty code, and then clean it.
- refactor with test-drive development so that the program always works. large refactorings are dangerous.

### 15 - JUnit Intervals

- The boyscout rule: we should leave things cleaner than we found them

### 16 - Refactoring SerialDate

- another exercise

### 17 - Smells and Heuristics

- A long list summarizing this entire book