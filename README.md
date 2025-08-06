# Python + JavaScript: Full Stack App (Contacts List)

Quick Setup Process:  
npm create vite@latest frontend -- --template react  
cd backend  
pip install Flask  
pip install Flask-SQLAlchemy  
pip install flask-cors  
or  
python -m pip install `<package-name>`  

-----------------------------------------------------------------------------------------------------------------------------------------
To Test for Full-Stack:  
Split Terminal into 2 (cmd Terminals)  

Database Testing:  
cd backend  
python main.py  

API application Testing:  
cd frontend  
npm run dev  

-----------------------------------------------------------------------------------------------------------------------------------------

<!-- markdownlint-disable MD033 -->
<div style="display: flex; justify-content: center; align-items: center;">
  <img
    src="https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png"
    width="600"
    height="300"
    alt="Python Logo"
    style="margin-right: 20px;"
  >
  <img
    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpuYdLEzBvwemix8pwsncUkLLOQqnByncadg&s"
    width="300"
    height="300"
    alt="JavaScript Logo"
  >
</div>
<!-- markdownlint-enable MD033 -->

<!--
<p align="center">
  <img src="https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png" width="600" height="300" alt="Python Logo">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpuYdLEzBvwemix8pwsncUkLLOQqnByncadg&s" width="300" height="300" alt="JavaScript Logo">
</p>
-->

> On the backend, Flask and SQLAlchemy in Python expose RESTful CRUD endpoints for a contacts database, while JavaScript React components on the frontend consume those APIs to display and manage the contacts list.

This project implements a contacts management application with full CRUD functionality. The backend is powered by Python, Flask, and SQLAlchemy, exposing a RESTful API. The frontend uses React and JavaScript to provide a dynamic user interface.

- Major Disclaimer:
  - This contacts list application is provided "as-is" and proper safeguards must be implemented before deploying.
  - This is not production-hardened and doesn't include comprehensive security measures such as authentication, input validation, encryption, or compliance with data protection regulations.
  - As stated within the License, you must obtain permission by the Author of this project.

## Installing / Getting Started

A quick introduction of the minimal setup you need to get a Hello World up & running in VS Code.

```shell
Install "VS Code" and "Python"
Ensure the "Environment Variable" is included in "the Path" within Python ("Click the Checkbox")
Install the needed "Extensions for VS Code" ["Python by Microsoft, Python Debugger by Microsoft, etc"]
Other Extensions may include ["GitHub, Markdown, Elint/lint, etc"] to utilize GitHub Version Control and other language syntax
Start coding Python
You can run the code by using the following: ["python filename.py"]
```

Congrats! You just created your first Python file and there's so much more you can do so experiment to your hearts content!

### Initial Configuration

Requirements:
  
- Ensure that the project file/folder and other dependencies you plan to make is within the range for code execution.
  
- Ensure you have a GitHub account to make project repos and save changes to prevent loss of progress with your code in the future.

## Developing

In order to start developing the project further:

```shell
git clone https://github.com/username/project-name.git
cd project-name/
```

After setting up GitHub and the GitHub repo, you should be able to clone/commit/publish your progress as you make changes to the project.

### Building

To build the project after some code changes:

```shell
commit changes by using the GitHub extensions from VS Code or by using the terminal via commands
stash/push the changes into the main/master branch of the project or in another branch if needed
```

After commiting and pushing the changes into GitHub, you should see the project repo change to reflect the most recent code.

### Deploying / Publishing

In case you want to publish your project to a server:

```shell
Ensure that the project is fully functional and give appropiate credit to all contributors/authors.
Provide a step-by-step process of how you managed to complete the project.
Check the project and live server before finalizing the project status.
```

If you want to use GitHub or any other 3rd party platform for your server, you can but it may prove to be difficult with the lack of updated tutorials for all sorts of software services. 
[You can checkout the masterPortfolio repo to see how to use GitHub pages]

## Features

This project repo has the following:

- Backend (Flask + SQLAlchemy)
  - RESTful CRUD endpoints for creating, reading, updating, and deleting contacts
  - SQLAlchemy models with migrations to manage database schema changes
  - Input validation and serialization for request/response payloads
  - Error handling with meaningful HTTP status codes and JSON error messages
  - Search, filtering, and pagination support on contacts endpoints
  - Configuration management via environment variables (development, testing, production)
  - Logging of requests, errors, and database operations
  - Unit and integration tests (pytest) covering routes, models, and business logic

- Frontend (React + JavaScript)
  - Responsive contacts list view with sorting and real-time updates
  - Dynamic add/edit contact forms with client-side validation
  - State management using Context API or a lightweight store (Ex: Redux)
  - Service layer (fetch or Axios) to interact with backend API endpoints
  - React Router for navigating between list, detail, and form views
  - Optimistic UI updates and loading indicators for better UX
  - User notifications for success, error, and validation feedback
  - Unit and integration tests (Jest, React Testing Library) for components and services

- DevOps & Tooling
  - CI/CD pipeline (e.g., GitHub Actions) for linting, tests, and deployments
  - ESLint and Prettier setup to enforce code style and consistency
  - Environment variable management for API URLs

- (To be continued)...

## Links

Helpful links that you can use with your project:

- GitHub Commands Cheat Sheet: [https://github.com/tiimgreen/github-cheat-sheet]
- In case of sensitive bugs like security vulnerabilities, please use the issue tracker or contact me directly. 
  We value your effort to improve the security and privacy of this project!

## References

"Give Credit where its Due": Credit goes to all the original repo owners, contributors, and author into making this project.
(If possible, please provide the GitHub URLs and names to all that contributed including the project owner)

"Python + JavaScript - Full Stack App Tutorial" by Tech With Tim [[YouTube]](https://www.youtube.com/watch?v=PppslXOR7TA)
<!-- - "Title" by Author [Social Media/Location] -->

## Licensing

[![License](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](LICENSE)

"The project is licensed under MIT license."