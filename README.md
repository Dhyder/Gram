# GrimGram
## Author
* [Shaggy](https://github.com/Dhyder)

## Description
GrimGram the Instagram recreation.

## Screenshots
![GrimGram](https://user-images.githubusercontent.com/86789832/144753638-d3d58ec7-3098-4d9f-b5d6-38995e1efb41.PNG)
![GrimGram](https://user-images.githubusercontent.com/86789832/144753970-cf2d6b1e-cc5a-44cb-853a-d2f60238275a.PNG)
![GrimGram](https://user-images.githubusercontent.com/86789832/144753642-1d84f709-18a9-4736-968f-69c2f22ebb5e.PNG)

## Live Link
You can view the site at: [GrimGram](https://grimgram.herokuapp.com/)

## User Story
- Sign in or create profile in GrimGram to start using.
- Upload content to the application.
- See your profile with all your pictures.
- Search for different users using their usernames.
- Follow other users and see their pictures on your timeline.


## SetUp / Installation Requirements
### Prerequisites
* Django 2.2.24
* python3.8.10
* virtualenv
* pgAdmin4
* HTML5  
* CSS3
* Javascript 
* Font Awesome
* jQuery

### Cloning
* In your terminal:

        git clone https://github.com/Dhyder/gram.git
        cd gram/

## Running the Application
* Creating the virtual environment

        virtualvenv virtual
        source virtual/bin/activate
 or (windows)
 
        source virtual/Scripts/activate

* Installing Dependencies

        pip install -r requirements.txt
        
* Making Migrations

        python manage.py makemigrations instagram
        
* Migrate

        python manage.py migrate

* Running the application:

        python3.8 manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        python3.8 manage.py test

## Technologies Used
* Python3.8.10
* Django2.2.24

## Known Bugs
* No known bugs at the moment
## Author's Contact Information
* For any queries, you can reach out at [desastrecaliente@gmail.com]

### MIT License:
Copyright (c) 2021 **Shaggy**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
