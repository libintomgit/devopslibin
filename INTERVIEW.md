TELL ME ABOUT YOURSELF

I am an IT infrastructure enthusiasist. Over the past 9 plus year I have been helping several companies to design, implement and manage their IT Infra in a highly available and higlhy scalable architecture for their software application delivery to end customers.

I also have experience in leading teams especially for the project deliverables with the agile and devops environment having continues integration, continues deployment and continues monitoring systems in place.

I have started my career in techsupport domain helping internal customers in JPAC region. Later challanged myself to work on the datacenter implementations and handling production systems. Where I have gained knowledge on virtualizations in hyperv, xen, kvm and later worked in several projects in migrating the on-prem systems to cloud environment.

I always focus on resource optimization to improve the cost effeciency and management overheads with a data-driven approach, so I aways like to test and adapt to latest tools and technology in the market which fits for the organization. I think that is my strength so far and that is something I wish to bring on to the table.

There are way too many systems, tools, technologies available according to the needs of an organization but the I belive as far as infrastructure concerned. Its about implementing them in a right way, scalable in the long run or adapting the industry bestpractices. Indepth documentation.

So is this experties Amazon looking for in this role ?

STAR

1. Tell me about the time when you had a conflict with a co-worker.

There were many situations and almost they occurs when the expectations is not set very clearly among the team on each individuals roles and responsibilities i belive.

SITUATION
but apart from that, I remember, in one of my project to we had to automate the container deployment for a new application. I had proposed the a system using Terraform, Jenkins, Spinaker, Helm and AKS but my colleague had a different approch in mind using Azure Devops which he was more femilier with. This led to a conflict between us.

TASK
The task at had was to streemline the deployment process to enhance effeciency and reduce manual errors. Our responsibility was to evalute the various tools and implement the most suitable one for our infrastructure.

ACTION
So to address this conflict, I initiated a discussion to understand his perspective better. Through this conversation I gained valuable insigts into his experience and the strengths of the system he proposed.

However, I also shared my viewpoint regarding the system that I had proposed and explained the advantages as the most of the infrastructure we used in the organisation was opensource. I highlighted the advantages of cost effeciency in the long-run and only the proper documentation was needed to handle the system.

Moreover, insted of insisting solely on my decision. I suggessted a data driven approch to list down the advantages a disadvantages of the both of our proposal and one more approch and conducting a pilot project in a controled environment to evaluate the performance and operational over head becasue it was one time effort and that could make all of our life easy going forward.

RESULT
The pilot project proved insightfull with data that on the long run the opensource system was more cost-effective and more in our control. Through collabrative effort and open communication we both could come to satisfactory conclusion and best part is that with a contrate data we could present it our manager and it also  strengthend our working relationship. 


To conclude, i guess colnflicts are inavitable in the technical roles but its just about having an open mind to listen to others ideas and find a way make it positive relationship.


2. Tell me about the time when you have to solve a difficlut problem

SITUATION

In a previous role as devops infrastructure engineer, one of the application infrastructure experienced critical performance issue during peak hours. Users were experiencing significant latency and occational downtime, impacting the overall userexperience and revenue.It was crusial to identify the root cause and fix the problem immediately.

TASK
My task was to investigate the performance issue, identify the base cause and implement a solution.

ACTION
To address the issue, I first gathered metrics from the monitoring tool prometheus and logs to analyse the performance metrics during peak usage hour. Thorugh this analysis I identified a sudden spike in CPU and memory utilization in the database instances.
Next collabrating closely with our database administrators and developers, conducted a review of database configurations, indexing stratergies and query performance to gain insights about the applications database interactions and query patterns.

During this investigation, we noticed that a software update that introduced a suboptimal database query that was causing excessive resource consumption. The query was generating unnessesary joins and scans leading to inefficient query execution plan and increased the load on the database server.

Then the I have worked with dev team to check on optimising the query and they refactored it to use more efficient indexing stratergies and query execution techniques. Then I implementd, proactive moniroing and alerting rules to mitigate similar performance issue.

RESULT
By implementing these solutions we were able to significantly improve the system performance during peak hour. Moreover, the proactive monitoring and alerting helped to detect performance bottelnecks earlyon. 
Overall, this experience highlighted the importance of proactive problem-solving, collaboration across teams, and leveraging data-driven insights to resolve complex technical challenges effectively. It also reinforced the value of continuous improvement and proactive maintenance in ensuring the reliability and performance of our infrastructure.




Delivered excellent customer service

Situation:
In a previous role as a DevOps infrastructure engineer, I was responsible for managing our company's cloud infrastructure. One day, we encountered a critical issue where a production server went down unexpectedly during peak hours, affecting our customers' ability to access our services.

## When you made a mistake

Situation:
In a previous project, I was tasked with implementing a new CI/CD pipeline to automate the deployment process for our applications. The goal was to streamline development workflows and accelerate the delivery of new features to production.

## When disagreed with your boss

Situation:
In a previous role, I was working on a project where we were transitioning our infrastructure to a cloud-based environment. As part of this transition, my team and I were responsible for selecting the cloud provider and designing the architecture for our applications. I knew that most of my teammates were proffecient in the AWS but Azure was providing the credits with was significant in terms of cost.

But I had to explain the manager about the teams strength and also a constructive document to show that in the long run that it might not make much difference in terms of cost. 

As an action I have tried to explore the cost in both providers and could provide some what level of data and also requested the manager that we can setup a multicloud environment and monitor for a certain period for the cost difference and also the operational overhead and take a right decision later without imacting the application.

As result manager approved the request and also appriciated the approach and this approach will not impact the application availability in case of low knowledge in the new environment.


## you had a conflict with a co-worker

There were many situations and almost they occurs when the expectations is not set very clearly among the team on each individuals roles and responsibilities i belive.

SITUATION
but apart from that, I remember, in one of my project to we had to automate the container deployment for a new application. I had proposed the a system using Terraform, Jenkins, Argocd, Helm and AKS but my colleague had a different approch in mind using Azure Devops which he was more femilier with. This led to a conflict between us.

Task:
I took an initiative to resolve this conflict by communicating with my workmate and take a constructive decision to finalise the proposal.

Action:
As an action I have initiated the discussion and listend actively to understand his thought process and I have explained him my reason for the proposal as I was more concerned about the managibility in the future becasue most of us in the team had only experience with jenikins and with such level of work pressure it would have been challanging to learn and troubleshoot a new tool. On top jenkins was already available. However I suggested that we can use try his proposal in a POC type setup or with a low priority application and once everyone gets inline with the system we can implement the same to higher priority application if required.

Result:
As a result of the discussion, we both came to conclussion and were on the same page and the conflict was resolved between us. Also our manager was very happy with our approch to work together to come to a conclusion proactively with improved the relationship with our manager.


## Tell me about a time when you faced challenging problem at work and how did you handle it ?

Stituation:
Application moniroting was reporting intermitent connection issue to kafka service from the producers and consumers. Kafka was under loadbalancer type service and a public network loadbalancer was running.

Taks was to indentify the root couse and implement the solution.

As an action I started to look at the logs of load balancers and applications, however no construct log evidence was available to find the root cause. Further I tought of checking the port connection activity continuously using telnet in the watch tool for every 2 secods and noticed that the ip address was changing each time to public and private ip address. So I checked the loadbalancer subnets and understood that the it had 2 subnets and one of them was private which triggered some thing worng and I check the aws cloud trail for all the cloud api changes. That provided and idea that private subnet was add recently to the loadbalancer becasue one of the site reliablity engineer created a private subnet as the IPs for one of the node group in the same cluser was exhausted however he copied all the tags from this subnet and the kubernetes watched for the same and added the subnet to the LB. To resolve the issue i had recreate the loadbalcer and its not possible to remove the subnet once added to the loadbalancer.

As a result the issue was resolved permanently and also added a manual check in the documentation to avoid such issues in the future. Also shared this root cause anlaysis report within the enineering team for the transparancy.

you had to work as part of a team. What was your role, and how did you contribute?

## solve a difficlut problem

SITUATION

In a previous role as devops infrastructure engineer, one of the application infrastructure experienced critical performance issue during peak hours. Users were experiencing significant latency and occational downtime, impacting the overall userexperience and revenue.It was crusial to identify the root cause and fix the problem immediately.
