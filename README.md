# MLDEC2
## Car price prediction

## Deployment on AWS EC2

### Create an AWS EC2 Instance:

1. **Launch an EC2 Instance:**
    - Open the AWS Management Console.
    - Navigate to the EC2 service.
    - Click on "Launch Instance" to start the instance creation process.

2. **Select an Appropriate AMI and Instance Type:**
    - Choose an Amazon Machine Image (AMI) based on your project requirements.
    - Select an instance type based on your project's computational needs.

3. **Configure Security Groups:**
    - In the instance configuration, set up security groups to control inbound and outbound traffic.
    - Ensure that necessary ports are open for your application.

### Connect to EC2 Instance:

1. **Use SSH to Connect:**
    - Open a terminal on your local machine.

2. **Locate Your Key Pair:**
    - Ensure you have the key pair (.pem) associated with your EC2 instance.

3. **Connect to the Instance:**
    ```bash
    ssh -i "your-key-pair.pem" ec2-user@your-ec2-instance-ip
    ```
    Replace "your-key-pair.pem" with the path to your key pair file and "your-ec2-instance-ip" with the public IP address of your EC2 instance.

### Project Setup on EC2:

1. **Upload Project Files:**
    - Copy your project files to the EC2 instance using `scp` or any preferred method.

2. **Install Dependencies:**
    - Navigate to your project directory on the EC2 instance.
    - Install any necessary dependencies.
    ```bash
    # Example for installing Python dependencies
    pip install -r requirements.txt
    ```

3. **Run the Project:**
    - Start your application or service.
    ```bash
    # Example for running a Python script
    python your_script.py
    ```

### Note:
- Ensure that your EC2 instance has the required IAM role and permissions to access other AWS services if needed.
- Terminate your EC2 instance when it's no longer needed to avoid unnecessary costs.

## License

Specify the license for your project. For example, MIT License.
