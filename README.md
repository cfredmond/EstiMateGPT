<p align="center">
  <img src="logo.png" alt="EstiMateGPT" width="300"/>
</p>

**EstiMateGPT** is a digital tool designed to provide users with tailored GPT-4 implementation estimates for their projects. By inputting details about their domain, desired features, and other relevant information, users can gain insights into the scope, timeline, and potential costs associated with their GPT-4 endeavors. The application aims to streamline the initial stages of project planning, offering an intuitive interface that interacts with the ChatGPT API to generate dynamic and informative estimates. 

---

### AWS Resources

- **Amazon Lambda**: Serverless compute service.
- **Amazon API Gateway**: Service for creating and securing APIs.
- **Amazon S3 (Simple Storage Service)**: Object storage service (optional for this schedule).
- **Amazon CloudWatch**: Monitoring and observability service.
- **AWS Identity and Access Management (IAM)**: Service for access control and permissions.
- **AWS Certificate Manager**: Provides SSL/TLS certificates (optional for this schedule).
- **Amazon Route 53**: DNS web service and domain registration (optional for this schedule).

---

### 3-Day Development Schedule

### Day 1: Planning, Design, and AWS Setup
**Total Budget for Day 1: $30**
   - [**Requirement Gathering**](#requirement-gathering): Re-evaluate the core features for the MVP.
   - [**Design Mockup Creation**](#design-mockup-creation): Draft a wireframe of EstiMateGPT's user interface.
   - [**AWS Setup**](#aws-setup): Configure AWS services, including Lambda and API Gateway.
   - [**Technology Stack Decision**](#technology-stack-decision): Confirm tools, services, and libraries.

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

---

### Day 1

#### Requirement gathering

For the **EstiMateGPT** project, the core features for the Minimum Viable Product (MVP) would be:

- **User Input Interface**:
  - Fields for users to specify project details such as domain, desired features, and other relevant information.

- **Estimation Engine**:
  - Integration with the ChatGPT API to process user inputs and provide GPT-4 implementation estimates.
  - Backend logic (using AWS Lambda) to process the estimation based on user input.

- **Results Display**:
  - Dynamic presentation of the estimation results to the user in a clear and concise format.
  - Potential breakdown of the estimate, explaining factors considered.

- **Feedback Mechanism**:
  - Option for users to provide feedback on the estimation or report issues.
  - Enhances iterative development and refinement of the tool.

- **Basic Error Handling**:
  - Notifications for users in cases of delays, API issues, or missing information.
  - Ensures a smooth user experience even when issues arise.

- **Responsive Design**:
  - A user interface that adapts to various screen sizes, ensuring usability on both desktop and mobile devices.

- **Secure API Integration**:
  - Safe and secure communication between the frontend and backend using Amazon API Gateway.

- **Guidance Features**:
  - Tooltips or help icons to guide users on how to fill out their project details.

These core features ensure that the MVP provides users with a functional tool to get GPT-4 implementation estimates while also offering a foundation for further enhancements and features in subsequent development phases.

[Back to top](#)

---

### Design Mockup Creation

1. **Header**:
   - **Logo**: Positioned on the top-left, representing **EstiMateGPT**.
   - **Navigation Bar**: Horizontally aligned links to potential other pages or sections such as 'About', 'Help', and 'Contact'.

2. **Main Content Area**:
   
   - **Title & Subtitle**:
     - Large, clear title: "EstiMateGPT".
     - Subtitle or brief description: "Get tailored GPT-4 implementation estimates."

   - **User Input Section**:
     
     - **Domain Selection**:
       - Label: "Select Your Domain".
       - Dropdown menu or radio buttons with options like 'E-commerce', 'Healthcare', 'Finance', etc.
     
     - **Desired Features**:
       - Label: "Choose Desired Features".
       - Checklist with common features like 'Chatbot Integration', 'Content Generation', 'Data Analysis', etc.
       - An "Other" field for custom features.
     
     - **Project Description**:
       - Label: "Describe Your Project".
       - Text area for users to input more detailed information about their project.
     
     - **Additional Details** (optional):
       - More specific fields depending on the scope, like "Estimated User Base Size" or "Preferred Implementation Timeline".
     
     - **Estimation Button**:
       - Centrally placed button labeled "Get Estimate".

   - **Results Display Section**:
     - A dedicated area that will dynamically showcase the estimation once the user submits their details.
     - Potential to include a breakdown of the estimate, visuals like graphs or charts, and explanatory notes.

3. **Feedback & Help Sidebar** (optional but recommended for MVP):
   
   - **FAQ**:
     - Collapsible questions and answers to assist users in understanding how to use **EstiMateGPT** effectively.
   
   - **Feedback Form**:
     - A simple form or link where users can provide feedback on the tool or report issues.

4. **Footer**:
   - Contains links to 'Terms of Service', 'Privacy Policy', and potentially 'Contact Information'.
   - Copyright notice and date.

This outline gives a structured view of how the user interface for **EstiMateGPT** can be organized. Actual design decisions, like colors, fonts, and spacing, would be determined during the design phase, but this provides a foundational structure for the wireframe.

[Back to top](#)

---

### AWS Setup

**Objective**: 
Establish the necessary infrastructure on AWS to support the functionalities of EstiMateGPT, ensuring scalability, security, and optimal performance.

**Steps**:

1. **Account Configuration**:
   - If not already done, sign up for an AWS account.
   - Set up billing and account details.

2. **IAM (Identity and Access Management) Setup**:
   - Create IAM roles and permissions to ensure secure access to AWS services.
   - Set up policies that allow specific AWS services (like Lambda, API Gateway) to interact with each other.

3. **Initialize AWS Lambda**:
   - Create a new Lambda function that will act as the serverless backend for the application.
   - Define the runtime environment (e.g., Python, Node.js) and allocate resources (memory, timeout).
   - Upload or write the function code to handle requests from the frontend, communicate with the ChatGPT API, and return the processed results.

4. **Configure Amazon API Gateway**:
   - Set up a new API endpoint that the frontend will use to communicate with the Lambda function.
   - Define the HTTP methods (e.g., GET, POST) that the API will support.
   - Configure security settings, such as CORS (Cross-Origin Resource Sharing) and authentication, to ensure safe interactions between the frontend and backend.

5. **Testing and Debugging**:
   - Initially test the Lambda function and API Gateway to ensure they are correctly set up and can communicate without errors.
   - Use sample requests to simulate user interactions.

6. **Monitoring and Logging**:
   - Activate Amazon CloudWatch for the Lambda function and API Gateway.
   - This will allow monitoring of the application's performance, capturing logs, and setting up alerts for potential issues.

7. **Optional Services**:
   - Depending on the requirements, additional AWS services like Amazon S3 (for static website hosting) or Amazon RDS (for database needs) might be initialized and configured.

[Back to top](#)

---

### Technology Stack Decision

### Backend:

1. **Serverless Computing**: 
   - **Choice**: AWS Lambda
   - **Reason**: Continues to be an excellent choice for serverless architecture. You can write your Lambda functions in Python.
   
2. **API Management**:
   - **Choice**: Amazon API Gateway
   - **Reason**: Consistent and secure way to expose the Python-based Lambda functions to the frontend.

3. **Integration with GPT-4**:
   - **Choice**: OpenAI's official Python SDK
   - **Reason**: This SDK can be integrated directly into the Python codebase you deploy on Lambda.

### Frontend:

1. **Web Framework**:
   - **Choice**: Vue.js
   - **Reason**: Vue.js is a progressive JavaScript framework that is easy to integrate and offers a clear separation of components. It has a gentle learning curve and robust community support.

2. **Styling and Components**:
   - **Choice**: BootstrapVue
   - **Reason**: BootstrapVue combines Bootstrap (a popular CSS framework) and Vue.js, allowing for the creation of responsive and attractive user interfaces with pre-styled components.

### Database (if required later):

1. **Database Service**:
   - **Choice**: Amazon DynamoDB
   - **Reason**: Still remains a good choice due to its serverless nature, scalability, and integration with AWS services. SDKs are available for Python.

### Other Tools & Services:

1. **Version Control**:
   - **Choice**: Git with GitHub or Bitbucket
   - **Reason**: Standard tool for source code management and collaboration.

2. **Continuous Integration/Continuous Deployment (CI/CD)**:
   - **Choice**: AWS CodePipeline or Jenkins with plugins/support for Python and Vue.js.
   - **Reason**: To automate the build, test, and deployment process, ensuring smooth updates and rapid iterations.

3. **Monitoring & Logging**:
   - **Choice**: Amazon CloudWatch
   - **Reason**: To keep an eye on application performance, set alerts, and log data for future analysis.

With Python on the backend, Vue.js for the frontend, and Bootstrap for styling, this updated tech stack provides a solid foundation for **EstiMateGPT**. It aligns with modern best practices and offers scalability and maintainability.

[Back to top](#)

---