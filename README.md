# The Movie Quiz - A console game made with Python

README Contents

1. [About](#about)
2. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
3. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
4. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
5. [Features](#features)
6. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    3. [Tools](#tools)
7. [Validation and Testing](#validation-and-testing)
    1. [Python Validation](#python-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
    1. [Code](#code)
    2. [Acknowledgements](#acknowledgements)
11. [License](#license)

# Introduction
A quiz where the user is presented with a movie title and needs to guess the year the movie was released. The user is given the option of having a clue to assist their guess but should they not use the clue they will receive bonus points. Once the user has entered their answer, the score is calculated based on the accuracy of the answer. After 5 questions the game is completed and the user is shown their total score.

## Project Goals

### User Goals

- Play a fun little game
- Have a variation of questions
- Interesting scoring system
- Winning

### Site Owner Goals

- Offer a fun game
- Make sure that the user understands the rules
- Make the game feel engaging
- Encourage replayability

## User Experience

### Target Audience

- Everyone who wants to play a little game
- People who want a simple game
- People who like movies

### User Requirements and Expectations

- Easy to navigate
- Can complete multiple games
- Large range of movies

### User Stories

As a user I want to:

1. Start a game
2. Know the rules
3. Know more about the developer
4. Relatively quick game
5. See a large variety of movie titles
6. Know my final score
7. Be guided through the game

## Technical Design

### Flowchart

The following flowchart shows the structure and logic of the The Movie Quiz.

<details><summary>Open flowchart</summary>
<img src="assets/readme_img/flowchart.jpg">
</details>

## Features

The app has 9 features in total

### Main menu

- Shows the main menu
- Contains the following options:
    - Start Quiz
    - Quiz Guide
    - About the Developer
    - Exit
- User stories covered: 1, 2, 3

![Main menu](assets/readme_img/main_menu.jpg)

### Instructions Page

- Explains how the quiz works
- Directly accessible from the main menu
- Navigates back to the main menu
- User stories covered: 2

![Instructions page](assets/readme_img/quiz_guide.jpg)

### About the Developer Page

- Shows the help
- Directly accessible from the main menu
- Navigates back to the main menu
- User stories covered: 3

![Help page](assets/readme_img/developer.jpg)

### Quiz/question page

- Show current question number and total question number
- Show movie title
- Offer user chance to see a clue
- Show points scored for each question
- Show total points scored for quiz so far
- Consistent and clear navigation 
- User stories covered: 1, 4, 5, 7

![Game start](assets/readme_img/quiz.jpg)

### Results Page

- Show user the total score out of total possible score
- Offer user chance to play again, return to menu or exit programme

![Results page](assets/readme_img/results.jpg)

## Technologies Used

### Languages

- Python

### Tools

- Git
- GitHub
- Heroku - to deploy the app
- Pycodestyle - for validation
- Lucid - for the flowchart [LucidChart](https://www.lucidchart.com/)
- [Regex101](https://regex101.com/) - to test regex expressions

## Validation and Testing

### Python Validation

Python validation was done with pycodestyle linter
The linter showed no errors or other problems

#### Python validation locally

1. Install pycodestyle

```python
pip3 install pycodestyle
```

2. Select pycodestyle as linter

<details>
 <summary>Screenshot from console</summary>
 <img src="#">
</details>

### Testing user stories

#### As a user I want to

1. Start a game

|Feature|Action|Expected result|Actual result|
|---|---|---|---|
Start game option|Select option 1 in the start menu|Game starts|Works as expected|

2. Learn how to play

|Feature|Action|Expected result|Actual result|
|---|---|---|---|
Quiz guide page|Select option 2 in the start menu|Shows the instructions|Works as expected|

3. Learn about the developer

|Feature|Action|Expected result|Actual result|
|---|---|---|---|
About the developer page|Select option 3 in the start menu|Shows the help|Works as expected|









## Bugs



## Deployment

Heroku:

1. Create an account at Heroku and login.
2. Click the "Create new app" button on your dashboard, add app name and region.
3. Click on the "Create app" button.
4. Click on the "Settings" tab.
5. Under "Config Vars" click "Reveal Config Vars" add your credentials as value with "CREDS" as key.
6. Under "Buildpacks" click "Add buildpack" and then choose "Python" first and click "Save changes"
7. Add a second buildpack "nodejs" and click "Save changes"
8. Go to the "Deploy" tab and choose GitHub as your deployment method
9. Connect your GitHub account
10. Enter your repository name, search for it and click connect when it appears below.
11. In the manual deploy section click "Deploy branch"
12. Optional: You can enable automatic deploys if you want the app to automatically update

You can fork the repository by following these steps:

1. Go to the repository on GitHub  
2. Click on the "Fork" button in the upper right hand corner

You can clone the repository by following these steps:

1. Go to the repository on GitHub
2. Locate the "Code" button above the list of files and click it  
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the "copy" button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <https://github.com/YOUR-USERNAME/YOUR-REPOSITORY>)  
7. Press Enter to create your local clone.

## Credits

### Code

- [ASCII art generator](http://patorjk.com/software/taag/)
- [Console clear function](https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console)

### Acknowledgements

- A special thanks to my mentor Gareth McGirr for his feedback and advice, especially on the documentation.
- A thanks to the Code Institute for the great learning resources



