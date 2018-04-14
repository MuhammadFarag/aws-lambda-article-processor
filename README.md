## AWS Lambda Article Processor
A test app that attempts to recreate concpets from actor model design patterns in Lambda. The focus is on lambda rather than the on the programming language itself. I have choosen Python because it gives a quicker feedback loop and shorter cold start time.

#### Motivation
I have had experience working with Akka Actor model and I feel that their are some degree of resimplance between lambda functions and stateless actors. However, I need to understand more in order to be able to draw that comparison. TDD'ing, writing and deploying actors is rather simple in Scala. I am curious if the same can be achieved with AWS lambda.

#### Design consideration
I am going to treat each lambda as a stateless actor. It should be able to do one thing only (from domain prespective) and do it very well.

#### Domain
For the purposes of this exercise, I am assuming that I want to go throw a collection or a stream of articles. Each article has the following fields

- author
- content
- priority

The operations I am going to perfrom

1. Validate that a record has an author name attached
2. Count the number of words in the content
3. In the same time

    - Capitalize the first letter of each word of the author name

    - Add five to the priority (this channel has higher priority compared to other channels