# Infura Test

This application is inspired by an assessment taken by a friend who needed help load testing his code. This [StackOverflow question](https://stackoverflow.com/questions/46893226/performance-load-and-stress-testing-in-django) has its implementation in this repository.

## Prerequisites

* Ensure you have [Postman](https://www.postman.com/downloads/) installed to run commands

## Building The Application

To run the app, take the following steps:

* Register for an [INFURA Project ID](https://infura.io/register) and grab the PROJECT ID from them. It's free and does not need a credit card.

* Clone the repository into your local machine

* Rename `.env.example` to `.env` and paste your PROJECT ID from the first step.

* Build the Docker image with `docker build -t infura_api .`

* Run the application with `docker run --env-file .env -p 5000:5000 infura_api`

## Unit Testing

To run tests, perform the following actions:

* Build the Docker image with `docker build -t infura_test -f testing.Dockerfile`

* Run the application with `docker run --env-file .env infura_test`

## Load Test

### Setup

Start up the locust server using the command `locust` on the terminal.

There are other tools that help with load testing applications. More information can be found on [Blazemeter](https://www.blazemeter.com/blog/open-source-load-testing-tools-which-one-should-you-use).

### Load Test Results Analysis

You can click on the [results file](results/load_test.html) and open it in a browser to see a detailed report of the load testing.

Here's some high level summary of my analysis:

* This application can accept an aggreggated 36.2 Requests Per Second when 100 users with a spawn rate of 5 new users every second until 100 users mark is reached.

* However, the application has an aggregated response time of 1.5 seconds in the 99th Percentile.
