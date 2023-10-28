<p align="center">
  <img src="logo.png" alt="EstiMateGPT" width="300"/>
</p>

**EstiMateGPT** is a digital tool designed to provide users with tailored GPT-4 implementation estimates for their projects. By inputting details about their domain, desired features, and other relevant information, users can gain insights into the scope, timeline, and potential costs associated with their GPT-4 endeavors. The application aims to streamline the initial stages of project planning, offering an intuitive interface that interacts with the ChatGPT API to generate dynamic and informative estimates. 

---

### AWS Resources

For the 3-day schedule of the **EstiMateGPT** project, the following AWS resources would be essential:

1. **Amazon Lambda**:
   - Serverless compute service that lets you run code without provisioning or managing servers.
   - Used to create the middleware function that communicates with the ChatGPT API and processes the user's requests.

2. **Amazon API Gateway**:
   - Service to create, publish, maintain, monitor, and secure APIs.
   - Used to expose a secure endpoint for the frontend to communicate with the AWS Lambda function.

3. **Amazon S3 (Simple Storage Service)**:
   - (Optional for this schedule but commonly used in real-world scenarios)
   - Object storage service that offers scalability, data availability, security, and performance.
   - Could be used to host static frontend assets like HTML, CSS, and JavaScript files if you decide to deploy the MVP to the web.

4. **Amazon CloudWatch**:
   - Monitoring and observability service.
   - Useful for monitoring the performance of Lambda functions, logging API calls in API Gateway, and setting alarms for potential issues.

5. **AWS Identity and Access Management (IAM)**:
   - Service that helps securely control access to AWS resources.
   - Used to set permissions and roles for the Lambda function, API Gateway, and other resources to ensure they can interact with each other.

6. **AWS Certificate Manager**:
   - (Optional for this schedule but important for real-world deployments)
   - Provides SSL/TLS certificates for secure data transfer and to establish a secure connection if you decide to deploy the MVP.

7. **Amazon Route 53**:
   - (Optional for this schedule but important for real-world deployments)
   - Scalable Domain Name System (DNS) web service and domain registration.
   - Could be used if you decide to associate a custom domain name with the MVP.

---

### 3-Day Development Schedule

### Day 1: Planning, Design, and AWS Setup
**Total Budget for Day 1: $30**
   - **Requirement Gathering**: Re-evaluate the core features for the MVP.
   - **Design Mockup Creation**: Draft a wireframe of EstiMateGPT's user interface.
   - **AWS Setup**: Configure AWS services, including Lambda and API Gateway.
   - **Technology Stack Decision**: Confirm tools, services, and libraries.

### Day 2: Backend Development with ChatGPT API
**Total Budget for Day 2: $40**
   - **Backend Development with ChatGPT API**: Develop an AWS Lambda function to act as middleware, integrated with the ChatGPT API.
   - **Backend Testing and Debugging**: Test the Lambda function with sample requests.

### Day 3: Expanded Frontend Development and Testing
**Total Budget for Day 3: $30**
   - **Frontend Development**:
     - **Design and Layout**: Craft EstiMateGPT's layout with HTML/CSS.
     - **Integration with Backend**: Use JavaScript for backend communication.
     - **User Feedback and Interaction**: Enhance user experience with feedback mechanisms.
   - **Testing and Debugging**: Ensure the frontend and backend work seamlessly.
