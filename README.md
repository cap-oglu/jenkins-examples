# Jenkins CI/CD Example with Python

This project demonstrates a complete CI/CD pipeline setup using Jenkins with a simple Python calculator application.

## Project Structure

```
jenkins-examples/
├── app.py              # Main Python application (Calculator)
├── test_app.py         # Unit tests for the application
├── requirements.txt    # Python dependencies
├── Jenkinsfile        # Jenkins pipeline configuration
└── README.md          # This file
```

## Application Overview

The project contains a simple Calculator class with the following operations:
- Addition
- Subtraction
- Multiplication
- Division (with zero division handling)
- Power calculation

## Prerequisites

- Python 3.7 or higher
- Jenkins server with:
  - Pipeline plugin
  - Python environment
  - Coverage plugin (for coverage reports)

## Local Development

### Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Run Tests

```bash
# Run all tests
pytest test_app.py -v

# Run tests with coverage
pytest --cov=app test_app.py
```

### Code Quality Check

```bash
pip install flake8
flake8 app.py test_app.py --max-line-length=100
```

## Jenkins Pipeline

The `Jenkinsfile` defines a complete CI/CD pipeline with the following stages:

1. **Checkout**: Get source code from repository
2. **Setup Environment**: Create Python virtual environment and install dependencies
3. **Lint Code**: Run code quality checks with flake8
4. **Run Tests**: Execute unit tests with pytest
5. **Test Coverage**: Generate test coverage reports
6. **Run Application**: Test application execution
7. **Archive Artifacts**: Save build artifacts

### Pipeline Features

- ✅ Automated testing
- ✅ Code quality checks
- ✅ Test coverage reporting
- ✅ Artifact archiving
- ✅ Email notifications on failure
- ✅ Automatic cleanup

## Setting up in Jenkins

1. Create a new Pipeline job in Jenkins
2. Configure the job to use "Pipeline script from SCM"
3. Set the repository URL and credentials
4. Set the script path to `Jenkinsfile`
5. Save and run the pipeline

## Environment Variables

The pipeline uses the following environment variables:
- `PYTHON_VERSION`: Python version (default: 3.9)
- `VENV_NAME`: Virtual environment name (default: jenkins-venv)

## Test Coverage

The pipeline generates both XML and HTML coverage reports:
- XML report: `coverage.xml` (for Jenkins coverage plugin)
- HTML report: `htmlcov/` directory (for human-readable coverage)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is for educational purposes and demonstrates Jenkins CI/CD best practices. 